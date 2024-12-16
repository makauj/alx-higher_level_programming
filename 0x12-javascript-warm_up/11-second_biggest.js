#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(arg => parseInt(arg));
if (num.length < 2) {
    console.log(0);
} else {
    const sortedNum = [...new Set(num)].sort((a, b) => b - a);
    console.log(sortedNum[1] || 0);
}