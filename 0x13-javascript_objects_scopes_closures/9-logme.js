#!/usr/bin/node
let nrg = 0;

exports.logMe = function (itm) {
  console.log(nrg + ': ' + itm);
  nrg++;
};
