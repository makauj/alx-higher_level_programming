#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (isNaN(num2) || isNaN(num1)) {
  console.log('Missing or invalid number');
} else {
  console.log(add(num1, num2));
}
