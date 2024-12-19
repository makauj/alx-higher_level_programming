#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && Number.isInteger(w)) || h > 0 && Number.isInteger(h)) {
      this.height = h;
      this.width = w;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
