#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (sze) {
    super(sze, sze);
  }
}

module.exports = Square;
