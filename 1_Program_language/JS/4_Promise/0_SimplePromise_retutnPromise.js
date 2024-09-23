//let i = 2; - если расскоментировать, то выполнится только finally и catch и всёёёёё.
let i = 1;

let prom = new Promise((okk, rej)=>{
        console.log('Promise START');
        if (i === 1){
                okk('OKK from Promise ');
        }else{
                rej("ERR from Promise ");
        }
        console.log('Promise STOP');
});

let kk = 0;

prom.finally(()=>console.log('It is from finally kk = ' + kk))
        .then((res)=>{console.log("It is First then and message form Promise = " + res); kk = 2; // В then возвращаем promise. Все остальные вызовы ждут когда этот Promise закончится и цепочка продолжит выполнение дальше.
                return new Promise((su, er)=>{
                        setTimeout(()=> su("This is result of work"), 2000); // если здесь вызвать er то остальные промисы пропустятся и выполнится catch
                });
        })
        .then((ress)=>{console.log("It is Second Then and arg form First Then = " + ress)}) // Сюда придёт результат из вложенного промиса. "This is result of work"
        .then((ress)=>{console.log("It is Third Then and arg form Second Then = " + ress)})
        .catch((err)=>{console.log('Errooooor ' + err)});

console.log('After then kk = ', kk);

/*
Всё это работает, потому что вызов promise.then тоже возвращает промис, так что мы можем вызвать на нём следующий .then.
Когда обработчик возвращает какое-то значение, то оно становится результатом выполнения соответствующего промиса и передаётся в следующий .then.
*/

/*
Promise START
Promise STOP
After then kk =  0
It is from finally kk = 0
It is First then and message form Promise = OKK from Promise
It is Second Then and arg form First Then = This is result of work
It is Third Then and arg form Second Then = undefined
*/