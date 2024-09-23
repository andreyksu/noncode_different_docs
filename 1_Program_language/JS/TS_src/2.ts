type A_Type = {
    a: string,
    b: string,
    c: string
}

const A_Obj = {
    a: 'a',
    b: 'b',
    c: 'c',
    d: 'd'
}

const A_Obj1 = {
    a: 'a',
    b: 'b',
    c: 'c',
    d: 'd',
    e: 'e'
}

class A_class {
    constructor() { }
    a = 'a';
    b = 'b';
    c = 'c';
    d = 'd';
    e = 'e';

}

function funcc(argg: A_Type) {
    console.log(argg.a);
}

funcc(A_Obj);
funcc(new A_class());

function funcc1(argg: typeof A_Obj) {
    console.log(argg.a);
}

funcc1(A_Obj1);
funcc1(new A_class());


function funcc2<T extends number>(argg: T) {
    console.log(typeof argg);
}
funcc2(2)