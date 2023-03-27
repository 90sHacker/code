class TwoSum: 
    def __init__(self):
        return None

    def two_sum(self, nums, target):
        diff = 0
        for num in nums:
            diff = target - num
            if diff in nums:
                return [nums.index(diff), nums.index(num)]

def main():
    solve = TwoSum()
    print(solve.two_sum([3,2,4], 6))

if __name__ == "__main__":
    main()