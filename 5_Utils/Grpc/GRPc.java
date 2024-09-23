// -------------------------------Protobuf-------------------------------
// Как сереализовать и десереализовать в протобуф (пока без обмена клиент-сервер т.е. без Grpc)

// 0. Для сереализация и десереализации достаточно только одной зависимости
	<dependency>
	    <groupId>com.google.protobuf</groupId>
	    <artifactId>protobuf-java</artifactId>
	    <version>${protobuf.version}</version>
	</dependency>

// 1. Описываем .proto
	// 1.1. Наименование полей в .proto через подчёркивание "_"

		syntax = "proto3";

		package sometargetname;

		//option java_multiple_files = true;
		option java_package = "ru.annikonenkov.protobuf";		
		option java_outer_classname = "AddressBookProtos";


		message Person {
		    required string name = 1;
		    required int32 id = 2;
		    optional string email = 3;

		    repeated string numbers = 4;
		}

		message AddressBook {
		    repeated Person people = 1;
		}

// 2. Генерируем классы на базе .proto:
		protoc -I=. --java_out=. addressbook.proto
	// или
		mvn clean compile

// 3. Т.к. нас интересует только сереализация и десереализация, то здесь сервисы не были описаны.

// 4. Создание объекта:
	AddressBookProtos.Person person = AddressBookProtos.Person.newBuilder().setId(id).setName(name).setEmail(email).addNumbers(number).build();

// 5. Сереализация на диск:
	AddressBookProtos.AddressBook addressBook = AddressBookProtos.AddressBook.newBuilder().addPeople(person).build();
	FileOutputStream fos = new FileOutputStream(filePath);
	addressBook.writeTo(fos);

// 6. Десереализация с диска:
	AddressBookProtos.AddressBook deserialized = AddressBookProtos.AddressBook.newBuilder().mergeFrom(new FileInputStream(filePath)).build();


// -------------------------------Protobuf<--->JSON-------------------------------

// 1. Зависимости 
		<dependencies>
		    <!-- Protobuf Java -->
		    <dependency>
		        <groupId>com.google.protobuf</groupId>
		        <artifactId>protobuf-java</artifactId>
		        <version>3.25.1</version>
		    </dependency>
		    
		    <!-- Protobuf Java Util (for JSON conversion) -->
		    <dependency>
		        <groupId>com.google.protobuf</groupId>
		        <artifactId>protobuf-java-util</artifactId> //The protobuf-java-util library handles all the heavy lifting of the conversion process.
		        <version>3.25.1</version>
		    </dependency>
		</dependencies>

// 2. Пример данных

	syntax = "proto3";

	package example;

	message Person {
	    string name = 1;
	    int32 id = 2;
	    string email = 3;
	    repeated string phones = 4;
	}

// 3. Генерируем классы на базе proto

	import com.google.protobuf.util.JsonFormat;
	import example.Person;

	public class JsonProtobufConverter {

	    // Convert Protobuf to JSON
	    public static String protobufToJson(Person person) throws Exception {
	        return JsonFormat.printer()
	                .includingDefaultValueFields()
	                .preservingProtoFieldNames()
	                .print(person);
	    }

	    // Convert JSON to Protobuf
	    public static Person jsonToProtobuf(String json) throws Exception {
	        Person.Builder builder = Person.newBuilder();
	        JsonFormat.parser()
	                .ignoringUnknownFields()
	                .merge(json, builder);
	        return builder.build();
	    }

	    public static void main(String[] args) throws Exception {
	        // Create a sample Protobuf object
	        Person person = Person.newBuilder()
	                .setName("John Doe")
	                .setId(1234)
	                .setEmail("john@example.com")
	                .addPhones("555-1234")
	                .addPhones("555-5678")
	                .build();

	        // Convert Protobuf to JSON
	        String json = protobufToJson(person);
	        System.out.println("Protobuf to JSON:");
	        System.out.println(json);

	        // Convert JSON back to Protobuf
	        Person parsedPerson = jsonToProtobuf(json);
	        System.out.println("\nJSON to Protobuf:");
	        System.out.println(parsedPerson);
	    }
	}

