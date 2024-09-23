/*
По сути, Spring предлагает контейнер, часто называемый контекстом приложения Spring, который создает компоненты приложения и управляет ими. Эти компоненты, или bean-компоненты, объединяются внутри контекста Spring, образуя полноценное приложение.

Жизненный цикл Spring Beans
+  1. Instantation
        Инстанцирование бина: Создает экземпляр бина из класса определения бина.
+  2. Dependency Injection
        Заполнение свойств бина: Внедряет значения и ссылки на другие бины в свойства текущего бина, используя конфигурацию, заданную в XML, аннотациях или конфигурации.
            - Через конструктор
            - Через поле - @Autowired
            - Через сеттеры – используется, если зависимость может изменяться после создания бина.
            - Через аннотации @Value, @Qualifier
  3. Aware-интерфейсы
        Вызов методов жизненного цикла `BeanNameAware`, `BeanClassLoaderAware`, `BeanFactoryAware` и т.д.: Если бин реализует один из Aware интерфейсов, он вызывает соответствующие методы, передавая экземпляру бина ссылку на контекст, фабрику бинов и т.д.

+  4. Post-Processing Bean: Перед инициализацией бина, он дает возможность BeanPostProcessor'ам обработать объект. Это может быть использовано для проксирования бинов или для иной предварительной обработки.

+ 5.  Вызов метода инициализации: Если для бина определен метод инициализации (через аннотацию `@PostConstruct`, интерфейс `InitializingBean` или атрибут `init-method` в XML-конфигурации), он вызывает его после того, как все свойства бина были установлены.

+  6. BeanPostProcessor после инициализации: Готовность к использованию: После вызова метода инициализации бин полностью инициализирован и готов к использованию в приложении.
+  7. Вызов метода уничтожения: Когда контекст приложения закрывается, и бины должны быть уничтожены, он вызывает метод уничтожения для бинов, которые определяют его (через аннотацию `@PreDestroy`, интерфейс `DisposableBean` или атрибут `destroy-method` в XML-конфигурации).
        - @PreDestroy
*/


//@PostConstruct и @PreDestroy
import jakarta.annotation.PostConstruct;
import org.springframework.stereotype.Component;

@Component
public class MyBean {

    private String message;

    @PostConstruct
    public void init() {
        this.message = "Bean is initialized!";
        System.out.println(message);
    }

    @PreDestroy
    public void cleanup() {
        System.out.println("Cleaning up resources or performing final actions!");
    }

    // ... other methods ...
}
/*
Типичные ситуации, когда это бывает нужно:
	- Чтение конфигурации и инициализация некоторых свойств
	- Установка ресурсов, таких как соединение с базой данных
	- Регистрация бинов во внешних системах
*/

// Фабричный подход Ну когда создаёшь класс @configuration и вешаешь на методы @bean






/*
Рекомендации
    Используйте @PostConstruct и @PreDestroy вместо реализации интерфейсов
    Избегайте прямого использования Aware-интерфейсов. 
    Группируйте код инициализации в одном месте
    Обеспечьте корректное освобождение ресурсов в методах уничтожения

    Вместо реализации ApplicationContextAware можно использовать. Предпочитайте внедрение зависимостей вместо прямого доступа к контексту.
        @Autowired
        private ApplicationContext context;

        @Autowired        
        private Environment environment;
*/

// Главный бин с логами всех этапов
@Component
class MyBean implements BeanNameAware, ApplicationContextAware, InitializingBean, DisposableBean {
    
    private String beanName;
    private ApplicationContext context;

    public MyBean() {
        System.out.println("1. Конструктор MyBean вызван (Instantiation)");
    }

    @Autowired
    public void setDependency(MyDependency dependency) {
        System.out.println("2. Зависимость MyDependency внедрена (DI)");
    }

    @Override
    public void setBeanName(String name) {
        this.beanName = name;
        System.out.println("3. BeanNameAware: Имя бина - " + name);
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.context = applicationContext;
        System.out.println("3. ApplicationContextAware: Контекст передан");
    }

    @PostConstruct
    public void postConstruct() {
        System.out.println("5. @PostConstruct: Бин проинициализирован");
    }

    @Override
    public void afterPropertiesSet() {
        System.out.println("5. InitializingBean: Бин завершил инициализацию");
    }

    @PreDestroy
    public void preDestroy() {
        System.out.println("7. @PreDestroy: Перед уничтожением бина");
    }

