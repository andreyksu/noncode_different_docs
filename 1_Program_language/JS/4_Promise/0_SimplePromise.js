//let i = 2; - если расскоментировать, то выполнится только finally и catch и всёёёёё.
let i = 1;

let prom = new Promise((okk, rej)=>{
        console.log('Promise START ');
        if (i === 1){
                okk(' OKK from Promise '); // Асинхронное место
        }else{
                rej(" ERR from Promise "); // Асинхронное место. И оно не останавливает выполнение.
        }
        console.log('Promise STOP '); // Т.е выполнится до then
});

let kk = 0;

prom.finally(()=>console.log('It is from finally ::: kk = ' + kk))                                                                      // Не должен принимать ничего и не должен возвращать ничего. И нужно использовать первым - так рекамендуют.
        .then((res)=>{console.log("It is First then and arg form Promise = " + res); kk = 2; return "___From First Then___"})           // Изменяем внешнюю переменную.
        .then((ress)=>{console.log("It is Second Then and arg form First Then = " + ress)})                                             // Ничего не возвращаем. И в следующем выводе будет undefined
        .then((ress1)=>{console.log("It is Third Then and arg form Sirst Then = " + ress); throw new Error("___messageRrror___")})      // Выкидываем исключение и оно будет перехватано в catch
        .then((res)=>console.log('It is then kk = ' + kk))// Это НЕ будет обработано из за исключения
        .catch((err)=>{console.log('Errooooor ' + err)});

console.log('After then kk = ', kk); // Т.е выполнится до then

// Вывод
/*
 promise START 
 promise STOM 
0
It is from finally kk = 0
It is res from first then and message form Promise =  It is result okk from Promise
It is second Then and arg form First Then =  'Return form First Then'
It is second Then and arg form First Then = undefined
Errooooor Error: messageRrror
*/

/*
Всё это работает, потому что вызов promise.then тоже возвращает промис, так что мы можем вызвать на нём следующий .then.
Когда обработчик возвращает какое-то значение, то оно становится результатом выполнения соответствующего промиса и передаётся в следующий .then.

Т.е. из кода 'return "___From First Then___' превращается в возвращённый промис.
*/