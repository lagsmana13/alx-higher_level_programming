#!/usr/bin/node
class Rectangle {
  constructor (s, n) {
    if ((s > 0) && (n > 0)) {
      this.width = s;
      this.height = n;
    }
  }
}

module.exports = Rectangle;
