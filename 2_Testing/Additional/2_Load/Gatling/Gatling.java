//Write to File
//Java Code Example:
package com.example.simulations;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;
/*
    The exec method is used to execute an action. Actions are usually requests (HTTP, WebSocket, JMS, MQTT…) that will be sent during the simulation. Any action that will be executed will be called with exec.
    
    A Gatling scenario is a workflow where every step is an Action. Sessions are the messages that are passed along a scenario workflow.
        Session instances are immutable, meaning that methods such as set return a new instance and leave the original instance unmodified!
        
    Gatling EL uses a #{attributeName} syntax to define placeholders to be replaced with the value of the matching attributeName attribute’s value stored in the virtual user’s Session, eg: request("page").get("/foo?param=#{bar}").
        
    The first step is to inject state into the virtual users.
    
    В setUp (передаётся ScenarioBuilder)
    
    ScenarioBuilder - исполняет ChainBuilder или List<ChainBuilder> через 
        CoreDsl.scenario(scenarioName).exec(List<ChainBuilder>)
    Именно на ScenarioBuilder - вызывается injectOpen()
        Здесь тоже появляется
            repeat().on(ChainBuilder)
    
    ChainBuilder - Исполняент ActionBuilder (HttpRequestActionBuilder)
        Исполнение Execs.exec(ActinBuilder)
            
        Здесь появляются:
            pause(...)
            feed(...)
            exitHereIf(...)
            repeat().on(ChainBuilder)
        
    Scenario Chain builder is executed only once per simulation and it creates chain of actions which is then used by each individual user as something like template for all requests. 
     
    Session is a virtual user’s state.
        
*/


import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;

import java.io.FileWriter;
import java.io.PrintWriter;

public class PersistDataSimulation extends Simulation {

    // HTTP protocol configuration
    HttpProtocolBuilder httpProtocol = http
            .baseUrl("https://example.com")
            .acceptHeader("application/json");

    // A simple function to persist data to a file
    private void saveData(String data) {
        try (PrintWriter out = new PrintWriter(new FileWriter("persisted_data.txt", true))) {
            out.println(data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Define a chain that creates an entity and extracts its id
    ScenarioBuilder scn = scenario("Persist Data Scenario")
            .exec(
                http("Create Entity")
                    .post("/entity")
                    .body(StringBody("{ \"field\": \"value\" }")).asJson()
                    // Assume the response contains JSON like: { "id": "12345", ... }
                    .check(jsonPath("$.id").saveAs("entityId"))
            )
            .exec(session -> {
                // Retrieve the entity id from the session
                String id = session.getString("entityId");
                // Persist the extracted id
                saveData(id);
                return session;
            });

    {
        setUp(
                scn.injectOpen(rampUsers(5).during(10))
        ).protocols(httpProtocol);
    }
}}

//------------------------------------------------------------------------------------------------------------------------------------
package com.example.simulations;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

public class PersistDataSimulation extends Simulation {

    // Shared concurrent queue to hold entity IDs from all users
    private static Queue<String> entityIds = new ConcurrentLinkedQueue<>();

    // HTTP protocol configuration
    HttpProtocolBuilder httpProtocol = http
            .baseUrl("https://example.com")
            .acceptHeader("application/json");

    ScenarioBuilder scn = scenario("Persist Data Scenario")
            .exec(
                http("Create Entity")
                    .post("/entity")
                    .body(StringBody("{ \"field\": \"value\" }")).asJson()
                    // Save the extracted id from JSON response to session
                    .check(jsonPath("$.id").saveAs("entityId"))
            )
            .exec(session -> {
                // Add the id from the session to our shared queue
                String id = session.getString("entityId");
                if (id != null) {
                    entityIds.add(id);
                }
                return session;
            });

    {
        setUp(
                scn.injectOpen(rampUsers(5).during(10))
        ).protocols(httpProtocol);

        // After the simulation, write the collected entity IDs into a file
        after(() -> {
            try (PrintWriter out = new PrintWriter(new FileWriter("persisted_entities.txt", true))) {
                for (String id : entityIds) {
                    out.println(id);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }
}