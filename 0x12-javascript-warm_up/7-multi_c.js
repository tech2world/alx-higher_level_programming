#!/usr/bin/node

const num = process.argv[2];

if (isNaN(parseInt(num))) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
