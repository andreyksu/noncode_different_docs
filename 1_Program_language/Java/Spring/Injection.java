// Инжектируем Engine

// Constructor Injection
// The dependencies are passed when an instance of the class is created.
public class Car {
    private Engine engine;
    public Car(Engine engine) {
        this.engine = engine;
    }
}

// Setter Injection
// In setter injection, the dependent object is provided to the class via a setter method after the class is instantiated. This allows you to change the dependencies dynamically.
public class Car {
    private Engine engine; 
    public void setEngine(Engine engine) {
        this.engine = engine;
    }
}

// Field Injection
// The Dependency Injection automatically injects the dependency without requiring explicit constructor or setter methods.
public class Car {
    @Autowired
    private Engine engine;
}




/*
BeanFactory: BeanFactory is the simplest container and is used to create and manage beans.
It is a basic container that initializes beans lazily (i.e., only when they are needed). 
It is typically used for lightweight applications where the overhead of ApplicationContext is not required.

Note: This will create a Car bean inside the IoC container, which will be initialized when requested.
*/
<bean id="car" class="com.example.Car"/>

/*
Application Context: ApplicationContext is an advanced container that extends BeanFactory and provides additional features like internationalization support, event propagation, and AOP (Aspect-Oriented Programming) support.
The ApplicationContext is preferred in most Spring applications because of its enhanced features.

Note: This will scan the specified package for annotated components beans like @Component, @Service, @Repository, etc.

ApplicationContext belongs to the Spring framework. Spring IoC container is responsible for instantiating, wiring, configuring, and managing the entire life cycle of beans or objects. BeanFactory and ApplicationContext represent the Spring IoC Containers.

*/
<context:component-scan base-package="com.example"/>

/*
Spring Annotation
@Component: Marks a class as a Spring bean, allowing Spring to automatically detect and manage it during classpath scanning.
@Autowired: Automatically injects dependencies into a class. It can be used on fields, constructors, or methods, allowing Spring to resolve and inject the required beans.
@Bean: Defines a Spring bean explicitly within a configuration (@Configuration) class. This is used to create and configure beans that are not automatically detected by classpath scanning.
@Configuration: Indicates that a class contains bean definitions and acts as a source of bean configuration. It is used to mark a class as a configuration class that contains methods annotated with @Bean to define beans.
*/


/*
Beans are Java objects that are configured at run-time by Spring IoC Container. 
BeanFactory represents a basic IoC container which is a parent interface of ApplicationContext. 
BeanFactory uses Beans and their dependencies metadata to create and configure them at run-time. 
BeanFactory loads the bean definitions and dependency amongst the beans based on a configuration file (XML) or the beans can be directly returned when required using Java Configuration.
*/






/*
Step-by-Step Implementation to Configure Bean Factory in Spring
Step 1: Create a Student POJO class.

Now we will define bean inside the Student class file.

Student.java:

*/
// Java Program where we are
// creating a POJO class

// POJO class
public class Student {

  // Member variables
  private String name;
  private String age;

  // Constructor 1
  public Student() {
  }

  // Constructor 2
  public Student(String name, String age) {
    this.name = name;
    this.age = age;
  }

  // Method inside POJO class
  @Override
  public String toString() {

    // Print student class attributes
    return "Student{" + "name='" + name + '\'' + ", age='" + age + '\'' + '}';
  }
}

/*
Step 2: Configure the Student bean in the bean-factory-demo.xml file.
XML Bean Configuration:
*/

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="student" class="com.gfg.demo.domain.Student">
        <constructor-arg name="name" value="Tina"/>
        <constructor-arg name="age" value="21"/>
    </bean>
</beans>

/*
Step 3: Now let's write the main class file.
*/

@SpringBootApplication
// Main class
public class DemoApplication 
{
// Main driver method
  public static void main(String[] args) 
  {
    // Creating object in a spring container (Beans)
    BeanFactory factory = new ClassPathXmlApplicationContext("bean-factory-demo.xml");
    Student student = (Student) factory.getBean("student");

    System.out.println(student);
  }
}




/*
 Пример объявления для прямого вызова метода setDataSource и передачи в него готового объекта
*/

public class JdbcCorporateEventDao implements CorporateEventDao {
    private JdbcTemplate jdbcTemplate;
    public void setDataSource(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }
    // Реализации методов CorporateEventDao с поддержкой JDBC следуют...
}

/*
 Пример передачи через аннотации. Благодаря аннотации @Autowired в метод setDataSource будет инжектирован объект dataSource.
*/
@Repository 
public class JdbcCorporateEventDao implements CorporateEventDao {
    private JdbcTemplate jdbcTemplate;
    @Autowired 
    public void setDataSource(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource); 
    }
    // Реализации методов CorporateEventDao с поддержкой JDBC следуют...
}

// Соответствующиие XML - для первого варианта
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">
    <bean id="corporateEventDao" class="com.example.JdbcCorporateEventDao">
        <property name="dataSource" ref="dataSource"/>
    </bean>
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
        <property name="driverClassName" value="${jdbc.driverClassName}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>
    <context:property-placeholder location="jdbc.properties"/>
</beans>

// Соответствующиие XML - для второго варианта

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">
    <!-- Поиск в базовом пакете приложения классов с аннотацией @Component для конфигурирования в качестве бинов  -->
    <context:component-scan base-package="org.springframework.docs.test" />
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
        <property name="driverClassName" value="${jdbc.driverClassName}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>
    <context:property-placeholder location="jdbc.properties"/>
</beans>



