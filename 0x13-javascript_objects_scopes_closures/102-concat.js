#!/usr/bin/node
const { readFileSync, writeFile } = require('fs');
const { argv } = require('process');

const getFileContent = (filePath) => {
  return readFileSync(filePath, 'utf8');
};

const sourceFile1 = argv[2];
const sourceFile2 = argv[3];
const destinationFile = argv[4];

const concatenatedContent = getFileContent(sourceFile1) + getFileContent(sourceFile2);

writeFile(destinationFile, concatenatedContent, 'utf8', (err) => {
  if (err) throw err;
});
