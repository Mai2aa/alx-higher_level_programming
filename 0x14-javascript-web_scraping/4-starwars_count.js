#!/usr/bin/node
const request = require('request');
let count = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
