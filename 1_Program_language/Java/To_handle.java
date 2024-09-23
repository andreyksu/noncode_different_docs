/*
    Тестирование безопасности: nmap, Nessus, OWASP ZAP
    
    Что мы хотим получить как результат работы?
        Прокликать без понимания, одно.
        Осознанное тестирование, с доверительными результатами, это другое.
    
    Прохождение ПМИ - результат только поверхностное понимание работы софта.
        Не подлежит установке на объект для эксплуатации.
        Не подлежит отправке на МВИ только ПМИ и на устранение замечаний.
        
    
    
*/
InputStreamReader (byte -> char)
OutputStreamWriter (char -> byte)

Core Java
    Lambda/Stream
---        Прочитать/набить руку
    Reflection
---        Вообще вспомнить/прочитать
    InnerClass
    Generic
    Thread
        Набить руку [Пока просто прочитал и то не всё]
    I/O NIO

Additional
    JUnit 5 
    Lambock
    XML (namespace) , JaxB, Json
    Spring JDBC
    Kafka
    GRPC

//-----------------------------------------------------------------I/O----------------------------------------------------------------

private String readFromInputStream(InputStream inputStream) throws IOException {
    StringBuilder resultStringBuilder = new StringBuilder();
    try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) { //    BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), "UTF-8"));
        String line;
        while ((line = br.readLine()) != null) {
            resultStringBuilder.append(line).append("\n");
        }
    }
  return resultStringBuilder.toString();
}

// Обработка исключений до try с ресурсами.
FileInputStream fis = null;
try {
    fis = new FileInputStream("file.txt");
    // Чтение файла...
} catch (FileNotFoundException e) {
    System.err.println("Файл не найден: " + e.getMessage());
} catch (IOException e) {
    System.err.println("Ошибка ввода-вывода: " + e.getMessage());
} finally {
    if (fis != null) {
        try {
            fis.close();
        } catch (IOException e) {
            System.err.println("Ошибка при закрытии файла: " + e.getMessage());
        }
    }
}

// Копирование файла.
public void copyFile(String sourcePath, String destPath) throws IOException {
    try (InputStream in = new FileInputStream(sourcePath);
         OutputStream out = new FileOutputStream(destPath)) {
        
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = in.read(buffer)) != -1) {
            out.write(buffer, 0, bytesRead);
        }

    } catch (FileNotFoundException e) {
        throw new IOException("Файл не найден: " + e.getMessage(), e);
    } catch (IOException e) {
        throw new IOException("Ошибка копирования файла", e);
    }
}


//---------------------------NIO
//------------Буферы (Buffers)
ByteBuffer buffer = ByteBuffer.allocate(1024); // Выделение буфера

// Запись в буфер
buffer.put("Hello".getBytes());

// Чтение из буфера
buffer.flip(); // Переключаем в режим чтения
while (buffer.hasRemaining()) {
    System.out.print((char) buffer.get());
}

//============ 
/*
FileChannel — работа с файлами. FileChannel нельзя переключить в неблокирующий режим.
DatagramChannel — канал для работы по UDP-соединению
SocketChannel — канал для работы по TCP-соединению
ServerSocketChannel содержит в себе SocketChannel и схож с принципом работы веб-сервера
*/
RandomAccessFile aFile = new RandomAccessFile("C:/javarush/file.txt", "rw");
FileChannel inChannel = aFile.getChannel();

ByteBuffer buf = ByteBuffer.allocate(100);
int bytesRead = inChannel.read(buf);

while (bytesRead != -1) {
  System.out.println("Read " + bytesRead);
  buf.flip(); // Позволяет из буффера извлечь данные. Подготавливает буффер для извлечения из него данных.
	  while(buf.hasRemaining()){
	      System.out.print((char) buf.get());
	  }
  buf.clear(); // Нужно перед записью в буффер. Т.е. перед чтением в беффер. Т.е. сбрассывает внутренние указатели в беффере.
  bytesRead = inChannel.read(buf);
}
aFile.close();
//============

