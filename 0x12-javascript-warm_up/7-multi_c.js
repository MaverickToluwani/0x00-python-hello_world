#!/usr/bin/node
const str = 'C is fun';
const arg = process.argv[2];
if (arg <= 0) {
  // pass
}
if (!arg || isNaN(Number(arg))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(str);
  }
}
