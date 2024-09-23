/*
In programming languages, a literal is a way to represent a fixed value directly in the source code. It's a way for the programmer to tell the computer exactly what value they want to use. 

Here's a breakdown:

Imagine a literal as a specific, unchanging piece of information you give to a computer.

Examples:

 Numbers: 10, 3.14, -5 (representing integers, floating-point numbers, and negative numbers)
 Strings: "Hello, world!", "My name is Bob", "123" (representing text enclosed in quotes)
 Booleans: True, False (representing logical values)

Why are literals important?

 Direct Representation: They directly represent the value you want to use without any calculations or variables.
 Constant Values:  Literals don't change during program execution. Their values are fixed.
 Readability: Literals make your code easier to understand. You can immediately see the values being used.
*/

//======================================
// Common
//======================================

// К полю объекта можно всегда добраться через строковое представление имени поля: someInstance['targetFieldName']
	// Проверил, в JS все так  для instance класса можно получить доступ к полям через instancep['field']
// Если в качестве ключа(вместо строкового представления имени) мы передаём объект, то для него вызвается toString(). И именно оно будет использоваться для доступа.
// А вообще еще можно привязывать поля через  Object.assign(targetObject, targetValue); 
// Пример Object.assign(this, initialData);
// Аналогично для получения Object.keys(this); Object.values(this); Object.entries(this);

let obj = {
  toString(){ // Но для доступа к полю через объект нужно явно реализовывать этот метод. Допустим для let obj = {message:'Hello'}  toString() даст [object Object]
    console.log('toString called') //Note that toString will get called whenever the obj is used in an index position.
    return 'Hello' 
  }
}

let foo: any = {};
foo[obj] = 'World'; // toString called // In JS
//foo[obj.toString()] = 'World'; // In TS
console.log(foo[obj]); // toString called, World // In JS
console.log(foo['Hello']); // World


// Проверка на null : x!.toStirng()
	// Writing ! after any expression is effectively a type assertion that the value isn’t null or undefined

	function liveDangerously(x?: number | null) {
	  // No error
	  console.log(x!.toFixed()); // Зачем это нужно? После компиляции это пропадает и всё равно будет ошибка (в runtime). Видимо только для компиляции. Но здесь тогда должно быть условие if(x) итд.
	}

// Проверка типа:
	// typeof val
	function padLeft(padding: number | string, input: string): string {
		if (typeof padding === "number") { // Интересная проверка, проверяется как строка.
			return " ".repeat(padding) + input; // repeat работает только для number
		}
		return padding + input;
	}


	// false "if" (0, NaN, "", 0n, null, undefined). А вот пустой массив в отличии от python дастр true.
	// typeof string[] === "object"
	// Массив можно объявить и так Array<number> или number[] а проверить массив ли это можно так Array.isArray(x)
	// при явном объявлении типа, можно его не аннотировать
	let myName: string = "Alice";
	let myName = "Alice"; // Будет вычисленно.

	function printAll(strs: string | string[] | null) {
		if (strs && typeof strs === "object") { // Т.е. не null и object. ???
			for (const s of strs) {
			  console.log(s);
			}
		} else if (typeof strs === "string") {
			console.log(strs);
		}
	}