//------------Каналы (Channels) - Channel - является двух-сторонним. Поддерживает асинхронный поток данных как в режиме блокировки, так и без блокировки.
// Чтение файла
try (FileChannel channel = FileChannel.open(Paths.get("file.txt"))) {
    ByteBuffer buffer = ByteBuffer.allocate(1024);
    while (channel.read(buffer) > 0) {
        buffer.flip();
        // Обработка данных
        buffer.clear();
    }
}

// Запись в файл
try (FileChannel channel = FileChannel.open(
    Paths.get("output.txt"), 
    StandardOpenOption.CREATE, 
    StandardOpenOption.WRITE)) {
    
    ByteBuffer buffer = ByteBuffer.wrap("Hello NIO".getBytes());
    channel.write(buffer);
}
//------------Селекторы (Selectors) Селекторы — это ключевой компонент Java NIO, позволяющий одному потоку мониторить множество каналов (Channels) на предмет готовности к операциям ввода-вывода. Это основа неблокирующего и высокопроизводительного сетевого программирования.

/*
1. Для чего нужны селекторы?
    - Серверы с 10k+ соединениями (например, чат-серверы)
    - Эффективное управление множеством соединений без создания потока на каждое.
    - Избежание блокировок при работе с сокетами.
    - Оптимизация ресурсов (1 поток вместо N потоков для N соединений).

2. Как работают селекторы?
    - Каналы регистрируются в селекторе.
    - Селектор мониторит зарегистрированные каналы.
    - Когда канал готов к операции (чтение/запись/подключение), селектор сообщает об этом.
    - Приложение обрабатывает готовые каналы в одном потоке
    
5. Важные нюансы
    configureBlocking(false)
        Каналы должны быть в неблокирующем режиме для работы с селектором.
    selectedKeys() и удаление ключей
        Ключи нужно удалять после обработки, иначе они будут обрабатываться повторно.
    Производительность
        Селекторы эффективны при множестве соединений с низкой активностью.
        Для высоконагруженных систем лучше использовать Netty или Project Loom.
    Обработка ошибок
        Всегда проверяйте key.isValid() перед операциями
*/

Selector selector = Selector.open(); // Создание селектора
SocketChannel channel = SocketChannel.open();
channel.configureBlocking(false); // Неблокирующий режим
SelectionKey key = channel.register(selector, SelectionKey.OP_READ); // Регистрация интереса на чтение


//-----------------------------------------------------------------Args of Method-----------------------------------------------------


/*
    Шилдт, "Подробный анализ передачи аргументов"
        При передаче методу ссылки на объект сама ссылка передаётся с примененеием вызова по значению.
            Но поскольку передаваемое значение относится к объекту, копия этого значения по прежнему будет ссылаться на тот же объект, что и соответствуюющий аргумент.
*/
String st = new String("Outer");
newLink(st); 
/*
    В st по прежнему будет Outer. Т.к. передаётся ссылка, а ссылка передаётся по значению, т.е. создаётся внутри метода новая ссылка. У неё мы и меняем объект. А исходная ссылка остаётся с прежним объектом
*/

public static void newLink(String aSt) { //Создали еще одну ссылку на целевой объект.
	String i_st = new String("InnerOfMethod"); 
	aSt = i_st; //Созданной ссылке задали новый объект. Теперь новая ссылка указывает на новый объект. А вот ссылка st по прежнему указывает на исходный объект.
}

//-----------------------------------------------------------------Generic------------------------------------------------------------

/*
    Лучше всего параметризацию рассматривать в части класса Pair<T> и допустим Иерархии Фруктов и/или Овощей.
    Куда лучше понимается и ограничения и др. вещи.
    
    Допустим, почему при Pair<? super Fuit> разрешено класть Apple, получая при этом пару какого-то Объекта и Apple.
        Да можно сделать Pair<? super Fuit> po = new Pair<Object>(); и положив туда все что ниже Fruit - получим пару Объекта и Apple.
        Допустим здесь работаем с туристическими принадлежностями. Нужно в поход взять пару предметов. Какой-то объект (нож/верёвка) и Фрукт.
    
    И то что из такого метода как method(Pair<? super Fuit> pf) не нужно что-то возвращать. Достаточно, что то в нём сделать и всё.
        Т.е. нужно void method(Pair<? super Fuit> pf){
                            //work with pf. Делаем и меняем объект по ссылке. И при этом возвращать не нужно из метода что либо.
                        }
    
    Или можно рассмотреть Ящик с конкретными фруктами.
        Почему Ящик<Яблоки> не есть Ящик<Апельсины>. Но Ящик<Яблоки> соотносится с СпецЯщик<Яблоки>.
*/
  