// 4. Дополнительные настройки:
	// Customizing JSON Conversion
	// For more control over JSON conversion:
	String json = JsonFormat.printer()
	        .omittingInsignificantWhitespace()  // Compact format
	        .preservingProtoFieldNames()       	// Keep original field names
	        .includingDefaultValueFields()      // Include fields with default values
	        .print(protobufMessage);

	// Handling Unknown Fields
	// When parsing JSON to Protobuf:
	JsonFormat.parser()
        .ignoringUnknownFields()  // Ignore fields not in the proto definition
        .merge(json, builder);

    // Working with Different Formats
    // For base64-encoded bytes fields:
	JsonFormat.printer().printingEnumsAsInts().print(protobufMessage);

	// Error Handling
	// Always wrap these operations in try-catch blocks as they can throw exceptions:
	try {
	    String json = protobufToJson(person);
	    Person parsed = jsonToProtobuf(json);
	} catch (InvalidProtocolBufferException e) {
	    // Handle malformed JSON or Protobuf data
	    e.printStackTrace();
	}



// -------------------------------Grpc-------------------------------


// gRPC is a high-performance, open-source RPC (Remote Procedure Call) framework that uses Protocol Buffers (Protobuf) as its default data serialization format and interface definition language (IDL).
// Purpose	Transport framework for remote procedure calls
// Interface Definition	.proto files define services & messages
// Communication	Supports unary, streaming (client/server/bidirectional)
// Performance	Fast (HTTP/2 + binary Protobuf)

// 1. Описание объектов-сообщений и сервиса
	syntax = "proto3";

	service UserService {
	    rpc GetUser (UserRequest) returns (UserResponse);
	}

	message UserRequest {
	    int32 user_id = 1;
	}

	message UserResponse {
	    string name = 1;
	    string email = 2;
	}

// 2. Generate gRPC Code (Server & Client stubs)
	protoc --java_out=. --grpc-java_out=. user_service.proto


// 3. Implement Server (Java). То что здесь сделали (реализовали, мы по регисрирруем в сервере Grpc. Server server = ServerBuilder.forPort(50051).addService(new UserServiceImpl()))

	public class UserServiceImpl extends UserServiceGrpc.UserServiceImplBase {
	    @Override
	    public void getUser(UserRequest request, StreamObserver<UserResponse> responseObserver) {
	        UserResponse response = UserResponse.newBuilder().setName("Alice").setEmail("alice@example.com").build();
	        responseObserver.onNext(response);
	        responseObserver.onCompleted();
	    }
	}

// 4. Call from Client (Java)
	ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 8080).usePlaintext().build();
	UserServiceGrpc.UserServiceBlockingStub stub = UserServiceGrpc.newBlockingStub(channel);

	UserResponse response = stub.getUser(UserRequest.newBuilder().setUserId(123).build());
	System.out.println("User: " + response.getName());



/* 
Примечание
	3. На клиенте, из одндоименных классов-Сервисов с препиской Grpc получаем заглушки Stub (по виду реализации заглушки) через одноименные статические мтоды. 
		Заглушка (это по сути сокрытие реализации- через которые клиент обращается к серверу словно вызвает локально.
		У этой заглушки как раз и вызываем метод сервиса, передавая туда сообщения message что описаны в .proto	

*/

// -------------------------------Proto++++Ptoro-------------------------------


/*
	protobuf-example/
	├── src/
	│   ├── main/
	│   │   ├── java/
	│   │   └── proto/  # .proto files go here
	│   │       ├── address.proto
	│   │       └── person.proto
	└── pom.xml
*/

// 1. address.proto (separate file)
	syntax = "proto3";

	package example.address;

	message Address {
	  string street = 1;
	  string city = 2;
	  string state = 3;
	  string zip_code = 4;
	  
	  enum AddressType {
	    HOME = 0;
	    WORK = 1;
	    OTHER = 2;
	  }
	  
	  AddressType type = 5;
	}