// ==============================================================================
// type - создаёт псевдоним.

	type FileContents = string | any[] | object
	type NewMyType = 'back' | 'forward' // union 
	type SecondMyType = string


	interface Circle {
		kind: "circle";
		radius: number;
	}
	 
	interface Square {
	  kind: "square";
	  sideLength: number;
	}
	 
	type Shape = Circle | Square;

	// -----------------
	/*
		Согласно оффициальной документации type и interface одно и то-же. Но type не может быть расширен (видимо говорится о extends). Хотя у type есть "&" который объединяет поля.
	*/

	// This defines a type alias Dog that represents a function type.
	// You can use this type to create variables that hold functions matching this signature.
	type Dog = (name: string) => boolean; // По сути задаёт шаблон типа.

	// А можно так
	type Dog = {
		(name: string) : boolean;
		someField : string; //Да еще и поле добавить можно.
	}

	// Callable Interface
	// This defines an interface Dog that describes a callable object. In this case, any object conforming to this interface can be called as a function
	// This is different from the previous examples because it does not define a method; instead, it defines the interface itself as a function.
	interface Dog {
		(name : string) : boolean;
	}

	const dogFunction: Dog = (name: string) => { // Это реализация типа Dog
		console.log(`Dog's name is ${name}`);
		return true;
	};
	dogFunction("Buddy"); // Calling the function

	// Идентичное объявление.
	// This defines an interface Dog with a property set, which is a function
	// This means that any object conforming to this interface must have a set property that is a function with the specified signature.
	interface Dog {
		set: (name : string) => boolean;
	}

	// This is another way to define the same interface as the previous example.
	// This is a more concise syntax for defining methods in interfaces.
	interface Dog {
		set(name: string) : boolean;
	}

	class MyDog implements Dog {
		set(name: string): boolean {
			console.log(`Setting dog's name to ${name}`);
			return true;
		}
	}


	/**
	 * Make all properties in T optional
	 */
	type Partial<T> = {
	    [P in keyof T]?: T[P];
	};

	/**
	 * Make all properties in T required
	 */
	type Required<T> = {
	    [P in keyof T]-?: T[P];
	};

	/**
	 * Make all properties in T readonly
	 */
	type Readonly<T> = {
	    readonly [P in keyof T]: T[P];
	};

	// ----------------------------------------------------------------
	type DescribableFunction = {
	  description: string;
	  (someArg: number): boolean;
	};
	function doSomething(fn: DescribableFunction) {
	  console.log(fn.description + " returned " + fn(6)); // Вот это интересно.
	}
	 
	function myFunc(someArg: number) { // А внутри можно объявить поле???
	  return someArg > 3;
	}
	myFunc.description = "default description";// И вот это интеерсно, взяли добавили поле к методу.
	 
	doSomething(myFunc);

	// ----------------------------------------------------------------
	// Идентичные записи.
	interface Person {
		name: string;
		age: number;
	}

	type Person = {
		name: string;
		age: number;
	};

// ==============================================================================
// interface - по аналогии с Java создаёт интерфейс


	// unknown - неизвестный тип, но с таким типом ничего нельзя сделать.
	// any - это отключение проверки типов.

		// unknown присваивается самому себе или any, а any - чему угодно.

		let anyValue: any = 1;
		let unknownValue: unknown = 1;

		let str: string;

		str = anyValue; // Ошибки нет
		str = unknownValue; // получаем ошибку TypeScript. Вообще с таким типом ничего нельзя сделать.

