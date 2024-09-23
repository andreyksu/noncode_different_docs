interface CallableInterff {
    (aarg: number): number;
}

function firstt(aarg: number): number {
    console.log(`aarg = ${aarg}`)
    return aarg;
}

function secondd(fn: CallableInterff): void {
    fn(123);
}

secondd(firstt);