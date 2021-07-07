var maxProductDifference = function(nums) {
    const sorted = nums.sort((a, b) => a - b);
    const a = sorted.pop()
    const b = sorted.pop()
    const c = sorted.shift()
    const d = sorted.shift()
    return (a * b - c * d);
};