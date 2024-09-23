interface CallableInterf {
    (aarg: number): number;
    (aarg: string) : string;
}

function first_4(aarg: number): number {
    console.log(`aarg = ${aarg}`)
    return aarg;
}

function second_4(fn: CallableInterf): void {
    fn(123);
}

//second_4(first_4); // It doesnt perimt. Не соответствует интерфесу.
