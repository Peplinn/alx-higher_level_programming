#!/usr/bin/node
/* Prints x times “C is fun” */
const numRepeat = parseInt(process.argv[2]);

if (isNaN(numRepeat)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numRepeat; i++) {
    console.log('C is fun');
  }
}