    @Override
    public void destroy() {
        System.out.println("7. DisposableBean: Бин уничтожен");
    }
}

// Дополнительный бин для DI
@Component
class MyDependency {
    public MyDependency() {
        System.out.println("1. Конструктор MyDependency вызван (Instantiation)");
    }
}

// BeanPostProcessor для логирования этапов postProcessBeforeInitialization и postProcessAfterInitialization
@Component
class MyBeanPostProcessor implements BeanPostProcessor {
    
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) {
        if (bean instanceof MyBean) {
            System.out.println("4. BeanPostProcessor: Before Init - " + beanName);
        }
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) {
        if (bean instanceof MyBean) {
            System.out.println("6. BeanPostProcessor: After Init - " + beanName);
        }
        return bean;
    }
}

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
/*
📌 Вывод в консоль
1. Конструктор MyDependency вызван (Instantiation)
1. Конструктор MyBean вызван (Instantiation)
2. Зависимость MyDependency внедрена (DI)
3. BeanNameAware: Имя бина - myBean
3. ApplicationContextAware: Контекст передан
4. BeanPostProcessor: Before Init - myBean
5. @PostConstruct: Бин проинициализирован
5. InitializingBean: Бин завершил инициализацию
6. BeanPostProcessor: After Init - myBean
>>> Контекст запущен

>>> Закрытие контекста
7. @PreDestroy: Перед уничтожением бина
7. DisposableBean: Бин уничтожен
*/







// Еще пример
Полный пример жизненного цикла бина в Spring Boot
Структура проекта
src/main/java
    com.example
        lifecycle
            MyBean.java
            AppConfig.java
            Application.java
Основной класс приложения
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
Конфигурация
@Configuration
public class AppConfig {
    @Bean(initMethod = "init", destroyMethod = "destroy")
    public MyBean myBean() {
        return new MyBean();
    }
}
Основной бин с полным жизненным циклом
@Component
public class MyBean {
    private String name;
    
    // Конструктор
    public MyBean() {
        System.out.println("1. Конструктор вызван");
    }
    
    // Метод инициализации через @PostConstruct
    @PostConstruct
    public void init() {
        System.out.println("2. Инициализация через @PostConstruct");
        name = "Initialized Bean";
    }
    
    // Пользовательский метод инициализации
    public void init() {
        System.out.println("3. Пользовательский init метод");
    }
    
    // Метод уничтожения через @PreDestroy
    @PreDestroy
    public void destroy() {
        System.out.println("5. Уничтожение через @PreDestroy");
    }
    
    // Пользовательский метод уничтожения
    public void destroy() {
        System.out.println("6. Пользовательский destroy метод");
    }
    
    // Обычный метод бина
    public void doSomething() {
        System.out.println("4. Бин используется: " + name);
    }
}
//Тестирование жизненного цикла
@SpringBootTest
class LifecycleTest {
    @Autowired
    private MyBean myBean;
    
    @Test
    void testLifecycle() {
        // Вызов метода бина
        myBean.doSomething();
        
        // Имитация завершения работы приложения
        // (в реальном приложении это произойдет автоматически)
    }
}
/*
    Порядок выполнения
    Создание бина:
        Вызывается конструктор
        Внедряются зависимости

    Инициализация:
        Вызывается метод с аннотацией @PostConstruct
        Вызывается указанный initMethod
        Выполняется пользовательский метод init

    Использование:
    Бин готов к работе
    Можно вызывать его методы

    Уничтожение:
    При завершении работы приложения:
        Вызывается метод с аннотацией @PreDestroy
        Вызывается указанный destroyMethod
        Выполняется пользовательский метод destroy

    Вывод в консоль
    При запуске приложения будет выведено:

        1. Конструктор вызван
        2. Инициализация через @PostConstruct
        3. Пользовательский init метод
        4. Бин используется: Initialized Bean
        5. Уничтожение через @PreDestroy
        6. Пользовательский destroy метод

    Рекомендации
        Используйте @PostConstruct и @PreDestroy вместо реализации интерфейсов
        Группируйте код инициализации в одном месте
        Обеспечьте корректное освобождение ресурсов в методах уничтожения
        Избегайте прямого использования Spring API в бизнес-логике
        Используйте initMethod и destroyMethod только при необходимости
        Такой подход обеспечивает современный и гибкий способ управления жизненным циклом бинов в Spring Boot приложениях.
*/