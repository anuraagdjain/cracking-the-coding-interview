function isUnique(str){
    const uniqset = {};
    str = str.toLowerCase().replace(/\s/g, "");
    for (char of str) {
        if (uniqset[char]) return false;
        uniqset[char]=1;
    }
    return true;
}

let str = "holà";
console.log(isUnique(str));

