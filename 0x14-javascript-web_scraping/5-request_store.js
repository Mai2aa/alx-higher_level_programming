#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, content, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
