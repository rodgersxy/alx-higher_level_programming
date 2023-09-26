#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(path, body, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
