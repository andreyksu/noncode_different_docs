/*
В JavaScript this является «свободным», его значение вычисляется в момент вызова метода и не зависит от того, где этот метод был объявлен, 
а скорее от того, какой объект вызывает метод (какой объект стоит «перед точкой»).

У стрелочных функций нет this. Если происходит обращение к this, его значение берётся снаружи.
Стрелка => ничего не привязывает. У функции просто нет this. При получении значения this – оно, как обычная переменная, берётся из внешнего лексического окружения.
*/


function outerFunc(){
	console.log("It is the outerFunc function = ", this.aa);
}

let outerArrowFunc = () => { 
	console.log("It is the outerArrowFunc function = ", this.aa);	
}

class A{
	constructor(a){
		this.aa = a;
	}

	innerFunc(funcc){
		console.log("It is the innerFunc function = ", this.aa);
		funcc();			// (1)
		funcc.call(this);	// (2)
	}

	arrowFunc = () => {
		console.log("It is the ARROW function = ", this.aa);
	}
}

let instA = new A("A condtructor");


instA.innerFunc(outerFunc); 		// (1) undefined (2) correct


instA.innerFunc(outerArrowFunc); 	// Для стрелочнной функции что (1) что (2) приводит к undefinded.
									// Получается стрелочную функцию нельзя передавать в качестве аргумента в метод класса (this в любом случае теряется).

// И здесь в любом виде теряется this.
instA.arr = outerArrowFunc.bind(instA); // bind тоже не помогает. И call тоже не помогает.
instA.arr();

/*

It is the innerFunc function =  A condtructor
It is the outerFunc function =  undefined
It is the outerFunc function =  A condtructor
It is the innerFunc function =  A condtructor
It is the outerArrowFunc function =  undefined
It is the outerArrowFunc function =  undefined
It is the outerArrowFunc function =  undefined
*/

//---------------------------------------------------------------------------------------------
class B{
	constructor(b){
		this.bb = b;
	}

	arrowFuncB = () => {
		console.log("It is the arrowFuncB function = ", this.bb);
	}

	innerFuncB(funcc){
		console.log("It is the innerFuncB function = ", this.bb);
	}
}

class A{
	constructor(a){
		this.aa = a;
	}

	innerFuncA(funcc){
		console.log("It is the innerFuncA function = ", this.aa);
		//funcc();			// (1)
		funcc.call(this);	// (2)
	}

	arrowFunc = () => {
		console.log("It is the ARROW function = ", this.aa);
	}
}

let instA = new A("A condtructor");
let instB = new B("B condtructor");

instA.innerFuncA(instB.arrowFuncB); // Для (1) и (2) для стрелочной функции поведение одинаковое и у стрелочной функции this всегда то месте где она объявлена. И не важно (1) и (2)
instA.innerFuncA(instB.innerFuncB); // (1)  - контекст утерян и в методе 'arrowFuncB = ()' вызов 'this.bb' приводит к ошибке т.к. this мы потеряли на этапе 'instB.innerFuncB'
									// (2) - контекст привязали к instA - и там уже this есть, а поиск 'bb' приводит к undefined, т.к. привязали instA а там 'bb' отсутствует.

// Одним словом, this теряется у обычной функции когда мы её куда-то передаём или объявляем в виде: instance.method
// У стерлочной функции this - соответсвует месту, где стерлочная функция объявлена?

/*
It is the innerFuncA function =  A condtructor
It is the arrowFuncB function =  B condtructor	// А стрелочной функции все равно, она живёт в том контексте, где была объявлена. И ей все равно на 'call()'
It is the innerFuncA function =  A condtructor
It is the innerFuncB function =  undefined    	// Т.к. bb у instA отсутствует.
*/


//---------------------------------------------------------------------------------------------
// Внутреннаяя функция не имеет доступа к this объемлющей функции. Помогает call.

class A{
	constructor(a){
		this.aa = a;
	}

	innerFuncA(){
		console.log("It is the innerFuncA function = ", this.aa);
		function innerInnerFuncA(){
			console.log("It is the innerInnerFuncA function = ", this.aa);
		}
		// innerInnerFuncA(); 			// (1) Внутреннаяя функция не имеет доступа к внешней this. Будет ошибка.
		innerInnerFuncA.call(this); // (2) А так нормально работает.
	}

	arrowFunc = () => {
		console.log("It is the ARROW function = ", this.aa);
	}
}

let instA = new A("A condtructor");
instA.innerFuncA();

/*
It is the innerFuncA function =  A condtructor
It is the innerInnerFuncA function =  A condtructor
*/