// ==============================================================================
// index signature

	// It allows you to create an array-like structure where the keys are numbers (indices) and the values are strings. This is useful for defining types for arrays or objects that behave like arrays.

		// Define the StringArray interface
		interface StringArray {
		    [index: number]: string;
		    // [index: string]: any; // А вобще можно так и тогда можно создавать любой класс с любыми полями.
		}

		// Create a variable of type StringArray
		let myArray: StringArray = ["apple", "banana", "cherry"];

		// А вот для этого интерфейса подходит объект.
		interface StringArray1 {
			[index: string]: string;
		}

		let myArray1: StringArray1 = {first: 'first', second : 'second'}; // Это литеральный объект.

		// А можно и так задать тип:
		let foo:{ [index:string] : {message: string} } = {}; // Это будет означать, что каждое поле foo должно хранить объект с полем message
		// -----------------------------------------------
		// А так можно обоначить объект с индексами
		type typee = {[index: string] : string}

		// const MyType = {...} // Вероятно для объявления ниже, нужно будет сделать этот тип const
		type Tmp = { [key in keyof MyType]: MyType[key]; }



		// -----------------------------------------------
		// Define the StringArray interface
		interface StringArray {
		    [index: number]: string;
		}

		// Implement the StringArray interface in a class
		class MyStringArray implements StringArray {

			/*
				The reason for this repetition is that TypeScript needs to ensure that the class has the same shape as the interface it implements. By repeating the index signature in the class, you're telling TypeScript that the class has the same indexable properties as the interface, which allows TypeScript to perform type checking and ensure type safety.
				If you don't repeat the index signature in the class, TypeScript won't be able to verify that the class conforms to the interface, and you may encounter type-related errors.
				In summary, the repetition of the index signature in the class is a necessary step to ensure that the class implementation matches the contract defined by the interface, which is a fundamental principle of TypeScript's type system.
			*/
		    items: string[] = [];

		    [index: number]: string; // Таковы правила, это нужно дублировать при расширении.

		    // Не понятно, почему для такой формы записи индексов, допустимы методы. А если так [index: string]: string; - то методы не возможно добавить.
		    add(str: string): void {
		        this.items.push(str);
		    }

		    get(): string[] {
		        return this.items;
		    }

		    getTarget(): string | undefined {
		        let tmp = this.items.pop();
		        if (tmp) {
		            return tmp;
		        } else {
		            return '';
		        }
		    }

		}

		// Example usage
		const myStrings: StringArray = new MyStringArray();

		// -----------------------------------------------
		// Пример с функцией
		type Func = (i: string) => string;

		interface StringArray {
		    [index: string]: Func; //Для функции.
		    // [index: string]: any; // А вобще можно так и тогда можно создавать любой класс с любыми полями. Но это по сути уже без типизации.
		}

		// Implement the StringArray interface in a class
		class MyStringArray {   
		    [index: string]: Func;

		    // Method to get a string by index
		    get(index: string): string {
		        return this.items[index];
		    }

		}

		// Example usage
		const myStrings: StringArray = new MyStringArray();


		// -----------------------------------------------

		// Пример с union. Где класс может иметь как поля string так и методы.
		type targetMethodType = (a: string) => string;

		interface targetMethodType1 { // Без union так и не получилось реализовать этот интерфейс классом. Хотя для [index: string]: string; методы можно добавить. Не понимаю почему так. Как так?
		    (a: string): string;
		}

		interface MyInterface {
		    [index: string]: string | targetMethodType1;
		}

		class MyImplementation implements MyInterface {
		    [index: string]: string | targetMethodType;

		    constructor(data: MyInterface) {
		        // You can directly access properties using the index signature
		        Object.assign(this, data);
		    }

		    getProperty(key: string): string {
		        // Accessing a property (guaranteed to be a string)
		        return <string>this[key];
		    }
		}

		// Это конечно из др. области. 
		const meType: MyInterface = new MyImplementation();
		type Tmp = { [key in keyof MyImplementation]: MyImplementation[key]; } // Т.е. мой тип может состоять только из ключей и их значений что содержатся в MyImplementation????

		let aaa: Tmp = {
		    get(i: string): string {
		        return '';
		    },
		    gg: '', // А почему это можно? Ведь private а keyof для public
		    ggg: '' // А почему это можно??? Ведь такого поля нет.
		}

		// А видимо по этому и выходит на первый план // Literal Object - т.е. по сути const

		// Literal Object Types
		const person1 = { name: 'Alice', age: 30 };
		type PersonType = typeof person1; //  PersonType is a literal object type

		const person2 = { name: 'Bob', age: 25, city: 'New York' };
		type PersonType2 = typeof person2; 

		//  Incorrect Usage (not literal object types)
		let person3 = { name: 'Charlie' }; // Variable, not a literal 
		type PersonType3 = { name: string, age: number }; // Generic, not a literal

		// Comparing Literal Object Types
		type MyPoint = { x: number, y: number }; // Generic, not a literal
		type MyPointLiteral = { x: 10, y: 20 }; // Literal

		// Using Literal Object Types
		function greet(user: PersonType) {
		  console.log(`Hello, ${user.name}!`); 
		}

		//  Invalid
		greet({ name: 'Dave', age: 40, location: 'London' }); // Error! //  Doesn't match PersonType. 
		// Но эта ошибка будет и для "let person1" а не только для 'const person1'

