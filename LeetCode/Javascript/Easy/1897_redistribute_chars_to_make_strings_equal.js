const makeEqual = words => {
    const initialLength = words.length;
    const word = words.join("");
    const counts = {};
    if(initialLength === 1)
        return true
    for(let i = 0; i < word.length; i++)
        counts[word[i]] = counts[word[i]] ? counts[word[i]] + 1 : 1;
    for(const [key, val] of Object.entries(counts))
        if(val % initialLength !== 0)
            return false;
    return true;
};