#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const k in valsUniq) {
  const list = [];
  for (const l in totalist) {
    if (totalist[l][1] === valsUniq[k]) {
      list.unshift(totalist[l][0]);
    }
  }
  newDict[valsUniq[k]] = list;
}
console.log(newDict);