/*  
2. Интересный подход. Когда в параметризованном методе с Pair<?> мы не возвращаем тип с Pair<?>
    А работаем внутри этого метода со ссылкой и дальше при выходе из метода работаем с невозврщаемым объектом Pair<?> а с сылкой которую передали и знаем их тип.
*/  
    public class PairTest {

	public static void main(String[] args) {
		Pair<? extends Number> pi = getPair(1, 2.2);
		Number inttf = pi.getFirst();
		Number intts = pi.getSecond();
		var pn = setAnddGetPair(pi); // Вот передали и не обязательно тут было бы пользоваться возвращённой ссылкой. Можно и продолжать ползоваться Pi
		System.out.println(pn == pi); // true
        // Но вот у pn - мы не сможем получить нормальный тип. А у pi - сможем т.к. у него всё известно.
        
        Pair<? extends Fruit> pf = new Pair<>(new Orange(), new Apple());
		setAnddGetPair(pf);
	}

	public static <T> Pair<T> getPair(T aFirst, T aSecond) {
		return new Pair<>(aFirst, aSecond);
	}

	public static Pair<?> setAnddGetPair(Pair<?> p) { // Здесь для примера возврат. Но можно не возвращать. Т.к. меняется исходный объект по ссылке.
		return setAndGetPair(p);
	}

	public static <T> Pair<T> setAndGetPair(Pair<T> p) { // Метод захвата переменной типа.
		T f = p.getFirst();
		T s = p.getSecond();
		p.setFirst(s);
		p.setSecond(f);
		return p; // Можно не возвращать, т.к. мы поработали с сылкой и все изменения уже доступны и видны в ней.
	}

}
class Fruit {
}

class Apple extends Fruit {
}

class Orange extends Apple {
}



/*
Между Pair<S> и Pair<T> нет никаких отношений наследования, как бы нестроились друг с другом обобщеннные типы S и T

Pair<Fruit> a = new Pair<Apple> // Запрещено.
//Пара фруктов не равна паре яблок, т.к. там может быть пара апельсинов.

List<Fruit> l = new ArrayList<Fruit>(); // Разрешено. 
// Ящик с фруктами и конкретный вид ящика с фруктами
*/


//-----------------------------------------------------------------Coding-------------------------------------------------------------

/*
    Хорстман стр. 83. 10изд.

    Раньше char описывал один символ. А теперь символ может быть описан двумя char (Unicode).
    char charr = '\u2122';
    
    У string length - возвращает число "кодовых ЕДИНИЦ" для целевой строки. (В кодировке UTF-16)
    targetString.length(); // возвращает количество "кодовых ЕДИНИЦ". Для сурагатных символов в одном символе/кодовой точке две кодовых единицы
    targetString.codePointCoutn(0, targetString.length()); // Число "кодовых ТОЧЕК".   
    
    targetString.charAt(n); //возвращает кодовую единицу на позиции n [0, len-1]. 
    targetString.codePointAt(n); //возвращает кодовую точку.
    
    
    //Используйте кодовые единицы, когда работаете только с символами BMP
    Кодовая единица это 16-битное значение char. 
    Кодовая точка - полные значения симвовлов Unicode (могут быть 32-бита) - для сурогатных символов.
    
    Кодовая точка состоит из кодовых единиц???
*/

//-----------------------------------------------------------------Class Loader-------------------------------------------------------

