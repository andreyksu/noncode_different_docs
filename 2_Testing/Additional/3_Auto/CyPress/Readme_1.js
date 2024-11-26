Для взаимодействия с элементом нужно использовать then()

0. Get vs Find
    The cy.get command always starts its search from the cy.root element. In most cases, it is the document element, unless used inside the .within() command. The .find command starts its search from the current subject.

1. cy.get(...).then((elem)=>{...})
    в it всё асинхронное как и в promise. cy.get(...) это асинхронное место.
        Если нужно дождаться результата из этого cy.get(...) то следует использовать then
        
        Синхронные места как и в promise выполняются сразу. По этой причине:
            cy.get(...).as(elem)
            let param = elem.text - приведёт к undefinde т.к. к этому моменту cy.get(...) еще не выполнится а лишь поставиться в очередь выполнения.
            
            Нужно так
                cy.wait(elem).then()
                

 Anti-Pattern: Sharing page objects, using your UI to log in, and not taking shortcuts.
 Best Practice: Test specs in isolation, programmatically log into your application, and take control of your application's state.
 
 Anti-Pattern: Using highly brittle selectors that are subject to change.
 Best Practice: Use data-* attributes to provide context to your selectors and isolate them from CSS or JS changes.
 
 Anti-Pattern: Trying to assign the return value of Commands with const, let, or var.
 Best Practice: Use aliases and closures to access and store what Commands yield you.
        Many first time users look at Cypress code and think it runs synchronously.
        