// 2. person.proto (imports address.proto)
	syntax = "proto3";

	package example.person;

	import "proto/address.proto";  // Import from another file

	message Person {
	  string name = 1;
	  int32 id = 2;
	  string email = 3;
	  
	  // Nested message
	  message PhoneNumber {
	    string number = 1;
	    PhoneType type = 2;
	    
	    enum PhoneType {
	      MOBILE = 0;
	      HOME = 1;
	      WORK = 2;
	    }
	  }
	  
	  repeated PhoneNumber phones = 4;  // Using nested message
	  
	  example.address.Address address = 5;  // Using imported message
	}

				// Комменты и уточнения по поводу Enum
				// In Protocol Buffers (Protobuf), an enum is encoded as an integer (int32) when serialized, but it's represented as a strongly-typed value in your code.
				// Generated code (in Person.java). Protobuf generates a type-safe Java enum for PhoneType:
				public enum PhoneType {
				    MOBILE(0), HOME(1), WORK(2);
				    private final int value;
				    // ...
				}

				// JSON Conversion: When converting to JSON: By default, enums are serialized as strings ("MOBILE"). You can force integers with:
					JsonFormat.printer().printingEnumsAsInts().print(protoMessage);

// 3. Java Implementation Example

	import example.address.Address;
	import example.person.Person;
	import example.person.Person.PhoneNumber;

	public class ProtobufExample {
	    public static void main(String[] args) {
	        // Create Address (from address.proto)
	        Address address = Address.newBuilder()
	                .setStreet("123 Main St")
	                .setCity("New York")
	                .setState("NY")
	                .setZipCode("10001")
	                .setType(Address.AddressType.HOME)
	                .build();

	        // Create Person (from person.proto)
	        Person person = Person.newBuilder()
	                .setName("John Doe")
	                .setId(1234)
	                .setEmail("john@example.com")
	                .addPhones(PhoneNumber.newBuilder()
	                        .setNumber("555-1234")
	                        .setType(Person.PhoneNumber.PhoneType.MOBILE)
	                        .build())
	                .addPhones(PhoneNumber.newBuilder()
	                        .setNumber("555-5678")
	                        .setType(Person.PhoneNumber.PhoneType.WORK)
	                        .build())
	                .setAddress(address)  // Set the imported Address
	                .build();

	        System.out.println(person);
	    }
	}




// -------------------------------GRPC++++SpringBoot-------------------------------
/*
	Here's a full example demonstrating gRPC integration with Spring Boot, including:
    	Service definition
    	Server implementation
    	Client implementation    	
    	Configuration
*/

/*
	<dependencies>
	    <!-- Spring Boot -->
	    <dependency>
	        <groupId>org.springframework.boot</groupId>
	        <artifactId>spring-boot-starter</artifactId>
	    </dependency>

	    <!-- gRPC Spring Boot Starter -->
	    <dependency>
	        <groupId>net.devh</groupId>
	        <artifactId>grpc-spring-boot-starter</artifactId>
	        <version>2.15.0.RELEASE</version>
	    </dependency>

	    <!-- Protobuf Java -->
	    <dependency>
	        <groupId>com.google.protobuf</groupId>
	        <artifactId>protobuf-java</artifactId>
	        <version>3.25.1</version>
	    </dependency>
	</dependencies>

	<build>
	    <plugins>
	        <!-- Protobuf Compiler -->
	        <plugin>
	            <groupId>org.xolstice.maven.plugins</groupId>
	            <artifactId>protobuf-maven-plugin</artifactId>
	            <version>0.6.1</version>
	            <configuration>
	                <protocArtifact>com.google.protobuf:protoc:3.25.1:exe:${os.detected.classifier}</protocArtifact>
	                <pluginId>grpc-java</pluginId>
	                <pluginArtifact>io.grpc:protoc-gen-grpc-java:1.60.0:exe:${os.detected.classifier}</pluginArtifact>
	            </configuration>
	            <executions>
	                <execution>
	                    <goals>
	                        <goal>compile</goal>
	                        <goal>compile-custom</goal>
	                    </goals>
	                </execution>
	            </executions>
	        </plugin>
	    </plugins>
	</build>

*/