/*
Aspect-Oriented Programming (AOP)
Как я понял это модулность по зоне ответственности.
    Aspect-Oriented Programming allows us to think differently about the structure of the program by enabling the modularization of concerns. It helps in breaking down the logic into parts known as concerns and the concerns help in dividing the business logic of an application and in increasing the modularity. Compared to OOP, AOP has no comparison as AOP emerged out of the OOP paradigm. Just like class is the key to the modularity of OOP, aspect is the key to the modularity of AOP.

The Spring framework is modular and consists of several modules that provide different functionalities to help build enterprise applications. 
The modules can be broadly categorized into four main areas:
- Core Container
    - Spring Core: This module provides the fundamental functionality of the Spring framework, including IoC and DI. The IoC container is the heart of the Spring Framework, responsible for creating and managing instances of JavaBeans. It uses dependency injection to wire the beans together.
    - Spring Beans: This module provides the BeanFactory, which is the basic building block of the IoC container, and the BeanWrapper, which is responsible for managing the lifecycle of a bean. The Bean Factory is the core interface for accessing the IoC container. It provides methods for retrieving beans.
    - Spring Context: This module provides the ApplicationContext, which is an advanced version of the BeanFactory and provides additional features, such as internationalization and resource loading, and the ability to publish and consume events.
    - Spring Expression Language (SpEL): This module provides a powerful expression language for querying and manipulating objects during runtime. SpEL supports a wide range of features, including property access, method invocation, conditionals, loops, and type conversion. It also provides support for accessing variables and functions defined in the application context, as well as support for defining custom functions and variables.
- Data Access/Integration
    - Spring JDBC: This module provides a simple JDBC abstraction layer that reduces the amount of boilerplate code required to work with JDBC. Spring JDBC provides support for transaction management, allowing developers to manage database transactions declaratively using Spring's transaction management.
    - Spring ORM: This module provides integration with Object-Relational Mapping (ORM) frameworks, such as Hibernate and JPA. Spring ORM provides a higher-level abstraction layer on top of ORM frameworks, allowing developers to write less boilerplate code and more easily integrate ORM technologies with other Spring features, such as transaction management and caching.
    - Spring Data: This module provides a consistent and easy-to-use programming model for working with data access technologies, including databases, NoSQL, and cloud-based data services. Spring Data provides a wide range of features, including automatic CRUD (Create, Read, Update, Delete) operations, query generation from method names, support for pagination and sorting, integration with Spring's transaction management, and more. Additionally, Spring Data provides support for common data access patterns, such as repositories and data access objects (DAOs).
    - Spring Transaction: This module provides support for declarative transaction management in Spring applications. Spring Transaction provides support for various transaction propagation and isolation levels, allowing developers to manage transactions at different levels of granularity. Additionally, Spring Transaction provides support for different transaction management strategies, such as using a JTA transaction manager or a simple JDBC transaction manager.
- Web
    - Spring MVC: This module provides a Model-View-Controller (MVC) framework for building web applications. Spring MVC provides a range of features, including support for handling HTTP requests and responses, form handling, data binding, validation, and more. It also provides support for different view technologies, such as JSP (JavaServer Pages), Thymeleaf, and Velocity, allowing developers to choose the view technology that best suits their needs.
    - Spring WebFlux: This module provides a reactive programming model for building web applications that require high concurrency and scalability. Spring WebFlux provides support for building reactive web applications using a range of technologies, such as Netty, Undertow, and Servlet 3.1+ containers. It also provides a range of features, including support for reactive data access, reactive stream processing, and reactive HTTP clients.
    - Spring Web Services: This module provides support for building SOAP-based and RESTful web services. Spring Web Services provides support for generating WSDL (Web Services Description Language) from Java classes, and for generating Java classes from WSDL. This allows developers to define the contract (i.e., the interface) of their web service using WSDL, and to generate the Java classes that implement the web service from the WSDL.
- Miscellaneous.
    - Spring Security: This module provides authentication and authorization features for Spring applications. Spring Security provides a range of authorization mechanisms, such as role-based access control and expression-based access control. It also provides support for securing different parts of the application using different security configurations, allowing developers to apply fine-grained security policies.
    - Spring Integration: This module provides support for building message-driven and event-driven architectures. Spring Integration provides a range of integration patterns, such as messaging, routing, and transformation. It provides support for a range of messaging systems, such as JMS, AMQP, and Apache Kafka. It also provides support for integrating with different protocols, such as FTP, HTTP, and TCP.
    - Spring Batch: This module provides support for batch processing and integration with enterprise systems. Spring Batch provides a range of tools and utilities for building and managing batch processing applications, such as support for testing and debugging batch jobs, logging and monitoring, and integration with other Spring modules, such as Spring Data and Spring Integration.
    - Spring Cloud: This module provides support for building cloud-native applications using Spring technologies. Spring Cloud provides a range of features for building cloud-native applications, such as service discovery, configuration management, and load balancing. It provides support for integrating with different cloud platforms, such as AWS and GCP, and for using different cloud-native technologies, such as containers and serverless computing.
*/



/*
Bean Life Cycle Phases
The lifecycle of a Spring bean consists of the following phases, which are listed below

Container Started: The Spring IoC container is initialized.
Bean Instantiated: The container creates an instance of the bean.
Dependencies Injected: The container injects the dependencies into the bean.
Custom init() method: If the bean implements InitializingBean or has a custom initialization method specified via @PostConstruct or init-method.
Bean is Ready: The bean is now fully initialized and ready to be used.
Custom utility method: This could be any custom method you have defined in your bean.
Custom destroy() method: If the bean implements DisposableBean or has a custom destruction method specified via @PreDestroy or destroy-method, it is called when the container is shutting down.
*/