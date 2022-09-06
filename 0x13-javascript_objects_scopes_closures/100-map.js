#!/usr/bin/node

const list = require('./100-data');
console.log(list);
list.map((item, index) => item * index);
