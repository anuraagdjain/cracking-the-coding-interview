function urlify(str) {
    // remove white spaces in end of string. Alternative to .trim().
    // return str.trim().replace(/\s/g,'%20');
    return str
        .replace(/\s+$/g, "")
        .replace(/\s/g, "%20");
}

console.log(urlify('Mr John Smith   '));