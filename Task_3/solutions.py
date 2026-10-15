### Q1. Find the Frequency of Each Word in a Sentence
def freq_cnt(a):
    words = a.lower().split()
    cnt = {x: words.count(x) for x in words}
    return cnt

## Q2. Find the Frequency of Each Character in a Word
def char_cnt(a):
    cnt = {x: a.count(x) for x in a}
    return cnt

## Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(a):
    for x in a:
        if a.count(x) == 1:
            return x
    return None

## Q4. Check Whether Two Strings Are Anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

## Q5. Find the First Repeating Character in a String
def first_repeating(a):
    for x in a:
        if a.count(x) > 1:
            return x
            break
    return None

## Q6. Move All Zeros to the End of a List
def move_zeros(lst):
    non_zero_lst = []
    zero_lst = []
    for num in lst:
        if num == 0:
            zero_lst.append(num)
        else:
            non_zero_lst.append(num)
    return non_zero_lst + zero_lst

## Q7. Find the Second Highest Distinct Number in a List
def second_largest(a):
    unique_numbers = list(set(a))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

## Q8. Remove Duplicates Without Changing the Original Order
def after_removal(lst):
    dup = []
    for i in lst:
        if i not in dup:
            dup.append(i)
    return dup

## Q9. Find the Missing Number from 1 to N
def missing_number(nums, n):
    total = n * (n + 1) // 2
    return total - sum(nums)

## Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []

## Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    return min(nums, key=lambda x: (abs(x), -x))

## Q12. Find Common Elements Between Two Lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

## Q13. Rotate a List to the Right by K Steps
def rotate_right(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k else nums

## Q14. Find the Maximum Sum of Consecutive Elements in a List
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

## Q15. Find All Pairs of Numbers in a List That Sum to a Target
def all_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])
                if pair not in pairs:
                    pairs.append(pair)

    pairs.sort()
    return pairs
