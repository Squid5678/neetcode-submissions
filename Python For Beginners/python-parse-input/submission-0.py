from typing import List

def read_integers() -> List[int]:
    nums = input().split(",")
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return nums

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
