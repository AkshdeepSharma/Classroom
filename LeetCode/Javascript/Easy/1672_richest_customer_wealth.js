var maximumWealth = function(accounts) {
    let best = 0;
    for(let i=0; i < accounts.length; i++){
        best = Math.max(best, accounts[i].reduce((sum, x) => sum + x));
    }
    return best;
};