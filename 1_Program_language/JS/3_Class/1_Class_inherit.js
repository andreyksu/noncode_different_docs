class EmptyImplementation extends Error {
  constructor(message) {
    super(message);
    this.name = "DoesnImplement";
  }
}

class A { //Родительский класс. Метод aa() не имеет реализации
	constructor (paramm){
		this.param = paramm;
	}

	aa(){
		//console.log('from aa method of A');
		throw new EmptyImplementation("Have not got implement");
	}
}

class B extends A{ //Наследник, который переопределяет метод aa()
	constructor (paramm){
		super(paramm);// Вызывает родительский конструктор.
	}

	aa(){
		// super.aa(); // Error // Пример вызова родительского метода. Закомментировал чтоб не падать по генерации исключения из базовой реализации.
		console.log('from aa method of B');
	}

	bb(){
		console.log('from bb method of B');
	}
}

class C extends A{
	constructor (paramm){
		super(paramm);
	}

	aa(){
		console.log('from aa method of C');
	}

	cc(){
		console.log('from cc method of C');
	}
}

class D extends B{
	constructor (paramm){
		super(paramm);
	}

	aa(){
		console.log('-------------------');
		super.aa(); //Вызов родительского метода.
		console.log('from aa method of D');
	}

	dd(){
		console.log('from dd method of D');
		console.log('The paramm is ' + this.param);
	}
}

let a = new A('AAA');
let b = new B('BBB');

let c = new C('CCC');
let d = new D('DDD');

console.log(a instanceof A); // true
console.log(d instanceof A); // true
console.log(d instanceof B); // false
//a.aa(); // Убрал из за дефолтной реализации будет ошибка.
d.aa(); // Вызовится реализация из B потом своя.
d.dd();

