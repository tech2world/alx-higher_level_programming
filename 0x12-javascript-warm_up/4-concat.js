#!/usr/bin/node

if (!process.argv[2]) {
  console.log('undefined');
} else if (!process.argv[3]) {
  console.log('undefined');
}
console.log(process.argv[2] + ' is ' + process.argv[3]);
