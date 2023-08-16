#!/usr/bin/node
/* script that concatenates 2 files */

const fs = require('fs');

const path1 = process.argv[2];
const path2 = process.argv[3];
const path3 = process.argv[4];

fs.readFile(path1, 'utf8', (err, data) => {
  if (err) throw err;
  fs.readFile(path2, 'utf8', (err, data2) => {
    if (err) throw err;
    fs.writeFile(path3, data + data2, (err) => {
      if (err) throw err;
    });
  });
});
