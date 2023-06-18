#!/usr/bin/node

const parsedInt = parseInt(process.argv[2]);

if (parsedInt) {
  console.log('My number: ' + Math.round(process.argv[2]));
} else {
  console.log('Not a number');
}
