-- for i in {4294967000..4294967295}; do echo -n ${i} | nc -4u -w0 192.168.226.200 8000 ;done
-- sudo tcpdump -i lo -w 2024_07_03_udp_2.dmp
-- sudo tcpdump -i eth0 -w 2024_07_03_1.dmp

-- tshark -Y "tcp"  -X "lua_script:pcap_file.lua" -r 2024_07_03_udp_2.dmp > 111.TMP

-- pcap_file_reader.lua
--------------------------------------------------------------------------------
--[[
    This is a Wireshark Lua-based pcap capture file reader.

    Author: Hadriel Kaplan <hadrielk at yahoo dot com>
    Copyright (c) 2014, Hadriel Kaplan

    This code is in the Public Domain, or the BSD (3 clause) license if Public Domain does not apply
    in your country.

    Version: 1.0

    This "capture file" reader reads pcap files - the old style ones. Don't expect this to
    be as good as the real thing; this is a simplistic implementation to show how to
    create such file readers, and for testing purposes.

    For a more comprehensive example, see "fileshark_pcap.lua" or "acme_file.lua".

    This script requires Wireshark v1.11.3 or newer.
--]]
--------------------------------------------------------------------------------

-- do not modify this table
local debug = {
    DISABLED = 0,
    LEVEL_1  = 1,
    LEVEL_2  = 2
}

-- set this DEBUG to debug.LEVEL_1 to enable printing debug info
-- set it to debug.LEVEL_2 to enable really verbose printing
local DEBUG = debug.LEVEL_2


local wireshark_name = "Wireshark"
if not GUI_ENABLED then
    wireshark_name = "Tshark"
end

-- verify Wireshark is new enough
local major, minor, micro = get_version():match("(%d+)%.(%d+)%.(%d+)")
if major and tonumber(major) <= 1 and ((tonumber(minor) <= 10) or (tonumber(minor) == 11 and tonumber(micro) < 3)) then
        error(  "Sorry, but your " .. wireshark_name .. " version (" .. get_version() .. ") is too old for this script!\n" ..
                "This script needs " .. wireshark_name .. "version 1.11.3 or higher.\n" )
end

-- verify we have the FileHandler class in wireshark
assert(FileHandler.new, wireshark_name .. " does not have the FileHandler class!")

--------------------------------------------------------------------------------
-- early definitions
-- throughout most of this file I try to pre-declare things to help ease
-- reading it and following the logic flow, but some things just have to be done
-- before others, so this sections has such things that cannot be avoided
--------------------------------------------------------------------------------

-- first some variable declarations for functions we'll define later
local parse_file_header, parse_rec_header, read_common -- Это фнукнции - реализация ниже. Здесь для использования в коде.

-- these will be set inside of parse_file_header(), but we're declaring them up here
-- Это таблица для значений по умолчанию. Далее эти значения копируются обновляются в соответствии с прочитанной информацией и записываются в capture.private_table (делается это для привязки настройки к конкретному файлу, т.е. это для случая если этот скрипт будет использоваться в Wireshark и в одим момент будет открыто несколько файлов)
-- Нужно отметить, что frame в tshark/tcpdump т.е. в формате pcap - имеет расширенные поля. См. функцию fram, что передайтся read()
-- Т.е. сначала идёт мета-информация а потом сам сетевой frame (при этом сам сетевой frame содержит все поля от Ehernet(mac) до IP и DUP)
-- Расширенные поля - расшифровываются с помощью шаблона rec_hdr_patt - т.е. по сути 16Байт.
local default_settings =
{
    debug           = DEBUG,
    corrected_magic = 0xa1b2c3d4, --поле в первых Байтах - несёт информацю какой формат имеет файл. У файла tcpdump др. значения. См. таблицу magic_spells ниже.
    version_major   = 2,
    version_minor   = 4,
    timezone        = 0,
    sigfigs         = 0,
    read_snaplen    = 0, -- the snaplen we read from file
    snaplen         = 0, -- the snaplen we use (limited by WTAP_MAX_PACKET_SIZE)
    linktype        = -1, -- the raw linktype number in the file header
    wtap_type       = wtap_encaps.UNKNOWN, -- the mapped internal wtap number based on linktype
    endianness       = ENC_BIG_ENDIAN,
    time_precision  = wtap_filetypes.TSPREC_USEC, -- wtap_filetypes - что это за таблица? С ходу не смог найти в документации.
    rec_hdr_len     = 16,            -- default size of record header
    rec_hdr_patt    = "I4 I4 I4 I4", -- pattern for Struct to use 
    num_rec_fields  = 4,             -- number of vars in pattern
}
-- Настройка печати исходя из заданного уровня логгирования.
local dprint = function() end
local dprint2 = function() end
local function reset_debug()
    if default_settings.debug > debug.DISABLED then
        dprint = function(...)
            print(table.concat({"Lua:", ...}, " "))
        end

        if default_settings.debug > debug.LEVEL_1 then
            dprint2 = dprint
        end
    end
