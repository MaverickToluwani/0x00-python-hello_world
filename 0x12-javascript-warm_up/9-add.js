#!/usr/bin/node
const numOne = Number(process.argv[2]);
const numTwo = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(numOne, numTwo));
