class A{
	static staticFieldIn = 'Static Default In';
	dynamicField = 'Default val of dynamicField';

	constructor (arg){
		console.log("In constructor = ", this.dynamicField);
		this.dynamicField = arg;
	}

	static staticPrint(){
		console.log("In static method_A this = ", this); // Возвращает класс.
		console.log("In static method staticFieldInOut = ", this.staticFieldInOut); // У статик метода видно сатитк поле 'staticFieldIn'
		console.log("In static method staticFieldIn = ", this.staticFieldIn); // У статик метода видно сатитк поле 'staticFieldIn'
		console.log("In static method dynamicField = ", this.dynamicField); // У статик метода НЕ видно обычное поле 'dynamicField', хотя к этому времени оно уже проинициализированно. Что соответствует для Java.
	}

	dynamicPrint(){
		console.log("In method_A this = ", this); // Возвращает объект
		console.log("In method staticFieldInOut = ", this.staticFieldInOut); // У обычного метода НЕ видно сатик поле 'staticFieldIn'
		console.log("In method staticFieldIn = ", this.staticFieldIn); // У обычного метода НЕ видно сатик поле 'staticFieldIn'
		console.log("In method dynamicField = ", this.dynamicField); // У обычного метода видно обычное поле поле 'dynamicField'
	}
}


a = new A('Val from constructor for "a" instance');
A.staticFieldInOut = 'Static Default Out';
A.staticPrint();
a.dynamicPrint();
console.log('a.dynamicField = ', a.dynamicField); 		// Прямой доступ к полю.
console.log("a['dynamicField'] = ", a['dynamicField']);	// Прямой доступ к полю.

console.log('Object.getPrototypeOf(a) = ', Object.getPrototypeOf(a));
console.log('A.prototype = ', A.prototype);				// Но почему пустой объект? Там же уже сть поля?
console.log('a.__proto__ = ', a.__proto__);				// Но почему пустой объект? Там же уже есть поля? Но при этом вывод даёт все верно: Object.getOwnPropertyNames(a.__proto__) =  [ 'constructor', 'dynamicPrint' ]
console.log('a.prototype = ', a.prototype);				// Все правильно у инстенса уже нет этого поля. Это поле только у конструктора.
console.log('Object.getOwnPropertyNames(a.__proto__) = ', Object.getOwnPropertyNames(a.__proto__)); 
console.log('Object.getOwnPropertyNames(a.__proto__.__proto__) = ', Object.getOwnPropertyNames(a.__proto__.__proto__));


/*
То что видно в консоли Chrome
В this инстенса лежит одно поле dynamicField
И [[Prototype]]: Object						//Т.е. еще раз согласно теории. У объекта созданного из класса или функции есть поле [[Prototype]], - которое является тоже объектом. У этого объекта есть два поля constructor и [[Prototype]]
	Внутри: 								//И еще поля, в виде добавляемых функций.
		constructor: class A
		dynamicPrint: f dynamicPrint()
		[[Prototype]]: Object


А вот внутри "constructor: class A" уже статические попля и метод staticPrint.
*/


/*
Вывод NodeJS
In constructor =  Default val of dynamicField
In static method_A this =  [class A] {
  staticFieldIn: 'Static Default In',
  staticFieldInOut: 'Static Default Out'
}
In static method staticFieldInOut =  Static Default Out
In static method staticFieldIn =  Static Default In
In static method dynamicField =  undefined
In method_A this =  A { dynamicField: 'Val from constructor for "a" instance' }
In method staticFieldInOut =  undefined
In method staticFieldIn =  undefined
In method dynamicField =  Val from constructor for "a" instance
a.dynamicField =  Val from constructor for "a" instance
a['dynamicField'] =  Val from constructor for "a" instance
Object.getPrototypeOf(a) =  {}
A.prototype =  {}
a.prototype =  {}
a.prototype =  undefined
Object.getOwnPropertyNames(a.__proto__) =  [ 'constructor', 'dynamicPrint' ]
Object.getOwnPropertyNames(a.__proto__.__proto__) =  [
  'constructor',
  '__defineGetter__',
  '__defineSetter__',
  'hasOwnProperty',
  '__lookupGetter__',
  '__lookupSetter__',
  'isPrototypeOf',
  'propertyIsEnumerable',
  'toString',
  'valueOf',
  '__proto__',
  'toLocaleString'
]

*/