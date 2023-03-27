const readline = require('readline');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const fs = require('fs');

function generate() {
  let myInterface = readline.createInterface({
    input: fs.createReadStream('nb_request_log1.json')
  });

  let lineno = 0;
  
  // myInterface.on('line', function (line) {
  //   //console.log('Line number ' + lineno + ': ' + line);
  //   line = JSON.parse(line);
  //   //console.log(typeof(line))
  //   const finalArray = [];
  //   for (const key in line._source) {
  //     const finalObj = {}
  //     finalObj[key] = line._source[key]
  //     finalArray.push(finalObj);
  //     return finalArray
  //       //console.log(finalArray);
  //   };
  // });
    

    //lineno++;
  // const fileName = 'nb_request_log1.csv';
  // const tempFile = `./${fileName}`;
  // const csvWriter = createCsvWriter({
  //   path: tempFile,
  //   header: [
  //     { id: 'mno', title: 'mno' },
  //     { id: 'msg_string', title: 'msg_string' },
  //     { id: 'msg_type', title: 'msg_type' },
  //     { id: 'msisdn', title: 'msisdn' },
  //     { id: 'sessionid', title: 'sessionid' },
  //     { id: 'createdAt', title: 'time' },
  //   ]
  // });
  // //console.log(finalArray)
  // csvWriter.writeRecords(finalA);
  // });
}

generate()
