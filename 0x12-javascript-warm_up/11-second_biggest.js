#!/usr/bin/node
let max = 0;
if (process.argv.length === 2) console.log(max);
else if (process.argv.length === 3) console.log(max);
else {
  process.argv.forEach((item, index) => {
    if (Number(item) > max) max = Number(item);
  });
  console.log(max);
}
