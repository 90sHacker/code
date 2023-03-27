function twoSum (nums, target) {
    let diff = 0;
    for (let i = 0; i < nums.length; i++) {
        diff = target - nums[i];
        console.log(diff);
        if(nums.includes(diff)) {
            return  [].concat(i, nums.indexOf(diff))
        }
    }
    
}

console.log(twoSum([2, 7, 15, 18], 22));