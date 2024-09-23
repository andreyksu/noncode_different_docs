let i = 1;

let prom = new Promise((okk, rej) => {
    console.log('Promise START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise '), 4000);
    } else {
        rej("ERR from Promise ");
    }
    console.log('Promise STOP');
});

let prom1 = new Promise((okk, rej) => {
    console.log('Promise1 START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise1 '), 2000);
    } else {
        rej("ERR from Promise1 ");
    }
    console.log('Promise1 STOP');
});

prom
    .then((res) => { // Внутренний промис имеет меньшую задержку, по этой причине и выполняется первым.
        prom1.then((ress) => { console.log(ress) });
        return "From outer first then"
    })
    .then((resss) => { console.log('Finish', resss) })
    .catch((err) => { console.log(err) });

/*
Promise START
Promise STOP
Promise1 START
Promise1 STOP
OKK from Promise1
Finish From outer first then
*/

let i = 1;

let prom = new Promise((okk, rej) => {
    console.log('Promise START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise '), 2000);
    } else {
        rej("ERR from Promise ");
    }
    console.log('Promise STOP');
});

let prom1 = new Promise((okk, rej) => {
    console.log('Promise1 START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise1 '), 4000);
    } else {
        rej("ERR from Promise1 ");
    }
    console.log('Promise1 STOP');
});

prom
    .then((res) => { // Поменял время и теперь видно, что внешний промис выполняется без ожидания внутреннего.
        prom1.then((ress) => { console.log(ress) });
        return "From outer first then"
    })
    .then((resss) => { console.log('Finish', resss) })
    .catch((err) => { console.log(err) });

/*
Promise START
Promise STOP
Promise1 START
Promise1 STOP
Finish From outer first then
OKK from Promise1
*/

let i = 1;

let prom = new Promise((okk, rej) => {
    console.log('Promise START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise '), 2000);
    } else {
        rej("ERR from Promise ");
    }
    console.log('Promise STOP');
});

let prom1 = new Promise((okk, rej) => {
    console.log('Promise1 START');
    if (i === 1) {
        setTimeout(() => okk('OKK from Promise1 '), 4000);
    } else {
        rej("ERR from Promise1 ");
    }
    console.log('Promise1 STOP');
});

prom
    .then((res) => { // А вот здесь уже ждём внутренний промис.
        return prom1.then((ress) => { console.log(ress + "   " + res); return res });
        //return "From outer first then"
    })
    .then((resss) => { console.log('Finish', resss) })
    .catch((err) => { console.log(err) });

/*
Promise START
Promise STOP
Promise1 START
Promise1 STOP
OKK from Promise1    OKK from Promise           <<<< Вывод внутреннего promise.
Finish OKK from Promise
*/




//Вот и здесь пример из интернета. Все три делают одно и тоже

loadScript("/article/promise-chaining/one.js")
    .then(function (script) {
        return loadScript("/article/promise-chaining/two.js");
    })
    .then(function (script) {
        return loadScript("/article/promise-chaining/three.js");
    })
    .then(function (script) {
        // вызовем функции, объявленные в загружаемых скриптах,
        // чтобы показать, что они действительно загрузились
        one();
        two();
        three();
    });
  
  
loadScript("/article/promise-chaining/one.js")
    .then(script => loadScript("/article/promise-chaining/two.js"))
    .then(script => loadScript("/article/promise-chaining/three.js"))
    .then(script => {
        // скрипты загружены, мы можем использовать объявленные в них функции
        one();
        two();
        three();
    });
  
  
loadScript("/article/promise-chaining/one.js")
    .then(script1 => {
        loadScript("/article/promise-chaining/two.js")
        .then(script2 => {
            loadScript("/article/promise-chaining/three.js")
            .then(script3 => {// эта функция имеет доступ к переменным script1, script2 и script3
                one();
                two();
                three();
            });
        });
    });