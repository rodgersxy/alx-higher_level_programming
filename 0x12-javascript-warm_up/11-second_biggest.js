#!/usr/bin/node

const args = process.argv;

if (args.slice(2).length < 2) {
  console.log('0');
} else {
  const max = args.sort((a, b) => a - b).reverse()[1];
  console.log(max);
}
