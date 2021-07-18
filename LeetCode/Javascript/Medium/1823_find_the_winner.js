const findTheWinner = (n, k) => {
    let ans = 0;
    for(let i = 1; i < n + 1; i++)
        ans = (ans + k) % i;
    return ans + 1;
};