#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
