# **CompletableFuture в Java: Подробный разбор**  

`CompletableFuture` — это мощный инструмент для асинхронного программирования в Java (появился в Java 8). Он позволяет:  
- Запускать задачи в фоне.  
- Строить цепочки вычислений.  
- Комбинировать несколько асинхронных операций.  
- Обрабатывать ошибки.  

В отличие от `Future` из `java.util.concurrent`, `CompletableFuture` неблокирующий и поддерживает callback'и.  

---

## **1. Создание CompletableFuture**  

### **1.1. Простое создание**  
```java
CompletableFuture<String> future = new CompletableFuture<>();
future.complete("Результат"); // Завершаем вручную
```

### **1.2. Запуск асинхронной задачи**  
```java
// Запуск в ForkJoinPool.commonPool()
CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
    System.out.println("Запущено в фоне");
});

// С собственным Executor
ExecutorService executor = Executors.newFixedThreadPool(2);
CompletableFuture<Void> customFuture = CompletableFuture.runAsync(() -> {
    System.out.println("Запущено в кастомном пуле");
}, executor);
```

### **1.3. Асинхронное вычисление с результатом**  
```java
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "Результат вычисления";
});

// Получение результата (блокирует поток!)
String result = future.get(); // или future.join() (без checked исключений)
```

---

## **2. Цепочки вычислений (Chaining)**  

### **2.1. `thenApply()` – преобразование результата**  
```java
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Hello")
    .thenApply(s -> s + " World") // "Hello World"
    .thenApply(String::toUpperCase); // "HELLO WORLD"
```

### **2.2. `thenAccept()` – потребитель (void)**  
```java
CompletableFuture.supplyAsync(() -> "Data")
    .thenAccept(data -> System.out.println("Получено: " + data));
```

### **2.3. `thenRun()` – выполнить после завершения**  
```java
CompletableFuture.supplyAsync(() -> "Done")
    .thenRun(() -> System.out.println("Завершено"));
```

### **2.4. `thenCompose()` – объединение Future (flatMap)**  
```java
CompletableFuture<String> getUser = CompletableFuture.supplyAsync(() -> "Alice");
CompletableFuture<Integer> getScore = CompletableFuture.supplyAsync(() -> 100);

CompletableFuture<String> result = getUser.thenCompose(name -> 
    getScore.thenApply(score -> name + ": " + score) // "Alice: 100"
);
```

---

## **3. Комбинирование Future**  

### **3.1. `thenCombine()` – объединить два Future**  
```java
CompletableFuture<String> hello = CompletableFuture.supplyAsync(() -> "Hello");
CompletableFuture<String> world = CompletableFuture.supplyAsync(() -> "World");

CompletableFuture<String> combined = hello.thenCombine(world, (h, w) -> h + " " + w);
// "Hello World"
```

### **3.2. `allOf()` / `anyOf()` – ожидание нескольких Future**  
```java
CompletableFuture<String> task1 = CompletableFuture.supplyAsync(() -> "A");
CompletableFuture<String> task2 = CompletableFuture.supplyAsync(() -> "B");

// Ждём завершения всех
CompletableFuture<Void> all = CompletableFuture.allOf(task1, task2);
all.thenRun(() -> {
    String result1 = task1.join();
    String result2 = task2.join();
    System.out.println(result1 + ", " + result2); // "A, B"
});

// Ждём первого завершённого
CompletableFuture<Object> any = CompletableFuture.anyOf(task1, task2);
any.thenAccept(result -> System.out.println("Первый: " + result));
```

---

## **4. Обработка ошибок**  

### **4.1. `exceptionally()` – обработка исключения**  
```java
CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
    if (Math.random() > 0.5) throw new RuntimeException("Ошибка!");
    return 42;
}).exceptionally(ex -> {
    System.err.println("Ошибка: " + ex.getMessage());
    return 0; // Возвращаем значение по умолчанию
});
```

### **4.2. `handle()` – универсальная обработка (успех/ошибка)**  
```java
CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> 10 / 0)
    .handle((result, ex) -> {
        if (ex != null) {
            System.err.println("Деление на ноль!");
            return -1;
        }
        return result;
    });
```

### **4.3. `whenComplete()` – логирование без изменения результата**  
```java
CompletableFuture.supplyAsync(() -> "Успех")
    .whenComplete((res, ex) -> {
        if (ex != null) System.err.println("Ошибка: " + ex);
        else System.out.println("Результат: " + res);
    });
```

---

## **5. Дополнительные возможности**  

### **5.1. Таймауты (`orTimeout`, `completeOnTimeout`)** (Java 9+)  
```java
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    try { Thread.sleep(2000); } catch (InterruptedException e) {}
    return "Готово";
}).orTimeout(1, TimeUnit.SECONDS) // TimeoutException, если не успел
  .exceptionally(ex -> "Таймаут!");

// Или подстановка значения при таймауте
CompletableFuture<String> safe = future.completeOnTimeout("По умолчанию", 1, TimeUnit.SECONDS);
```

### **5.2. Явное завершение (`complete`, `completeExceptionally`)**  
```java
CompletableFuture<String> future = new CompletableFuture<>();

new Thread(() -> {
    try {
        future.complete("Успех");
    } catch (Exception e) {
        future.completeExceptionally(e);
    }
}).start();
```

---

## **6. Пример: Асинхронный REST-клиент**  
```java
public CompletableFuture<String> fetchUserData(String userId) {
    return CompletableFuture.supplyAsync(() -> {
        // Имитация HTTP-запроса
        try { Thread.sleep(500); } catch (InterruptedException e) {}
        return "{ \"id\": \"" + userId + "\", \"name\": \"Alice\" }";
    });
}

public CompletableFuture<Integer> fetchUserScore(String userId) {
    return CompletableFuture.supplyAsync(() -> {
        try { Thread.sleep(300); } catch (InterruptedException e) {}
        return 95;
    });
}

// Комбинируем запросы
CompletableFuture<String> combined = fetchUserData("123")
    .thenCombine(fetchUserScore("123"), (data, score) -> data + ", \"score\": " + score + " }");

combined.thenAccept(System.out::println);
// { "id": "123", "name": "Alice", "score": 95 }
```

---

## **Итоги**  
✅ **Плюсы `CompletableFuture`:**  
- Гибкость (цепочки, комбинирование).  
- Неблокирующие операции.  
- Удобная обработка ошибок.  

⚠ **Минусы:**  
- Сложность отладки.  
- Риск "callback hell" без правильного структурирования.  

**Когда использовать?**  
- Асинхронные вызовы (HTTP, DB).  
- Параллельные вычисления.  
- Реактивные pipelines.  

Для сложных сценариев можно использовать **Reactive Streams** (Project Reactor, RxJava), но `CompletableFuture` отлично подходит для большинства задач.  

Если нужны конкретные примеры или разбор кейсов — спрашивайте! 🚀