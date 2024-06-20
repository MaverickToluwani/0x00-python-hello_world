#!/usr/bin/node
const args = process.argv;
let count = 0;
let i;
for (i in args) {
  count++;
}
if (count <= 2) {
  console.log('No argument');
} else {
  for (i = 2; i < count; i++) {
    console.log(args[i]);
  }
}
