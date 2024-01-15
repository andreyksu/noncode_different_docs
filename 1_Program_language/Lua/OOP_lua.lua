-- -----------------------------------------------------
-- Таблица, это объект в Lua - но в единственном экземпляре.
    -- Для создания экземпяров (и унаследования свойств) - делаются ухищерения в видет TargetOuterTable:new(....). 
      -- Внутри таблицы "TargetOuterTable" создаётся новая внутренняя таблица котороая наделяется свойствами объемлющей таблицей через метатаблицу (эта метатаблица по сути является объемлющая таблица). И далее возвращается внутренная таблица в методе new.
-- Для объекта можно объявить по разному методы. Во всех трёх случаях в метод передаётся текущий объект.
-- Просто там где в объявлении colon т.е. : - там неявно передаётся self и явно указывтаь в объявлении не нужно.
-- Аналогично и при вызове. Если через colon : то автоматом передаётся self. Там где вызов через точку, там нужно принудительно передать  сам объет.
    -- В этом случае таблица уже создана и она по сути является инстансом/экземпляром по этому и передаём.
    -- Всякие new - далее по тексту нужно для создания 

-- Разумеется передача объекта в метод нужно для доступа к внутреннему состоянию таблицы.
Account = { balance=200,
            withdraw = function (self, v)
                         self.balance = self.balance - v
                         print("withdraw(...) self.balance = " .. self.balance)
                       end
          }

function Account:deposit (v)
  self.balance = self.balance + v
  print("deposit(...) self.balance = " .. self.balance)
end

function Account.deposit1 (self, v)
  self.balance = self.balance + v
  print("deposit1(...) self.balance = " .. self.balance)
end

function Account:printBalance()
  print("printBalance() self.balance = " .. self.balance)
end


Account.deposit(Account, 200.00)
Account:deposit(200.00)
Account:deposit1(200.00)
Account.deposit1(Account, 200.00)
Account:withdraw(100.00) -- Весь этот набор будет влиять на состояние полей созданных обхектов - см. ниже для b = Account:new(); b:printBalance() - после всего этого набора будет 900

-- -----------------------------------------------------

local firstTable = {a = 'aa'}
local secondTable = {b = 'bb'}
local thirdTable = {c = 'cc'}

local resTable = setmetatable(firstTable, secondTable)

-- local resTable = setmetatable(firstTable, {b = 'bb', __index = thirdTable}) - а можно так. Создаём анонимную таблицу и передаём её в качестве метатаблицы, у которой указана таблица для поиска.

secondTable.__index = thirdTable -- т.е. здесь мы у метатаблицы указываем где икать поля. А поля будем искать в другой таблица а не в метатаблице.


print(resTable.a)
print(resTable.b) -- Здесь будет nil. Т.к. для поиска неизвестных полей у метатаблицы указана таблица thirdTable
print(resTable.c) -- Т.к. метатаблица через __index ссылается на thirdTable


-- Порядок такой:
-- У ЦелевойТаблицы, указывается метатаблица. А у метотаблицы указывается в поле __index указывается таблица где будут искаться поля, в случае если у ЦелевойТаблицы не найдено запрашиваемое поле. 
    -- По этому в методе new делается так self.__init = self. Т.е. мы делаем поиск полей в объемлющей таблице если не нашли в новой созданной таблице целевого поля.
-- При этом поле __index имеет значение только для метатаблицы. Для ЦелевойТаблицы - это поле не имеет значение.
-- Т.е. firstTable.__index = thirdTable - не приведёт ни к чему.

-- More specifically, if we have two objects a and b, all we have to do to make b a prototype for a is setmetatable(a, {__index = b})
-- -----------------------------------------------------

function Account:new (o)
  o = o or {}   -- create object if user does not provide one
  setmetatable(o, self) -- Указали для внутренней таблицы в качестве метатаблицы объемлющую таблицу.
  self.__index = self   -- Для поиска указываем тоже внешнюю таблицу.
  return o
end


a = Account:new{balance = 0} -- Передали готовый объект с полем balance - что присутствует в Account - но так как в ЦелевойТаблице такое поле присутствует, поиск будет производиться в ЦелевойТаблице.
a:printBbalance() -- Даст 0
Account:withdraw(100.00) -- А это НЕ влияет на состояние объеата.
a:printBalance() -- Так же даст 0
a:deposit(100.00) -- Эквивалентно  getmetatable(a).__index.deposit(a, 100.00) -- Эквивалентно Account.deposit(a, 100.00)
-- That is, Lua calls the original deposit function, but passing a as the self parameter. So, the new account a inherited the deposit function from Account. By the same mechanism, it can inherit all fields from Account.
-- The inheritance works not only for methods, but also for other fields that are absent in the new account. Therefore, a class provides not only methods, but also default values for its instance fields

b = Account:new() -- Здесь будет создан новая таблица, т.к. мы её не передали в new. И следовательно поле balance в ЦелевойТаблице отсутствует и будет использоваться из Account т.к. 200 - т.к. именно он указан как метатаблица где будут искаться незивестные значения.
b:printBalance() -- Даст 200 (если конечно все вызовы вида (Account.deposit(Account, 200.00)) см. выше будут закомментированы)
Account:withdraw(100.00) -- А это влияет на состояние объекта b - получается что то виде статического поля???
b:printBalance()