/*
1. В рамках одного классЛоадера (ClassLoader context) существует лишь один экземпляра класса SomeType.class.
    Следовательно SomeType.getClass() или SomeType.class у двух экземпляров одного типа с операцией сравнения "==" будет давать true. Т.к. они ссылаются на один экземпляр Class<SomeType>.
    Т.е. получая class у инстенсов и сравнивая их мы будем проверять а не указывают ли ссылки их классов на один объект класса (т.е. не одного ли они типа).
2. Если два класслоадера загрузили один класс, то == будет возвращать false.


    https://java-online.ru/java-classloader.xhtml

    ClassLoader
    
    Bootstrap ClassLoader       (Loads core Java classes (rt.jar and other libraries in $JAVA_HOME/jre/lib); Written in native code (not Java); 
       ↑                        Parent of all other ClassLoaders; Has no parent itself) [rt.jar]
       ↑
    Extension ClassLoader       (Loads classes from Java extension directories ($JAVA_HOME/jre/lib/ext); Child of Bootstrap ClassLoader) [jre/lib/ext]
       ↑ 
    System/Application ClassLoader (Loads application-level classes from the classpath; Child of Extension ClassLoader) [CLASSPATH]
       ↑
   Custom ClassLoader(s)
   
   Здесь каждый классЛоадер на своём уровне производит поиск не только уже загруженных но поиск в своих целевых местах с целью загрузить класс/байткод.
   Java – язык с отложенной загрузкой кода.
    Главный класс приложения всегда загружается системным загрузчиком (это который указывается при запуске т.е. содержит main)
        Первоначально загружается только один класс – тот, который передан в качестве параметра утилите «java». Как только код этого класса обращается к какому-то другому классу (любым способом: вызовом конструктора, обращением к статическому методу или полю), загружается другой класс. По мере выполнения кода, загружаются всё новые и новые классы. Ни один класс не загружается до тех пор, пока в нем не возникнет реальная потребность. Такое поведение заложено в стандартный системный загрузчик.
   
   Java uses delegation hierarchy for class loading:
        When a class needs to be loaded, the JVM first asks the current ClassLoader
        The ClassLoader delegates the request to its parent before attempting to load the class itself
        This continues up to the Bootstrap ClassLoader
        If no parent can load the class, the current ClassLoader attempts to load it
    
    
    protected Class<?> loadClass(String name, boolean resolve) // Loads the class with the specified binary name                
    protected Class<?> findClass(String name) // Finds the specified class (to be implemented by custom ClassLoaders)
    
    loadClass()
        Default implementation in ClassLoader class
        Follows the parent-first delegation model
        Contains the complete class loading algorithm:
            Checks if class is already loaded (findLoadedClass())
            Delegates to parent classloader
            Only if parent can't find it, calls findClass()
    
    findClass()
        Responsibility: Contains the actual class loading logic
        Meant to be overridden by custom classloaders
        Doesn't implement any delegation - focuses only on finding the class
        Must call defineClass() to convert bytes into Class object
        
        
    Override findClass() when:
        You want to load classes from non-standard locations
        You want to maintain standard delegation behavior
        Example: Loading classes from database or encrypted files

    Override loadClass() when:
        You need to modify delegation behavior (e.g., child-first)
        You need complete control over loading process  
        Example: Implementing OSGi-like class isolation
    
    Unique Classes: The same class loaded by different ClassLoaders are treated as different types by the JVM
    
    
    How Modules Affect Class Loading
        1. Module-Aware ClassLoaders
        The built-in classloaders became module-aware:
            Bootstrap ClassLoader: Loads java.base and other platform modules
            Platform ClassLoader: Replaces the Extension ClassLoader, loads other platform modules
            Application ClassLoader: Loads application modules

        2. Modified Delegation Model
            Module resolution changes the delegation flow:
                First finds the appropriate module containing the class
                Then delegates to the module's classloader
                
                
    - Так исключение ClassNotFoundException возникает при динамической загрузке класса во время выполнения программы, когда загрузчики не могут найти требуемый класс ни в кэше, ни по пути нахождения классов.
    - А вот ошибка NoClassDefFoundError является более критичной и возникает в том случае, когда во время компиляции искомый класс был доступен, но не виден во время выполнения программы. Это может произойти, если в поставку программы забыли включить библиотеку, которую она использует.
                
    Загрузка байт-кода.
    Создание экземпляра класса Class.
    Загрузка родительских классов.
        Если родительские классы не нашли. то считается текущий класс - не загруженным.
    Связывание/линковка
        Verification, происходит проверка корректности полученного байт-кода.
        Preparation, выделение оперативной памяти под статические поля и инициализация их значениями по умолчанию (при этом явная инициализация, если она есть, происходит уже на этапе инициализации).
        Resolution, разрешение символьных ссылок типов, полей и методов.
        
        
    
*/

