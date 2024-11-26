// Все три варианта про одно. Просто разные подходы к синдхронизации.

// Здесь синхронизации нет.

let pr1 = new Promise(function(res, rej){
	console.log("First :::: Promise 1"); // 1
	setTimeout(() => {
		console.log("Second :::: Promise 1"); // 7
		res("FirstPromese");
  	}, 1000);
  	
	console.log("Third :::: Promise 1"); // 2
});

let pr2 = new Promise(function(res, rej){
	console.log("Fourth :::: Promise 2"); // 3
	setTimeout(() => {
		console.log("Fifth :::: Promise 2"); // 5
    	res("SecondPromese");
  	}, 3000);
	console.log("Sixth :::: Promise 2"); // 4
});

console.log("Outer 1"); // 5
pr1.then((ress)=>{
	console.log("In the outer Then:::: ress = ", ress); // 8
	pr2.then((resss)=>{
		console.log("In the nested Then:::: resss = ", resss); // 10 // Его никто не ждёт. Он сам заканчивает при этом последним.
	})
	console.log("In the outer Then and after nested"); // 9
})	
console.log("Outer 2"); // 6

/*
First :::: Promise 1
Third :::: Promise 1
Fourth :::: Promise 2
Sixth :::: Promise 2
Outer 1
Outer 2

Second :::: Promise 1
In the outer Then:::: ress =  FirstPromese
In the outer Then and after nested              // Здесь уже занкончил выполняться первый promise а второй выполнится с запазданием, и выполнение втрого никто не ждёт.

Fifth :::: Promise 2    
In the nested Then:::: resss =  SecondPromese
*/

//-----------------------------------------------------------------------------------------------------------
// Синхронизация за счет добавления в цепочку второго промиса команд из внешнего/первого промиса.
let pr1 = new Promise(function(res, rej){
	console.log("First :::: Promise 1"); // 1
	setTimeout(() => {
		console.log("Second :::: Promise 1"); // 7
		res("FirstPromese");
  	}, 1000);
  	
	console.log("Third :::: Promise 1"); // 2
});

let pr2 = new Promise(function(res, rej){
	console.log("Fourth :::: Promise 2"); // 3
	setTimeout(() => {
		console.log("Fifth :::: Promise 2"); // 8
    	res("SecondPromese");
  	}, 3000);
	console.log("Sixth :::: Promise 2"); // 4
});

console.log("Outer 1"); // 5
pr1.then((ress)=>{	
	pr2.then((resss)=>{
		console.log("In the nested Then:::: resss = ", resss); // 9
                                                                    // Теперь ждём за счет добавления цепочки then.
	}).then(()=>{                                                   // А после того как дождались, вызываем то что должно выполниться в объемлющем промисе.
		console.log("In the outer Then:::: ress = ", ress); // 10
		console.log("In the outer Then and after nested"); // 11
	})
	
	
})	
console.log("Outer 2"); // 6

/*
First :::: Promise 1
Third :::: Promise 1
Fourth :::: Promise 2
Sixth :::: Promise 2
Outer 1
Outer 2

Second :::: Promise 1

Fifth :::: Promise 2
In the nested Then:::: resss =  SecondPromese

In the outer Then:::: ress =  FirstPromese
In the outer Then and after nested

*/


//-----------------------------------------------------------------------------------------------------------
// Синхронизация за счет вызова функции.
let pr1 = new Promise(function(res, rej){
	console.log("First :::: Promise 1"); // 1
	setTimeout(() => {
		console.log("Second :::: Promise 1"); // 7
		res("FirstPromese");
  	}, 1000);
  	
	console.log("Third :::: Promise 1"); // 2
});

let pr2 = new Promise(function(res, rej){
	console.log("Fourth :::: Promise 2"); // 3
	setTimeout(() => {
		console.log("Fifth :::: Promise 2"); // 8
    	res("SecondPromese");
  	}, 3000);
	console.log("Sixth :::: Promise 2"); // 4
});

console.log("Outer 1"); // 5
pr1.then((ress)=>{
	function inner(){
		console.log("inner");
		console.log("In the outer Then:::: ress = ", ress); // 10
		console.log("In the outer Then and after nested"); // 11
	}
	pr2.then((resss)=>{
		inner();
		console.log("In the nested Then:::: resss = ", resss); // 9 // Теперь ждём.
	})
	
})	
console.log("Outer 2"); // 6

/*
First :::: Promise 1
Third :::: Promise 1
Fourth :::: Promise 2
Sixth :::: Promise 2
Outer 1
Outer 2

Second :::: Promise 1

Fifth :::: Promise 2

inner

In the outer Then:::: ress =  FirstPromese
In the outer Then and after nested

In the nested Then:::: resss =  SecondPromese

*/