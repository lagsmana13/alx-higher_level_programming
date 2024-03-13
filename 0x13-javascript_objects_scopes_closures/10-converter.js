#!/usr/bin/node

exports.converter = function (bse) {
  return function (nm) {
    return nm.toString(bse);
  };
};
