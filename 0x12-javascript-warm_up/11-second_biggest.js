#!/usr/bin/node

function secondBiggest (n) {
  if (n.length < 2) {
    return (0);
  }
  let max = Number.MIN_SAFE_INTEGER;
  let max2 = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < n.length; i++) {
    const num = parseInt(n[i], 10);
    if (num > max) {
      max2 = max;
      max = num;
    } else if (num > max2 && num < max) {
      max2 = num;
    }
  }
  return max2;
}

const args = process.argv.slice(2);
console.log(secondBiggest(args));
