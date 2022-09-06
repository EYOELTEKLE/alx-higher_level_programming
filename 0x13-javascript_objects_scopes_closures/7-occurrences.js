#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const hash = {};
  for (const item of list) {
    if (!(item in hash)) hash[item] = 0;
    hash[item] += 1;
  }
  return hash[searchElement] === undefined ? 0 : hash[searchElement];
};