/*

Что происходит "под капотом" (JVM)
new в байт-коде:
- Инструкция new выделяет память (но ещё не вызывает конструктор);
- dup дублирует ссылку на стеке;
- invokespecial вызывает конструктор.

Пример байт-кода для MyClass obj = new MyClass();:
    NEW MyClass          // выделение памяти
    DUP                  // копирование ссылки
    INVOKESPECIAL MyClass.<init>()  // вызов конструктора
    ASTORE 1             // сохранение в переменную obj
    
    
Итог
    - Память выделяется → поля = значения по умолчанию.
    - Выполняется цепочка конструкторов (родители → дети).
    - Инициализируются поля и блоки в порядке объявления.
    - Запускается тело конструктора.
    - Ссылка возвращается в переменную.
*/

//-----------------------------------------------------------------Lambda-------------------------------------------------------------

/*
    Переменные определённые в объемлющей области действия лямбда-выражения, достпуны внутри лямбда-выражения.
    Лямбда выражение имеет доступ к сcылке this (явно и неявно) которая ссылается на вызывающей экземпляр, включающего лямбда-выражение.
    Лямбда выражение не имеет собственного this.

*/

//-----------------------------------------------------------------Threads-------------------------------------------------------------

/*
    Многопточка.
        Если у объекта есть два метода f и g с synchronized то если один поток зашел в один из этих методов, то второй не может зайти в этот метод и во второй метод.
        
        У объекта есть монитор, который является частью этого объекта.
        При вызове метода synchronized у данного объекта, объект переходит в состояние блокировки. И пока поток не выйдет из этого метода, другие потоки не могут зайти в другие synchronized методы этого объекта.
        
        Читающий и пишущий потоки должны синхранизироваться по одному объекту.
        
        Аналогично и для статических методов с synchronized.
        
    Runnable и run() это задачи.
        Нужно и рассматривать как задачу при размышлении.
    
    Объект Thread не удаляется сборщиком мусора.
        По мнению Эккеля - это конкретная реализация выполнении задачи. Просто реализация. Низкоуровневое представление.
    
    Executor вместо Thread.
        ExecutorService.
            CachedThreadPool - создаёт один поток для каждой задачи.
            
            ExecutorService exec = Executors.newCachedThreadPool(); //ExecutorService exec = Executors.newFixedThreadPool(5); - предпочтительнее чем newCachedThreadPool()
            for(int i = 0; i < 5; i++)
                exec.execute(new LiftOff());
            exec.shutdown(); // Предотвращает передачу новых задач объекту Executor.
    
        Создание потока дорого по времени, по этому лучше создать один раз набор потоков и дальше их использовать для задач. Для этих задач подходит Executors.newFixedThreadPool(5);
            Все пулы повторно используют те же потоки.
            
            
        SingleThreadExecutor - использует один поток. И все задачи переданные ему ставит в очередь и выполняется одна за одной, после окончания предыдущей.
            Удобно либо для серии коротких задач, либо для одной долгой задачи для просшуливания порта.
            А так как есть очерёдность, серию задач можно выполнить без заботы о синхранизации допустим если речь идёт об обработки одного файла.
        
    У Daemon - finally не выполняется при завершении потока.
        Но вот у обычного потока finally выпоняется.
        
        
    Runnable    -> Callable
    run         -> call
    execute     -> submit
            
    Collable - задача аналогичная Runnable но умеет возвращать значение.
        execute -> submit
        run -> call
        
        У Future  get() блокируется до готовности.
        

    thr.join() - чтоб дождаться окончания thr
    
    
    Для обработки неперехваченных исклчючений в потоке
        MyUncaughtExceptionHandler implements Thread.UncaughtExceptionHandler с реализациекй метода uncaughtException(Thread t, Trhowable e){}
        
        Формирование фабрики HandlerThreadFactory implements ThreadFacotry где для потока указывается обработчик thr.setUncaughtEcxeptionHandelr(new MyUncaughtExceptionHandler())
        И указание этой фабрики  Executors.newCachedThreadPool(new HandlerThreadFactory())
        
        Т.о. метод uncaughtException будет перехватывать исключения. 
*/

    private ReentrainLock lock = new ReentraintLock();
        boolean captured = false;
        try{
            captured = lock.tryLock(2, TimeUnit.SECONDS); //в течении 2х сек будет пытаться занять лок. Вероятно хорошая возможность для избегания вечной блокировки в отдельных задачах. Или для возможности потоком еще поработать.
        }catch(InterruptedExctption e){
            throw new RintimeExctption(e);
        }
        try{
            do something;
        }finaly{
            if(captured)
                lock.unlock();
        }


