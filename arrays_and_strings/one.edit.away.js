"use strict";

// For replacement of a char.
function charReplace(str1, str2) {
  let found = false;
  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) {
      if (found) {
        return false;
      }
      found = true;
    }
  }
  return true;
}

/**
 * str1 = longer string
 * str2 = shorted string
 */
function charEdit(str1, str2) {
  let idx1 = 0,
    idx2 = 0,
    found = false;
  while (idx1 < str1.length && idx2 < str2.length) {
    if (str1[idx1] !== str2[idx2]) {
      if (found) return false;
      found = true;
      if (str1.length === str2.length) idx2++;
    } else {
      idx2++;
    }
    idx1++;
  }
  return true;
}

function oneEditAway(str1, str2) {
  const diff = str1.length - str2.length;
  /**
   * case 1: strings are equal in length
   * case 2: str2 is a longer string
   * case 3: str1 is a longer string
   */
  if (diff === 0) return charEdit(str1, str2);
  else if (Math.sign(diff) === -1) return charEdit(str2, str1);
  else return charEdit(str1, str2);
}

[["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]].forEach(words =>
  console.log(oneEditAway(words[0], words[1]))
);
