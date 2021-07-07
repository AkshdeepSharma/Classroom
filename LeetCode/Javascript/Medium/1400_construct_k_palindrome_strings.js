const canConstruct = (s, k) => {
    let oddCount = 0
    const charCount = new Map();
    if(k > s.length)
        return false;
    for(let i=0; i < s.length; i++){
        if(charCount.has(s[i]))
            charCount.set(s[i], charCount.get(s[i]) + 1);
        else
            charCount.set(s[i], 1);
    }
    for(const [key, value] of charCount.entries())
        if(value % 2 == 1)
            oddCount++;
    return oddCount <= k;
};