// ==============================================================================
// class 
// ==============================================================================
		class GoodGreeter {
			readonly name: string = "world"; // This prevents assignments to the field outside of the constructor.
		  	name: string;
		 
		  	constructor(otherName?: string) {
				if (otherName !== undefined) {
					this.name = otherName;
				}
			}

			calcLen(): int {
				return name.len()
			}
		}


		// - If you have a base class, you’ll need to call super(); in your constructor body before using any this. members
		// - Class constructors are very similar to functions. You can add parameters with type annotations, default values, and overloads.

		constructor(x: number, y: number);
		constructor(xy: string);
		constructor(x: string | number, y: number = 0) {
			// Code logic here
		}


		// !!!!! Note that inside a method body, it is still mandatory to access fields and other methods via this.. An unqualified name in a method body will always refer to something in the enclosing scope:

		let x: number = 0;

		class C {
			x: string = "hello";

			m() {
				// This is trying to modify 'x' from line 1, not the class property
				x = "world";
				Type 'string' is not assignable to type 'number'.
			}
		}

// ==============================================================================
		function identity<Type>(arg: Type): Type {
		  return arg;
		}

		let output = identity<string>("myString");

		let output = identity("myString"); //Here we use type argument inference — that is, we want the compiler to set the value of Type for us automatically based on the type of the argument we pass in



		//----------------------
		function identity<Type>(arg: Type): Type {
		  return arg;
		}
		 
		let myIdentity: <Type>(arg: Type) => Type = identity;

		let myIdentity: { <Type>(arg: Type): Type } = identity;
		// You're correct that the syntax { <Type>(arg: Type): Type } looks like an object type, but in this context, it is actually describing a function type. 
		// In TypeScript, you can define a function type using an object-like syntax, which can sometimes be confusing.
		// When you see { <Type>(arg: Type): Type }, it is indeed a way to describe a function type, not an object with properties.
		// This is not an object with properties; it is a function signature.

		//-----------------
		function combine<Type>(arr1: Type[], arr2: Type[]): Type[] {
		  return arr1.concat(arr2);
		}
		const arr = combine<string | number>([1, 2, 3], ["hello"]);

		//-----------------

		interface GenericIdentityFn {
		  <Type>(arg: Type): Type;
		}
		 
		function identity<Type>(arg: Type): Type {
		  return arg;
		}
		 
		let myIdentity: GenericIdentityFn = identity;

		//-----------------

		interface GenericIdentityFn<Type> {
		  (arg: Type): Type;
		}
		 
		function identity<Type>(arg: Type): Type {
		  return arg;
		}
		 
		let myIdentity: GenericIdentityFn<number> = identity;

		//-----------------


		class GenericNumber<NumType> {
				zeroValue: NumType;
				add: (x: NumType, y: NumType) => NumType;
			}
			 
		let myGenericNumber = new GenericNumber<number>();
		myGenericNumber.zeroValue = 0;
		myGenericNumber.add = function (x, y) {
			return x + y;
		};

