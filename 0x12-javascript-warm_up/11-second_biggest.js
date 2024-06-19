#!/usr/bin/node
/* script that searches the second biggest integer in the list */

let largetstNum = -Infinity;
let secondLargestNum = -Infinity;
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (largetstNum < args[i]) {
      secondLargestNum = largetstNum;
      largetstNum = args[i];
    } else if (secondLargestNum < args[i] && args[i] !== largetstNum) {
      secondLargestNum = args[i];
    }
  }
  console.log(secondLargestNum);
}
