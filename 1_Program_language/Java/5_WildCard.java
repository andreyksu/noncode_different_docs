class MammalAnimal extends Animal {
}

class WildAnimal extends MamalAnimal {
}

class FlatAnimal extends MamalAnimal {
}

class Woolf extends WildAnimal {
}

class GrayWoolf extends Woolf {
}

class Bear extends WildAnimal {
}

class WhiteBear extends Bear {
}

class Sparivatel<T extends WildAnimal> {
	private T t;

	public Sparivatel(T t) {
		this.t = t;
	}

	protected void doSomething(T aT) {
	}

	public void work_1(Sparivatel<T> spar) {// То что сюда пришло известно.
		doSomething(t);
		doSomething(spar.getT());

		spar.doSomething(spar.getT());// +++ Здесь понятно, тип точный и во время исполенния все нормально кастится.
		spar.doSomething(t);// ++++ Здесь понятно, тип точный и во время исполенния все нормально кастится.
	}

	public void work_2(Sparivatel<? extends T> spar) { // Что сюда передадут в RunTime не известно. Может быть Woolf, а может Bear - и соответственно здесь запрет на передачу В метод что есть у переменной spar.
 		doSomething(t);
		doSomething(spar.getT());
		
		// У spar в методе doSomething принимаемый параметр звучит так: принимаем какой-то из подтипов T но какой конкретно - не известно.
		//spar.doSomething(spar.getT());// --- Не даёт так сделать. Т.е. самого себя не принимает.
		//spar.doSomething(t);// --- Здесь нельзя, но по какой причине, то что это подтип по отношенитю к Т или то что это не известный тип. Скорее причина в том, что мы не знаем что приняли.
	}

	public <V extends T> void work_3(Sparivatel<V> spar) {
		doSomething(t);
		doSomething(spar.getT());

		spar.doSomething(spar.getT());// +++ Бессмыслица, но можно. Так можно, по той причине, что это известный тип и сам себя он может принять.
		//spar.doSomething(t); // --- Логично что так нельзя, т.к. здесь дочерний тип V по отношению к T. Но блин, а как же полиморфизм (ведь дочерний же - вроде как должно быть можно)
	}

	public T getT() {
		return t;
	}
}

public class Test_1 {
	public static void main(String[] args) {
		Sparivatel<Woolf> sW1 = new Sparivatel<>(new Woolf());
		Sparivatel<Woolf> sW2 = new Sparivatel<>(new Woolf());
		Sparivatel<Woolf> gW1 = new Sparivatel<>(new GrayWoolf());
		Sparivatel<Bear> sB1 = new Sparivatel<>(new Bear());
		Sparivatel<Bear> sB2 = new Sparivatel<>(new Bear());

		sW1.work_1(sW2);
		sW1.work_2(gW1);
		sW1.work_3(gW1);

	}

}

//----------------------------------------------------------------------------------------------------
class Animal_{
	public void getName() {
		System.out.println(this.getClass().toString());
	}
}

class MammalAnimal_ extends Animal_ {
}

class WildAnimal_ extends MammalAnimal_ {
}

class FlatAnimal_ extends MammalAnimal_ {
}

class Woolf_ extends WildAnimal_ {
}

class GrayWoolf_ extends Woolf_ {
}

class Bear_ extends WildAnimal_ {
}

class WhiteBear_ extends Bear_ {
}


public class Deamond{

	public static void main(String[] args) {
		List<Animal_> la = new ArrayList<>();
		la.add(new Animal_());
		la.add(new MammalAnimal_());
		la.add(new WildAnimal_());
		la.add(new Bear_());
		
		List<MammalAnimal_> lma = new ArrayList<>();		
		lma.add(new MammalAnimal_());
		lma.add(new WildAnimal_());
		lma.add(new Bear_());
		
		for (Animal_ a: lma) {
			a.getName();
		}
		
		
		//List<? extends MammalAnimal_> lmae1 = la;// +++ Так не даёт из за ограничения 

		List<? extends MammalAnimal_> lmae = lma;// Вооот тут не известно же что пришло! Внутри могут быть и Woolf и Bear и FlatAnimal. Предположим это метод void method(List<? extends MammalAnimal_> lmae) и что передали в качестве аргумента нам не известно.
		boolean add(E e); // так выглядет метод в List. Т.е. 'е' представлен как '? extends MammalAnimal_' - а что это за тип не известно
		// lmae.add(new MammalAnimal_()); // И По этой причине мы не знам что сюда можно положить. А может здесь только FlatAnimal или Cat - а мы попытаемся сюда положить/передать Bear
		lmae.get(0); // Но извлечь можем и мы знаем что там будет по крайней мере Animal_
		
		
		//List<? super Animal_> las1 = lmae; // Так не даёт из за ограничения.
		List<? super Animal_> las = la;// И тут тоже не известно что пришло! Здесь могту быть и Woolf и Bear и FlatAnimal и даже Object.
		las.add(new MammalAnimal_()); // Но здесь уже можно положить всё что что ниже Animal_.
		las.get(0); // А здесь извлекаем только Object
	}

}


