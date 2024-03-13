#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
