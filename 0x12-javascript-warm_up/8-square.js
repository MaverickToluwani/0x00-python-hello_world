#!/usr/bin/node
const str = 'X';
const arg = process.argv[2];
let string = '';
if (arg <= 0) {
  // pass;
}
if (!arg || isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      string = string + str;
    }
    console.log(string);
    string = '';
  }
}
