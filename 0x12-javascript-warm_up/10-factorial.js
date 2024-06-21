#!/usr/bin/node
const n = Number(process.argv[2]);

function factorial (n) {
  if (!n) return 1;
  if (n === 0) return 1;
  if (n === 1) return 1;
  return n * factorial(n - 1);
}

const res = factorial(n);
console.log(res);