//----------------------------------------------------------------------------------------------------
// Разбирается параметризация вида: BaseStream<T, S extends BaseStream<T, S> 
// Очень похоже на рекурсию. Но это не рекурсия - это ограничение накладываемое на S. Ни в коме случае не нужно думать об этом как о рекрсии.
// Stream<T> extends BaseStream<T, Strema<T>>
// IntStream extends BaseStream<Integer, IntStream>

// Вот пример String extends Comparable<String> 
// А можно так было бы объявить так Comparable<T extends Compaparable<T>> и тогда снова String exnteds Comparable<String>

public class HouseBuilder<T extends HouseBuilder<T>> { 

    private int rooms;
    private String color;

    public T setRooms(int rooms) {
        this.rooms = rooms;
        return (T) this; // Note the cast here
    }

    public T setColor(String color) {
        this.color = color;
        return (T) this;
    }

    public House build() {
        return new House(rooms, color);
    }
}

// Explanation:
// HouseBuilder<T extends HouseBuilder<T>>:This makes sure any class T extending HouseBuilder must also use itself (T) as a type argument. 
// Fluent API:The setRooms and setColor methods return T (which will be the concrete builder subtype) to enable method chaining.



// Concrete Builder
public class MyHouseBuilder extends HouseBuilder<MyHouseBuilder> { 
   // ... Additional methods specific to MyHouseBuilder
}

MyHouseBuilder builder = new MyHouseBuilder();
House myHouse = builder.setRooms(4).setColor("Blue").build(); 

// Key Points:
// The Curiously Recurring Generic Pattern (CRGP)
// Type Safety: The CRGP ensures that when you call setRooms or setColor on a concrete builder (like MyHouseBuilder), the return type is also MyHouseBuilder, maintaining type safety during method chaining.
// Not Limited to Builders:The CRGP can be applied in other scenarios where you need to express recursive type relationships for enhanced type safety within a class hierarchy.


//----------------------------------------------------------------------------------------------------
// Вообще запись вида
<R> Stream<R> map(Function<? super T, ? extends R> mapper);
// Говорит: Принимает функцию метод которой может принять значение Т, и вернуть R

//----------------------------------------------------------------------------------------------------
// Равнозначные записи:
Comparable<T>;
Comparable<T extends Comparable<T>>;

// Эта запись удовлетворяет две верхние записи
String extends Comparable<String>




// Хорстман стр. 404
// Это характерно для LocalDate который расширяет ChronoLocalDate а тот реализует Comparable<ChronoLocalDate>
// Т.о. LocalDate расширяет Comparable<ChronoLocalDate> а не Comparable<LocalDate>
// По этой причине следует ограничение задать таким образом иначе сравнивать не получится.
// public static <T extends Comparable<? super T>> T min(T[] a) ...
// Т.о. метод принимает вид int compareTo(? super T)

// В этом плане для String всё просто 
// public static <T extends Comparable<T>> T min(T[] a)

//----------------------------------------------------------------------------------------------------
public class Pair<T> {
	private T first;
	private T second;

	public Pair() {
		first = null;
		second = null;
	}

	public Pair(T first, T second) {
		this.first = first;
		this.second = second;
	}

	public T getFirst() {
		return first;
	}

	public T getSecond() {
		return second;
	}

	public void setFirst(T newValue) {
		first = newValue;
	}

	public void setSecond(T newValue) {
		second = newValue;
	}

	public String toString() {
		return "First = " + first.toString() + " second = " + second.toString();
	}
}