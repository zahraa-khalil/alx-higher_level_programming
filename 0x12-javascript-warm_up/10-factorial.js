#!/usr/bin/node
const factorialNum = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num) || num <= 0) {
    return 1;
  } else {
    const result = num * factorial(num - 1);
    return result;
  }
}

console.log(factorial(factorialNum));