// Generics

	function combine<Type>(arr1: Type[], arr2: Type[]): Type[] {
		return arr1.concat(arr2);
	}

	const arr = combine<string | number>([1, 2, 3], ["hello"]);// Т.е. это "или"" а именно можно передалть оба типа одновременно. А что за тип вернётся? Видим тоже можно или тот или тот.
	
	/*
	Chainable<undefinde>
			- Такой вид, обычно применяется для "Chainable", и говорится о том: то что внутри не имеет ничего значемого.
			- Т.к. методы внутри возвращают снова "Chainable", то тут делается упор, на возврате "Chainable" а не то что содержится внутри.
	*/

	// ------------------- The similar

	function firstElement1<Type>(arr: Type[]) { // Но это предпочтительнее.
	return arr[0];
	}

	function firstElement2<Type extends any[]>(arr: Type) {
	return arr[0];
	}

	// a: number (good)
	const a = firstElement1([1, 2, 3]);
	// b: any (bad)
	const b = firstElement2([1, 2, 3]);


	// -------------------
	type Point = { x: number; y: number }; // Эквивалентно записи type P = "x" | "y"
	type P = keyof Point;


	type Person = { age: number; name: string; alive: boolean };
	type I1 = Person["age" | "name"]; // type I1 = string | number
	type I2 = Person[keyof Person];	// type I2 = string | number | boolean

	type AliveOrName = "alive" | "name";
	type I3 = Person[AliveOrName]; type I3 = string | boolean

	/*
		CommandFn<T extends keyof ChainableMethods>
			- In this example, CommandFn is constrained to only accept the keys of ChainableMethods, ensuring type safety and preventing errors at compile time.

		См. здесь у методов по одному параметру. И дальше этот метод используется в др. месте. 
		??? Получается что типы могту быть разыне а количество аргуметов одинаковым?
	*/
		
		type ChainableMethods = { 
			add: (num: number) => Chainable;
			multiply: (num: number) => Chainable;
		};

		type CommandFn<T extends keyof ChainableMethods> = (method: T, value: number) => Chainable; // Описание типа.

		const executeCommand: CommandFn<'add'> = (method, value) => { // Реализация типа.
			// Implementation here
			return new Chainable().add(value); // Example usage
		};

		// This would be valid
		executeCommand('add', 5);

	/*
		This would cause a TypeScript error because 'subtract' is not a key of ChainableMethods
		executeCommand('subtract', 5);
	*/


	/*	
	FirstType<T extends keyof SecondType>
		- This type parameter T is constrained to be one of the keys of another type, SecondType
		- When you write FirstType<T extends keyof SecondType>, you are defining a generic type FirstType that takes a type parameter T. 
			- The type T is constrained to be one of the keys of SecondType. This means that when you use FirstType, you can only pass in keys that exist in SecondType.

		- This construct provides type safety by ensuring that T can only be one of the keys of SecondType, and it allows you to access the corresponding value type based on the key.
	*/	

	type SecondType = {
	    a: number;
	    b: string;
	    c: boolean;
	};

	// Define a generic type FirstType that takes a key from SecondType
		type FirstType<T extends keyof SecondType> = {
		    key: T; // The key must be one of 'a', 'b', or 'c'
		    value: SecondType[T]; // The value type will correspond to the type of the key in SecondType
		};

		// Example usage
		const example1: FirstType<'a'> = {
		    key: 'a',
		    value: 42, // value is of type number
		};

		const example2: FirstType<'b'> = {
		    key: 'b',
		    value: 'Hello', // value is of type string
		};

		// This would cause a TypeScript error because 'd' is not a key of SecondType
		// const example3: FirstType<'d'> = {
		//     key: 'd',
		//     value: 'Not valid', // Error: Type '"d"' is not assignable to type '"a" | "b" | "c"'.
		// };

	// Claude-3 Define a type with methods
		interface SecondType {
		  name: string;
		  age: number;
		  email: string;
		  greet(): void;
		  calculateAge(birthYear: number): number;
		}

		class FirstType<T extends keyof SecondType> {
		  private value: SecondType[T];

		  constructor(value: SecondType[T]) {
		    this.value = value;
		  }

		  getValue(): SecondType[T] {
		    return this.value;
		  }

		  setValue(newValue: SecondType[T]): void {
		    this.value = newValue;
		  }

		  callMethod(methodName: T, ...args: Parameters<SecondType[T]>): ReturnType<SecondType[T]> {
		    const method = (this.value as any)[methodName];
		    return method.call(this.value, ...args);
		  }
		}

		// Example usage
		const personInstance = new FirstType<'name'>('John Doe');
		personInstance.greet(); // Calls SecondType.greet()

		const ageInstance = new FirstType<'calculateAge'>(null);
		const currentAge = ageInstance.callMethod('calculateAge', 1990);
		console.log(currentAge); // Calls SecondType.calculateAge()


	// GPT-4 Define the SecondType with some properties and methods
		interface SecondType {
		    name: string;
		    age: number;
		    greet(): string;
		    incrementAge(): void;
		}

		// Define the FirstType that takes a generic type T constrained to the keys of SecondType
		class FirstType<T extends keyof SecondType> {
		    private secondTypeInstance: SecondType;

		    constructor(instance: SecondType) {
		        this.secondTypeInstance = instance;
		    }

		    // Method to get a property value from SecondType
		    getProperty(key: T): SecondType[T] {
		        return this.secondTypeInstance[key];
		    }

		    // Method to call a method from SecondType
		    callMethod(key: T): string | void {
		        if (typeof this.secondTypeInstance[key] === 'function') {
		            return (this.secondTypeInstance[key] as Function)();
		        }
		    }
		}

		// Example usage
		const secondTypeInstance: SecondType = {
		    name: "Alice",
		    age: 30,
		    greet() {
		        return `Hello, my name is ${this.name}`;
		    },
		    incrementAge() {
		        this.age += 1;
		    }
		};

		// Create an instance of FirstType
		const firstTypeInstance = new FirstType(secondTypeInstance);

		// Access properties
		console.log(firstTypeInstance.getProperty("name")); // Output: Alice
		console.log(firstTypeInstance.getProperty("age"));  // Output: 30

		// Call methods
		console.log(firstTypeInstance.callMethod("greet")); // Output: Hello, my name is Alice
		firstTypeInstance.callMethod("incrementAge");
		console.log(firstTypeInstance.getProperty("age"));  // Output: 31



	// -------------------
	/*
		FirstType<SecondType[T]>
			- When you write FirstType<SecondType[T]>, you are essentially saying that you want to create an instance of FirstType using the type that corresponds to the key T in SecondType.
			- SecondType[T]: This accesses the type of the property in SecondType that corresponds to the key T.
			- FirstType<SecondType[T]>: This creates a new type based on the type obtained from SecondType[T], allowing you to define a structure that uses that type.
	
	*/

	// Define a type with different properties
		type SecondType = {
		    a: number;
		    b: string;
		    c: boolean;
		};

		// Define a generic type that takes a type parameter
		type FirstType<T> = {
		    value: T; // The value will be of type T
		};

		// Now, we can use FirstType with SecondType[T]
		type ExampleA = FirstType<SecondType['a']>; // This will be FirstType<number>
		type ExampleB = FirstType<SecondType['b']>; // This will be FirstType<string>
		type ExampleC = FirstType<SecondType['c']>; // This will be FirstType<boolean>

		// Example usage
		const example1: ExampleA = {
		    value: 42, // value is of type number
		};

		const example2: ExampleB = {
		    value: 'Hello', // value is of type string
		};

		const example3: ExampleC = {
		    value: true, // value is of type boolean
		};

	// Claude-3 Define a type with methods
		interface SecondType {
		  name: string;
		  age: number;
		  email: string;
		  greet(): void;
		  calculateAge(birthYear: number): number;
		}

		class FirstType<T extends keyof SecondType> {
		  private value: SecondType[T];

		  constructor(value: SecondType[T]) {
		    this.value = value;
		  }

		  getValue(): SecondType[T] {
		    return this.value;
		  }

		  setValue(newValue: SecondType[T]): void {
		    this.value = newValue;
		  }

		  callMethod(methodName: T, ...args: Parameters<SecondType[T]>): ReturnType<SecondType[T]> {
		    const method = (this.value as any)[methodName];
		    return method.call(this.value, ...args);
		  }
		}

		// Example usage
		const nameInstance = new FirstType<'name'>('John Doe');
		console.log(nameInstance.getValue()); // Output: 'John Doe'
		nameInstance.setValue('Jane Smith');
		console.log(nameInstance.getValue()); // Output: 'Jane Smith'
		nameInstance.callMethod('greet'); // Calls SecondType.greet()

		const ageInstance = new FirstType<'age'>(30);
		console.log(ageInstance.getValue()); // Output: 30
		ageInstance.setValue(35);
		console.log(ageInstance.getValue()); // Output: 35
		const currentAge = ageInstance.callMethod('calculateAge', 1990);
		console.log(currentAge); // Calls SecondType.calculateAge()

	
	// GPT-4 Define a type with methods
		type SecondType = {
		    add: (num: number) => number;          // Method that takes a number and returns a number
		    greet: (name: string) => string;       // Method that takes a string and returns a string
		    isActive: () => boolean;                // Method that takes no arguments and returns a boolean
		};

		// Define a generic type that takes a type parameter
		type FirstType<T> = {
		    result: T; // The result will be of type T
		};

		// Now, we can use FirstType with the return types of methods in SecondType
		type AddReturnType = FirstType<ReturnType<SecondType['add']>>;    // This will be FirstType<number>
		type GreetReturnType = FirstType<ReturnType<SecondType['greet']>>; // This will be FirstType<string>
		type IsActiveReturnType = FirstType<ReturnType<SecondType['isActive']>>; // This will be FirstType<boolean>

		// Example usage
		const addExample: AddReturnType = {
		    result: 42, // result is of type number
		};

		const greetExample: GreetReturnType = {
		    result: 'Hello, Alice!', // result is of type string
		};

		const isActiveExample: IsActiveReturnType = {
		    result: true, // result is of type boolean
		};

		// Function to demonstrate usage of SecondType methods
		const executeMethod = <K extends keyof SecondType>(method: K, ...args: Parameters<SecondType[K]>): FirstType<ReturnType<SecondType[K]>> => {
		    const secondTypeInstance: SecondType = {
		        add: (num) => num + 10,
		        greet: (name) => `Hello, ${name}!`,
		        isActive: () => true,
		    };

		    const result = secondTypeInstance[method](...args);
		    return { result }; // Return the result wrapped in FirstType
		};

		// Example calls
		const addResult = executeMethod('add', 5); // { result: 15 }
		const greetResult = executeMethod('greet', 'Alice'); // { result: 'Hello, Alice!' }
		const isActiveResult = executeMethod('isActive'); // { result: true }

		// Log the results
		console.log(addResult); // { result: 15 }
		console.log(greetResult); // { result: 'Hello, Alice!' }
		console.log(isActiveResult); // { result: true }


