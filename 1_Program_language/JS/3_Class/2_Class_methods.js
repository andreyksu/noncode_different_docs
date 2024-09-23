function outerFunc(){
	console.log("It is the outerFunc function = ", this.aa);
}

class A{
	constructor(a){
		this.aa = a;
	}

	innerFunc(){
		console.log("It is the innerFunc function = ", this.aa);
	}

	arrowFunc = () => {
		console.log("It is the ARROW function = ", this.aa);
	}
}

let instA = new A("A condtructor");

instA.outerFuncr = outerFunc;
// --------------------------------------------------------------------
//let func1 = instA.innerFunc; // - Потеря this - так не работает.
//func1();
// --------------------------------------------------------------------
let func2 = instA.innerFunc.bind(instA); // + this - прибили компьютером
func2();
// --------------------------------------------------------------------
instA.arrowFunc(); // + Работает и this находится нормально!!!
// --------------------------------------------------------------------
let func3 = instA.arrowFunc; // + Работает и this находится нормально!!!
func3();
// --------------------------------------------------------------------
instA.outerFuncr(); // Тоже нормально работает