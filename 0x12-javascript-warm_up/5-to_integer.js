#!/usr/bin/node
const args = process.argv;
const val = Number(args[2]);
if (val && !isNaN(val)) {
  console.log('My number: ' + Math.floor(val));
} else {
  console.log('Not a number');
}
