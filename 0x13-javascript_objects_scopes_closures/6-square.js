#!/usr/bin/node

const BaseSquare = require('./5-square');
class ExtendedSquare extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = ExtendedSquare;
