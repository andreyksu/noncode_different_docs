//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	//Java-Based Configuration   Самый современный.
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// One of the modern approaches in Spring is to use Java-based configuration with annotations instead of XML. The main techniques are:

//@Configuration and @Bean   (@Configuration, @Bean, @Import и @DependsOn.)

//@Configuration:
	//This annotation marks a class as a source of bean definitions. It’s similar to the XML configuration files of older Spring versions.
//@Bean:
	//Methods annotated with @Bean inside a @Configuration class produce a bean managed by the Spring container. You can define the instantiation, any dependency injection, and configuration within that method.

// @Configuration – это аннотация на уровне класса, указывающая на то, что объект является источником определений бина. Классы, аннотированные @Configuration, объявляют бины через методы, аннотированные @Bean.
// Помните, что классы, аннотированные @Configuration, в конечном итоге являются лишь еще одним бином в контейнере: Это означает, что они могут использовать преимущества внедрения @Autowired и @Value и другие возможности так же, как и любой другой бин.

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean
    public MyComponent myComponent() {
        return new MyComponent();
    }

    @Bean
    public MyService myService() {
        // Spring automatically injects myComponent() bean into the myService bean if MyService has a constructor or setter that accepts it
        return new MyService(myComponent());
    }
}


// @Import
// Подобно элементу <import/>, используемому в XML-файлах Spring, аннотация @Import позволяет загружать определения, помеченные аннотацией @Bean, из другого класса конфигурации для облегчения модульной организации конфигураций, как показано в следующем примере:


@Configuration
public class ConfigA {
    @Bean
    public A a() {
        return new A();
    }
}

@Configuration
@Import(ConfigA.class)
public class ConfigB {
    @Bean
    public B b() {
        return new B();
    }
}

public static void main(String[] args) {
    ApplicationContext ctx = new AnnotationConfigApplicationContext(ConfigB.class);
    // теперь оба бина A и B будут доступны...
    A a = ctx.getBean(A.class);
    B b = ctx.getBean(B.class);
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	//XML-Based Configuration
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//In this XML configuration, the beans for MyComponent and MyService are defined similarly to the Java-based configuration.
/*
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
         http://www.springframework.org/schema/beans 
         https://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="myComponent" class="com.example.MyComponent" />

    <bean id="myService" class="com.example.MyService">
        <constructor-arg ref="myComponent" />
    </bean>
</beans>
*/
// The id attribute is a string that identifies the individual bean definition.
// The class attribute defines the type of the bean and uses the fully qualified class name.

ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
// retrieve configured instance
PetStoreService service = context.getBean("petStore", PetStoreService.class);

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	//Spring Boot Auto-Configuration
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	// Automatically configuring many components based on dependencies present on the classpath.
	// Using sensible defaults to reduce boilerplate.

/*
Auto-configuration classes:

	Spring Boot’s auto-configuration features inspect the classpath and bean definitions to automatically set up the application context.
	This behavior is enabled by the @SpringBootApplication annotation, which is itself a composite of several annotations (one of which is @EnableAutoConfiguration)
*/

/*
	application.properties / application.yml

	Example (application.properties):

	server.port=8081
	spring.datasource.url=jdbc:mysql://localhost:3306/mydb
	spring.datasource.username=dbuser
	spring.datasource.password=dbpassword

	These external properties are then injected into your beans, for instance, through the @Value annotation or by using a dedicated @ConfigurationProperties class.
*/

/*
	Using @ConfigurationProperties

	For binding a group of properties into a POJO, Spring Boot provides this annotation. It helps in managing structured configuration data.
*/
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private String name;
    private int version;

    // getters and setters

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getVersion() {
        return version;
    }
    public void setVersion(int version) {
        this.version = version;
    }
}
/*
	With a corresponding entry in your application.properties
	app.name=My Spring Application
	app.version=1
*/

//-----------------------------------------------
//Conditional Configuration
/*
	Spring allows you to apply configuration conditionally using annotations such as:
	@Conditional:
	This annotation can be used to conditionally include beans based on some criteria.
	@Profile:
*/

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
public class DataSourceConfig {

    @Bean
    @Profile("dev")
    public DataSource devDataSource() {
        // return a DataSource configured for development
    }

    @Bean
    @Profile("prod")
    public DataSource prodDataSource() {
        // return a DataSource configured for production
    }
}
//You can activate a profile via the command line (e.g., --spring.profiles.active=dev), in the properties file, or programmatically


//-----------------------------------------------
// @Qualifier
// Resolves ambiguity when multiple beans of the same type are candidates for dependency injection.
// When you have more than one bean implementing the same interface or of the same type, and you need to specify which bean should be injected. It customizes injection on a per-dependency level.

// @Profile
// Controls bean registration based on the active environment or runtime profile (e.g., development, testing, production).
// When you want to define different beans (or configurations) for different environments. For example, you might have a different datasource for development than for production.

// @Qualifier sharpens the injection selection when multiple beans of the same type are defined.
// @Profile governs the registration of beans based on the environment or deployment scenario.
//-----------------------------------------------


// @Qualifier
// In Spring, when multiple beans of the same type exist in the ApplicationContext, the container may not know which one should be injected into a dependency. The @Qualifier annotation is used in conjunction with dependency injection (typically with @Autowired) to resolve this ambiguity by specifying which bean should be injected.


package com.example.demo;

public interface PaymentService {
    void processPayment(double amount);
}

package com.example.demo;

import org.springframework.stereotype.Component;

@Component
@Qualifier("creditCardPayment")
public class CreditCardPaymentService implements PaymentService {
    @Override
    public void processPayment(double amount) {
        System.out.println("Processing credit card payment of $" + amount);
    }
}

package com.example.demo;

import org.springframework.stereotype.Component;

@Component
@Qualifier("paypalPayment")
public class PayPalPaymentService implements PaymentService {
    @Override
    public void processPayment(double amount) {
        System.out.println("Processing PayPal payment of $" + amount);
    }
}

// When you inject PaymentService into another bean, you can specify which implementation you need by using @Qualifier:

package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class PaymentProcessor {

    private final PaymentService paymentService;

    @Autowired
    public PaymentProcessor(@Qualifier("paypalPayment") PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void process(double amount) {
        paymentService.processPayment(amount);
    }
}

@Component
public class PaymentProcessor {

    @Autowired
    @Qualifier("creditCardPayment")
    private PaymentService paymentService;

    public void process(double amount) {
        paymentService.processPayment(amount);
    }
}

//@Primary Alternative
// If you frequently use one implementation, you can mark it with @Primary so that it becomes the default injection candidate when multiple beans of the same type are available.
// In this case, you might not need a @Qualifier unless you want to override that behavior in a specific situation.

@Component
@Primary
public class CreditCardPaymentService implements PaymentService {
    // implementation details...
}