#!/usr/bin/node

const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
