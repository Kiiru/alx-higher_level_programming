#!/usr/bin/node
const args = process.argv;
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : args[2]);
