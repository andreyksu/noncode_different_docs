//+++++++++++++++++++++++++++++++++++++++++++++++++++
//	XML
//+++++++++++++++++++++++++++++++++++++++++++++++++++
//Сначала сделаем простой класс:

public class HelloWorld {
    public void init() throws Exception
    {
        System.out.println("Я инит-метод " + this.getClass().getSimpleName());
    }

    public void destroy() throws Exception
    {
        System.out.println("Я дестрой-метод " + this.getClass().getSimpleName());
    }
}

//Чтобы использовать пользовательские методы init() и destroy() нам необходимо зарегистрировать их в Spring XML конфигурационном файле при описании бина:

/*
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

    <bean id="helloWorld" class="HelloWorld" init-method="init" destroy-method="destroy"/>

</beans>
*/

//Также потребуется класс-runner, который и запустит наш контекст:


public class App {
    public static void main(String[] args) {
        ConfigurableApplicationContext context
        					= new ClassPathXmlApplicationContext("spring.xml");
        context.close();
        }
}

//Обратите внимание, что в нём указан адрес файла конфигурации бинов.

//+++++++++++++++++++++++++++++++++++++++++++++++++++
//	Java-код («программный метод»)
//+++++++++++++++++++++++++++++++++++++++++++++++++++
/*
	Для того чтобы это реализовать необходимо в классе бина HelloWorldByJavaCode имплементировать два интерфейса, InitializingBean и DisposableBean, а затем переопределить методы afterPropertiesSet() и destroy().
	Метод afterPropertiesSet() вызывается при запуске спринг-конейтнера и инстанцировании бина, а метод destroy() сразу после того как контейнер завершит свою работу.
	Чтобы вызвать метод destroy() нам необходимо явно закрыть спринг-контекст, вызвав метод close() у объекта ConfigurableApplicationContext.
*/

public class HelloWorldByJavaCode implements InitializingBean, DisposableBean {
    @Override
    public void destroy() throws Exception { //DisposableBean 
        System.out.println("Я дестрой-метод " + this.getClass().getSimpleName());
    }

    @Override
    public void afterPropertiesSet() throws Exception { //InitializingBean
        System.out.println("Я инит-метод " + this.getClass().getSimpleName());
    }
}

/*
В XML регистрация бина будет выглядеть так:
<bean id="helloWorldByJavaCode" class="HelloWorldByJavaCode"/>
*/

//Класс-runner остается прежним


//+++++++++++++++++++++++++++++++++++++++++++++++++++
//	С помощью аннотаций
//+++++++++++++++++++++++++++++++++++++++++++++++++++

/*
	Чтобы вызывать методы init() и destroy() нам необходимо указать над методами соответствующие аннотации - @PostConstruct и @PreDestroy.
	Чтобы вызвать метод destroy() нам необходимо явно закрыть спринг-контекст, вызвав метод close() у объекта ConfigurableApplicationContext. Класс-runner остается прежним
	Cоздадим бин HelloWorldByAnnotations.java и аннотируем соответствующие методы:
*/

public class HelloWorldByAnnotations {

    @PostConstruct
    public void init() throws Exception
    {
        System.out.println("Я инит-метод " + this.getClass().getSimpleName());
    }

    @PreDestroy
    public void destroy() throws Exception
    {
        System.out.println("Я дестрой-метод " + this.getClass().getSimpleName());
    }
}

/*
В XML-файле появится дополнительная строчка, отвечающая за бин, читающий аннотации:

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

    <bean id="helloWorldByAnnotations" class="HelloWorldByAnnotations"/>
    <bean class="org.springframework.context.annotation.CommonAnnotationBeanPostProcessor"/>

</beans>
*/

/*
Аннотации @PostConstruct и @PreDestroy, стандартизированные JSR-250, обычно считаются лучшей методикой получения обратных вызовов жизненного цикла в современном приложении на Spring.
Использование данных аннотаций означает, что ваши бины не связаны с интерфейсами, специфичными для Spring.
*/