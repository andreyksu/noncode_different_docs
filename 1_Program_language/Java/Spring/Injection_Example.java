//-----------------------------------------------
import javax.inject.Inject;
import org.springframework.stereotype.Component;

@Component
public class MyService {

    private final MyComponent myComponent;

    @Inject
    public MyService(MyComponent myComponent) {
        this.myComponent = myComponent;
    }

    public void performService() {
        myComponent.doSomething();
    }
}

//-----------------------------------------------
//It is typically used when you want to inject a bean based on a specific name or when you need to reference external resources.
//Note that if you don't specify the name, it will use the field name by default to resolve the bean.

import javax.annotation.Resource;
import org.springframework.stereotype.Component;

@Component
public class MyService {

    @Resource(name = "myComponent")
    private MyComponent myComponent;

    public void performService() {
        myComponent.doSomething();
    }
}


//-----------------------------------------------
//If your bean has only one constructor, you can omit the @Autowired annotation. Spring will automatically use this constructor for dependency injection.
//Simply define a single constructor in your class with the required dependencies, and Spring will inject them.
import org.springframework.stereotype.Component;

@Component
public class MyService {

    private final MyComponent myComponent;

    // No need for @Autowired if there's only one constructor
    public MyService(MyComponent myComponent) {
        this.myComponent = myComponent;
    }

    public void performService() {
        myComponent.doSomething();
    }
}

//-----------------------------------------------
//Dependency injection can also be done through setter methods. You can annotate a setter method with @Autowired, @Inject, or @Resource.
//This is useful if the dependency is optional or mutable after initial construction.
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MyService {

    private MyComponent myComponent;

    @Autowired
    public void setMyComponent(MyComponent myComponent) {
        this.myComponent = myComponent;
    }

    public void performService() {
        myComponent.doSomething();
    }
}