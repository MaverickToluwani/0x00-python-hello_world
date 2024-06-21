#!/usr/bin/node
const args = process.argv;
const copy = args.slice(2);
const len = copy.length;
let swp;

if (args.length <= 3) {
  console.log(0);
  process.exit(0);
}

for (let i = 0; i <= len; i++) {
  for (let j = 0; j <= len; j++) {
    if (copy[j] > copy[j + 1]) {
      swp = copy[j + 1];
      copy[j + 1] = copy[j];
      copy[j] = swp;
    }
  }
}

console.log(copy[len - 2]);
