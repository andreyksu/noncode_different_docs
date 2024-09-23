package ru.annikonenkov.pair3;

public class PairTest {

	public static void main(String[] args) {
		// Пара(Пар с фруктами)
		Pair<? extends Pair<? extends Fruit>> p = new Pair<>(new Pair<>(new GoldenApple("GA1_1"), new Fruit("F1_1")), new Pair<>(new GoldenApple("GA1_2"), new Orange("O1_2")));
		
		// А здесь Пара(Пар с Любыми объектами).
		Pair<? super Pair<? super Fruit>> p1 = new Pair<>(new Pair<>(new Object(), new Fruit("F2_1")), new Pair<>(new GoldenApple("GA2_2"), new Orange("O2_2")));

		Pair<Object> poo = new Pair<>(new Object(), new Object());
		Pair<Grass> pg = new Pair<>(new Grass("Grass1"), new Grass("Grass2"));
		Pair<Fruit> pf = new Pair<>(new Fruit("Fruit1"), new Fruit("Fruit2"));
		Pair<Apple> pa = new Pair<>(new Apple("Apple1"), new Apple("Apple2"));
		Pair<Orange> po = new Pair<>(new Orange("Orange1"), new Orange("Orange2"));
		Pair<GoldenApple> pga = new Pair<>(new GoldenApple("GreenApple1"), new GoldenApple("GreenApple2"));

		maethodd(pg);
		System.out.println(pg); // First = GreenApple_3 second = Grass2
		maethodd(pf);
		System.out.println(pf); // First = GreenApple_3 second = Fruit2
		// maethodd(pga); // Не разрешено.

	}

	private static void maethodd(Pair<? super Fruit> pf) {
		pf.setFirst(new GoldenApple("GreenApple_3"));
		// Всё логично. Мы можем сюда передать пару из Объектов но положить можем только
		// то, чем ограничились фрукты и ниже.
	}

}

class Grass {
	private final String nameString;

	public Grass(String aName) {
		nameString = aName;
	}

	public void meth(Object o) {
		System.out.println("Obj in Grass");
	}

	public String toString() {
		return nameString;
	}
}

class Fruit extends Grass {
	public Fruit(String aName) {
		super(aName);
	}

	public void meth(String o) {
		System.out.println("Strr in Fruit");
	}

	public void meth(Object o) {
		System.out.println("Obj in Fruit");
		this.meth(o.toString());
	}

	public String toString() {
		return super.toString();
	}
}

class Apple extends Fruit {
	public Apple(String aName) {
		super(aName);
	}

	public String toString() {
		return super.toString();
	}
}

class GoldenApple extends Apple {
	public GoldenApple(String aName) {
		super(aName);
	}

	public String toString() {
		return super.toString();
	}
}

class Orange extends Fruit {
	public Orange(String aName) {
		super(aName);
	}

	public String toString() {
		return super.toString();
	}
}
