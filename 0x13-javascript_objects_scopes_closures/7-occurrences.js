#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let newList = [];
  newList = list.filter(x => x === searchElement);
  return newList.length;
};
