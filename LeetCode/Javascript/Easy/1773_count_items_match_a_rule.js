const countMatches = (items, ruleKey, ruleValue) => {
    let matches = 0;
    ruleIndex = {
        'type': 0,
        'color': 1,
        'name': 2
    };
    for(let i=0; i < items.length; i++)
        if(items[i][ruleIndex[ruleKey]] === ruleValue)
            matches++;
    return matches;
};