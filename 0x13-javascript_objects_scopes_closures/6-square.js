#!/usr/bin/node

const Squared = require('./5-square');

class Square extends Squared {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let box = '';
      for (let j = 0; j < this.width; j++) {
        box += c;
      }
      console.log(box);
    }
  }
}

module.exports = Square;
