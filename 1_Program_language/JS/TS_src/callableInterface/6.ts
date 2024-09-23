interface CallableInterfff {
    (aarg: number): number;
    (aarg: string): string;
    paaram: string;
}


function first_6(aarg: any): any {
    console.log(`aarg = ${aarg}`)
    return aarg;
}

function second_6(fn: CallableInterfff): void {
    fn(123);
}
first_6.paaram = "";

second_6(first_6);