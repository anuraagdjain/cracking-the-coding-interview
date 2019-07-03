function extractPermutations(str1, str2) {
    const str1Obj = {};
    const permutations = [];

    for (char of str1) {
        str1Obj[char] = 1;
    }

    function isCharPresent(str) {
        let ctr = {};
        for (char of str) {
            if (str1Obj[char]) ctr[char] = 1;
        }
        return JSON.stringify(Object.keys(ctr).sort()) === JSON.stringify(Object.keys(str1Obj).sort());
    }

    for (let i = 0; i < str2.length; i++) {
        const subStr = str2.substr(i, str1.length);
        if(subStr.length < str1.length) break;
        if (isCharPresent(subStr)) permutations.push(subStr);
    }

    return permutations;
}

function isPermutation(str1, str2) {
    if(str1.length != str2.length) return false;
    return str1
        .split("")
        .sort()
        .join("") ===
        str2
            .split("")
            .sort()
            .join("")
}

console.log(extractPermutations("abc", "aabcdbsccba")); // abc,cba
console.log(isPermutation('abc', 'cba')); // true
console.log(isPermutation('abcdef', 'zcba')); // false