Anti-Pattern: Coupling multiple tests together.
Best Practice: Tests should always be able to be run independently from one another and still pass.
            
            
    1.1. Series Commands passed into a central queue and to be executed asynchronously at a later time.
    1.2. Cypress connands dont do anything at the moment they are invoked, but rather enqueue themselves to be run later.
    1.3. Each Cypress command (or chain of commands return immediatly, having only been append to queue to be executed later time). having been appended - будучи добавленный.
    1.4. Commands are enqueued and managed enterly behind the scenes.
    1.5. The first and most important concept you should recognize is... 
            You cannot assign or work with the return values of any Cypress command. Commands are enqueued and run asynchronously.            
    1.6. After a test function is finished running, Cypress goes to work executing the commands that were enqueued using the cy.* command chains.
    1.7. While the API may look similar to Promises, with its then() syntax, Cypress commands and queries are not promises - they are serial commands passed into a central queue, to be executed asynchronously at a later date. These commands are designed to deliver deterministic, repeatable and consistent tests.
        While Cypress does have a .then() command, Cypress commands are not Promises and cannot be awaited. 
        
        These actions will always happen serially (one after the other), never in parallel (at the same time).
            
            // this won't work the way you think it does
            const button = cy.get('button')
            const form = cy.get('form')

            button.click()
            
            To access what each Cypress command yields you use .then().

            cy.get('button').then(($btn) => {
              // $btn is the object that the previous
              // command yielded us
            })
            
            
        The commands outside of the .then() will not run until all of the nested commands finish.
        
        then, should
        
        
        cy.wrap('some value').as('exampleValue')
        cy.get('@exampleValue').should('equal', 'some value')
        
        cy.fixture('users.json').as('users')
        cy.get('@users').then((users) => {
        
        
        
        cy.get('button').then(($btn) => {
          // redefine text reference
          text = $btn.text()
        })
        
2. Contains
    Следует использовать только в рамках get или within (т.к. ищет с корня).
    
    get - тоже ищет с корня, исключение только если within
    
3. Все as(...) между it очищаются. Как и очищается контекст брауезра итд.
    По этой причине если нужна авторизация или какое-то поле, то следует использовать beforeEach.

4. Цепочка
    cy.get(...).then((val1)=>{....;return val2;}).then((val2)=>...)
    
    cy.get('button').then(($btn) => {

      // store the button's text
      const txt = $btn.text()

      // submit a form
      cy.get('form').submit()

      // compare the two buttons' text
      // and make sure they are different
      cy.get('button').should(($btn2) => {
        expect($btn2.text()).not.to.eq(txt)
      })
    })
    
    // these commands run after all of the
    // other previous commands have finished
    cy.get(...).find(...).should(...)
    
    // -------------------------------------------------------------------------
    
   // cypress test code
    cy.get('[data-testid="num"]').then(($span) => {
      // capture what num is right now
      const num1 = parseFloat($span.text())

      cy.get('button')
        .click()
        .then(() => {
          // now capture it again
          const num2 = parseFloat($span.text())

          // make sure it's what we expected
          expect(num2).to.eq(num1 + 1)
        })
    }) 

    
    
5. Общая структура:   
    describe('describe_name', ()=>{ // Группа целевых проверок.
        ...
        beforeEach(()=>{})

        context ('context_name1'), ()=>{
            it('test_name', ()={callMethodOfPageOrComponent});
            ...
            it('test_name1', ()={callMethodOfPageOrComponent});
        }

        context ('context_name1'), ()=>{
            it('test_name', ()={callMethodOfPageOrComponent});
            ...
            it('test_name1', ()={callMethodOfPageOrComponent});
        }

        ....
    })
    
    
6. Еще раз про синхронность и асинхронность в CyPress


        it("", () => {
            function f(i) {
                cy.log("In the f i = ", i).wait(15000)
                    .then((vaal1) => {//Из wait ничего не возвращается, по тому vaal1 == null.
                        console.log(' i = ', i);
                        if (i > 10) {
                            return 10;
                        }
                        cy.wait(10000);
                        cy.log("cy.log After wait ");           // Выполнится после окончания cy.wait(10000);
                        console.log("console.log After wait "); // Выполнится сразу, еще до окончания cy.wait(10000);
                        cy.reload();
                        return f(++i); // Если здесь, то все OK.
                        /*
                            Возврат и соответственно вызов функции выполнится внутри then мгновенно.
                            Но это мгновенное выполнение будет - когда содержимое then начинает выполняться. Видимо оно выполняется не сразу и внутреннее содержимое then не кладётся в очередь сразу.
                            По тому вроде не будет бесконечной рекурсии.
                        */
                    })
                    .then((vaal2) => {
                        console.log("console.log vaal2 = ", vaal2) 
                        /*
                            Самое интересное, что это будет выполнено не сразу а только после выполнения предыдущих всех циклов рекурсии т.к. после выполнения предыдущего then (хоть здесь синхронная операция).
                            
                            Все логично. Каждый then добавляется в очередь на выполнение.
                            А всё что внутри этого then не важно синхронное или асинхронное будет выполнться только тогда, кода очередь дойдёт до этого then.
                            Т.е. внутри этого then очередь синхронности и асинхронности своя и не связана в внешней очередью.
                        */                        
                    })
                    // return f(++i); // Если здесь оставить, то будет стекОверФлоу по реркусии.
                    /*
                        Видимо причина в том, что then ставится в очередь но содержимое выполняется когда начинает выполняться очередь.
                        А return выполняется мгновенно но до условия так и не добираемся, т.к. внутри then еще не начали выполнять.
                    */
            }
            cy.visit("/").then(() => {
                f(1);
            })
        });

        it.skip("", () => { // Это пример с официального сайта.
            const checkAndReload = () => {
                cy.get('#result').should('not.be.empty').invoke('text').then(parseInt)
                    .then((number) => { // Видимо каждую итерацию рекурсии доходим до сюда и останавливаемся, до момента пока не будет выполнено внутреннее содержимое.
                        if (number === 7) {
                            cy.log('lucky **7**')
                            return
                        }
                        cy.wait(500, { log: false })
                        cy.reload()         // У них тоже идёт микс синхронного кода и асинхроннгго кода.
                        checkAndReload()    // Парни тоже вызывают рекурсивную фунцию в then.
                    })
            }
            cy.visit('public/index.html')
            checkAndReload()
        })
    });
    
    //-----------------------------------------------------------------
    // then действительно выполняет что синхронное, что асинхронное у себя внутри в тот момент, как туда дойдет очередь.
    // А вот внутри then уже нужно правильно расставлять синхронный и асинхронный код.
    
    // Если необходимость/условие для вызова рекурсивной функции зависит от асинхронной операции допустим от get() то такой вызов функции должен находиться внутри then.
    // Иначе все вызовы будут выполнены мгновенно и без учёта результата.
    // По этой части while и не подходит. Он будет находиться на одном уровне с вызываемым кодом и все синхронное будет автоматом выполнено.
        it("Проверка URL --- После переключения на страницу", () => {
            cy.log("Before the f()").wait(12000)
                .then((vaal1) => {
                    function f(i) { 
                        console.log(' i = ', i);
                        if (i > 10) {
                            return 10;
                        }
                        cy.wait(10000);
                        cy.log("cy.log After wait ");           
                        console.log("console.log After wait ");
                        cy.reload();
                        return f(++i); // Вызов рекурсивной функции из then ибо пока не выполнится внутреннее не вызовится эта функция. Тем самым не будет безудержным вызовом без остановки.
                    }
                    f(1);
                    /*  
                        Выполнится мгновенно и все 10 раз. При этом распечатав console.log(' i = ', i); и console.log("console.log After wait "); без промедлений.
                        А вот всё что 'cy' выполнится потом когда-то. Все это будет добавлено в очередь. Все эти 10 раз.
                    */
                })
                .then((vaal2) => {                    
                    console.log("console.log vaal2 = ", vaal2) // Самое интересное, что это будет выполнено не сразу а только после выполнения предыдущих всех циклов рекурсии
                })         
            cy.visit("/").then(() => {
            })
        });