/*
    volatile - обеспечивает только видимость между потоками (т.е. говорим не размещать в память локального потока, а сразу писать в общее место)
        Но никак не говорит и не влияет на атормарость операции. Атомарность это когда планировщик не может прервать посередине выполнение.
        
        
    Для целей напротив создать для каждого потока своё экземпляр переменной это использоватине 
        ThreadLocal
        
        
    sleep() - не освобождает блокировку. Нужно использовать wait()
*/

/*
    Завершение выполняется либо путём проверки и изменения значения поля статического и волатильного.
    Либо в таком виде thr.interrupt(). При этом будет возбуждено исключение для потока если он уже заблокирован или пытается выполнить блокирующую операцию (как пример sleep())
    
    try{
        while (!Thread.interapted(){
            try{
                do target deals
            }finally{
                do finish
            }            
        }
    }catch(InterraptedException e){
        todo
    }
    
    ...
    thr.interrupt();
    
    Эккель Глава.21 стр. 950
    Если поток находится в ожидании IO то исключения не будет. И поток не прервётся.
        Т.е. на io можно подвесить многопоточную программу. По этому одним из подходов - закрытие io.
    Или если поток ожидает синхронизированную блокировку (т.е. пытается установить синхранизированную блокировку) то исключения тоже не будет. И поток не прервётся.

*/

//-----------------------------------------------------------------Современные подходы ----------------------------------------------------------
/*
Вывод
- Используйте высокоуровневые API (java.util.concurrent).
- Избегайте shared mutable state.
- Предпочитайте иммутабельность и атомарные операции.
- Для сложных сценариев – CompletableFuture, StampedLock, ForkJoinPool.
*/

//CompletableFuture. В отличие от Future из java.util.concurrent, CompletableFuture неблокирующий и поддерживает callback'и.
//------------------- Простое создание.
CompletableFuture<String> future = new CompletableFuture<>();
future.complete("Результат"); // Завершаем вручную

//------------------- Запуск асинхронной задачи
CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
    System.out.println("Запущено в фоне");
});

// С собственным Executor
ExecutorService executor = Executors.newFixedThreadPool(2);
CompletableFuture<Void> customFuture = CompletableFuture.runAsync(() -> {
    System.out.println("Запущено в кастомном пуле");
}, executor);

//------------------- Асинхронное вычисление с результатом
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "Результат вычисления";
});

// Получение результата (блокирует поток!)
String result = future.get(); // или future.join() (без checked исключений)


//------------------- thenApply() – преобразование результата
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Hello")
    .thenApply(s -> s + " World") // "Hello World"
    .thenApply(String::toUpperCase); // "HELLO WORLD"

CompletableFuture.supplyAsync(() -> fetchData())
    .thenApplyAsync(data -> transform(data), executor)
    .exceptionally(ex -> handleError(ex));

//Parallel Stram
List<Integer> results = dataList.parallelStream()
    .filter(x -> x > 0)
    .map(x -> x * 2)
    .collect(Collectors.toList());

//-----------------------------------------------------------------Test Plan----------------------------------------------------------

