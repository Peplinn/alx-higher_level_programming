#!/usr/bin/node
/* prints the number of arguments already printed and the new argument value. */

const logList = [];

exports.logMe = function (item) {
  const nb = logList.push(item);
  console.log(nb - 1 + ': ' + item);
};