// 1. Proto File (src/main/proto/hello.proto)
	syntax = "proto3";

	package hello;

	service Greeter {
	  rpc SayHello (HelloRequest) returns (HelloResponse);
	}

	message HelloRequest {
	  string name = 1;
	}

	message HelloResponse {
	  string message = 1;
	}

// 2.Server Implementation 

	//gRPC Service
	import io.grpc.stub.StreamObserver;
	import net.devh.boot.grpc.server.service.GrpcService;

	@GrpcService
	public class GreeterService extends GreeterGrpc.GreeterImplBase { // Built-in Connection Pooling: The gRPC server (Netty-based) automatically manages multiple client connections. Each client connection is handled in its own thread

	    @Override
	    public void sayHello(HelloRequest request, StreamObserver<HelloResponse> responseObserver) {
	        String message = "Hello " + request.getName();
	        HelloResponse response = HelloResponse.newBuilder()
	                .setMessage(message)
	                .build();
	        responseObserver.onNext(response);
	        responseObserver.onCompleted();
	    }
	}

	// Application Class
	import org.springframework.boot.SpringApplication;
	import org.springframework.boot.autoconfigure.SpringBootApplication;

	@SpringBootApplication
	public class GrpcServerApplication {
	    public static void main(String[] args) {
	        SpringApplication.run(GrpcServerApplication.class, args);
	    }
	}

// 3. Client Implementation.

	// Configuration
	import org.springframework.context.annotation.Bean;
	import org.springframework.context.annotation.Configuration;
	import io.grpc.ManagedChannel;
	import io.grpc.ManagedChannelBuilder;

	@Configuration
	public class GrpcClientConfig {

	    @Bean
	    public ManagedChannel grpcChannel() {
	        return ManagedChannelBuilder.forAddress("localhost", 9090)
	                .usePlaintext()
	                .build();
	    }

	    @Bean
	    public GreeterGrpc.GreeterBlockingStub greeterStub(ManagedChannel channel) {
	        return GreeterGrpc.newBlockingStub(channel);
	    }
	}

	// Client Service
	import org.springframework.stereotype.Service;
	import hello.GreeterGrpc;
	import hello.HelloRequest;
	import hello.HelloResponse;

	@Service
	public class GreeterClientService {

	    private final GreeterGrpc.GreeterBlockingStub greeterStub;

	    public GreeterClientService(GreeterGrpc.GreeterBlockingStub greeterStub) {
	        this.greeterStub = greeterStub;
	    }

	    public String sayHello(String name) {
	        HelloRequest request = HelloRequest.newBuilder()
	                .setName(name)
	                .build();
	        HelloResponse response = greeterStub.sayHello(request);
	        return response.getMessage();
	    }
	}

	// Client Application
	import org.springframework.boot.SpringApplication;
	import org.springframework.boot.autoconfigure.SpringBootApplication;
	import org.springframework.boot.CommandLineRunner;
	import org.springframework.beans.factory.annotation.Autowired;

	@SpringBootApplication
	public class GrpcClientApplication implements CommandLineRunner {

	    @Autowired
	    private GreeterClientService greeterClientService;

	    public static void main(String[] args) {
	        SpringApplication.run(GrpcClientApplication.class, args);
	    }

	    @Override
	    public void run(String... args) throws Exception {
	        String response = greeterClientService.sayHello("World");
	        System.out.println("Response from server: " + response);
	    }
	}


// 4. Application Properties
	/*
	Server (application.properties)
		grpc.server.port=9090

	Client (application.properties)
		# No special configuration needed for client

	Running the Example
    	Start the server:
			mvn spring-boot:run -pl server

    Start the client (in a separate terminal):
			mvn spring-boot:run -pl client

	You should see the client output:
		Response from server: Hello World

Key Features Demonstrated:
    Automatic gRPC server startup with Spring Boot
    Dependency injection for gRPC services
    Clean separation of client and server
    Configuration through properties
    Protobuf code generation

	This example shows a complete, production-ready setup for Spring Boot with gRPC. The grpc-spring-boot-starter handles all the boilerplate, letting you focus on business logic.
	*/