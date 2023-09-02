/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return await Promise.all([promise1, promise2])
        .then((results) => {
            const [firstResult, secondResult] = results;
            const sum = firstResult + secondResult;
            return sum;
        });   
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
