const restoreString = (s, indices) => {
    const arr = new Array(s.length)
    for(let i=0; i < s.length; i++)
        arr[indices[i]] = s[i];
    return arr.join("");
};