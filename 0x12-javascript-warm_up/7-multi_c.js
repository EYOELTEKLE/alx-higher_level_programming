#!/usr/bin/node
if (isNaN(process.argv[2])) console.log('Missing number of occurrences');
const number = Number(process.argv[2]);
for (let i = 0; i < number; i++) {
  console.log('c is fun');
}