//-----------------------------------------------------------------
    function simple(i) {
        while (i < 10) {
            cy.log("cy.log::::: The i = ", i); // Это с интервалом 2200 последовательно.
            cy.wait(2200);
            console.log("console.log::::: The i = ", i); // Это выполнится мгновенно. Сразу все N-раз.
            i++;
        }
    }
    
    function simple1(i) {        
            cy.log("cy.log::::: The i = ", i); // Это с интервалом 2200 последовательно.
            cy.wait(2200);
            console.log("console.log::::: The i = ", i); // Это выполнится мгновенно. Сразу все N-раз.
            if (i < 10){
                simple1(++i);
            }
            return;
        }
    }

    context('Проверка наличия элементов на странице библиотеки --- После переключения на страницу ', () => {
        it("Проверка URL --- После переключения на страницу", () => {
            cy.visit("/").then(() => {
                console.log("console.log::::: Visit loooog"); // Выведится первым
            })

            cy.log("cy.log::::: Before Then --- 1").wait(2000) // Потом это.
                .then((vaal1) => {
                    simple1(4);
                    cy.log("cy.log::::: Then --- 1"); // Это после cy.log("cy.log::::: The i = ", i); 
                    cy.wait(2100);
                    console.log("console.log::::: Then --- 1"); // И это мгновенно еще до cy.log("cy.log::::: The i = ", i);
                })

            cy.log("cy.log::::: Before Then --- 2").then((vaal2) => {
                cy.wait(2400);
                cy.log("cy.log::::: Then --- 2");               // Это выполнится после нижележащего console.log но и САМОЕ ВАЖНО - ПОСЛЕ вышележащих всех console.log.                
                console.log("console.log::::: Then --- 2");     // Эта синхранная часть выполнится ПОСЛЕ всего предыдущего асинхронного. Что подтверждает
                /*
                    Всё это подтверждает, что у then локальная своя область синхронности/асинхронности
                    Then сам встаёт в очередь общего порядка на его же уровне. Но все что внутри этого then выполняется в совём порядка и в той точке, где стоит then.

                */
            })

            cy.log('After After'); // Самое последнее.

        });



//Еще один пример асинхронносои и вызова рекурсивной функции из примера:
// a regular ol' function folks
function req () {
  cy.request(...)
    .then((resp) => {
      // if we got what we wanted

      if (resp.status === 200 && resp.body.ok === true)
        // break out of the recursive loop
        return // Снова выход внутри then

      // else recurse
      req() // Снова вызов внутри then
    })
}

cy
  // do the thing causing the side effect
  .get('button').click()

  // now start the requests
  .then(req)

//---------------------------------------------------
.should() is great in that it waits and retries, which you can't achieve with .expect(), nor with .then().


Alias the request using .as()
cy.request('https://jsonplaceholder.cypress.io/comments').as('comments')

cy.get('@comments').should((response) => {
  expect(response.body).to.have.length(500)
  expect(response).to.have.property('headers')
  expect(response).to.have.property('duration')
})


cy.request('POST', 'http://localhost:8888/users/admin', { name: 'Jane' }).then(
  (response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('name', 'Jane') // true
  }
)

//---------------------------------------------------
//Запуск CyPress

CyPress-Run

cypress run -- --spec 'path/to/files/*.spec.js'
npm run --spec 'path/to/files/*.spec.js'

cypress run --spec "cypress/e2e/examples/actions.cy.js"
cypress run --spec "cypress/e2e/login/**/*"
cypress run --spec "cypress/e2e/examples/actions.cy.js,cypress/e2e/examples/files.cy.js"


cypress run --browser chrome
cypress run --browser /usr/bin/chromium

npx cypress run --record --spec "cypress/e2e/my-spec.cy.js"

npm run e2e:chrome -- --spec "cypress/e2e/my-spec.cy.js"


+ cypress run --config '{"watchForFileChanges":false,"specPattern":["**/*.cy.js","**/*.cy.ts"]}'


cypress run --config-file tests/cypress.config.js


cypress run --group admin-tests --spec 'cypress/e2e/admin/**/*'


cypress run --spec "cypress/e2e/login/**/*"

cypress run --spec "cypress/e2e/examples/actions.cy.js,cypress/e2e/examples/files.cy.js"



cypress run --headed --browser chromium --config '{"watchForFileChanges":false,"specPattern":["**/CriticalPath/*.cy.js"]}'
cypress run --browser chromium --config '{"watchForFileChanges":false,"specPattern":["**/1_*.cy.js","**/*.cy.ts"]}'


cypress run --config-file tests/cypress.config.js

//---------------------------------------------------

The command above executes tests in headless mode

npx cypress run [--spec <path_to_spec_file]
npx cypress run --spec "./cypress/integration/demo/firsttest.js"

Headed Mode
npx cypress open

Headless Mode
npx cypress run