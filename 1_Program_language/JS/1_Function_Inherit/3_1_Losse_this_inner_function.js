// Первый пример с вложенной функцией и потерей this
let worker = {
  someMethod() {
    return 1;
  }
};

function outer_method(x){
  console.log(this.someMethod() + " outer");
  function inner_method(){
    console.log(this.someMethod() + " inner");// Проблемное место. Отсутствие доступа к this у вложенной функции
  }
  // inner_method.call(this); // Так работает. Мы прокинули контекст из внешней функции во внутреннюю через call.
  inner_method(); // Так не работает. У внутренней функции нет доступа к this внешней функции. Но здесь бы помогла стрелочная функция, кторая не имеет своего this и взяла бы из внешней.
}

worker.new_method = outer_method;

worker.new_method("s");

// =============================================================================================
// Вот второй рабочий пример с добавлением переменной.
let worker = {
  someMethod() {
    return 1;
  }
};

function outer_method(x){
  let kk = this; // Добавляем переменную с this
  console.log(this.someMethod() + " outer");
  function inner_method(){
    console.log(kk.someMethod() + " inner"); // Используем эту переменную во внутренней функции
  }  
  inner_method(); // Можно вызывтаь без проблем
}

worker.new_method = outer_method;

worker.new_method("s");
