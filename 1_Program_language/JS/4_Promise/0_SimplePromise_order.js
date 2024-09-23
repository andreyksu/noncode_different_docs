let i = 1;

let prom = new Promise((okk, rej)=>{
        console.log('Promise START');   // Sync act
        if (i === 1){
                setTimeout(()=>okk('OKK from Promise '), 4000);
        }else{
                rej("ERR from Promise ");
        }
        console.log('Promise STOP'); // Sync act
});

let prom1 = new Promise((okk, rej)=>{
        console.log('Promise1 START'); // Sync act
        if (i === 1){
                setTimeout(()=>okk('OKK from Promise1 '), 2000);
        }else{
                rej("ERR from Promise1 ");
        }
        console.log('Promise1 STOP'); // Sync act
});

prom.then((res)=>{console.log(res)}).catch((err)=>{console.log(err)});
prom1.then((res)=>{console.log(res)}).catch((err)=>{console.log(err)});

/*
Promise START           // Sync act
Promise STOP            // Sync act
Promise1 START          // Sync act
Promise1 STOP           // Sync act
OKK from Promise1       // Выполнится первым. Т.к. время меньше. Но в жизни мы не знаем по времени задержки.
OKK from Promise
*/