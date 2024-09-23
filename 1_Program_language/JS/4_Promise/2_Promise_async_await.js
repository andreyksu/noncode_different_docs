let i = 1;

let prom = new Promise((okk, rej)=>{
        console.log('Promise START');
        if (i === 1){
                setTimeout(()=>okk('OKK from Promise '), 4000); // Все равно это выполнится первым.
        }else{
                rej("ERR from Promise ");
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
        let resProm = await prom;
        console.log("It is in async ===", resProm);
        let resProm1 = await prom1;
        console.log("It is in async1 ===", resProm);

        return "It is ok"; // Такая функция async тоже возвращает промис. По этому с ней тоже нужно работать как с Promise
}

f().then((ress)=>{console.log(ress)}); 

/*
Promise START
Promise STOP
Promise1 START
Promise1 STOP
It is in async === OKK from Promise
It is in async1 === OKK from Promise
It is ok
*/