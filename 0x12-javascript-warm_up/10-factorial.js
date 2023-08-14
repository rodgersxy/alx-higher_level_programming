#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return (1);
  } else {
    return (factorial(n - 1) * n);
  }
}

const n = parseInt(process.argv[2]);
if (n) {
  const result = factorial(n);
  console.log(result);
} else {
  console.log(1);
}