//==============================================================================
	interface DB {
	  filterUsers(someFunc: (someArgUser: User) => boolean): User[];
	}
	//In this version, the someFunc function takes a parameter someArgUser of type User. When you call someFunc, you pass a User instance as an argument, and you can access the properties of the User object using the someArgUser parameter.

	/*
	Example Comparison
	Let's illustrate both approaches with examples.
	*/

	//Using this Parameter


		interface User {
		  name: string;
		  age: number;
		}

		interface DB {
		  filterUsers(someFunc: (this: User) => boolean): User[];
		}

		class UserDatabase implements DB {
		  private users: User[];

		  constructor(users: User[]) {
		    this.users = users;
		  }

		  filterUsers(someFunc: (this: User) => boolean): User[] {
		    return this.users.filter(user => someFunc.call(user)); // Привязка вызова метода к конкретному инстенсу. По этому в этом метод можноо использовать this.
		  }
		}

		// Example usage
		const users: User[] = [
		  { name: 'Alice', age: 25 },
		  { name: 'Bob', age: 30 },
		  { name: 'Charlie', age: 35 }
		];

		const userDB = new UserDatabase(users);

		const result = userDB.filterUsers(function() {// Здесь ничего не передаётся. Всё видимо вычисляется из контекста метда someFunc.
		  return this.age > 28; // 'this' refers to the current user. Ранее мы привязали его через call.
		});

		console.log(result); // Output: [{ name: 'Bob', age: 30 }, { name: 'Charlie', age: 35 }]


		//Using Argument Parameter

			interface User {
			  name: string;
			  age: number;
			}

			interface DB {
			  filterUsers(someFunc: (someArgUser: User) => boolean): User[];
			}

			class UserDatabase implements DB {
			  private users: User[];

			  constructor(users: User[]) {
			    this.users = users;
			  }

			  filterUsers(someFunc: (someArgUser: User) => boolean): User[] {
			    return this.users.filter(user => someFunc(user)); // Pass user as an argument
			  }
			}

			// Example usage
			const users: User[] = [
			  { name: 'Alice', age: 25 },
			  { name: 'Bob', age: 30 },
			  { name: 'Charlie', age: 35 }
			];

			const userDB = new UserDatabase(users);

			const result = userDB.filterUsers(function(someArgUser) {
			  return someArgUser.age > 28; // Access properties using the argument
			});

			console.log(result); // Output: [{ name: 'Bob', age: 30 }, { name: 'Charlie', age: 35 }]

		/*
			Summary of Differences
			Context: In the first approach, you use this to refer to the User instance, while in the second approach, you use a parameter to refer to the User instance.
			Readability: The second approach (using an argument) can be more explicit and easier to read, especially for those who may not be familiar with the this context in JavaScript/TypeScript.
			Flexibility: Both approaches are valid, and the choice between them often comes down to personal or team preference. The this parameter can be useful when you want to maintain a specific context, while the argument approach is straightforward and clear.
			In both cases, you can access the properties of the User object, either through this or through the argument passed to the function.
		*/