end
-- call it now
reset_debug()

--------------------------------------------------------------------------------
-- file reader handling functions for Wireshark to use
--------------------------------------------------------------------------------

----------------------------------------
-- The read_open() is called by Wireshark once per file, to see if the file is this reader's type.
-- Wireshark passes in (1) a File object and (2) CaptureInfo object to this function
-- It expects in return either nil or false to mean it's not our file type, or true if it is
-- In our case what this means is we figure out if the file has the magic header, and get the
-- endianness of the file, and the encapsulation type of its frames/records
-- Этот метод вызывается автоматически tshark-ом при открытии файла.
local function read_open(file, capture)
    -- io.write("Read_open", "---Printed from Read_open method");
    dprint2("read_open() called")

    local file_settings = parse_file_header(file) -- Читаем из файла заголовок файла.

    print('  captureinfo.encap = ' ..  capture.encap)
    print('  captureinfo.time_precision = ' ..  capture.time_precision)
    print('  captureinfo.snapshot_length = ' ..  capture.snapshot_length)
    print('  captureinfo.comment = ' ..  (capture.comment == nil and capture.comment or "Empty"))
    print('  captureinfo.hardware = ' ..  (capture.hardware == nil and capture.hardware or "Empty"))
    print('  captureinfo.os = ' ..  (capture.os == nil and capture.os or "Empty"))
    print('  captureinfo.user_app = ' ..  (capture.user_app == nil and capture.user_app or "Empty"))
    -- print('  captureinfo.hosts = ' ..  (capture.hosts == nil and capture.hosts or "Empty")) -- В отличии от предыдущих - падает на отсутствии этого поля.


    if file_settings then

        dprint2("read_open: success, file is for us")

        -- save our state - Это поле есть в документации и оно согласно описанию, видимо специально для этого создано.
        capture.private_table = file_settings

        -- if the file is for us, we MUST set the file position cursor to
        -- where we want the first call to read() function to get it the next time
        -- for example if we checked a few records to be sure it's or type
        -- but in this simple example we only verify the file header (24 bytes)
        -- and we want the file position to remain after that header for our read()
        -- call, so we don't change it back
        --file:seek("set",position)

        -- these we can also set per record later during read operations
        capture.time_precision  = file_settings.time_precision -- ХЗ от куда. Взято в этой таблице default_settings ---> time_precision  = wtap_filetypes.TSPREC_USEC но почему это значение и что за таблица такая ХЗ
        capture.encap           = file_settings.wtap_type
        capture.snapshot_length = file_settings.snaplen

        print('  !!! aptureinfo.encap = ' ..  capture.encap)
        print('  !!! Берётся из системной таблицы (wtap_filetypes.TSPREC_USEC) captureinfo.time_precision = ' ..  capture.time_precision)
        print('  !!! captureinfo.snapshot_length = ' ..  capture.snapshot_length .. '   см. Snaplen got from header of file')

        return true
    end

    dprint2("read_open: file not for us")

    -- if it's not for us, wireshark will reset the file position itself

    return false
end

----------------------------------------
-- Wireshark/tshark calls read() for each frame/record in the file
-- It passes in (1) a File, (2) CaptureInfo, and (3) FrameInfo object to this function
-- It expects in return the file offset position the record starts at,
-- or nil/false if there's an error or end-of-file is reached.
-- The offset position is used later: wireshark remembers it and gives
-- it to seek_read() at various random times
local function read(file, capture, frame)
	print('--------------------Read---Line---------------------')
    -- io.write("hello", "Lua");

    dprint2("read() called")

    -- call our common reader function
    local position = file:seek() -- запоминает позицию - видимо именно строчку. Чтоб потом прочитать следующую строчку. По этому дальше читая байты, мы не сбиваем позицию. Т.к. здесь мы запомнили её.
    print('Currnet position of file. Got via file:seek()  = ' .. position)
    print('(Limited by WTAP_MAX_PACKET_SIZE = 65_535) capture.snapshot_length = ' .. capture.snapshot_length)

    if not read_common("read", file, capture, frame) then
        -- this isnt' actually an error, because it might just mean we reached end-of-file
        -- so let's test for that (read(0) is a special case in Lua, see Lua docs)
        if file:read(0) ~= nil then
            dprint("read: failed to call read_common")
        else
            dprint2("read: reached end of file")
        end
        return false
    end

    dprint2("read: success")

    -- return the position we got to (or nil if we hit EOF/error)
    return position
end

