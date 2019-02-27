'use strict';

function isSubStr(str, subStr) {
  return str.includes(subStr);
}

function stringRotation(str, subStr) {
  try {
    if (str.length === subStr.length) return isSubStr(str + str, subStr);
    return false;
  } catch (e) {
    // to handle when either of them is null
    return false;
  }
}

[['waterbottle', 'erbottlewat'], ['ABACD', 'CDAZBA'], ['ABACD', 'CDABA']].forEach(w =>
  console.log(stringRotation(w[0], w[1]))
);

// Expected o/p
// ------
// true
// false
// true
