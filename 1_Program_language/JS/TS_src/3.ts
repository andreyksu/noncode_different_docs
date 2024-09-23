function simpleArray(bound: number): number[] {
    let res: number[] = [1, 2, 3];
    if (bound <= 4)
        return res;
    for (let i = 4; i <= bound; i++) {
        let doAppend = true;
        for (let k = 2; k < i; k++) {
            if (i % k == 0) {
                doAppend = false;
                break;
            }
        }
        if (doAppend)
            res.push(i);
    }
    return res;
}


function getSimpleElem(target: number): number[] {
    let res: number[] = [1];
    let simpleArrayy = simpleArray(target);
    for (let i = 1; i < simpleArrayy.length; i++) {
        while (target % simpleArrayy[i] == 0 && target > 0) {
            res.push(simpleArrayy[i]);
            target = Math.floor(target / simpleArrayy[i]);
        }
        if(target < simpleArrayy[i]){
            break;
        }
    }
    return res;


}
console.log(5544, getSimpleElem(5544));
console.log(255, getSimpleElem(255));
console.log(238, getSimpleElem(238));
console.log(392, getSimpleElem(392));
console.log(675, getSimpleElem(675));