#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
