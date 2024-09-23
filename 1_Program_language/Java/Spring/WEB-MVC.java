//WEB-MVC

@ModelAttribute
public void addAttributes(Model model) {
    model.addAttribute("msg", "Welcome to the Netherlands!");
}

	// In general, Spring MVC will always make a call to that method first, before it calls any request handler methods. Basically, @ModelAttribute methods are invoked before the controller methods annotated with @RequestMapping are invoked. This is because the model object has to be created before any processing starts inside the controller methods.


//-------------------------------------------------------------------------------------

@RequestMapping(value = "/addEmployee", method = RequestMethod.POST)
public String submit(@ModelAttribute("employee") Employee employee) {
    // Code that uses the employee object

    return "employeeView";
}
	// We populate the employee model attribute with data from a form submitted to the addEmployee endpoint. Spring MVC does this behind the scenes before invoking the submit method.

	// When we use the annotation as a method argument, it indicates to retrieve the argument from the model. When the annotation isn’t present, it should first be instantiated, and then added to the model. Once present in the model, the arguments fields should populate from all request parameters that have matching names.



//Наименования в форме и в атрибуте не обязательно должны совпадать, но есть важные моменты, которые нужно учитывать.
<!-- Вариант 1 -->
<form th:object="${order}" method="post">
    <input type="text" th:field="*{name}" />
</form>

<!-- Вариант 2 -->
<form th:object="${tacoOrder}" method="post">
    <input type="text" th:field="*{name}" />
</form>

@PostMapping("/submit")
public String processOrder(@ModelAttribute("order") TacoOrder order) {
    // Обработка заказа
    return "success";
}

@PostMapping("/submit")
public String processOrder(@ModelAttribute("tacoOrder") TacoOrder order) {
    // Обработка заказа
    return "success";
}
//---
Синтаксис th:field
	*{имяПоля} - относительный путь к полю объекта
	$(имяОбъекта.имяПоля) - абсолютный путь

Пример с вложенными объектами
<form th:object="${order}" method="post">
    <!-- Прямой доступ к полю -->
    <input type="text" th:field="*{customer.name}" />
    
    <!-- Или через абсолютный путь -->
    <input type="text" th:field="${order.customer.name}" />
</form>