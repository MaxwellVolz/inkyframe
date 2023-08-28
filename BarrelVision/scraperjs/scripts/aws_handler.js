// const AWS = require('aws-sdk');
// const lambda = new AWS.Lambda();

function sendDataToAWS(data) {
    console.log(data)
    //   const params = {
    //     FunctionName: 'YourLambdaFunction',
    //     Payload: JSON.stringify(data)
    //   };

    //   lambda.invoke(params, (err, result) => {
    //     if (err) console.error(err);
    //     else console.log(result);
    //   });
}

module.exports = sendDataToAWS;
