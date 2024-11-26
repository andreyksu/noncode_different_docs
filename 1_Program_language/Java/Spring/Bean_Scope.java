//По умолчанию используется область Singleton. Бины с такой областью создаются ровно один раз за все время существования приложения. Каждая инъекция такого бина использует один и тот же объект.


// Область Prototype означает, что новый бин будет создан на каждый запрос (инъекцию):
import org.springframework.beans.factory.config.ConfigurableBeanFactory;
import org.springframework.stereotype.Component;

@Scope("prototype")
@Component
public class PrototypeBean {}


//Область Request означает, что новый бин создается на каждый HTTP-запрос. Актуально только для веб-приложений:
import org.springframework.stereotype.Component;
import org.springframework.web.context.annotation.RequestScope;

@RequestScope
@Component
public class RequestScopedBean {}

// Области видимости request, session, application и websocket доступны, только если вы используете реализацию ApplicationContext в фреймворке Spring с поддержкой веб (например, XmlWebApplicationContext). Если вы используете эти области видимости с обычными IoC-контейнерами Spring, такими как ClassPathXmlApplicationContext, будет сгенерирован IllegalStateException c сообщением о неизвестной области видимости бина.