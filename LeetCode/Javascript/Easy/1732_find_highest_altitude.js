const largestAltitude = (gain) => {
    let best = 0;
    let current = 0;
    for(let i=0; i < gain.length; i++){
        current += gain[i];
        best = Math.max(best, current);
    }
    return best;
};