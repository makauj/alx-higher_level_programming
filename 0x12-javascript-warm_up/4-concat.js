#!/usr/bin/node
const args = process.argv.slice(2);
let myVar = 'is';
if (args.length === 0) {
        args[0] = 'undefined';
        args[1] = 'undefined';
    }
console.log(args[0], myVar, args[1]);
