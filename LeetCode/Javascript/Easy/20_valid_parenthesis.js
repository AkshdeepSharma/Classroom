const isValid = s => {
    const stack = [];
    const pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for(let i=0; i < s.length; i++){
        const lastChar = stack[stack.length - 1];
        if(pairs[s[i]]){
            if(pairs[s[i]] == lastChar)
                stack.pop()
            else
                return false
        } else {
            stack.push(s[i])
        }
    }
    return !stack.length;
};