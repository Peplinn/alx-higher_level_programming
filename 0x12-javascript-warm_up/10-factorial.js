#!/usr/bin/node
/* Comput the factorial of a number */

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(process.argv[2]));
