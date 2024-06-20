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
  console.log(args[2]);
  }
