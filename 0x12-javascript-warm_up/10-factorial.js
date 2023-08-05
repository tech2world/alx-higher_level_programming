#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0 || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
const num = parseInt(process.argv[2], 10);
console.log(factorial(num));