/*
IEEE 829

Мастер тест план — это комплексный план тестирования. Включает высокоуровневую информацию, которая не часто меняется в ходе тестирования и требования к которой не часто пересматриваются.
Виды тест-планов
    Можно использовать разные виды, в зависимости от целей тестирования и этапа, на котором сейчас находится процесс разработки.
        Стратегический — это документ, который описывает общую QA-стратегию для проекта или организации. В нем план расписан широкими мазками: он охватывает цели и задачи тестирования, подходы, риски и ресурсы.
        Тактический — это уже более детализированный документ, который описывает тестирование конкретного продукта, проекта или релиза.
        Операционный — это документ, который описывает конкретную последовательность действий при тестировании: кто, что, когда и как должен сделать.
    Что в итоге: стратегические тест-планы определяют общие цели и методы, тактические — детализируют их для конкретных проектов, а операционные планы отражают четкие инструкции для выполнения тестов.
3. Введение
    Что соибраемся делать. Для закачика/клиента. Какие услуги предоставлвяет процесс тестирование. Виды тестирования
            +++ Цели и задачи тестирования
4. Объект тестирования
    Какие функциональные возможности будут протестированны. Краткое содержание тест-плана.
            +++ Конкретные фцнции и модули
                Производительность
                Безопасность
                Удобство использования.
            
            Что надо тестировать?
                описание объекта тестирования: системы, приложения, оборудования
5. Проблемы и риски
    Организационные: отпуска, увольнения, квалификация итд. Отсутствие мощностей
6. Функции которые нужно протестировать
    Перечень функций и время за кторые они должны быть протестированны
    
        Что будете тестировать?
            список функций и описание тестируемой системы и её компонент в отдельности
7. Функции которые не нужно тестировать
    Какие и почему.
8. Подходы
    Методы и виды тестирования. Здесь же и тест.кейсы.
            +++ Стартегия
                Методы тестирования
                    Ручное
                    Автоматизированное
                    Функциональное
                    Производительности
                    Безопасности

            Стратегия тестирования (test strategy): Высокоуровневое описание уровней тестирования, которые должны быть выполнены, и тестирования, входящего в эти уровни, для организации или программы из одного или более проектов. (ISTQB)
9. Критерии прохождения тестов.
    Наличие серьёзных багов. Критерии начала и остановки тестирования.
    Здесь по сути метрики.
10. Критерии остановки и требования для возобновления тестирования.
11. Результаты тестирования.
    Описываем результаты.
    Время, количество ошибок, количество пройденных тестов и отражения покрытия функционала.
12. Оставшиеся задачи тестирования.
    Что останется за рамками если не успеем. итд.
13. Требовния среды.
    Инструменты, окружения.
        Ресурсы и инструменты как тестирования так и диагностики.
14. Требовния по части кадров и их обучение.
        Требования к ресурсам. как человеческим так и техническим.
15. Обязанности
16. Рассписание.
17. Планирование рисков и непредвиденных обстоятельств.
18. Утверждение
19. Глоссарий

*/

//-----------------------------------------------------------------Linux-Route--------------------------------------------------------

