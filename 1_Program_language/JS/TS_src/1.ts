function getDiviters(i: number): string { //{ 'result': number[], 'len': number }
    let result: number[] = [];
    for (let count: number = 1; count <= i; count++) {
        if (i % count == 0) {
            result.push(count);
        }

    }
    //return { 'result': result, 'len': result.length };
    //return `target : ${i} result: ${result}, len: ${result.length}`;
    return `target : ${i}\nresult: ${result}`;
}

console.log(getDiviters(7425), "\n", getDiviters(12375), "\n");
/*
console.log(getDiviters(34), getDiviters(68), "\n");
console.log(getDiviters(18), getDiviters(48), "\n");
console.log(getDiviters(29), getDiviters(45), "\n");
*/


function getNOK(i: number, k: number): string {
    let minn = i < k ? i : k;
    let maxx = i > k ? i : k;
    let startt = minn;
    let fuzze = true;

    let listtForMax: number[] = [];
    let listtForMin: number[] = [];

    while (fuzze) {
        let boolMin = startt % minn == 0;
        let boolMax = startt % maxx == 0;

        if (boolMin)
            listtForMin.push(startt);
        if (boolMax)
            listtForMax.push(startt);
        if (boolMin && boolMax) {
            fuzze = false;
        } else {

            startt += 1;
        }
    }

    return `${maxx} ::: maxList = ${listtForMax}\n${minn} ::: minList = ${listtForMin}\nNOK = ${startt}\n`;
}

console.log(getNOK(18, 27));
/*
console.log(getNOK(36, 90));
console.log(getNOK(45, 75));
console.log(getNOK(52, 39));
*/