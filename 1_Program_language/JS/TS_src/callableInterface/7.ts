interface CallableInterfff {
    (aarg: number): number;
    (aarg: string): string;
}


function firstttt<T extends number | string>(aarg: T): T {
    console.log(`aarg = ${aarg}`)
    return aarg;
}

function secondddd(fn: CallableInterfff): void {
    fn(123);
}

secondddd(firstttt);