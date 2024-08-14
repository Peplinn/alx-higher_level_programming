#!/usr/bin/node
/* Concate two files */
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.log('Error reading ' + fileA + ':', err);
    return;
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.log('Error reading ' + fileB + ':', err);
      return;
    }

    const concatenatedData = dataA + dataB;

    fs.writeFile(fileC, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.log('Error Writing to ' + fileC + ':', err);
      }
    });
  });
});
