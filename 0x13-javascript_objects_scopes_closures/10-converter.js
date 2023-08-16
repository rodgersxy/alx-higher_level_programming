#!/usr/bin/node

exports.converter = function (base) {
  return function (decNumber) {
    return decNumber.toString(base);
  };
};
