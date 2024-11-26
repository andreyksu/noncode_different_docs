let worker = {
    field: ' fieldd ',
    someMethod() {
        return " someMethod ";
    },
    slow(x) {
        console.log("Called with " + x + this.field + this.someMethod());
        console.log("Called with " + x + this.someMethod());
    }
};

let func = worker.slow; // Аналогично и здесь будет потеря this.
func.call(worker, ' With_call '); // Так норм.
func(' With_call '); // А тут ошибка

//==========================================================================
// Это исходная задача. Первая и главная проблема - это потеря this при присванивании
let worker = {
    field: 'fieldd',

    someMethod() {
        return 1;
    },

    slow(x) {
        console.log("Called with " + x);
        return x * this.someMethod();
    }
};

function cachingDecorator(func) {
    // console.log(this.field); (1) - т.к. у функции 'cachingDecorator()' контекста нет, т.к. мы привязываем к полю не 'cachingDecorator()', а то что она вернула.
    let cache = new Map();
    return function (x) {
        if (cache.has(x)) {
            return cache.get(x);
        }
        // let result = myThis.func(x); // Вот проблемное место. И это проблема не из за вложенности функций. Т.к. cachingDecorator() this не имеет см. (1)
        let result = func.call(this, x) + " cached ";
        cache.set(x, result);
        return result;
    };
}

console.log(worker.slow(1));
worker.slow = cachingDecorator(worker.slow); // Похоже --- здесь контекст утерян. По этой причине (1) не имеет доступа к this. 
/*
  Да все так. Мы в cachingDecorator() передаём просто ссылку на метод, которая ложится в 'func', и эта ссылка приходит без контекста this.
  Далее возвращаем Функцию 'return function(x)' которая пирвязывается к полю Объекта и в результате привязки возвращённая функция получает контекст this.
  Но внутри возвращённой функции ссылка func - по прежнему не имеет контекста (т.к. его не было при передаче и ему не от куда взяться).

    Т.е. проблема не про вложенность функций и невозможность получить доступ к this из внешней функции. т.е. let linkk = this в месте (1) не помогло бы.
*/
console.log(worker.slow(2));