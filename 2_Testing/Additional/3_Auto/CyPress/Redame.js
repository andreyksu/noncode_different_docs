Redame

Для работы в Dom
cy.get('#id') - поиск элементов
cy.get('.class')
cy.get('tag')
cy.get('tag[atr="val"][atr="val1"]')
cy.get('tag[atr="val"][atr="val1"]')
cy.get('[atr^="val"]')

После работы get уже работаем с find. Т.к. get всегда ищет из корня и не важно если даже так cy.get(...).get(...) - второй гет будет искать всёравно с корня.
    cy.find()

Или с 
    within()

cy.eq('index')

// Если у contains отсутствует тег, то get игнорируется???
cy.get('...').contains("div", "mask")
cy.get('...').contains("div", "mask")
cy.get('...').contains("div", "mask", {matchCase: false})
// cintains - не нужно использовать с title, getCookies
// Находит первый элемент в котором есть совпдаение.
// НО Если у элемента родитель input, button, a, label то вернётся родитель на не элемент у которого найдено совпадение.

// -----------------------------------------------------------

//Assertion

// Неявные проверки - проверки для объекта предоставленного предыдущей командой.
should(); and();

cy.get("...").should().and()
cy.url().should().and()


// Явные
extect();

cy.get("...").then( elem => {
	expect(elem).to.have.value(...);
})


// -----------------------------------------------------------

cy.get("...").trigger() // Event|Action

// -----------------------------------------------------------
.then(callbackFn)
.then(options, callbackFn) // Pass a function that takes the previously yielded subject as its first argument.

cy.get('.nav').then(($nav) => {}) // Yields .nav as first arg
cy.location().then((loc) => {}) // Yields location object as first arg

// To access what each Cypress command yields you use .then().
cy.get('button').then(($btn) => {
  // $btn is the object that the previous
  // command yielded us
})

// -----------------------------------------------------------
//Функция переключения по пагинации и поиска элемента на конкретной странице.
checkTargetLibrary(targetLibraryName) {
        cy.get(librarySelectors.libraryContainer).
            then((libContainer) => {
                cy.wrap(libContainer).find("tbody").as('libraryList');
                cy.wrap(libContainer).get(librarySelectors.paginationCnontainer).as('paginationContainer');
                cy.get('@paginationContainer').contains('В конец').click();
                cy.get('@paginationContainer').get(librarySelectors.page).last().invoke('text')
                    .then((pageAmount) => {

                        let resultOfSearch = false;
                        cy.get('@paginationContainer').contains('В начало').click().then(() => {
                            function bruteForce(targetPosition) {
                                cy.get('@paginationContainer').contains(targetPosition).click(); // 1 - добавится в очередь.
                                cy.get('@libraryList')  // 2 - добавится в очередь. Больше внутри этого мтеода добавлять в очередь нечего.
                                    .then((listOfElement) => { // Это начнёт выполняться когда дойдёт очередь до этого участка.
                                        console.log("then((listOfElement)", targetPosition, listOfElement);
                                        let tbodyy = listOfElement.find("tr [class^='DataTableCol_']");
                                        for (let i of tbodyy) {
                                            let tmpText = i.innerHTML.toString();
                                            if (tmpText.includes(targetLibraryName)) {
                                                console.log("Нашли ++++++++++++++++++++++++++++++++++", tmpText);
                                                resultOfSearch = true;
                                                break;
                                            }
                                        }
                                        // Синхронный код должен быть только с синхронным (без микса).
                                        // И условия в синхронном коде должны быть только синхроные, никаких завязок на результат асинхронного кода.
                                        if ((targetPosition >= pageAmount) || resultOfSearch) {
                                            return resultOfSearch;
                                        } else {
                                            bruteForce(++targetPosition);// Важно в этом случае сделать ++val иначе бесконечно. Т.к. передаст в функцию и лишь потом приплюсует, а нам нужно плюсованную передавать.
                                        }
                                    })
                                /*
                                if ((targetPosition >= pageAmount) || resultOfSearch) {
                                    return resultOfSearch;
                                } else {
                                    bruteForce(++targetPosition);
                                }
                                Если блок if разместить сюда, то рекурсия будет выполняться/вызываться ВСЕ разы (targetPosition >= pageAmount) переменная resultOfSearch меняться не будет, т.к. она в then и выполнится когда-то потом.
                                Т.е. вызвали функцию (bruteForce(1)). Прошлись и добавили все асинхронное в очередь (все асинхронное это два cy.get(...)) 
                                Сразу дошли до условия и выполнили его мгновенно. При этом вызов if-else выпонится все разы.
                                Т.к. targetPosition еще меньше чем количество страниц и resultOfSearch - БУДЕТ ВСЕГДА false - т.к. внутрь асинхронного блока еще не вошли
                                 */

                            }
                            return bruteForce(1); // 0 - вызывается метод
                        }).then((res1) => { cy.wrap(res1).should('be.true').then(() => { return res1; }) })
                    }).then((res2) => { cy.wrap(res2).should('be.true').then((res3) => { console.log("__res3 = ", res3); return res3; }) });
            }).then((res4) => { cy.wrap(res4).should('be.true') });
    }


