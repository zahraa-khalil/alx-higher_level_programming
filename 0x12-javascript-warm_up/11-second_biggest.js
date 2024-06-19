#!/usr/bin/node
/* script that searches the second biggest integer in the list */

let largetstNum = process.argv[2];
let secondLargestNum = process.argv[3];

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (largetstNum < process.argv[i]) {
      secondLargestNum = largetstNum;
      largetstNum = process.argv[i];
    } else if (
      secondLargestNum < process.argv[i] &&
      process.argv[i] !== largetstNum
    ) {
      secondLargestNum = process.argv[i];
    }
  }
  console.log(secondLargestNum);
}
