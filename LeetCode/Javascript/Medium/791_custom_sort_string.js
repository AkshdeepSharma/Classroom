const customSortString = (order, str) => {
    const counts = {};
    let notIncluded = "";
    let ans = "";
    let setOrder = new Set(order);
    for(let i=0; i < str.length; i++)
        if(!(setOrder.has(str[i])))
            notIncluded += str[i];
        else if(setOrder.has(str[i]))
            counts[str[i]] = counts[str[i]] ? counts[str[i]] + 1 : 1;
    for(let i=0; i < order.length; i++)
        if(counts[order[i]])
            ans += order[i].repeat(counts[order[i]]);
    return ans + notIncluded;
};