//---------------------------------------------------------------------
    //Это та же функция что и выше но оптимизированная и более корректная, т.к. у нас происходит возврат из рекурсивной функции её личного состояния.
    checkTargetLibrary(targetLibraryName) {
        const startPage = 1;
        cy.get(librarySelectors.libraryContainer).
            then((libContainer) => {
                cy.wrap(libContainer).find("tbody").as('libraryList');
                cy.wrap(libContainer).get(librarySelectors.paginationCnontainer).as('paginationContainer');
                cy.get('@paginationContainer').contains('В конец').click();
                cy.get('@paginationContainer').get(librarySelectors.page).last().invoke('text')
                    .then((pageAmount) => {
                        cy.get('@paginationContainer').contains('В начало').click().then(() => {
                            function bruteForce(targetPosition) {
                                cy.get('@paginationContainer').contains(targetPosition).click();
                                cy.get('@libraryList')
                                    .then((listOfElement) => { // Видимо доходим до сюда и останавливаемся (выполняем внутренний код) т.е. не происходит безудержное добавление в очередь.
                                        let tbodyy = listOfElement.find("tr [class^='DataTableCol_']");
                                        for (let i of tbodyy) {
                                            let tmpText = i.innerHTML.toString();
                                            if (tmpText.includes(targetLibraryName)) {console.log("Нашли ++++++++++++++++++++++++++++++++++", tmpText);
                                                return true;
                                            }
                                        }                                        
										return (targetPosition >= pageAmount) ? false : bruteForce(++targetPosition);
                                    })
                            }
                            return bruteForce(startPage);
                        }).then((res1) => { cy.wrap(res1).should('be.true').then(() => { return res1; }) })
                    }).then((res2) => { cy.wrap(res2).should('be.true').then((res3) => { console.log("__res3 = ", res3); return res3; }) });
            }).then((res4) => { cy.wrap(res4).should('be.true') });
    }



//---------------------------------------------------------------------
    // Это пример того как делать не нужно. Будут выполнены все страницы.
        checkTargetLibrary(targetLibrary) {
        cy.get(librarySelectors.libraryContainer).
            within(($libraryContainer) => {
                cy.wrap($libraryContainer).find(librarySelectors.pagination).as('pagination');
                cy.get('@pagination').contains('В конец').click();
                cy.get('@pagination').find(librarySelectors.page).last().invoke('text').then((value) => {
                    const lastPage = value;
                    cy.wrap($libraryContainer).find("tbody").as('libraryList');
                    let startPage = 1;
                    let resultOfSearch = false;
                    cy.get('@pagination').contains('В начало').click().then(() => {
                        const func = function (fuzze) {
                            cy.get('@pagination').find(librarySelectors.section).contains(fuzze).click();
                            cy.get('@libraryList').find(librarySelectors.tr).then((listOfElement) => {
                                for (let i of listOfElement) {
                                    let tmpText = i.innerHTML.toString();
                                    if (tmpText.includes(targetLibrary)) {
                                        resultOfSearch = true;
                                        break;
                                    }
                                }
                                if (resultOfSearch || fuzze >= lastPage) {
                                    return resultOfSearch;
                                }
                                else {
                                    func(++fuzze);
                                }
                            });
                        }
                        return func(startPage);
                    }).then(() => resultOfSearch);
                }).then((res) => { cy.wrap(res).should('be.true') });
            });
    }


//------------------------------------------------
// Cypress Script to Validate API calls in React Native App
describe('My First Test', () => {

    it('Verify API', () => {

        cy.intercept('*/users?*').as('users');

        cy.visit('http://localhost:19006/');

        cy.wait('@users').then(({response}) => {

            expect(response.statusCode).to.eq(200)

            expect(response.body.data.length).to.eq(6)

            expect(response.body.data[0].email).to.eq('george.bluth@reqres.in')

          })

   });

  })
  
  
//------------------------------------------------
// Порядок выполнения before на каждом уровне.

describe("Describe", () => {
    beforeEach(() => {
        cy.log('BeforeEachDescribe')
    })

    context("Context1", () => {
        beforeEach(() => {
            cy.log('BeforeEachContext1')
        })

        it("FirstIt", () => { //Для него выполнится BeforeEachDescribe и BeforeEachContext1
            cy.log("FirstIT");
        })

        it("SecondIt", () => { //Для него выполнится BeforeEachDescribe и BeforeEachContext1
            cy.log("SecondIt");
        })
    })

    context("Context2", () => { //Для него выполнится BeforeEachDescribe
        it("ThirdIt", () => {
            cy.log("ThirdIT");
        })

        it("FourthIt", () => { //Для него выполнится BeforeEachDescribe
            cy.log("FourthIt");
        })
    })
})