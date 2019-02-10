"use strict";

function stringCompression(str) {
  let idx = 0,
    strLen = str.length,
    result = "";
  while (idx < strLen && str[idx] !== null) {
    const currChar = str[idx];
    let ctr = 1;
    idx++;
    while (currChar === str[idx]) {
      ctr++;
      idx++;
    }
    result += `${currChar}${ctr}`;
  }
  return result.length < str.length ? result : str;
}

["aabcccccaaa", "abcd", "aaabaaaaccaaaaba", "aabccddeeaa", "aaaabbccccdddeee", "AAABBBBCC"].forEach(str =>
  console.log(stringCompression(str))
);

// Expected o/p
// -------------
// a2b1c5a3
// abcd
// a3b1a4c2a4b1a1
// aabccddeeaa
// a4b2c4d3e3
// A3B4C2
