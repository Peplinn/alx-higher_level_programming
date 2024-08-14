#!/usr/bin/node
/* Searches the second biggest integer in the list of arguments. */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(e => parseInt(e)).sort((a, b) => b - a);
  const uniqueIntegers = [...new Set(integers)];
  console.log(uniqueIntegers[1]);
}
