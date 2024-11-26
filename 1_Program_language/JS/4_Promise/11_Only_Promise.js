function httpGet(url) {
    return new Promise(function (resolve, reject) {
        // do the usual Http request
        var request = new XMLHttpRequest();
        request.open('GET', url);

        request.onload = function () {
            if (request.status == 200) {
                resolve(request.response);
            } else {
                reject(Error(request.statusText));
            }
        };

        request.onerror = function () {
            reject(Error('Network Error'));
        };

        request.send(); //Т.к. вызов resolve и reject не останавливают выполнение. Эта часть выполнится сразу.
    });
}

function httpGetJson(url) {
    return new Promise(function (resolve, reject) {
        // check if the URL looks like a JSON file and call httpGet.
        var regex = /\.(json)$/i;

        if (regex.test(url)) {
            // call the promise, wait for the result
            resolve(httpGet(url).then(function (response) { //внутри resolve вызываем функцию-promise
                return response;
            }, function (error) {
                reject(error);
            }));
        } else {
            reject(Error('Bad File Format'));
        }
    });
}

httpGetJson('file.json').then(function (response) {
    console.log(response);
}).catch(function (error) {
    console.log(error);
});