----------------------------------------
-- Wireshark/tshark calls seek_read() for each frame/record in the file, at random times
-- It passes in (1) a File, (2) CaptureInfo, (3) FrameInfo object, and the offset position number
-- It expects in return true for successful parsing, or nil/false if there's an error.
local function seek_read(file, capture, frame, offset)
    dprint2("seek_read() called")

    -- first move to the right position in the file
    file:seek("set",offset)

    if not read_common("seek_read", file, capture, frame) then
        dprint("seek_read: failed to call read_common")
        return false
    end

    return true
end

----------------------------------------
-- Wireshark/tshark calls read_close() when it's closing the file completely
-- It passes in (1) a File and (2) CaptureInfo object to this function
-- this is a good opportunity to clean up any state you may have created during
-- file reading. (in our case there's no real state)
local function read_close(file, capture)
    dprint2("read_close() called")
    -- we don't really have to reset anything, because we used the
    -- capture.private_table and wireshark clears it for us after this function
    return true
end

----------------------------------------
-- An often unused function, Wireshark calls this when the sequential walk-through is over
-- (i.e., no more calls to read(), only to seek_read()).
-- It passes in (1) a File and (2) CaptureInfo object to this function
-- This gives you a chance to clean up any state you used during read() calls, but remember
-- that there will be calls to seek_read() after this (in Wireshark, though not Tshark)
local function seq_read_close(file, capture)
    dprint2("First pass of read() calls are over, but there may be seek_read() calls after this")
    return true
end

----------------------------------------
-- ok, so let's create a FileHandler object
--
-- note the last argument defines our file handler type (r=reader), and its magic/heuristic
-- capability - this is used to determine the ordering of this file reader compared with
-- the built-in file readers in wireshark. When a user opens a file, wireshark automatically
-- tries to find a matching file reader for the file. The file extensions are used as hints,
-- but really the ordering is more important. So wireshark first tries all the "magic" readers,
-- meaning ones that can figure out if a file is their format based on a magic byte sequence
-- at the beginning of the file, and then wireshark runs through the "heuristic" file readers,
-- meaning ones that have to guess if the file is their format or not. The ordering of these
-- is very important, since a weak heuristic will incorrectly think a file is its format and
-- prevent a lower-ordered file reader from getting to check it. So if your file reader uses
-- a magic value, you should use the "m" flag, and if it uses a heuristic then no flag means
-- a weak heuristic, whereas a "s" means a strong one.
--
-- Here we use a strong magic (m=magic, s=strong). You should NEVER really use "ms" together,
-- because that puts it even above the built-in magic file readers, including pcap itself!
-- But since this example script is actually trying to replace the built-in pcap file
-- reader, it makes sense for this one example to do so.
local fh = FileHandler.new("Lua-based PCAP reader", "lua_pcap", "A Lua-based file reader for PCAP-type files","rms")

-- set above functions to the FileHandler
-- we could have just done it in the function definitions above, by doing things like:
-- "function fh.read_close(file, capture)...", but I prefer this way...
fh.read_open = read_open
fh.read = read
fh.seek_read = seek_read
fh.read_close = read_close
fh.seq_read_close = seq_read_close
fh.extensions = "pcap;cap" -- this is just a hint

-- and finally, register the FileHandler!
register_filehandler(fh)

dprint2("FileHandler registered")

--------------------------------------------------------------------------------
-- ok now for the boring stuff that actually does the work
--------------------------------------------------------------------------------

----------------------------------------
-- in Lua, we have access to encapsulation types in the 'wtap_encaps' table, but
-- those numbers don't actually necessarily match the numbers in pcap files
-- for the encapsulation type, because the namespace got screwed up at some
-- point in the past (blame LBL NRG, not wireshark for that)
-- but I'm not going to create the full mapping of these two namespaces
-- instead we'll just use this smaller table to map them
-- these are taken from wiretap/pcap-common.c
local pcap2wtap = {
    [0]   = wtap_encaps.NULL,
    [1]   = wtap_encaps.ETHERNET,
    [6]   = wtap_encaps.TOKEN_RING,
    [8]   = wtap_encaps.SLIP,
    [9]   = wtap_encaps.PPP,
    [101] = wtap_encaps.RAW_IP,
    [105] = wtap_encaps.IEEE_802_11,
    [127] = wtap_encaps.IEEE_802_11_RADIOTAP,
    [140] = wtap_encaps.MTP2,
    [141] = wtap_encaps.MTP3,
    [143] = wtap_encaps.DOCSIS,
    [147] = wtap_encaps.USER0,
    [148] = wtap_encaps.USER1,
    [149] = wtap_encaps.USER2,
    [150] = wtap_encaps.USER3,
    [151] = wtap_encaps.USER4,
    [152] = wtap_encaps.USER5,
    [153] = wtap_encaps.USER6,
    [154] = wtap_encaps.USER7,
    [155] = wtap_encaps.USER8,
    [156] = wtap_encaps.USER9,
    [157] = wtap_encaps.USER10,
    [158] = wtap_encaps.USER11,
    [159] = wtap_encaps.USER12,
    [160] = wtap_encaps.USER13,
    [161] = wtap_encaps.USER14,
    [162] = wtap_encaps.USER15,
    [186] = wtap_encaps.USB,
    [187] = wtap_encaps.BLUETOOTH_H4,
    [189] = wtap_encaps.USB_LINUX,
    [195] = wtap_encaps.IEEE802_15_4,
}

-- we can use the above to directly map very quickly
-- but to map it backwards we'll use this, because I'm lazy:
local function wtap2pcap(encap)
    for k,v in pairs(pcap2wtap) do
        if v == encap then
            return k
        end
    end
    return 0
end

----------------------------------------
-- here are the "structs" we're going to parse, of the various records in a pcap file
-- these pattern string gets used in calls to Struct.unpack()
--
-- we will prepend a '<' or '>' later, once we figure out what endianness the files are in
--
-- this is a constant for minimum we need to read before we figure out the filetype
local FILE_HDR_LEN = 24
-- a pcap file header struct
-- this is: magic, version_major, version_minor, timezone, sigfigs, snaplen, encap type
local FILE_HEADER_PATT = "I4 I2 I2 i4 I4 I4 I4"
-- it's too bad Struct doesn't have a way to get the number of vars the pattern holds
-- another thing to add to my to-do list?
local NUM_HDR_FIELDS = 7

-- these will hold the '<'/'>' prepended version of above
--local file_header, rec_header

-- snaplen/caplen can't be bigger than this
local WTAP_MAX_PACKET_SIZE = 65535

----------------------------------------
-- different pcap file types have different magic values
-- we need to know various things about them for various functions
-- in this script, so this table holds all the info
--
-- See default_settings table above for the defaults used if this table
-- doesn't override them.
--
-- Arguably, these magic types represent different "Protocols" to dissect later,
-- but this script treats them all as "pcapfile" protocol.
--
-- From this table, we'll auto-create a value-string table for file header magic field
local magic_spells =
{
    normal =
    {
        magic = 0xa1b2c3d4,
        name  = "Normal (Big-endian)",
    },
    swapped =
    {
        magic = 0xd4c3b2a1, -- это оно соответствует нашему tcpdump.
        name  = "Swapped Normal (Little-endian)",
        endianness = ENC_LITTLE_ENDIAN, -- little endia - это младший байт будет записан в младшем адресе или будет идти первым. Хотя для интернета порядок Big-endian (хранит старший байт числа по меньшему адресу памяти)
    },
    modified =
    {
        -- this is for a ss991029 patched format only
        magic = 0xa1b2cd34,
        name  = "Modified",
        rec_hdr_len    = 24,
        rec_hdr_patt   = "I4I4I4I4 I4 I2 I1 I1",
        num_rec_fields = 8,
    },
    swapped_modified =
    {
        -- this is for a ss991029 patched format only
        magic = 0x34cdb2a1,
        name  = "Swapped Modified",
        rec_hdr_len    = 24,
        rec_hdr_patt   = "I4I4I4I4 I4 I2 I1 I1",
        num_rec_fields = 8,
        endianness = ENC_LITTLE_ENDIAN,
    },
    nsecs =
    {
        magic = 0xa1b23c4d,
        name  = "Nanosecond",
        time_precision = wtap_filetypes.TSPREC_NSEC,
    },
    swapped_nsecs =
    {
        magic = 0x4d3cb2a1,
        name  = "Swapped Nanosecond",
        endianness      = ENC_LITTLE_ENDIAN,
        time_precision = wtap_filetypes.TSPREC_NSEC,
    },
}

-- create a magic-to-spell entry table from above magic_spells table
-- so we can find them faster during file read operations
-- we could just add them right back into spells table, but this is cleaner
local magic_values = {}
for k,t in pairs(magic_spells) do
    magic_values[t.magic] = t
end

-- the function which makes a copy of the default settings per file
local function new_settings()
    dprint2("creating new file_settings")
    local file_settings = {}
    for k,v in pairs(default_settings) do
        file_settings[k] = v
    end
    return file_settings
end

-- set the file_settings that the magic value defines in magic_values
-- Ищем прочитанное значение в нашей таблице. Но что это за 16_ыне значения?
local function set_magic_file_settings(magic)
    local t = magic_values[magic]
    print('Function: set_magic_file_settings got magic = ' .. magic)
    print('The got type of "magic" in function set_magic_file_settings = ' .. type(magic))
    if not t then
        dprint("set_magic_file_settings: did not find magic settings for:", magic)
        return false
    end

    local file_settings = new_settings() 
    -- Создаём копию словаря настроек defaul_settigns. Сам словарь/таблицу не трогаем.
    -- Далее его сохраним в capture. 
    -- Делается это для использования скрипта и тоткрытия множества файлов.

    -- the magic_values/spells table uses the same key names, so this is easy
    -- Докидываем значения из таблиы значений с 16_чных значений. Там же лежат правила разбора бинарей.
    for k,v in pairs(t) do 
        file_settings[k] = v
    end

    -- based on endianness, set the file_header and rec_header
    -- and determine corrected_magic
    if file_settings.endianness == ENC_BIG_ENDIAN then
        file_settings.file_hdr_patt = '>' .. FILE_HEADER_PATT	
	-- Берется или из  magic_spells или из default_settings если в magic нет.
        file_settings.rec_hdr_patt  = '>' .. file_settings.rec_hdr_patt
        file_settings.corrected_magic = magic
    else
        file_settings.file_hdr_patt = '<' .. FILE_HEADER_PATT
        file_settings.rec_hdr_patt  = '<' .. file_settings.rec_hdr_patt
        print('Struct.unpack(">I4", m) = ' .. magic)
		-- io.write("the magic = " .. magic )
        local m = Struct.pack(">I4", magic)
		-- print('Struct.pack(">I4", magic) = ' .. m)  -- Приводит к кривому выводу. Т.е. именно просто печатает в файл криво (кракозябрами).
        file_settings.corrected_magic = Struct.unpack("<I4", m)
		print('Struct.unpack("<I4", m) = ' .. file_settings.corrected_magic)
    end

    file_settings.rec_hdr_len = Struct.size(file_settings.rec_hdr_patt)

    return file_settings
end

----------------------------------------
-- internal functions declared previously
----------------------------------------

----------------------------------------
-- used by read_open(), this parses the file header
parse_file_header = function(file)
    dprint2("parse_file_header() called")

    -- by default, file:read() gets the next "string", meaning ending with a newline \n
    -- but we want raw byte reads, so tell it how many bytes to read
    -- FILE_HDR_LEN =  24 - т.е. читаем 24 байта.
    local line = file:read(FILE_HDR_LEN)

    -- it's ok for us to not be able to read it, but we need to tell wireshark the
    -- file's not for us, so return false
    if not line then return false end

    dprint2("parse_file_header: got this line:\n'", Struct.tohex(line,false,":"), "'") -- просто представляем бинарную строку в виде втроки hex - т.е. по сути цифры представляем в мечатном виде hex.

    -- let's peek at the magic int32, assuming it's big-endian
    -- print('raw_line_from_File = ' .. line) -- Приводит к кривому выводу
    -- unsigned int 0-4_294_967_295
    local magic = Struct.unpack(">I4", line) -- А здесь идёт парсинг, каждый байт интерпретируется и парсится как конкретный тип. В данном случае первые 4ре байта интерпретируется как int. Читаем сигнатуру файла.
    print('Struct.unpack(">I4", line) = ' .. magic)

    local file_settings = set_magic_file_settings(magic) -- Т.е. прочитали, распарсили как число, сравнили с заголовком. Узнали какой порядок, опять запаковали, и распаковали в правильной последовательности. Исхдя из того, что прочитали в файле.

    if not file_settings then
        dprint("magic was: '", magic, "', so not a known pcap file?")
        return false
    end

    -- this is: magic, version_major, version_minor, timezone, sigfigs, snaplen, encap type
    local fields = { Struct.unpack(file_settings.file_hdr_patt, line) }

    -- sanity check; also note that Struct.unpack() returns the fields plus
    -- a number of where in the line it stopped reading (i.e., the end in this case)
    -- so we got back number of fields + 1
    if #fields ~= NUM_HDR_FIELDS + 1 then
        -- this should never happen, since we already told file:read() to grab enough bytes
        dprint("parse_file_header: failed to read the file header")
        return nil
    end

    -- fields[1] is the magic, which we already parsed and saved before, but just to be sure
    -- our endianness is set right, we validate what we got is what we expect now that
    -- endianness has been corrected
    if fields[1] ~= file_settings.corrected_magic then
        dprint ("parse_file_header: endianness screwed up? Got:'", fields[1],
                "', but wanted:", file_settings.corrected_magic)
        return nil
    end

    file_settings.version_major = fields[2]
    file_settings.version_minor = fields[3]
    file_settings.timezone      = fields[4]
    file_settings.sigfigs       = fields[5]
    file_settings.read_snaplen  = fields[6]
    file_settings.linktype      = fields[7]

    -- wireshark only supports version 2.0 and later
    if fields[2] < 2 then
        dprint("got version =",VERSION_MAJOR,"but only version 2 or greater supported")
        return false
    end

    -- convert pcap file interface type to wtap number type
    print('file_settings.linktype = ' .. file_settings.linktype)

    file_settings.wtap_type = pcap2wtap[file_settings.linktype]
    if not file_settings.wtap_type then
        dprint("file nettype", file_settings.linktype,
               "couldn't be mapped to wireshark wtap type")
        return false
    end

    print('Snaplen got from header of file = ' .. file_settings.read_snaplen)
    file_settings.snaplen = file_settings.read_snaplen
    if file_settings.snaplen > WTAP_MAX_PACKET_SIZE then
        file_settings.snaplen = WTAP_MAX_PACKET_SIZE
    end

    dprint2("read_file_header: got magic='", magic,
            "', major version='", file_settings.version_major,
            "', minor='", file_settings.version_minor,
            "', timezone='", file_settings.timezone,
            "', sigfigs='", file_settings.sigfigs,
            "', read_snaplen='", file_settings.read_snaplen,
            "', snaplen='", file_settings.snaplen,
            "', nettype ='", file_settings.linktype,
            "', wtap ='", file_settings.wtap_type)

    --ok, it's a pcap file
    dprint2("parse_file_header: success")
    return file_settings
end

----------------------------------------
-- this is used by both read() and seek_read()
-- the calling function to this should have already set the file position correctly
read_common = function(funcname, file, capture, frame)
    dprint2(funcname,": read_common() called")

    -- get the state info
    local file_settings = capture.private_table

    -- first parse the record header, which will set the FrameInfo fields
    -- Здесь мы читаем метаинформацию о захваченном кадре. Т.е. в начала каждой строки располагается доп. информация не отноcящаяся к проктоколо.
    -- Но относящаяся и записываемая tcpdump-ом. Там есть время прияема и др. информация.
    if not parse_rec_header(funcname, file, file_settings, frame) then 
        dprint2(funcname, ": read_common: hit end of file or error")
        return false
    end

    frame.encap = file_settings.wtap_type

    -- now we need to get the packet bytes from the file record into the frame...
    -- we *could* read them into a string using file:read(numbytes), and then
    -- set them to frame.data so that wireshark gets it...
    -- but that would mean the packet's string would be copied into Lua
    -- and then sent right back into wireshark, which is gonna slow things
    -- down; instead FrameInfo has a read_data() method, which makes
    -- wireshark read directly from the file into the frame buffer, so we use that
--	if not frame:read_data(file, frame.captured_length) then
--      dprint(funcname, ": read_common: failed to read data from file into buffer")
--      return false
--  end
--  Отправка выполнялась командой [for i in {4294967000..4294967295}; do echo -n ${i} | nc -4u -w0 192.168.226.200 8000 ;done]
--  И видимо, каждая цифра числа 4294967000 была отправлена как символ. Допустим в ASCII - символ 4 имеет код  52(Decimal)  34(HexDecimal) 
--  По этому, вроде как число 4294967000 умещается в 4byte (как Int) ну или пусть 8byte(как Long) - а здесь при чтении мы вынуждены прочитать 10byte - причина в том, что символов то здесь 10 и как следствие 10byte.
--  Соответственно и разбирать эту часть нужно не как число Int или как число Long а как строчку а лишь после этого эту строчку конвертировать в num (int или byte).
	local startNumBytes = 43 -- Это позиция начала данных. В первых 42Б идёт информация о протоколе.
	local endNumBytes = 52
    -- сюда мы пришли уже прочитав метаинформацию, что нахоится в начале каждоый строки tcpdump. И со смещенным курсором уже на данные соответствующие реальному кадру Ethernet.
	local some_line = file:read(frame.captured_length) -- вероятно нам не нужно читать всё. Достаточно просто прочитать 42Б (Ethrnet+IP+UDP headers) И плюс первые N байт данных. В нашем случае 42Б + 10Б = 52Б
    print('type(some_line) = ' .. type(some_line))
	-- local some_line = file:read(frame.endNumBytes) -- как-то так.

	if not some_line then
		print('Function read_common() - some_line is False')
		return false
	end

    	-- print('some_line = ' .. some_line)
	local line_as_hex_sequence = Struct.tohex(some_line, false, ":") -- Из прочитанной банарной строки, формируем hex строку с разделителем : 
	print('line_as_hex_sequence = ' .. line_as_hex_sequence)

	local position = 0
	local splited_table = {} -- формируем массив строк. Где каждый элемент будет hex значением.
	for i in string.gmatch(line_as_hex_sequence, "[^:]+") do
		position = position + 1
		splited_table[position] = i
	end

	local protocolFromRow = splited_table[24] -- Это позиция отвечающая за протокол(позиция в хидере записи tcpdump). Нас интересует UDP - а это в hex - 11.
	print("splited_table[24] = " .. protocolFromRow .. ' type(protocolFromRow) = ' .. type(protocolFromRow))
	if protocolFromRow ~= '11' then
		print("!!!!!!!!!!!!!!!!!!!!!!!!Протокол не соответствует udp пропускаем!!!!!!!!!!!!!!!!!!!!!!!!")
		return true
	end

    -- Б`ольшая часть оставшегося, то разбор строки. И приобразование в num. Т.к. если это было бы реальным числом то мы бы прочитали примерно так Struct.pack("<I4", magic)
	local target_array_with_num = {}
	local ordered_position = 1
	for i = startNumBytes, endNumBytes do
		local got_val = splited_table[i]
		if got_val == nil then
			got_val = 0 --а может -1???
		end
		target_array_with_num[ordered_position] = got_val
		ordered_position = ordered_position + 1
	end

    -- Исключительндо для вывода и обучения/изучения.
    local tmpp_strr_res = ''
    for k,v in pairs(target_array_with_num) do
        tmpp_strr_res = tmpp_strr_res .. string.char('0x' .. v)
    end
    print('tmpp_strr_res = ' .. tmpp_strr_res)


	local resultHexString = table.concat(target_array_with_num, ":")
	print("resultHexString = " .. resultHexString)

	local resultBinaryStr = Struct.fromhex(resultHexString, ":")
	print("resultBinaryStr = " .. resultBinaryStr)

    print(tonumber(resultBinaryStr)) -- Вот оно число, что мы будем суммировать. Еще раз - число полученное из строки. Т.е. nc присылает символьные числа. Числа как ASCII символы.

	local fields = { Struct.unpack('<b b b b b b b b b b', resultBinaryStr) }
	print(fields[1] .. ' ' .. fields[2] .. ' ' .. fields[3])
    --local fields = { Struct.unpack('<I4 I4 I4', resultBinaryStr) }
    --print(fields[1] .. ' ' .. fields[2] .. ' ' .. fields[3])
    --local fields = { Struct.unpack('<I4 I4 xI4', resultBinaryStr) }
    --print(fields[1] .. ' ' .. fields[2] .. ' ' .. fields[3])
    --[[
    ASCII, decimal, hexadecimal, octal, and binary conversion table
    0   48  30  60  110000 ---- Символ 0 в ASCII имеет номер 0х30
    1   49  31  61  110001
    2   50  32  62  110010
    3   51  33  63  110011
    4   52  34  64  110100
    5   53  35  65  110101
    6   54  36  66  110110
    7   55  37  67  110111
    8   56  38  70  111000
    9   57  39  71  111001
    ]]--
	
    return true
end

----------------------------------------
-- the function to parse individual records
parse_rec_header = function(funcname, file, file_settings, frame)
    dprint2(funcname,": parse_rec_header() called")

    local line = file:read(file_settings.rec_hdr_len)
    print(' Position in file after read header of row (was read rec_hdr_len = 16B)  = ' .. file:seek())

    -- it's ok for us to not be able to read it, if it's end of file
    if not line then return false end

    -- this is: time_sec, time_usec, capture_len, original_len
    local fields = { Struct.unpack(file_settings.rec_hdr_patt, line) } --'< I4 I4 I4 I4'

    -- sanity check; also note that Struct.unpack() returns the fields plus
    -- a number of where in the line it stopped reading (i.e., the end in this case)
    -- so we got back number of fields + 1
    if #fields ~= file_settings.num_rec_fields + 1 then
        dprint(funcname, ": parse_rec_header: failed to read the record header, got:",
               #fields, ", expected:", file_settings.num_rec_fields)
        return nil
    end

    local nsecs = fields[2]

    if file_settings.time_precision == wtap_filetypes.TSPREC_USEC then
        nsecs = nsecs * 1000
    elseif file_settings.time_precision == wtap_filetypes.TSPREC_MSEC then
        nsecs = nsecs * 1000000
    end

    frame.time = NSTime(fields[1], nsecs)

    local caplen, origlen = fields[3], fields[4]

    print(' Was read from File ::::: capture_len = ' .. caplen .. ' original_len = ' .. origlen)

    -- sanity check, verify captured length isn't more than original length
    if caplen > origlen then
        dprint("captured length of", caplen, "is bigger than original length of", origlen)
        -- swap them, a cool Lua ability
        caplen, origlen = origlen, caplen
    end

    if caplen > WTAP_MAX_PACKET_SIZE then -- local WTAP_MAX_PACKET_SIZE = 65535
        dprint("Got a captured_length of", caplen, "which is too big")
        caplen = WTAP_MAX_PACKET_SIZE
    end

    frame.captured_length = caplen
    frame.original_length = origlen

    frame.flags = wtap_presence_flags.TS + wtap_presence_flags.CAP_LEN -- for timestamp|cap_len

    print('frame.captured_length = ' .. frame.captured_length .. '   frame.original_length = ' .. origlen)
    print('wtap_presence_flags.TS =' .. wtap_presence_flags.TS .. '')
    dprint2(funcname,": parse_rec_header() returning")
    return true
end



--------------------------------------------------------------------------------
-- file writer handling functions for Wireshark to use
--------------------------------------------------------------------------------

-- file encaps we can handle writing
local canwrite = {
    [ wtap_encaps.NULL ]        = true,
    [ wtap_encaps.ETHERNET ]    = true,
    [ wtap_encaps.PPP ]         = true,
    [ wtap_encaps.RAW_IP ]      = true,
    [ wtap_encaps.IEEE_802_11 ] = true,
    [ wtap_encaps.MTP2 ]        = true,
    [ wtap_encaps.MTP3 ]        = true,
    -- etc., etc.
}

-- we can't reuse the variables we used in the reader, because this script might be used to both
-- open a file for reading and write it out, at the same time, so we cerate another file_settings
-- instance.
-- set the file_settings for the little-endian version in magic_spells
local function create_writer_file_settings()
    dprint2("create_writer_file_settings called")
    local t = magic_spells.swapped

    local file_settings = new_settings()

    -- the magic_values/spells table uses the same key names, so this is easy
    for k,v in pairs(t) do
        file_settings[k] = v
    end

    -- based on endianness, set the file_header and rec_header
    -- and determine corrected_magic
    if file_settings.endianness == ENC_BIG_ENDIAN then
        file_settings.file_hdr_patt = '>' .. FILE_HEADER_PATT
        file_settings.rec_hdr_patt  = '>' .. file_settings.rec_hdr_patt
        file_settings.corrected_magic = file_settings.magic
    else
        file_settings.file_hdr_patt = '<' .. FILE_HEADER_PATT
        file_settings.rec_hdr_patt  = '<' .. file_settings.rec_hdr_patt
        local m = Struct.pack(">I4", file_settings.magic)
        file_settings.corrected_magic = Struct.unpack("<I4", m)
    end

    file_settings.rec_hdr_len = Struct.size(file_settings.rec_hdr_patt)

    return file_settings
end

----------------------------------------
-- The can_write_encap() function is called by Wireshark when it wants to write out a file,
-- and needs to see if this file writer can handle the packet types in the window.
-- We need to return true if we can handle it, else false
local function can_write_encap(encap)
    dprint2("can_write_encap() called with encap=",encap)
    return canwrite[encap] or false
end

local function write_open(file, capture)
    dprint2("write_open() called")

    local file_settings = create_writer_file_settings()

    -- write out file header
    local hdr = Struct.pack(file_settings.file_hdr_patt,
                            file_settings.corrected_magic,
                            file_settings.version_major,
                            file_settings.version_minor,
                            file_settings.timezone,
                            file_settings.sigfigs,
                            capture.snapshot_length,
                            wtap2pcap(capture.encap))

    if not hdr then
        dprint("write_open: error generating file header")
        return false
    end

    dprint2("write_open generating:", Struct.tohex(hdr))

    if not file:write(hdr) then
        dprint("write_open: error writing file header to file")
        return false
    end

    -- save settings
    capture.private_table = file_settings

    return true
end

local function write(file, capture, frame)
    dprint2("write() called")

    -- get file settings
    local file_settings = capture.private_table
    if not file_settings then
        dprint("write() failed to get private table file settings")
        return false
    end

    -- write out record header: time_sec, time_usec, capture_len, original_len

    -- first get times
    local nstime = frame.time

    -- pcap format is in usecs, but wireshark's internal is nsecs
    local nsecs = nstime.nsecs

    if file_settings.time_precision == wtap_filetypes.TSPREC_USEC then
        nsecs = nsecs / 1000
    elseif file_settings.time_precision == wtap_filetypes.TSPREC_MSEC then
        nsecs = nsecs / 1000000
    end

    local hdr = Struct.pack(file_settings.rec_hdr_patt,
                            nstime.secs,
                            nsecs,
                            frame.captured_length,
                            frame.original_length)

    if not hdr then
        dprint("write: error generating record header")
        return false
    end

    if not file:write(hdr) then
        dprint("write: error writing record header to file")
        return false
    end

    -- we could write the packet data the same way, by getting frame.data and writing it out
    -- but we can avoid copying those bytes into Lua by using the write_data() function
    if not frame:write_data(file) then
        dprint("write: error writing record data to file")
        return false
    end

    return true
end

local function write_close(file, capture)
    dprint2("write_close() called")
    dprint2("Good night, and good luck")
    return true
end

-- ok, so let's create another FileHandler object
-- we could have done in this in the same FileHandler we created earlier (they can be both
-- readers and writers at the same time), btu for testing purposes this does it separately)
local fh2 = FileHandler.new("Lua-based PCAP writer", "lua_pcap2", "A Lua-based file writer for PCAP-type files","wms")

-- set above functions to the FileHandler
fh2.can_write_encap = can_write_encap
fh2.write_open = write_open
fh2.write = write
fh2.write_close = write_close
fh2.extensions = "pcap;cap" -- this is just a hint

-- and finally, register the FileHandler!
register_filehandler(fh2)

dprint2("Second FileHandler registered")
