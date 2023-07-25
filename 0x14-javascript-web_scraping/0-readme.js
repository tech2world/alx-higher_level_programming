#!/usr/bin/node
const fs = require('fs');

// get file path from command line arg
const filePath = process.argv[2];

// read content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // handle error if it occurs during file opening
    console.error('Error occurred while reading the file:', err);
  } else {
    //console.log('File content:');
    console.log(data);
  }
});