//==============================================================================
	function isFish(pet: Fish | Bird): pet is Fish { // Это позволяет использовать в условии, при вызове метода.
	  return (pet as Fish).swim !== undefined;
	}

	let pet = getSmallPet();
	 
	if (isFish(pet)) {// Вот так.
	  pet.swim();
	} else {
	  pet.fly();
	}


//==============================================================================
	type DescribableFunction = {
	  description: string;
	  (someArg: number): boolean; // Note that the syntax is slightly different compared to a function type expression - use : between the parameter list and the return type rather than =>.
	};
	function doSomething(fn: DescribableFunction) {
	  console.log(fn.description + " returned " + fn(6)); // А вот это тоже интересно.
	}
	 
	function myFunc(someArg: number) {
	  console.log(myFunc.description); // Вот так можно обращаться к привязанной проперти.
	  return someArg > 3;
	}
	myFunc.description = "default description"; // Взяли к функции привязали поле. Это как???
	 
	doSomething(myFunc);


//==============================================================================
	declare function handleRequest(url: string, method: "GET" | "POST"): void;
	 
	const req = { url: "https://example.com", method: "GET"} as const;
	// const req = { url: "https://example.com", method: "GET" as "GET"}; // Можно так, взять и зафиксировать значение. Без этого нельзя будет. Т.к. можно изменить значение поле на SET
	//req.method = "SET"; // без as const можно будет менять поля. И по этой  причине нельзя будет передать в метод handleRequest. Т.к. метод ждёт именно "GET" | "POST" а не тип string.
	req['newNew'] = "ttt";
	console.log(req);
	//handleRequest(req.url, req.method);
//==============================================================================
