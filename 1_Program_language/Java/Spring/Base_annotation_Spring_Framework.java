//Основные аннотации Spring Framework
//Аннотации — это специальные метки в коде Java, которые предоставляют метаинформацию о компонентах приложения. В Spring они играют ключевую роль в конфигурации и управлении бинами.

//Базовые аннотации
//@Component — базовый маркер для любого компонента Spring:

    @Component
    public class MyComponent {
        // реализация
    }

//@Service — используется для бизнес-логики:

    @Service
    public class UserService {
        // методы сервиса
    }

//@Repository — для DAO и доступа к данным:

    @Repository
    public class UserRepository {
        // методы работы с данными
    }

//@Controller — для обработки HTTP-запросов:

    @Controller
    public class UserController {
        // обработчики запросов
    }

//Конфигурация
//@Configuration — указывает, что класс содержит методы для настройки бинов:

    @Configuration
    public class AppConfig {
        @Bean
        public MyBean myBean() {
            return new MyBean();
        }
    }

//@Bean — объявляет метод как фабрику бина:

    @Bean
    public UserService userService() {
        return new UserServiceImpl();
    }

//Автоматическое связывание
//@Autowired — для автоматического внедрения зависимостей:

    @Service
    public class UserService {
        @Autowired
        private UserRepository userRepository;
    }

//@Qualifier — для уточнения бина при множественных реализациях:

    @Autowired
    @Qualifier("primaryUserRepository")
    private UserRepository userRepository;

//Стереотипные аннотации
//@ComponentScan — указывает пакеты для сканирования компонентов:

    @Configuration
    @ComponentScan(basePackages = "com.example")
    public class AppConfig {
        // конфигурация
    }

//@Profile — активирует конфигурацию для определенных профилей:

    @Configuration
    @Profile("development")
    public class DevConfig {
        // конфигурация для разработки
    }

//Веб-аннотации
//@RequestMapping — для маппинга HTTP-запросов:

    @Controller
    public class UserController {
        @RequestMapping("/users")
        public String listUsers() {
            return "users";
        }
    }

//@RestController — комбинация @Controller и @ResponseBody:

    @RestController
    public class UserRestController {
        @GetMapping("/api/users")
        public List<User> getUsers() {
            return userService.getAllUsers();
        }
    }

Транзакции
@Transactional — для управления транзакциями:

    @Service
    public class UserService {
        @Transactional
        public void saveUser(User user) {
            // сохранение пользователя
        }
    }

Spring Boot аннотации
@SpringBootApplication — объединяет @Configuration, @ComponentScan и @EnableAutoConfiguration:

    @SpringBootApplication
    public class MyApplication {
        public static void main(String[] args) {
            SpringApplication.run(MyApplication.class, args);
        }
    }

Рекомендации по использованию
    Используйте стереотипные аннотации (@Service, @Repository, @Controller) вместо общего @Component
    Применяйте @Autowired только там, где это действительно необходимо
    Используйте @Qualifier для разрешения конфликтов внедрения
    Группируйте конфигурацию в отдельные классы с @Configuration
    При разработке на Spring Boot используйте @SpringBootApplication для основной конфигурации
    Правильное использование аннотаций делает код более понятным, поддерживаемым и масштабируемым.