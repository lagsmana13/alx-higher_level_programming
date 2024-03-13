#!/usr/bin/node
class Rectangle {
  constructor (s, n) {
    if ((s > 0) && (n > 0)) {
      this.width = s;
      this.height = n;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        l += 'X';
      }
      console.log(l);
    }
  }
}

module.exports = Rectangle;
