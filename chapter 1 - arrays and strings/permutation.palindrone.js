"use strict";
function isPermutationPalindrone(str) {
    str = str.replace(/\s+/g, "");
    const charMap = {};
    for (const char of str) {
        charMap[char] = charMap[char] ? charMap[char] + 1 : 1;
    }
    let odd = 0;
    Object.values(charMap).forEach(k => {
        if (k % 2 !== 0) odd++;
    });
    return odd > 1 ? false : true;
}

["never odd or even", "racer car"].forEach(word =>
    console.log(isPermutationPalindrone(word))
);
