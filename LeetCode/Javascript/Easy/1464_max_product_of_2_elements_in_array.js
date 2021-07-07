const maxProduct = (nums) => {
    const sortedNums = nums.sort((a, b) => a - b);
    return (sortedNums.pop() - 1) * (sortedNums.pop() - 1)
};