/*
    # Получение информации по таблице маршрутизации
ip route
        192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.201 — маршрут добавленный ядром. Подсеть 192.168.1.0/24 для машины 192.168.1.201
            proto kernel – маршрут создан ядром ( proto static – маршрут добавлен администратором)
            metric – приоритет маршрута (чем меньше значение metric, тем выше приоритет). 
                    При наличии двух маршрутов с одинаковой метрикой (не стоит так делать!), ядро начинает выбирать маршруты случайным образом.
            scope
                global — маршрут доступен для любых сетей (например, default gateway). Это с использованием 'via' т.е. нужен шлюз для доступа к др. подсети.
                link — только для directly connected сетей т.е. без шлюза т.е. без 'via' (например, ARP-доступные адреса). Т.е. все ПК текущий подсети. См. ниже маршрут от ядра добавляет для локалки.
                host — маршрут только для одного IP (например, loopback).
                    ip route add 192.168.1.10 dev eth0 scope host

    # Маршруты от ядра появляются При добавлении IP.
ip addr add 192.168.1.10/24 dev eth0
    # Ядро автоматом добавляет маршрут (на основании маски подсети и Указывает scope link, потому что сеть доступна напрямую (без шлюза).)
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10

    # Просмотр маршрута до IP
traceroute 192.168.22.30
ip route get 192.168.22.30 # Проверка маршрута до 192.168.22.30
ip route show to match 192.168.22.30

    # Изменение.
ip route replace 192.168.22.0/24 via 192.168.168.254 #Чтобы изменить уже существующий маршрут
ip route change 192.168.22.0/24 via 192.168.168.254
ip route del 192.168.22.0/24
ip route del default via 192.168.1.1 dev eth0
ip route replace default via 192.168.1.2        # Чтобы изменить параметры маршрута по умолчанию

    # Добавление маршрута через шлюз и интерфейс. Т.е. через какой интерфейс доступен шлюз
route add -net 192.168.32.0/24 gw 192.168.1.1 dev eth0
ip route add 192.168.32.0/24 via 192.168.1.1 dev eth0
ip route add 192.168.226.0/23 via 192.168.215.1 dev eth0
ip route add 192.168.1.0/24 via 10.0.0.1 dev eth0

    # Добавление маршрута через шлюз: 
ip route add 172.16.10.0/24 via 192.168.1.1 
    # Добавление маршрута через интерфейс: 
ip route add 172.16.10.0/24 dev eth0
    #  Маршрут с метрикой:
ip route add 172.16.10.0/24 dev eth0 metric 100

    # Для конкретного IP
ip route add 243.143.5.25 via 192.168.1.1 
ip route add default via 192.168.1.1 dev eth0 # Объединяет две строки # ip route add default dev eth0 # ip route add default via 192.168.1.1
    # Для подсети
ip route add 192.168.22.0/24 via 192.168.168.254 dev eth0 # Добавление нового статического маршрута через 192.168.168.254. После перезапуска слетит.


# Нужно писать в файл /etc/network/interfaces
auto eth0
iface eth0 inet static
address 10.48.141.23
netmask 255.255.255.0
gateway 10.48.141.254
# Add a second default route with higher metric (lower priority)
up ip route add default via 10.0.0.1 dev eth1 metric 200

# Или так.
auto eth0:1
iface eth0:1 inet dhcp
up ip route add 192.168.226.0/23 via 192.168.215.1 dev eth0

ip -s link show eth0    # Статистика.
ip -d link show eth0    # Детальнее.

ip neigh flush dev eth0  # Очистить кэш ARP для eth0
ping 192.168.1.1         # Проверить связь
ip neigh show            # Посмотреть обновлённую ARP-таблицу

sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip addr del 192.168.1.100/24 dev eth0
sudo ip link set eth0 up   # Включить
sudo ip link set eth0 down # Выключить
sudo ip link set eth0 name wan0

link - аналог из iproute2 (соответствует L2 - канальному уровню где MAC и ARP). Работает с MAC адресами и состоянием соединения.
interface - общее название для сетевого объекта (физического или внутреннего) eth0, wlan0
device - аппаратная или программная сущность.

ip addr - сетевой уровнь (L3) IP - адреса
ip link - канальный уровнь (L2) MAC - адреса.

ip link set eth0 down
ip link set eth0 up

ip link add link eht0 name eth0.100 type vlan id 100
# VLAN - пакеты с тегом VLAN 100 приходящие на ht0 перенаправляются в eth0.100
ip link set eht0.100 up                     # Включаем
ip addr add 192.168.100.1/24 dev eth0.100   # Назначаем IP
Коммутатор тоже должен быть настроен определённым образом.
    
*/

//-----------------------------------------------------------------Coding-------------------------------------------------------------
/*
прямой          straight    [streɪt]
растягивать     stretch     [streʧ]
shutdown    |закрытие, включение
acquire     |приобретать
halt        |остановка, останавливать (stop)
iterability |прерывисто, повторяемость
entran      |абитуриент, тот кто входит
dorman      |спящий, дремлющий
more accurately [ˈækjərətlɪ]
more precisely  [prɪˈsaɪslɪ]
more exactly    [ɪgˈzæktlɪ] clearly, specifically

As such		|Союз.так же(as well);Н. по существу (in essence)

gently		|Н.нежно,мягко;осторожно();спокойно;
perilous	|рискованный(risky), опасный(dangerous)
plague		|беспокоить(bother), мучить(torment)

//------------
firm		|твёрдый(solid), жёсткий(hard), решительный(strong), надёжный (reliable)
somehow		|как-то(once), почему-то(for some reason)
instance	|безумный, сумашедший, обезумевший (mad)
fuzzy		|размытый. нечёткий.
ambiguity	|неоднозначность, двусмысленность; неясность
*/