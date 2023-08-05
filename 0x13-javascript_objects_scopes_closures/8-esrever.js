#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const lastIndex = list.length - 1;

  for (let i = lastIndex; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
