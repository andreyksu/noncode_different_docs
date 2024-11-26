let i = 1;

let prom = new Promise((okk, rej)=>{
        console.log('Promise START');
        if (2 === 1){
                setTimeout(()=>okk('OKK from Promise '), 4000);
        }else{
                rej("ERR from Promise "); // Вызовится эта функция.
        }
        console.log('Promise STOP');
});

let prom1 = new Promise((okk, rej)=>{
        console.log('Promise1 START');
        if (i === 1){
                setTimeout(()=>okk('OKK from Promise1 '), 2000);
        }else{
                rej("ERR from Promise1 ");
        }
        console.log('Promise1 STOP');
});

async function f(){
        let resProm = undefined; 			// Это просто для объявления, чтоб было видно переменную в console.log
        try{
                resProm = await prom;
        }catch(Error){						// Обрабатываем как обычное исключение.
                console.log('Was error');
        }
        console.log("It is in async ===", resProm);
        let resProm1 = await prom1;
        console.log("It is in async1 ===", resProm);

        return "It is ok";
}

f().then((ress)=>{console.log(ress)});

/*
Promise START
Promise STOP
Promise1 START
Promise1 STOP
Was error
It is in async === undefined
It is in async1 === undefined
It is ok
*/