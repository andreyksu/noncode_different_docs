class A{
	static field = 'Static Default_A';
	arg = 'Default val of arg_A';

	constructor (arg){
		console.log("In constructor_A arg = ", this.arg);
		this.arg = arg;
	}

	static print(){
		console.log("In static method_A this = ", this); // Возвращает класс.
		console.log("In static method_A field = ", this.field); // У статик метода видно сатитк поле 'field'
		console.log("In static method_A arg = ", this.arg); // У статик метода НЕ видно обычное поле 'arg', хотя к этому времени оно уже проинициализированно.
	}

	print1(){
		console.log("In method_A this = ", this); // Возвращает объект
		console.log("In method_A field = ", this.field); // У обычного метода НЕ видно сатик поле 'field'
		console.log("In method_A arg = ", this.arg); // У обычного метода видно обычное поле поле 'arg'
	}
}

class B extends A{
	static field = 'Static Default_B';
	arg = 'Default val of arg_B';

	constructor(arg){
		super(arg);
	}

}


a = new A("new A1");
A.print();
a.print1();
console.log(a.arg); // Прямой доступ к полю.

/*
In constructor_A arg =  Default val of arg_A
In static method_A this =  [class A] { field: 'Static Default_A' }
In static method_A field =  Static Default_A
In static method_A arg =  undefined
In method_A this =  A { arg: 'new A1' }
In method_A field =  undefined
In method_A arg =  new A1
new A1
*/

b = new B("new B1");
B.print();
b.print1();
console.log(b.arg); // Прямой доступ к полю.
// До добавления своих полей. Идентичных с наименованием родительского класса. static field = 'Static Default_B'; и arg = 'Default val of arg_B';
/*
In constructor_A arg =  Default val of arg_A
In static method_A this =  [class B extends A]
In static method_A field =  Static Default_A
In static method_A arg =  undefined
In method_A this =  B { arg: 'new B1' }
In method_A field =  undefined
In method_A arg =  new B1
new B1
*/

// После добавления своих полей. Идентичныдх с наименованием родительского класса. static field = 'Static Default_B'; и arg = 'Default val of arg_B';
// Видно, что эти поля полностью перекрыли дочерние родительские поля.
/*
In constructor_A arg =  Default val of arg_A
In static method_A this =  [class B extends A] { field: 'Static Default_B' }
In static method_A field =  Static Default_B
In static method_A arg =  undefined
In method_A this =  B { arg: 'Default val of arg_B' }
In method_A field =  undefined
In method_A arg =  Default val of arg_B
Default val of arg_B
*/