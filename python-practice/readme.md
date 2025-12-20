## 📚 **45 Python Coding Questions for GitHub Portfolio**

### **Section 1: String Manipulation (Questions 1-8)**

#### **Problem 1: Reverse Words in String**

**Difficulty:** Medium

**Description:**
Given a string `s`, reverse the order of words. A word is defined as a sequence of non-space characters. Words are separated by single spaces.

**Example 1:**

```
Input: s = "Python is awesome"
Output: "awesome is Python"
```

**Example 2:**

```
Input: s = "Hello World"
Output: "World Hello"
```

**Constraints:**

- 1 <= len(s) <= 10^4
- `s` contains only printable ASCII characters

**Test Cases:**

```python
# Test Case 1
Input: "Python is awesome"
Output: "awesome is Python"

# Test Case 2
Input: "Hello World"
Output: "World Hello"

# Test Case 3
Input: "a"
Output: "a"

# Test Case 4
Input: "coding interview preparation"
Output: "preparation interview coding"

# Test Case 5
Input: "data structures and algorithms"
Output: "algorithms and structures data"

# Test Case 6
Input: "the quick brown fox"
Output: "fox brown quick the"
```


***

#### **Problem 2: Count Character Frequency**

**Difficulty:** Medium

**Description:**
Given a string `s`, return a dictionary where keys are characters and values are their frequencies. Ignore spaces and make it case-insensitive.

**Example 1:**

```
Input: s = "Hello World"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

**Constraints:**

- 1 <= len(s) <= 10^4
- `s` contains only alphabetic characters and spaces

**Test Cases:**

```python
# Test Case 1
Input: "Hello World"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Test Case 2
Input: "Python Programming"
Output: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

# Test Case 3
Input: "aaa"
Output: {'a': 3}

# Test Case 4
Input: "Data Science"
Output: {'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}

# Test Case 5
Input: "Artificial Intelligence"
Output: {'a': 2, 'r': 1, 't': 3, 'i': 4, 'f': 1, 'c': 2, 'l': 3, 'e': 3, 'n': 2, 'g': 1}

# Test Case 6
Input: "z"
Output: {'z': 1}
```


***

#### **Problem 3: Longest Substring Without Repeating Characters**

**Difficulty:** Medium

**Description:**
Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.
```

**Constraints:**

- 0 <= len(s) <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces

**Test Cases:**

```python
# Test Case 1
Input: "abcabcbb"
Output: 3

# Test Case 2
Input: "bbbbb"
Output: 1

# Test Case 3
Input: "pwwkew"
Output: 3

# Test Case 4
Input: ""
Output: 0

# Test Case 5
Input: "dvdf"
Output: 3

# Test Case 6
Input: "anviaj"
Output: 5
```


***

#### **Problem 4: Palindrome String Checker**

**Difficulty:** Medium

**Description:**
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Example 1:**

```
Input: s = "A man a plan a canal Panama"
Output: True
```

**Example 2:**

```
Input: s = "race a car"
Output: False
```

**Constraints:**

- 1 <= len(s) <= 2 * 10^5

**Test Cases:**

```python
# Test Case 1
Input: "A man a plan a canal Panama"
Output: True

# Test Case 2
Input: "race a car"
Output: False

# Test Case 3
Input: "racecar"
Output: True

# Test Case 4
Input: "Madam"
Output: True

# Test Case 5
Input: "hello"
Output: False

# Test Case 6
Input: "Was it a rat I saw"
Output: True
```


***

#### **Problem 5: String Compression**

**Difficulty:** Medium

**Description:**
Implement a method to perform basic string compression using the counts of repeated characters. For example, "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not smaller than the original, return the original string.

**Example 1:**

```
Input: s = "aabcccccaaa"
Output: "a2b1c5a3"
```

**Constraints:**

- 0 <= len(s) <= 10^4
- `s` consists of lowercase English letters only

**Test Cases:**

```python
# Test Case 1
Input: "aabcccccaaa"
Output: "a2b1c5a3"

# Test Case 2
Input: "abc"
Output: "abc"

# Test Case 3
Input: "aabbcc"
Output: "aabbcc"

# Test Case 4
Input: "aaaa"
Output: "a4"

# Test Case 5
Input: ""
Output: ""

# Test Case 6
Input: "abcdef"
Output: "abcdef"
```


***

#### **Problem 6: Group Anagrams**

**Difficulty:** Medium

**Description:**
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Constraints:**

- 1 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- `strs[i]` consists of lowercase English letters

**Test Cases:**

```python
# Test Case 1
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Test Case 2
Input: [""]
Output: [[""]]

# Test Case 3
Input: ["a"]
Output: [["a"]]

# Test Case 4
Input: ["listen", "silent", "enlist"]
Output: [["listen", "silent", "enlist"]]

# Test Case 5
Input: ["abc", "bca", "cab", "xyz"]
Output: [["abc", "bca", "cab"], ["xyz"]]

# Test Case 6
Input: ["dog", "god", "cat", "act", "tac"]
Output: [["dog", "god"], ["cat", "act", "tac"]]
```


***

#### **Problem 7: First Non-Repeating Character**

**Difficulty:** Medium

**Description:**
Given a string `s`, find the first non-repeating character and return its index. If it does not exist, return -1.

**Example 1:**

```
Input: s = "leetcode"
Output: 0
```

**Example 2:**

```
Input: s = "loveleetcode"
Output: 2
```

**Constraints:**

- 1 <= len(s) <= 10^5
- `s` consists of only lowercase English letters

**Test Cases:**

```python
# Test Case 1
Input: "leetcode"
Output: 0

# Test Case 2
Input: "loveleetcode"
Output: 2

# Test Case 3
Input: "aabb"
Output: -1

# Test Case 4
Input: "python"
Output: 0

# Test Case 5
Input: "aabbccddee"
Output: -1

# Test Case 6
Input: "abcdefg"
Output: 0
```


***

#### **Problem 8: Valid Parentheses with Brackets**

**Difficulty:** Medium

**Description:**
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if opening brackets are closed by the same type of brackets and in the correct order.

**Example 1:**

```
Input: s = "()[]{}"
Output: True
```

**Constraints:**

- 1 <= len(s) <= 10^4
- `s` consists of parentheses only '()[]{}'

**Test Cases:**

```python
# Test Case 1
Input: "()[]{}"
Output: True

# Test Case 2
Input: "([)]"
Output: False

# Test Case 3
Input: "{[]}"
Output: True

# Test Case 4
Input: "((("
Output: False

# Test Case 5
Input: ""
Output: True

# Test Case 6
Input: "{[()()]}"
Output: True
```


***

### **Section 2: List Operations (Questions 9-18)**

#### **Problem 9: Find Missing Number**

**Difficulty:** Medium

**Description:**
Given an array `nums` containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

**Example 1:**

```
Input: nums = [3,0,1]
Output: 2
```

**Constraints:**

- n == len(nums)
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in nums are unique

**Test Cases:**

```python
# Test Case 1
Input: [3,0,1]
Output: 2

# Test Case 2
Input: [0,1]
Output: 2

# Test Case 3
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

# Test Case 4
Input: [^0]
Output: 1

# Test Case 5
Input: [^1]
Output: 0

# Test Case 6
Input: [0,1,2,3,4,5,7]
Output: 6
```


***

#### **Problem 10: Rotate Array**

**Difficulty:** Medium

**Description:**
Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Constraints:**

- 1 <= len(nums) <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

**Test Cases:**

```python
# Test Case 1
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

# Test Case 2
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

# Test Case 3
Input: nums = [1,2], k = 3
Output: [2,1]

# Test Case 4
Input: nums = [^1], k = 1
Output: [^1]

# Test Case 5
Input: nums = [1,2,3,4,5], k = 0
Output: [1,2,3,4,5]

# Test Case 6
Input: nums = [1,2,3], k = 4
Output: [3,1,2]
```


***

#### **Problem 11: Two Sum**

**Difficulty:** Medium

**Description:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[^0] + nums[^1] = 9
```

**Constraints:**

- 2 <= len(nums) <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

**Test Cases:**

```python
# Test Case 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

# Test Case 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

# Test Case 3
Input: nums = [3,3], target = 6
Output: [0,1]

# Test Case 4
Input: nums = [1,5,3,7], target = 8
Output: [0,3]

# Test Case 5
Input: nums = [-1,-2,-3,-4,-5], target = -8
Output: [2,4]

# Test Case 6
Input: nums = [0,4,3,0], target = 0
Output: [0,3]
```


***

#### **Problem 12: Remove Duplicates from Sorted Array**

**Difficulty:** Medium

**Description:**
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.

**Example 1:**

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Constraints:**

- 1 <= len(nums) <= 3 * 10^4
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order

**Test Cases:**

```python
# Test Case 1
Input: [1,1,2]
Output: 2, nums = [1,2,_]

# Test Case 2
Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# Test Case 3
Input: [^1]
Output: 1, nums = [^1]

# Test Case 4
Input: [1,2,3]
Output: 3, nums = [1,2,3]

# Test Case 5
Input: [1,1,1,1]
Output: 1, nums = [1,_,_,_]

# Test Case 6
Input: [-3,-1,0,0,0,3,3]
Output: 4, nums = [-3,-1,0,3,_,_,_]
```


***

#### **Problem 13: Merge Sorted Arrays**

**Difficulty:** Medium

**Description:**
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. Merge `nums2` into `nums1` as one sorted array and return it.

**Example 1:**

```
Input: nums1 = [1,2,3], nums2 = [2,5,6]
Output: [1,2,2,3,5,6]
```

**Constraints:**

- 0 <= len(nums1), len(nums2) <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

**Test Cases:**

```python
# Test Case 1
Input: nums1 = [1,2,3], nums2 = [2,5,6]
Output: [1,2,2,3,5,6]

# Test Case 2
Input: nums1 = [^1], nums2 = []
Output: [^1]

# Test Case 3
Input: nums1 = [], nums2 = [^1]
Output: [^1]

# Test Case 4
Input: nums1 = [4,5,6], nums2 = [1,2,3]
Output: [1,2,3,4,5,6]

# Test Case 5
Input: nums1 = [1,3,5,7], nums2 = [2,4,6,8]
Output: [1,2,3,4,5,6,7,8]

# Test Case 6
Input: nums1 = [-1,0,0,3,3], nums2 = [-2,-1,2,5]
Output: [-2,-1,-1,0,0,2,3,3,5]
```


***

#### **Problem 14: Product of Array Except Self**

**Difficulty:** Medium

**Description:**
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Solve it without using division.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Constraints:**

- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30

**Test Cases:**

```python
# Test Case 1
Input: [1,2,3,4]
Output: [24,12,8,6]

# Test Case 2
Input: [-1,1,0,-3,3]
Output: [0,0,9,0,0]

# Test Case 3
Input: [2,3,4,5]
Output: [60,40,30,24]

# Test Case 4
Input: [1,1]
Output: [1,1]

# Test Case 5
Input: [5,9,2,6]
Output: [108,60,270,90]

# Test Case 6
Input: [0,0]
Output: [0,0]
```


***

#### **Problem 15: Find Peak Element**

**Difficulty:** Medium

**Description:**
A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
```

**Constraints:**

- 1 <= len(nums) <= 1000
- -2^31 <= nums[i] <= 2^31 - 1

**Test Cases:**

```python
# Test Case 1
Input: [1,2,3,1]
Output: 2

# Test Case 2
Input: [1,2,1,3,5,6,4]
Output: 5

# Test Case 3
Input: [^1]
Output: 0

# Test Case 4
Input: [1,2]
Output: 1

# Test Case 5
Input: [2,1]
Output: 0

# Test Case 6
Input: [1,3,2,4,6,5]
Output: 4
```


***

#### **Problem 16: Move Zeros to End**

**Difficulty:** Medium

**Description:**
Given an integer array `nums`, move all 0's to the end while maintaining the relative order of the non-zero elements. Do this in-place without making a copy of the array.

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Constraints:**

- 1 <= len(nums) <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

**Test Cases:**

```python
# Test Case 1
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

# Test Case 2
Input: [^0]
Output: [^0]

# Test Case 3
Input: [1,2,3]
Output: [1,2,3]

# Test Case 4
Input: [0,0,1]
Output: [1,0,0]

# Test Case 5
Input: [2,1]
Output: [2,1]

# Test Case 6
Input: [0,0,0,1,2,3]
Output: [1,2,3,0,0,0]
```


***

#### **Problem 17: Maximum Subarray Sum (Kadane's Algorithm)**

**Difficulty:** Medium

**Description:**
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
```

**Constraints:**

- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

**Test Cases:**

```python
# Test Case 1
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

# Test Case 2
Input: [^1]
Output: 1

# Test Case 3
Input: [5,4,-1,7,8]
Output: 23

# Test Case 4
Input: [-1]
Output: -1

# Test Case 5
Input: [-2,-1]
Output: -1

# Test Case 6
Input: [1,2,3,4,5]
Output: 15
```


***

#### **Problem 18: Contains Duplicate**

**Difficulty:** Medium

**Description:**
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: True
```

**Constraints:**

- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

**Test Cases:**

```python
# Test Case 1
Input: [1,2,3,1]
Output: True

# Test Case 2
Input: [1,2,3,4]
Output: False

# Test Case 3
Input: [1,1,1,3,3,4,3,2,4,2]
Output: True

# Test Case 4
Input: [^1]
Output: False

# Test Case 5
Input: [1,2]
Output: False

# Test Case 6
Input: [0,1,2,3,0]
Output: True
```


***

### **Section 3: Tuples \& Dictionary Operations (Questions 19-25)**

#### **Problem 19: Merge Two Dictionaries**

**Difficulty:** Medium

**Description:**
Given two dictionaries `dict1` and `dict2`, merge them. If a key exists in both dictionaries, sum their values.

**Example 1:**

```
Input: dict1 = {'a': 10, 'b': 20}, dict2 = {'b': 30, 'c': 40}
Output: {'a': 10, 'b': 50, 'c': 40}
```

**Constraints:**

- 0 <= len(dict1), len(dict2) <= 100
- Values are integers

**Test Cases:**

```python
# Test Case 1
Input: dict1 = {'a': 10, 'b': 20}, dict2 = {'b': 30, 'c': 40}
Output: {'a': 10, 'b': 50, 'c': 40}

# Test Case 2
Input: dict1 = {}, dict2 = {'x': 5}
Output: {'x': 5}

# Test Case 3
Input: dict1 = {'a': 1}, dict2 = {}
Output: {'a': 1}

# Test Case 4
Input: dict1 = {'a': 1, 'b': 2}, dict2 = {'a': 3, 'b': 4}
Output: {'a': 4, 'b': 6}

# Test Case 5
Input: dict1 = {'x': 10}, dict2 = {'y': 20, 'z': 30}
Output: {'x': 10, 'y': 20, 'z': 30}

# Test Case 6
Input: dict1 = {'a': -5}, dict2 = {'a': 5}
Output: {'a': 0}
```


***

#### **Problem 20: Tuple Intersection**

**Difficulty:** Medium

**Description:**
Given two tuples `tuple1` and `tuple2`, return a new tuple containing elements that appear in both tuples (intersection).

**Example 1:**

```
Input: tuple1 = (1, 2, 3, 4), tuple2 = (3, 4, 5, 6)
Output: (3, 4)
```

**Constraints:**

- 0 <= len(tuple1), len(tuple2) <= 1000
- Elements are unique within each tuple

**Test Cases:**

```python
# Test Case 1
Input: tuple1 = (1, 2, 3, 4), tuple2 = (3, 4, 5, 6)
Output: (3, 4)

# Test Case 2
Input: tuple1 = (1, 2), tuple2 = (3, 4)
Output: ()

# Test Case 3
Input: tuple1 = (), tuple2 = (1, 2)
Output: ()

# Test Case 4
Input: tuple1 = (5, 6, 7), tuple2 = (5, 6, 7)
Output: (5, 6, 7)

# Test Case 5
Input: tuple1 = (1,), tuple2 = (1,)
Output: (1,)

# Test Case 6
Input: tuple1 = (10, 20, 30, 40), tuple2 = (15, 25, 35)
Output: ()
```


***

#### **Problem 21: Most Frequent Element in List**

**Difficulty:** Medium

**Description:**
Given a list of integers `nums`, return the element that appears most frequently. If there are multiple elements with the same highest frequency, return any one of them.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3]
Output: 1
```

**Constraints:**

- 1 <= len(nums) <= 10^4
- -1000 <= nums[i] <= 1000

**Test Cases:**

```python
# Test Case 1
Input: [1,1,1,2,2,3]
Output: 1

# Test Case 2
Input: [^1]
Output: 1

# Test Case 3
Input: [1,2,3,4,5,5,5]
Output: 5

# Test Case 4
Input: [7,7,8,8]
Output: 7 (or 8)

# Test Case 5
Input: [2,2,2,3,3,4]
Output: 2

# Test Case 6
Input: [10,20,10,30,10]
Output: 10
```


***

#### **Problem 22: Dictionary Key with Maximum Value**

**Difficulty:** Medium

**Description:**
Given a dictionary `d` with integer values, return the key associated with the maximum value.

**Example 1:**

```
Input: d = {'a': 10, 'b': 50, 'c': 30}
Output: 'b'
```

**Constraints:**

- 1 <= len(d) <= 1000
- Values are integers

**Test Cases:**

```python
# Test Case 1
Input: {'a': 10, 'b': 50, 'c': 30}
Output: 'b'

# Test Case 2
Input: {'x': 100}
Output: 'x'

# Test Case 3
Input: {'p': -5, 'q': -10, 'r': -3}
Output: 'r'

# Test Case 4
Input: {'apple': 5, 'banana': 10, 'cherry': 3}
Output: 'banana'

# Test Case 5
Input: {'a': 0, 'b': 0}
Output: 'a' (or 'b')

# Test Case 6
Input: {'z': 999, 'y': 1000, 'x': 998}
Output: 'y'
```


***

#### **Problem 23: Flatten Nested List**

**Difficulty:** Medium

**Description:**
Given a nested list `nested_list`, flatten it into a single-level list.

**Example 1:**

```
Input: [[1, 2], [3, 4], [^5]]
Output: [1, 2, 3, 4, 5]
```

**Constraints:**

- 0 <= depth of nesting <= 10
- 0 <= total elements <= 10^4

**Test Cases:**

```python
# Test Case 1
Input: [[1, 2], [3, 4], [^5]]
Output: [1, 2, 3, 4, 5]

# Test Case 2
Input: [[]]
Output: []

# Test Case 3
Input: [[^1], [^2], [^3]]
Output: [1, 2, 3]

# Test Case 4
Input: [[1, 2, 3]]
Output: [1, 2, 3]

# Test Case 5
Input: [[[^1]], [[^2]], [[^3]]]
Output: [[^1], [^2], [^3]]

# Test Case 6
Input: [[10, 20], [], [30, 40, 50]]
Output: [10, 20, 30, 40, 50]
```


***

#### **Problem 24: Swap Dictionary Keys and Values**

**Difficulty:** Medium

**Description:**
Given a dictionary `d`, swap its keys and values. Assume all values are unique.

**Example 1:**

```
Input: d = {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}
```

**Constraints:**

- 1 <= len(d) <= 1000
- All values are unique

**Test Cases:**

```python
# Test Case 1
Input: {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}

# Test Case 2
Input: {'name': 'John', 'age': 30}
Output: {'John': 'name', 30: 'age'}

# Test Case 3
Input: {'x': 10}
Output: {10: 'x'}

# Test Case 4
Input: {1: 'one', 2: 'two', 3: 'three'}
Output: {'one': 1, 'two': 2, 'three': 3}

# Test Case 5
Input: {'apple': 'fruit', 'carrot': 'vegetable'}
Output: {'fruit': 'apple', 'vegetable': 'carrot'}

# Test Case 6
Input: {'a': True, 'b': False}
Output: {True: 'a', False: 'b'}
```


***

#### **Problem 25: Count Unique Elements in Tuple**

**Difficulty:** Medium

**Description:**
Given a tuple `t`, return the count of unique elements in it.

**Example 1:**

```
Input: t = (1, 2, 3, 2, 1, 4)
Output: 4
Explanation: Unique elements are 1, 2, 3, 4
```

**Constraints:**

- 0 <= len(t) <= 10^4
- Elements are integers

**Test Cases:**

```python
# Test Case 1
Input: (1, 2, 3, 2, 1, 4)
Output: 4

# Test Case 2
Input: ()
Output: 0

# Test Case 3
Input: (5,)
Output: 1

# Test Case 4
Input: (1, 1, 1, 1)
Output: 1

# Test Case 5
Input: (1, 2, 3, 4, 5)
Output: 5

# Test Case 6
Input: (7, 8, 9, 7, 8, 9)
Output: 3
```


***

### **Section 4: Loops \& Control Flow (Questions 26-33)**

#### **Problem 26: FizzBuzz**

**Difficulty:** Medium

**Description:**
Given an integer `n`, return a list of strings where:

- For multiples of 3, append "Fizz"
- For multiples of 5, append "Buzz"
- For multiples of both 3 and 5, append "FizzBuzz"
- Otherwise, append the number as a string

**Example 1:**

```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

**Constraints:**

- 1 <= n <= 10^4

**Test Cases:**

```python
# Test Case 1
Input: 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Test Case 2
Input: 3
Output: ["1","2","Fizz"]

# Test Case 3
Input: 5
Output: ["1","2","Fizz","4","Buzz"]

# Test Case 4
Input: 1
Output: ["1"]

# Test Case 5
Input: 10
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"]

# Test Case 6
Input: 30
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16","17","Fizz","19","Buzz","Fizz","22","23","Fizz","Buzz","26","Fizz","28","29","FizzBuzz"]
```


***

#### **Problem 27: Prime Numbers in Range**

**Difficulty:** Medium

**Description:**
Given two integers `start` and `end`, return a list of all prime numbers in the range [start, end] inclusive.

**Example 1:**

```
Input: start = 10, end = 20
Output: [11, 13, 17, 19]
```

**Constraints:**

- 1 <= start <= end <= 1000

**Test Cases:**

```python
# Test Case 1
Input: start = 10, end = 20
Output: [11, 13, 17, 19]

# Test Case 2
Input: start = 1, end = 10
Output: [2, 3, 5, 7]

# Test Case 3
Input: start = 20, end = 30
Output: [23, 29]

# Test Case 4
Input: start = 1, end = 1
Output: []

# Test Case 5
Input: start = 2, end = 2
Output: [^2]

# Test Case 6
Input: start = 50, end = 60
Output: [53, 59]
```


***

#### **Problem 28: Pyramid Pattern Printer**

**Difficulty:** Medium

**Description:**
Given an integer `n`, return a list of strings representing a pyramid pattern with `n` levels.

**Example 1:**

```
Input: n = 3
Output: 
  *
 ***
*****
```

**Constraints:**

- 1 <= n <= 20

**Test Cases:**

```python
# Test Case 1
Input: 3
Output: ["  *  ", " *** ", "*****"]

# Test Case 2
Input: 1
Output: ["*"]

# Test Case 3
Input: 5
Output: ["    *    ", "   ***   ", "  *****  ", " ******* ", "*********"]

# Test Case 4
Input: 2
Output: [" * ", "***"]

# Test Case 5
Input: 4
Output: ["   *   ", "  ***  ", " ***** ", "*******"]

# Test Case 6
Input: 6
Output: ["     *     ", "    ***    ", "   *****   ", "  *******  ", " ********* ", "***********"]
```


***

#### **Problem 29: Factorial Calculator**

**Difficulty:** Medium

**Description:**
Given an integer `n`, calculate its factorial (n!). Implement both iterative and recursive solutions.

**Example 1:**

```
Input: n = 5
Output: 120
```

**Constraints:**

- 0 <= n <= 20

**Test Cases:**

```python
# Test Case 1
Input: 5
Output: 120

# Test Case 2
Input: 0
Output: 1

# Test Case 3
Input: 1
Output: 1

# Test Case 4
Input: 10
Output: 3628800

# Test Case 5
Input: 3
Output: 6

# Test Case 6
Input: 7
Output: 5040
```


***

#### **Problem 30: Sum of Digits**

**Difficulty:** Medium

**Description:**
Given an integer `n`, return the sum of its digits. Handle negative numbers by treating them as positive.

**Example 1:**

```
Input: n = 1234
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10
```

**Constraints:**

- -10^9 <= n <= 10^9

**Test Cases:**

```python
# Test Case 1
Input: 1234
Output: 10

# Test Case 2
Input: 0
Output: 0

# Test Case 3
Input: -456
Output: 15

# Test Case 4
Input: 9999
Output: 36

# Test Case 5
Input: 100
Output: 1

# Test Case 6
Input: 505
Output: 10
```


***

#### **Problem 31: Armstrong Number Checker**

**Difficulty:** Medium

**Description:**
Given an integer `n`, determine if it is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

**Example 1:**

```
Input: n = 153
Output: True
Explanation: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```

**Constraints:**

- 0 <= n <= 10^6

**Test Cases:**

```python
# Test Case 1
Input: 153
Output: True

# Test Case 2
Input: 123
Output: False

# Test Case 3
Input: 9474
Output: True

# Test Case 4
Input: 0
Output: True

# Test Case 5
Input: 1
Output: True

# Test Case 6
Input: 371
Output: True
```


***

#### **Problem 32: Find GCD of Two Numbers**

**Difficulty:** Medium

**Description:**
Given two integers `a` and `b`, find their Greatest Common Divisor (GCD) using the Euclidean algorithm.

**Example 1:**

```
Input: a = 48, b = 18
Output: 6
```

**Constraints:**

- 1 <= a, b <= 10^6

**Test Cases:**

```python
# Test Case 1
Input: a = 48, b = 18
Output: 6

# Test Case 2
Input: a = 100, b = 50
Output: 50

# Test Case 3
Input: a = 17, b = 19
Output: 1

# Test Case 4
Input: a = 1, b = 1
Output: 1

# Test Case 5
Input: a = 24, b = 36
Output: 12

# Test Case 6
Input: a = 7, b = 14
Output: 7
```


***

#### **Problem 33: Count Vowels and Consonants**

**Difficulty:** Medium

**Description:**
Given a string `s`, return a dictionary with counts of vowels and consonants. Ignore spaces and special characters.

**Example 1:**

```
Input: s = "Hello World"
Output: {'vowels': 3, 'consonants': 7}
```

**Constraints:**

- 1 <= len(s) <= 10^4
- `s` consists of letters and spaces

**Test Cases:**

```python
# Test Case 1
Input: "Hello World"
Output: {'vowels': 3, 'consonants': 7}

# Test Case 2
Input: "aeiou"
Output: {'vowels': 5, 'consonants': 0}

# Test Case 3
Input: "bcdfg"
Output: {'vowels': 0, 'consonants': 5}

# Test Case 4
Input: "Python Programming"
Output: {'vowels': 5, 'consonants': 12}

# Test Case 5
Input: "a"
Output: {'vowels': 1, 'consonants': 0}

# Test Case 6
Input: "AEIOUaeiou"
Output: {'vowels': 10, 'consonants': 0}
```


***

### **Section 5: Advanced List Operations (Questions 34-40)**

#### **Problem 34: Find Kth Largest Element**

**Difficulty:** Medium

**Description:**
Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Constraints:**

- 1 <= k <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4

**Test Cases:**

```python
# Test Case 1
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

# Test Case 2
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

# Test Case 3
Input: nums = [^1], k = 1
Output: 1

# Test Case 4
Input: nums = [7,10,4,3,20,15], k = 3
Output: 10

# Test Case 5
Input: nums = [1,2,3,4,5], k = 1
Output: 5

# Test Case 6
Input: nums = [-1,-2,-3], k = 2
Output: -2
```


***

#### **Problem 35: Subarray with Given Sum**

**Difficulty:** Medium

**Description:**
Given an array of positive integers `nums` and a target sum `target`, find if there exists a continuous subarray with sum equal to `target`. Return the start and end indices if found, otherwise return [-1, -1].

**Example 1:**

```
Input: nums = [1,2,3,7,5], target = 12
Output: [1, 3]
Explanation: 2 + 3 + 7 = 12
```

**Constraints:**

- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^3
- 1 <= target <= 10^8

**Test Cases:**

```python
# Test Case 1
Input: nums = [1,2,3,7,5], target = 12
Output: [1, 3]

# Test Case 2
Input: nums = [1,2,3,4,5], target = 9
Output: [1, 3]

# Test Case 3
Input: nums = [5,8,3,1], target = 8
Output: [1, 1]

# Test Case 4
Input: nums = [1,2,3], target = 10
Output: [-1, -1]

# Test Case 5
Input: nums = [15,2,4,8,9,5,10,23], target = 23
Output: [7, 7]

# Test Case 6
Input: nums = [1,4,20,3,10,5], target = 33
Output: [2, 4]
```


***

#### **Problem 36: Sorted Squares of Array**

**Difficulty:** Medium

**Description:**
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Constraints:**

- 1 <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in non-decreasing order

**Test Cases:**

```python
# Test Case 1
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

# Test Case 2
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

# Test Case 3
Input: [1,2,3,4,5]
Output: [1,4,9,16,25]

# Test Case 4
Input: [-5,-4,-3,-2,-1]
Output: [1,4,9,16,25]

# Test Case 5
Input: [^0]
Output: [^0]

# Test Case 6
Input: [-1,0,1]
Output: [0,1,1]
```


***

#### **Problem 37: Next Permutation**

**Difficulty:** Medium

**Description:**
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, rearrange it as the lowest possible order.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Constraints:**

- 1 <= len(nums) <= 100
- 0 <= nums[i] <= 100

**Test Cases:**

```python
# Test Case 1
Input: [1,2,3]
Output: [1,3,2]

# Test Case 2
Input: [3,2,1]
Output: [1,2,3]

# Test Case 3
Input: [1,1,5]
Output: [1,5,1]

# Test Case 4
Input: [^1]
Output: [^1]

# Test Case 5
Input: [1,3,2]
Output: [2,1,3]

# Test Case 6
Input: [2,3,1]
Output: [3,1,2]
```


***

#### **Problem 38: Intersection of Two Arrays**

**Difficulty:** Medium

**Description:**
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [^2]
```

**Constraints:**

- 1 <= len(nums1), len(nums2) <= 1000
- 0 <= nums1[i], nums2[j] <= 1000

**Test Cases:**

```python
# Test Case 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [^2]

# Test Case 2
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

# Test Case 3
Input: nums1 = [1,2,3], nums2 = [4,5,6]
Output: []

# Test Case 4
Input: nums1 = [^1], nums2 = [^1]
Output: [^1]

# Test Case 5
Input: nums1 = [1,2,3,4,5], nums2 = [3,4,5,6,7]
Output: [3,4,5]

# Test Case 6
Input: nums1 = [7,8,9], nums2 = [7,8,9]
Output: [7,8,9]
```


***

#### **Problem 39: Find All Duplicates in Array**

**Difficulty:** Medium

**Description:**
Given an integer array `nums` of length n where all integers are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appear twice.

**Example 1:**

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

**Constraints:**

- n == len(nums)
- 1 <= n <= 10^5
- 1 <= nums[i] <= n

**Test Cases:**

```python
# Test Case 1
Input: [4,3,2,7,8,2,3,1]
Output: [2,3]

# Test Case 2
Input: [1,1,2]
Output: [^1]

# Test Case 3
Input: [^1]
Output: []

# Test Case 4
Input: [1,2,3,4,5]
Output: []

# Test Case 5
Input: [5,4,6,7,9,3,10,9,5,6]
Output: [5,6,9]

# Test Case 6
Input: [10,2,5,10,9,1,1,4,3,7]
Output: [10,1]
```


***

#### **Problem 40: Spiral Matrix Traversal**

**Difficulty:** Medium

**Description:**
Given an m x n matrix, return all elements of the matrix in spiral order.

**Example 1:**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Constraints:**

- m == len(matrix)
- n == len(matrix[i])
- 1 <= m, n <= 10

**Test Cases:**

```python
# Test Case 1
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

# Test Case 2
Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Test Case 3
Input: [[^1]]
Output: [^1]

# Test Case 4
Input: [[1,2],[3,4]]
Output: [1,2,4,3]

# Test Case 5
Input: [[1,2,3]]
Output: [1,2,3]

# Test Case 6
Input: [[^1],[^2],[^3]]
Output: [1,2,3]
```


***

### **Section 6: Lambda, Map, Filter (Questions 41-45)**

#### **Problem 41: Filter Even Squares**

**Difficulty:** Medium

**Description:**
Given a list of integers `nums`, use `filter()` and `lambda` to return only the squares of even numbers.

**Example 1:**

```
Input: nums = [1, 2, 3, 4, 5, 6]
Output: [4, 16, 36]
```

**Constraints:**

- 1 <= len(nums) <= 1000
- -1000 <= nums[i] <= 1000

**Test Cases:**

```python
# Test Case 1
Input: [1, 2, 3, 4, 5, 6]
Output: [4, 16, 36]

# Test Case 2
Input: [1, 3, 5, 7]
Output: []

# Test Case 3
Input: [2, 4, 6, 8]
Output: [4, 16, 36, 64]

# Test Case 4
Input: [^0]
Output: [^0]

# Test Case 5
Input: [-2, -1, 0, 1, 2]
Output: [4, 0, 4]

# Test Case 6
Input: [10, 15, 20, 25]
Output: [100, 400]
```


***

#### **Problem 42: Transform Names to Uppercase**

**Difficulty:** Medium

**Description:**
Given a list of names, use `map()` and `lambda` to convert all names to uppercase and add "Hello, " prefix.

**Example 1:**

```
Input: names = ["alice", "bob", "charlie"]
Output: ["Hello, ALICE", "Hello, BOB", "Hello, CHARLIE"]
```

**Constraints:**

- 1 <= len(names) <= 100
- 1 <= len(names[i]) <= 50

**Test Cases:**

```python
# Test Case 1
Input: ["alice", "bob", "charlie"]
Output: ["Hello, ALICE", "Hello, BOB", "Hello, CHARLIE"]

# Test Case 2
Input: ["john"]
Output: ["Hello, JOHN"]

# Test Case 3
Input: ["x", "y", "z"]
Output: ["Hello, X", "Hello, Y", "Hello, Z"]

# Test Case 4
Input: ["python", "javascript", "java"]
Output: ["Hello, PYTHON", "Hello, JAVASCRIPT", "Hello, JAVA"]

# Test Case 5
Input: ["a", "bb", "ccc"]
Output: ["Hello, A", "Hello, BB", "Hello, CCC"]

# Test Case 6
Input: ["Test", "Data", "Code"]
Output: ["Hello, TEST", "Hello, DATA", "Hello, CODE"]
```


***

#### **Problem 43: Sum of Filtered Numbers**

**Difficulty:** Medium

**Description:**
Given a list of numbers `nums`, use `filter()`, `map()`, and `lambda` to find the sum of squares of numbers greater than 5.

**Example 1:**

```
Input: nums = [1, 5, 8, 10, 3, 6]
Output: 200
Explanation: 8^2 + 10^2 + 6^2 = 64 + 100 + 36 = 200
```

**Constraints:**

- 1 <= len(nums) <= 1000
- -100 <= nums[i] <= 100

**Test Cases:**

```python
# Test Case 1
Input: [1, 5, 8, 10, 3, 6]
Output: 200

# Test Case 2
Input: [1, 2, 3, 4, 5]
Output: 0

# Test Case 3
Input: [6, 7, 8]
Output: 149

# Test Case 4
Input: [10, 20, 30]
Output: 1400

# Test Case 5
Input: []
Output: 0

# Test Case 6
Input: [^6]
Output: 36
```


***

#### **Problem 44: Custom Sort Using Lambda**

**Difficulty:** Medium

**Description:**
Given a list of tuples `data` where each tuple contains (name, age, score), sort the list first by score (descending), then by age (ascending) using `lambda`.

**Example 1:**

```
Input: data = [("Alice", 25, 85), ("Bob", 22, 90), ("Charlie", 25, 90)]
Output: [("Bob", 22, 90), ("Charlie", 25, 90), ("Alice", 25, 85)]
```

**Constraints:**

- 1 <= len(data) <= 1000
- All tuples have exactly 3 elements

**Test Cases:**

```python
# Test Case 1
Input: [("Alice", 25, 85), ("Bob", 22, 90), ("Charlie", 25, 90)]
Output: [("Bob", 22, 90), ("Charlie", 25, 90), ("Alice", 25, 85)]

# Test Case 2
Input: [("A", 30, 70)]
Output: [("A", 30, 70)]

# Test Case 3
Input: [("X", 20, 80), ("Y", 21, 80), ("Z", 19, 80)]
Output: [("Z", 19, 80), ("X", 20, 80), ("Y", 21, 80)]

# Test Case 4
Input: [("John", 25, 95), ("Jane", 23, 95)]
Output: [("Jane", 23, 95), ("John", 25, 95)]

# Test Case 5
Input: [("P", 30, 60), ("Q", 25, 70), ("R", 28, 65)]
Output: [("Q", 25, 70), ("R", 28, 65), ("P", 30, 60)]

# Test Case 6
Input: [("A", 20, 100), ("B", 21, 99), ("C", 20, 100)]
Output: [("A", 20, 100), ("C", 20, 100), ("B", 21, 99)]
```


***

#### **Problem 45: Chain Multiple Operations**

**Difficulty:** Medium

**Description:**
Given a list of numbers `nums`, perform the following operations in sequence using `filter()`, `map()`, and `lambda`:

1. Filter numbers divisible by 3
2. Square each number
3. Filter numbers greater than 50
4. Return as a sorted list

**Example 1:**

```
Input: nums = [3, 6, 9, 12, 15, 18]
Output: [81, 144, 324]
```

**Constraints:**

- 1 <= len(nums) <= 1000
- 1 <= nums[i] <= 100

**Test Cases:**

```python
# Test Case 1
Input: [3, 6, 9, 12, 15, 18]
Output: [81, 144, 324]

# Test Case 2
Input: [1, 2, 4, 5]
Output: []

# Test Case 3
Input: [9, 12, 15]
Output: [81, 144]

# Test Case 4
Input: [^3]
Output: []

# Test Case 5
Input: [21, 24, 27, 30]
Output: [441, 576, 729, 900]

# Test Case 6
Input: [6, 9, 12]
Output: [81, 144]
```


***

## 🎯 **FINAL PROJECT: Student Management System**

**Difficulty:** Hard
**Estimated Time:** 3-5 hours

### **Project Description:**

Create a comprehensive Student Management System that performs various operations on student data using all the concepts you've learned.

### **Requirements:**

#### **Data Structure:**

Each student is represented as a dictionary:

```python
{
    'id': int,
    'name': str,
    'age': int,
    'grades': [int],  # List of grades (0-100)
    'courses': [str]
}
```


#### **Features to Implement:**

**1. Add Student** *(Lists, Dictionaries)*

- Add a new student to the system
- Validate that ID is unique
- Return success/failure message

**2. Calculate Average Grade** *(Loops, Math Operations)*

- Calculate average grade for a student
- Use `sum()` function
- Handle empty grade lists

**3. Find Top Performers** *(Sorting, Lambda)*

- Return top N students by average grade
- Use `sorted()` with lambda
- Handle ties appropriately

**4. Search Students** *(String Operations, Filter)*

- Search by name (case-insensitive, partial match)
- Search by course enrollment
- Use `filter()` and lambda

**5. Update Student Info** *(Dictionary Operations)*

- Update name, age, or courses
- Add new grades
- Validate input data

**6. Generate Report** *(String Formatting, Loops)*

- Generate formatted report for all students
- Include: ID, Name, Age, Average Grade, Pass/Fail status
- Pass threshold: 60%

**7. Course Statistics** *(Dictionary, Aggregations)*

- Count students per course
- Find most popular course
- Return dictionary of course: student_count

**8. Grade Distribution** *(Tuples, Conditionals)*

- Categorize grades: A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
- Return tuple: (A_count, B_count, C_count, D_count, F_count)

**9. Bulk Import** *(File I/O, String Parsing)*

- Read student data from formatted string
- Parse and validate data
- Add multiple students at once

**10. Filter and Transform** *(Map, Filter, List Comprehension)*

- Get all students older than X
- Get names of students with average > Y
- Use list comprehensions and functional programming

***

### **Example Usage:**

```python
# Initialize system
sms = StudentManagementSystem()

# Add students
sms.add_student(1, "Alice Johnson", 20, [85, 90, 88], ["Python", "Data Science"])
sms.add_student(2, "Bob Smith", 22, [78, 82, 80], ["Python", "Web Dev"])
sms.add_student(3, "Charlie Brown", 21, [92, 95, 89], ["Data Science", "ML"])

# Calculate average
avg = sms.calculate_average(1)  # Returns 87.67

# Find top performers
top_students = sms.get_top_performers(2)  
# Returns: [{'id': 3, 'name': 'Charlie Brown', 'avg': 92.0}, 
#           {'id': 1, 'name': 'Alice Johnson', 'avg': 87.67}]

# Search
results = sms.search_by_name("alice")  # Case-insensitive
results = sms.search_by_course("Python")  # Returns Alice and Bob

# Generate report
report = sms.generate_report()
# Output:
# ====== STUDENT REPORT ======
# ID: 1 | Name: Alice Johnson | Age: 20 | Average: 87.67 | Status: PASS
# ID: 2 | Name: Bob Smith | Age: 22 | Average: 80.00 | Status: PASS
# ID: 3 | Name: Charlie Brown | Age: 21 | Average: 92.00 | Status: PASS

# Course statistics
stats = sms.course_statistics()
# Returns: {'Python': 2, 'Data Science': 2, 'Web Dev': 1, 'ML': 1}

# Grade distribution
dist = sms.grade_distribution()
# Returns: (1, 2, 0, 0, 0)  # 1 A student, 2 B students
```


***

### **Test Cases for Final Project:**

```python
# Test Case 1: Add and retrieve student
Input: add_student(1, "John", 20, [80, 85], ["Math"])
Output: "Student added successfully"
Verify: get_student(1) returns complete student data

# Test Case 2: Calculate average for empty grades
Input: add_student(2, "Jane", 21, [], ["Science"])
Output: calculate_average(2) returns 0 or None

# Test Case 3: Top performers with ties
Input: Three students with averages [90, 90, 85]
Output: get_top_performers(2) returns both students with 90

# Test Case 4: Search with no results
Input: search_by_name("Nonexistent")
Output: []

# Test Case 5: Update non-existent student
Input: update_student(999, {"name": "Test"})
Output: "Student not found"

# Test Case 6: Grade distribution with all failing students
Input: Students with grades [50, 45, 55]
Output: grade_distribution() returns (0, 0, 0, 0, 3)
```


***

### **Deliverables:**

1. **main.py** - Core implementation with class `StudentManagementSystem`
2. **test_sms.py** - Comprehensive test suite with all 6 test cases
3. **README.md** - Documentation with:
    - Project overview
    - Installation instructions
    - Usage examples
    - Function documentation
    - Complexity analysis
4. **sample_data.txt** - Sample student data for bulk import
5. **requirements.txt** - Any dependencies (if needed)

***

### **Bonus Features (Optional):**

- Export report to CSV file
- Implement data persistence (save/load from JSON)
- Add error handling and custom exceptions
- Create a simple CLI interface
- Add type hints
- Implement logging

***

## 📝 **How to Use These Questions:**

### **GitHub Repository Structure:**

```
python-dsa-practice/
├── README.md
├── strings/
│   ├── problem_001_reverse_words.py
│   ├── problem_002_character_frequency.py
│   └── ...
├── lists/
│   ├── problem_009_missing_number.py
│   └── ...
├── tuples_dicts/
│   ├── problem_019_merge_dicts.py
│   └── ...
├── loops/
│   ├── problem_026_fizzbuzz.py
│   └── ...
├── advanced_lists/
│   ├── problem_034_kth_largest.py
│   └── ...
├── functional/
│   ├── problem_041_filter_squares.py
│   └── ...
└── final_project/
    ├── student_management_system.py
    ├── test_sms.py
    └── README.md
```


### **Each Python File Format:**

```python
"""
Problem [Number]: [Title]
Difficulty: Medium
Topic: [Topic Name]

Description:
[Problem description]

Constraints:
[List constraints]

Example:
[Example with explanation]
"""

def solution(params):
    """
    Your solution here
    """
    pass

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    assert solution(...) == expected_output
    
    # Test Case 2
    ...
    
    print("All test cases passed!")
```


### **Question 1: Longest Consecutive Sequence (Google)**

**Difficulty:** Medium-Hard
**Topics:** Lists, Sets, Loops

**Description:**
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

**Example 1:**

```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.
```

**Example 2:**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]
```

**Constraints:**

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

**MAANG Tip:** Use a set for O(1) lookup and only start counting from sequence beginnings.

**Test Cases:**

```python
# Test Case 1
Input: [100, 4, 200, 1, 3, 2]
Output: 4

# Test Case 2
Input: [0,3,7,2,5,8,4,6,0,1]
Output: 9

# Test Case 3
Input: []
Output: 0

# Test Case 4
Input: [^1]
Output: 1

# Test Case 5
Input: [1,2,0,1]
Output: 3

# Test Case 6
Input: [9,1,4,7,3,-1,0,5,8,-2,6]
Output: 7
```

**Expected Time Complexity:** O(n)
**Expected Space Complexity:** O(n)

***

### **Question 2: Group Anagrams with Frequency Sorting (Amazon)**

**Difficulty:** Medium-Hard
**Topics:** Strings, Dictionaries, Tuples, Sorting, Lambda

**Description:**
Given an array of strings `strs`, group anagrams together, then sort each group by frequency of occurrence (most frequent first), and finally sort the groups by the frequency of the first element in descending order.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat","eat","tea"]
Output: [["eat","tea","eat","tea"], ["tan","nat"], ["bat"]]
Explanation: 
- "eat"/"tea" appears 4 times (2+2)
- "tan"/"nat" appears 2 times  
- "bat" appears 1 time
```

**Example 2:**

```
Input: strs = ["abc","bca","cab","xyz","zyx"]
Output: [["xyz","zyx"], ["abc","bca","cab"]]
```

**Constraints:**

- 1 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- strs[i] consists of lowercase English letters

**MAANG Tip:** Use tuple of sorted string as dictionary key, then count frequencies.

**Test Cases:**

```python
# Test Case 1
Input: ["eat","tea","tan","ate","nat","bat","eat","tea"]
Output: [["eat","tea","eat","tea"], ["tan","nat"], ["bat"]]

# Test Case 2
Input: ["abc","bca","cab","xyz","zyx"]
Output: [["xyz","zyx"], ["abc","bca","cab"]]

# Test Case 3
Input: ["a"]
Output: [["a"]]

# Test Case 4
Input: [""]
Output: [[""]]

# Test Case 5
Input: ["listen","silent","enlist","listen","silent"]
Output: [["listen","silent","listen","silent"], ["enlist"]]

# Test Case 6
Input: ["ab","ba","ab","ba","cd"]
Output: [["ab","ba","ab","ba"], ["cd"]]
```

**Expected Time Complexity:** O(n * k log k) where k is max string length
**Expected Space Complexity:** O(n * k)

***

### **Question 3: Three Sum (Meta/Facebook)**

**Difficulty:** Medium
**Topics:** Lists, Loops, Sets, Sorting

**Description:**
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[^0] + nums[^1] + nums[^2] = (-1) + 0 + 1 = 0
nums[^1] + nums[^2] + nums[^4] = 0 + 1 + (-1) = 0
nums[^0] + nums[^3] + nums[^4] = (-1) + 2 + (-1) = 0
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum to 0.
```

**Constraints:**

- 3 <= len(nums) <= 3000
- -10^5 <= nums[i] <= 10^5

**MAANG Tip:** Sort first, then use two-pointer technique to avoid O(n³).

**Test Cases:**

```python
# Test Case 1
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

# Test Case 2
Input: [0,1,1]
Output: []

# Test Case 3
Input: [0,0,0]
Output: [[0,0,0]]

# Test Case 4
Input: [-2,0,1,1,2]
Output: [[-2,0,2],[-2,1,1]]

# Test Case 5
Input: [-4,-1,-1,0,1,2]
Output: [[-1,-1,2],[-1,0,1]]

# Test Case 6
Input: [1,2,-2,-1]
Output: []
```

**Expected Time Complexity:** O(n²)
**Expected Space Complexity:** O(n)

***

### **Question 4: Decode String (Netflix)**

**Difficulty:** Medium
**Topics:** Strings, Loops, Stack (using lists)

**Description:**
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times.

**Example 1:**

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2:**

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3:**

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

**Constraints:**

- 1 <= len(s) <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'
- s is always a valid encoding

**MAANG Tip:** Use stack to handle nested brackets.

**Test Cases:**

```python
# Test Case 1
Input: "3[a]2[bc]"
Output: "aaabcbc"

# Test Case 2
Input: "3[a2[c]]"
Output: "accaccacc"

# Test Case 3
Input: "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

# Test Case 4
Input: "abc3[cd]xyz"
Output: "abccdcdcdxyz"

# Test Case 5
Input: "10[a]"
Output: "aaaaaaaaaa"

# Test Case 6
Input: "2[2[y]pq4[2[jk]e1[f]]]ef"
Output: "yypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
```

**Expected Time Complexity:** O(n)
**Expected Space Complexity:** O(n)

***

### **Question 5: Subarray Sum Equals K (Google)**

**Difficulty:** Medium-Hard
**Topics:** Lists, Dictionaries, Loops, Prefix Sum

**Description:**
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] and [1,1] are the two subarrays
```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [^3]
```

**Constraints:**

- 1 <= len(nums) <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

**MAANG Tip:** Use prefix sum and hashmap for O(n) solution.

**Test Cases:**

```python
# Test Case 1
Input: nums = [1,1,1], k = 2
Output: 2

# Test Case 2
Input: nums = [1,2,3], k = 3
Output: 2

# Test Case 3
Input: nums = [^1], k = 0
Output: 0

# Test Case 4
Input: nums = [1,-1,0], k = 0
Output: 3

# Test Case 5
Input: nums = [3,4,7,2,-3,1,4,2], k = 7
Output: 4

# Test Case 6
Input: nums = [1,2,1,2,1], k = 3
Output: 4
```

**Expected Time Complexity:** O(n)
**Expected Space Complexity:** O(n)

***

### **Question 6: Minimum Window Substring (Amazon)**

**Difficulty:** Hard
**Topics:** Strings, Dictionaries, Loops, Sliding Window

**Description:**
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
```

**Example 3:**

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
```

**Constraints:**

- 1 <= len(s), len(t) <= 10^5
- s and t consist of uppercase and lowercase English letters

**MAANG Tip:** Use sliding window with two pointers and character frequency maps.

**Test Cases:**

```python
# Test Case 1
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

# Test Case 2
Input: s = "a", t = "a"
Output: "a"

# Test Case 3
Input: s = "a", t = "aa"
Output: ""

# Test Case 4
Input: s = "ab", t = "b"
Output: "b"

# Test Case 5
Input: s = "abc", t = "cba"
Output: "abc"

# Test Case 6
Input: s = "cabwefgewcwaefgcf", t = "cae"
Output: "cwae"
```

**Expected Time Complexity:** O(|s| + |t|)
**Expected Space Complexity:** O(|s| + |t|)

***

### **Question 7: Top K Frequent Elements (Meta/Facebook)**

**Difficulty:** Medium
**Topics:** Lists, Dictionaries, Tuples, Sorting, Lambda

**Description:**
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [^1], k = 1
Output: [^1]
```

**Constraints:**

- 1 <= len(nums) <= 10^5
- k is in the range [1, number of unique elements]
- It's guaranteed that the answer is unique

**MAANG Tip:** Use dictionary for counting, then bucket sort or heap for O(n) solution.

**Test Cases:**

```python
# Test Case 1
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

# Test Case 2
Input: nums = [^1], k = 1
Output: [^1]

# Test Case 3
Input: nums = [4,1,-1,2,-1,2,3], k = 2
Output: [-1,2]

# Test Case 4
Input: nums = [1,2], k = 2
Output: [1,2]

# Test Case 5
Input: nums = [5,5,5,3,3,1,1,1,1], k = 1
Output: [^1]

# Test Case 6
Input: nums = [1,1,1,2,2,2,3,3,3], k = 3
Output: [1,2,3]
```

**Expected Time Complexity:** O(n)
**Expected Space Complexity:** O(n)

***

### **Question 8: Merge Intervals (Google)**

**Difficulty:** Medium
**Topics:** Lists, Tuples, Sorting, Lambda, Loops

**Description:**
Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap, so merge them into [1,6]
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping
```

**Constraints:**

- 1 <= len(intervals) <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

**MAANG Tip:** Sort by start time, then iterate and merge.

**Test Cases:**

```python
# Test Case 1
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

# Test Case 2
Input: [[1,4],[4,5]]
Output: [[1,5]]

# Test Case 3
Input: [[1,4],[0,4]]
Output: [[0,4]]

# Test Case 4
Input: [[1,4],[2,3]]
Output: [[1,4]]

# Test Case 5
Input: [[1,4],[0,1]]
Output: [[0,4]]

# Test Case 6
Input: [[2,3],[4,5],[6,7],[8,9],[1,10]]
Output: [[1,10]]
```

**Expected Time Complexity:** O(n log n)
**Expected Space Complexity:** O(n)

***

### **Question 9: Word Break (Amazon)**

**Difficulty:** Medium
**Topics:** Strings, Lists, Loops, Sets, Conditionals

**Description:**
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code"
```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple"
```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

**Constraints:**

- 1 <= len(s) <= 300
- 1 <= len(wordDict) <= 1000
- 1 <= len(wordDict[i]) <= 20
- All strings consist of lowercase English letters

**MAANG Tip:** Use dynamic programming with boolean array.

**Test Cases:**

```python
# Test Case 1
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

# Test Case 2
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

# Test Case 3
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

# Test Case 4
Input: s = "a", wordDict = ["a"]
Output: true

# Test Case 5
Input: s = "aaaaaaa", wordDict = ["aaaa","aaa"]
Output: true

# Test Case 6
Input: s = "goalspecial", wordDict = ["go","goal","goals","special"]
Output: true
```

**Expected Time Complexity:** O(n² * m) where m is avg word length
**Expected Space Complexity:** O(n)

***

### **Question 10: Valid Sudoku (Netflix)**

**Difficulty:** Medium
**Topics:** Lists (2D), Loops, Sets, Conditionals

**Description:**
Determine if a 9 x 9 Sudoku board is valid. Only filled cells need to be validated according to:

1. Each row must contain digits 1-9 without repetition
2. Each column must contain digits 1-9 without repetition
3. Each 3x3 sub-box must contain digits 1-9 without repetition

**Example 1:**

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Constraints:**

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'

**MAANG Tip:** Use sets to track seen numbers in rows, columns, and boxes.

**Test Cases:**

```python
# Test Case 1
Input: Valid board (as shown in example)
Output: true

# Test Case 2
Input: [[".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
Output: true

# Test Case 3
Input: Board with duplicate in row
Output: false

# Test Case 4
Input: Board with duplicate in column
Output: false

# Test Case 5
Input: Board with duplicate in 3x3 box
Output: false

# Test Case 6
Input: [["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
Output: false (duplicate 8 in first column)
```

**Expected Time Complexity:** O(1) - board is always 9x9
**Expected Space Complexity:** O(1)

***

## 🚀 **MAJOR PROJECT: E-Commerce Inventory Management System**

**Difficulty:** Advanced
**Estimated Time:** 8-12 hours
**Real-World Application:** Amazon-style inventory system

***

### **Project Overview:**

Build a comprehensive e-commerce inventory management system that handles products, orders, customers, and analytics. This project simulates real-world scenarios from companies like Amazon, Flipkart, and other e-commerce giants.[^2][^1]

***

### **System Architecture:**

```
inventory_system/
├── main.py                 # Main system class
├── product_manager.py      # Product CRUD operations
├── order_manager.py        # Order processing
├── customer_manager.py     # Customer management
├── analytics.py            # Data analytics & reporting
├── utils.py                # Helper functions
├── test_system.py          # Comprehensive test suite
├── data/
│   ├── products.json       # Product database
│   ├── orders.json         # Order history
│   └── customers.json      # Customer data
├── reports/
│   └── sales_report.txt    # Generated reports
└── README.md               # Documentation
```


***

### **Data Structures:**

#### **1. Product:**

```python
{
    'product_id': str,          # Unique ID (e.g., "PROD001")
    'name': str,                # Product name
    'category': str,            # Category (Electronics, Clothing, etc.)
    'price': float,             # Price in INR
    'stock': int,               # Available quantity
    'supplier': str,            # Supplier name
    'ratings': [float],         # List of ratings (1-5)
    'tags': [str],              # Search tags
    'description': str,         # Product description
    'discount': float,          # Discount percentage (0-100)
    'date_added': str           # ISO format date
}
```


#### **2. Customer:**

```python
{
    'customer_id': str,         # Unique ID (e.g., "CUST001")
    'name': str,                # Full name
    'email': str,               # Email address
    'phone': str,               # Phone number
    'address': {
        'street': str,
        'city': str,
        'state': str,
        'pincode': str
    },
    'membership': str,          # "Regular", "Silver", "Gold", "Platinum"
    'wallet_balance': float,    # Available balance
    'total_orders': int,        # Order count
    'total_spent': float,       # Total money spent
    'wishlist': [str],          # Product IDs
    'cart': [str],              # Product IDs
    'join_date': str            # ISO format date
}
```


#### **3. Order:**

```python
{
    'order_id': str,            # Unique ID (e.g., "ORD001")
    'customer_id': str,         # Customer who placed order
    'products': [               # List of ordered products
        {
            'product_id': str,
            'quantity': int,
            'price_at_purchase': float
        }
    ],
    'total_amount': float,      # Total order value
    'discount_applied': float,  # Total discount
    'payment_method': str,      # "Card", "UPI", "Wallet", "COD"
    'status': str,              # "Pending", "Confirmed", "Shipped", "Delivered", "Cancelled"
    'order_date': str,          # ISO format date
    'delivery_date': str,       # Expected/actual delivery
    'shipping_address': dict    # Same structure as customer address
}
```


***

### **Core Features (30 Functions):**

#### **A. Product Management (8 functions)**

**1. add_product()**

- Add new product to inventory
- Validate all fields
- Generate unique product ID
- Update products.json

**2. update_product()**

- Update product details (price, stock, discount, etc.)
- Validate product exists
- Log changes

**3. delete_product()**

- Remove product from system
- Check if product is in pending orders
- Archive product data

**4. search_products()**

- Search by name, category, tags (case-insensitive)
- Support partial matching
- Return sorted results by relevance

**5. filter_products()**

- Filter by price range, category, rating, stock availability
- Support multiple filters simultaneously
- Use lambda and filter()

**6. get_low_stock_alerts()**

- Return products with stock below threshold
- Sort by urgency (lowest stock first)
- Support custom threshold

**7. bulk_update_prices()**

- Update prices for multiple products
- Support percentage increase/decrease
- Apply to specific categories or all

**8. calculate_product_metrics()**

- Average rating, total sales, revenue
- Most reviewed product
- Return as dictionary

***

#### **B. Customer Management (6 functions)**

**9. register_customer()**

- Add new customer
- Validate email format and phone
- Generate unique customer ID
- Initialize wallet with welcome bonus

**10. update_customer_profile()**

- Update customer details
- Validate new data
- Track modification history

**11. upgrade_membership()**

- Upgrade based on total_spent
- Regular: < ₹10,000
- Silver: ₹10,000 - ₹50,000
- Gold: ₹50,000 - ₹1,00,000
- Platinum: > ₹1,00,000

**12. add_to_wishlist()**

- Add product to customer's wishlist
- Check product exists
- Prevent duplicates

**13. add_to_cart()**

- Add product to cart
- Check stock availability
- Prevent duplicates

**14. get_customer_recommendations()**

- Recommend products based on:
    - Purchase history (same category)
    - Wishlist items (similar products)
    - Popular in customer's city
- Use filter() and sorted() with lambda

***

#### **C. Order Management (8 functions)**

**15. create_order()**

- Process order from cart
- Validate stock availability
- Calculate total with discounts
- Apply membership discount
- Deduct from stock
- Update customer stats

**16. cancel_order()**

- Cancel order if status is "Pending" or "Confirmed"
- Refund to wallet
- Restore stock
- Update order status

**17. update_order_status()**

- Update order status
- Validate status transitions
- Send notifications (print messages)

**18. process_payment()**

- Handle different payment methods
- Validate wallet balance if wallet payment
- Apply payment-specific discounts
- Return transaction success/failure

**19. apply_coupon()**

- Validate coupon code
- Check expiry and usage limits
- Calculate discount
- Update order total

**20. get_order_history()**

- Get all orders for a customer
- Filter by status, date range
- Sort by date (recent first)

**21. calculate_delivery_date()**

- Calculate expected delivery based on:
    - Order date
    - Shipping address (city/state)
    - Product availability
- Return ISO date string

**22. generate_invoice()**

- Create formatted invoice
- Include all order details
- Calculate GST (18%)
- Return as formatted string

***

#### **D. Analytics \& Reporting (8 functions)**

**23. get_sales_report()**

- Generate sales report for date range
- Include: total orders, revenue, avg order value
- Group by day/week/month
- Return dictionary

**24. get_top_selling_products()**

- Return top N products by quantity sold
- Include product details and sales count
- Use sorted() with lambda

**25. get_category_performance()**

- Compare sales across categories
- Return: category name, total revenue, order count
- Sort by revenue (descending)

**26. get_customer_insights()**

- Customer lifetime value (CLV)
- Average order value per customer
- Customer retention rate
- Return comprehensive dictionary

**27. predict_restock_needs()**

- Analyze sales velocity
- Predict when products will run out
- Suggest reorder quantities
- Use average daily sales

**28. get_revenue_by_payment_method()**

- Break down revenue by payment type
- Calculate percentages
- Return dictionary with visualization data

**29. identify_loyal_customers()**

- Find customers with:
    - Most orders
    - Highest total spent
    - Longest membership
- Return top 10 in each category

**30. generate_dashboard_data()**

- Compile key metrics:
    - Total products, customers, orders
    - Today's revenue
    - Pending orders
    - Low stock count
    - Top category
- Return formatted dictionary

***

#### **E. Utility Functions (Bonus)**

**31. export_to_csv()**

- Export products/orders/customers to CSV
- Include all fields
- Use proper formatting

**32. import_from_csv()**

- Bulk import data from CSV
- Validate each row
- Handle errors gracefully

**33. backup_data()**

- Create backup of all JSON files
- Add timestamp to filename
- Compress if needed

**34. validate_pincode()**

- Check if pincode is valid Indian pincode
- Return city and state if available

***

### **Advanced Features:**

#### **1. Dynamic Pricing System**

```python
def calculate_dynamic_price(product_id):
    """
    Adjust price based on:
    - Time of day (night discounts)
    - Stock level (clearance for low stock)
    - Demand (increase for high-demand items)
    - Competition (match competitor prices)
    """
    pass
```


#### **2. Fraud Detection**

```python
def detect_suspicious_orders(order_id):
    """
    Flag suspicious orders based on:
    - Multiple orders from same IP
    - Unusually high order value for new customer
    - Multiple failed payment attempts
    - Shipping address mismatch
    """
    pass
```


#### **3. Personalized Discounts**

```python
def generate_personalized_offer(customer_id):
    """
    Create custom offers based on:
    - Browsing history
    - Cart abandonment
    - Birthday/anniversary
    - Inactive customer (win-back)
    """
    pass
```


#### **4. Inventory Optimization**

```python
def optimize_warehouse_allocation(product_id):
    """
    Suggest warehouse allocation based on:
    - Regional demand patterns
    - Shipping costs
    - Stock levels across warehouses
    """
    pass
```


***

### **Sample Data:**

```python
# Sample Products
SAMPLE_PRODUCTS = [
    {
        'product_id': 'PROD001',
        'name': 'iPhone 15 Pro',
        'category': 'Electronics',
        'price': 134900.0,
        'stock': 50,
        'supplier': 'Apple India',
        'ratings': [4.5, 5.0, 4.8, 4.9],
        'tags': ['smartphone', 'apple', 'premium', '5g'],
        'description': 'Latest iPhone with A17 Pro chip',
        'discount': 5.0,
        'date_added': '2024-01-15'
    },
    {
        'product_id': 'PROD002',
        'name': 'Samsung Galaxy S24',
        'category': 'Electronics',
        'price': 79999.0,
        'stock': 75,
        'supplier': 'Samsung India',
        'ratings': [4.3, 4.5, 4.6],
        'tags': ['smartphone', 'samsung', 'android', '5g'],
        'description': 'Flagship Samsung phone',
        'discount': 10.0,
        'date_added': '2024-02-01'
    },
    # Add 8 more products from different categories
]

# Sample Customers
SAMPLE_CUSTOMERS = [
    {
        'customer_id': 'CUST001',
        'name': 'Rahul Sharma',
        'email': 'rahul@example.com',
        'phone': '+91-9876543210',
        'address': {
            'street': '123 MG Road',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'pincode': '560001'
        },
        'membership': 'Gold',
        'wallet_balance': 5000.0,
        'total_orders': 15,
        'total_spent': 75000.0,
        'wishlist': ['PROD003', 'PROD005'],
        'cart': [],
        'join_date': '2023-06-15'
    },
    # Add 4 more customers
]

# Sample Orders
SAMPLE_ORDERS = [
    {
        'order_id': 'ORD001',
        'customer_id': 'CUST001',
        'products': [
            {
                'product_id': 'PROD001',
                'quantity': 1,
                'price_at_purchase': 128155.0  # After discount
            }
        ],
        'total_amount': 128155.0,
        'discount_applied': 6745.0,
        'payment_method': 'UPI',
        'status': 'Delivered',
        'order_date': '2024-03-15',
        'delivery_date': '2024-03-20',
        'shipping_address': {...}  # Same as customer address
    },
    # Add 4 more orders
]
```


***

### **Test Cases (10 Comprehensive Tests):**

```python
# Test Case 1: Complete Order Flow
"""
1. Register new customer
2. Add products to inventory
3. Customer adds to cart
4. Create order
5. Process payment
6. Update order status to delivered
7. Verify stock deduction
8. Verify customer stats update
Expected: All operations successful, data consistent
"""

# Test Case 2: Low Stock Management
"""
1. Set product stock to 5
2. Create order for 3 units
3. Create another order for 3 units (should fail)
4. Verify low stock alert triggered
Expected: Second order fails, alert generated
"""

# Test Case 3: Membership Upgrade
"""
1. Customer with ₹45,000 total_spent (Silver)
2. Place order for ₹10,000
3. Check if upgraded to Gold
4. Verify discount applied correctly
Expected: Membership upgraded, appropriate discount
"""

# Test Case 4: Order Cancellation & Refund
"""
1. Create order with wallet payment
2. Cancel order
3. Verify wallet refunded
4. Verify stock restored
5. Check order status updated
Expected: Full refund, stock back, status cancelled
"""

# Test Case 5: Search & Filter
"""
1. Search "phone" - should return smartphones
2. Filter Electronics, ₹50k-₹1L, rating > 4.0
3. Verify results match all criteria
4. Test case-insensitive search
Expected: Accurate filtered results
"""

# Test Case 6: Analytics Accuracy
"""
1. Create 10 orders across 5 customers
2. Generate sales report
3. Verify total revenue calculation
4. Check top selling products
5. Validate category performance
Expected: All metrics calculated correctly
"""

# Test Case 7: Bulk Operations
"""
1. Bulk update prices +10% for Electronics
2. Bulk import 20 products from CSV
3. Verify all updates successful
4. Check data integrity
Expected: All products updated, imports successful
"""

# Test Case 8: Edge Cases
"""
1. Order with product ID that doesn't exist
2. Update non-existent customer
3. Delete product that's in pending order
4. Apply expired coupon
Expected: Appropriate error handling, no crashes
"""

# Test Case 9: Recommendations
"""
1. Customer bought Electronics
2. Get recommendations
3. Verify recommendations from same category
4. Check popularity sorting
Expected: Relevant recommendations provided
"""

# Test Case 10: Full System Load Test
"""
1. Load 100 products
2. Register 50 customers
3. Process 200 orders
4. Generate complete dashboard
5. Export all data to CSV
Expected: System handles load, all operations complete
"""
```


***

### **Expected Outputs:**

#### **1. Dashboard Output:**

```
╔══════════════════════════════════════════════════════════╗
║           E-COMMERCE INVENTORY DASHBOARD                 ║
╠══════════════════════════════════════════════════════════╣
║ Total Products:        150                               ║
║ Total Customers:       50                                ║
║ Total Orders:          200                               ║
║ Pending Orders:        15                                ║
║ Low Stock Alerts:      8                                 ║
║                                                          ║
║ TODAY'S METRICS                                          ║
║ ├─ Revenue:           ₹2,45,000                         ║
║ ├─ Orders:            12                                ║
║ └─ Avg Order Value:   ₹20,416                           ║
║                                                          ║
║ TOP CATEGORY: Electronics (₹5,67,000)                   ║
║ TOP PRODUCT:  iPhone 15 Pro (45 sold)                   ║
╚══════════════════════════════════════════════════════════╝
```


#### **2. Invoice Output:**

```
╔══════════════════════════════════════════════════════════╗
║                        INVOICE                           ║
╠══════════════════════════════════════════════════════════╣
║ Order ID:     ORD001                                     ║
║ Customer:     Rahul Sharma                               ║
║ Date:         19-12-2025                                 ║
╠══════════════════════════════════════════════════════════╣
║ ITEMS                                                    ║
║ 1. iPhone 15 Pro                   ₹1,34,900 x 1        ║
║    Discount (5%):                  -₹6,745              ║
║                                                          ║
║ Subtotal:                          ₹1,28,155            ║
║ Membership Discount (Gold 5%):     -₹6,407              ║
║ GST (18%):                         +₹21,894             ║
╠══════════════════════════════════════════════════════════╣
║ TOTAL:                             ₹1,43,642            ║
╠══════════════════════════════════════════════════════════╣
║ Payment Method: UPI                                      ║
║ Status: Confirmed                                        ║
║ Expected Delivery: 24-12-2025                           ║
╚══════════════════════════════════════════════════════════╝
```


***

### **Evaluation Criteria:**

1. **Code Quality (25%)**
    - Clean, readable code
    - Proper naming conventions
    - Docstrings for all functions
    - Type hints (bonus)
2. **Functionality (35%)**
    - All 30+ functions working
    - Error handling
    - Edge cases covered
    - Data validation
3. **Data Structures (20%)**
    - Efficient use of lists, dicts, tuples
    - Proper data modeling
    - Memory optimization
4. **Python Concepts (20%)**
    - Lambda functions
    - Map, filter, sorted
    - List comprehensions
    - String formatting
    - File I/O
    - JSON handling
5. **Bonus Features (+10%)**
    - CLI interface
    - Data visualization
    - Logging system
    - Unit tests
    - Performance optimization

***

### **Deliverables:**

1. **Complete source code** (all .py files)
2. **README.md** with:
    - Project overview
    - Installation \& setup
    - Usage examples
    - API documentation
    - System architecture diagram
3. **Sample data files** (JSON)
4. **Test suite** with all 10 tests
5. **Requirements.txt**
6. **Demo video** (optional, 5-10 minutes)

***

### **Technologies \& Concepts Used:**

✅ **Strings:** Formatting, slicing, methods
✅ **Lists:** CRUD operations, comprehensions, sorting
✅ **Tuples:** Immutable data storage
✅ **Dictionaries:** Complex data structures
✅ **Loops:** for, while, nested loops
✅ **Functions:** Regular, lambda, decorators
✅ **File I/O:** JSON, CSV operations
✅ **Conditionals:** Complex decision making
✅ **Map/Filter/Reduce:** Functional programming
✅ **Error Handling:** try-except blocks
✅ **Date/Time:** datetime module
✅ **Math Operations:** Calculations, statistics





## 🎯 **SIMPLIFIED PROJECT: Library Book Management System**

**Difficulty:** Medium
**Estimated Time:** 4-6 hours
**Uses ONLY:** Lists, Tuples, Dictionaries, Loops, Functions, Strings, Lambda, Map, Filter

***

### **Project Description:**

Create a simple library management system using **only in-memory data structures** (no file I/O, no classes, no imports except basic Python).

***

### **Data Structures:**

#### **1. Books (List of Dictionaries):**

```python
books = [
    {
        'book_id': 'B001',
        'title': 'Python Programming',
        'author': 'John Doe',
        'category': 'Technology',
        'price': 500,
        'copies': 5,
        'issued_copies': 2,
        'ratings': [4, 5, 4, 5]  # List of ratings
    },
    # More books...
]
```


#### **2. Members (List of Dictionaries):**

```python
members = [
    {
        'member_id': 'M001',
        'name': 'Rahul Sharma',
        'age': 25,
        'books_issued': ['B001', 'B003'],  # List of book IDs
        'fine_amount': 50,
        'membership_type': 'Regular'  # Regular, Premium
    },
    # More members...
]
```


#### **3. Transactions (List of Tuples):**

```python
transactions = [
    ('M001', 'B001', 'Issue', '2024-12-01'),
    ('M002', 'B003', 'Return', '2024-12-05'),
    # More transactions...
]
```


***

### **Required Functions (15 Functions):**

#### **Section A: Book Management (5 functions)**

**1. add_book(books, book_id, title, author, category, price, copies)**

```python
"""
Add a new book to the library
- Validate that book_id is unique
- Add book dictionary to books list
- Return success message
"""
```

**Test:**

```python
books = []
result = add_book(books, 'B001', 'Python', 'John', 'Tech', 500, 5)
# Expected: "Book added successfully"
# books list should have 1 book
```


***

**2. search_books(books, search_term)**

```python
"""
Search books by title or author (case-insensitive)
- Use filter() and lambda
- Return list of matching books
"""
```

**Test:**

```python
books = [
    {'book_id': 'B001', 'title': 'Python Programming', 'author': 'John'},
    {'book_id': 'B002', 'title': 'Java Guide', 'author': 'Smith'}
]
result = search_books(books, 'python')
# Expected: [{'book_id': 'B001', ...}]
```


***

**3. get_available_books(books)**

```python
"""
Return list of books that have available copies
- Available copies = total copies - issued copies
- Use filter() and lambda
- Sort by title
"""
```

**Test:**

```python
books = [
    {'title': 'Python', 'copies': 5, 'issued_copies': 2},
    {'title': 'Java', 'copies': 3, 'issued_copies': 3}
]
result = get_available_books(books)
# Expected: [{'title': 'Python', ...}]
```


***

**4. get_top_rated_books(books, n)**

```python
"""
Return top N books by average rating
- Calculate average of ratings list
- Use sorted() with lambda
- Return top n books
"""
```

**Test:**

```python
books = [
    {'title': 'Python', 'ratings': [4, 5, 5]},  # avg: 4.67
    {'title': 'Java', 'ratings': [3, 3, 4]}     # avg: 3.33
]
result = get_top_rated_books(books, 1)
# Expected: [{'title': 'Python', ...}]
```


***

**5. get_books_by_price_range(books, min_price, max_price)**

```python
"""
Filter books within price range
- Use filter() and lambda
- Return sorted by price (ascending)
"""
```

**Test:**

```python
books = [
    {'title': 'Book1', 'price': 300},
    {'title': 'Book2', 'price': 600},
    {'title': 'Book3', 'price': 450}
]
result = get_books_by_price_range(books, 400, 700)
# Expected: [{'title': 'Book3'...}, {'title': 'Book2'...}]
```


***

#### **Section B: Member Management (4 functions)**

**6. register_member(members, member_id, name, age, membership_type)**

```python
"""
Register a new library member
- Validate member_id is unique
- Initialize books_issued as empty list
- Initialize fine_amount as 0
- Add to members list
"""
```

**Test:**

```python
members = []
result = register_member(members, 'M001', 'Rahul', 25, 'Regular')
# Expected: "Member registered successfully"
# members list should have 1 member
```


***

**7. get_members_with_fines(members)**

```python
"""
Return members who have pending fines (fine_amount > 0)
- Use filter() and lambda
- Sort by fine_amount (descending)
"""
```

**Test:**

```python
members = [
    {'name': 'Rahul', 'fine_amount': 50},
    {'name': 'Priya', 'fine_amount': 0},
    {'name': 'Amit', 'fine_amount': 100}
]
result = get_members_with_fines(members)
# Expected: [{'name': 'Amit'...}, {'name': 'Rahul'...}]
```


***

**8. get_member_stats(members)**

```python
"""
Calculate and return statistics:
- Total members
- Premium members count
- Total fines collected
- Average books per member
Return as dictionary
"""
```

**Test:**

```python
members = [
    {'membership_type': 'Premium', 'fine_amount': 50, 'books_issued': ['B1', 'B2']},
    {'membership_type': 'Regular', 'fine_amount': 30, 'books_issued': ['B3']}
]
result = get_member_stats(members)
# Expected: {'total_members': 2, 'premium_count': 1, 'total_fines': 80, 'avg_books': 1.5}
```


***

**9. upgrade_membership(members, member_id)**

```python
"""
Upgrade member from Regular to Premium
- Find member by ID
- Check if already Premium
- Change membership_type to 'Premium'
"""
```

**Test:**

```python
members = [{'member_id': 'M001', 'name': 'Rahul', 'membership_type': 'Regular'}]
result = upgrade_membership(members, 'M001')
# Expected: "Membership upgraded to Premium"
# member's membership_type should be 'Premium'
```


***

#### **Section C: Transaction Management (3 functions)**

**10. issue_book(books, members, transactions, member_id, book_id)**

```python
"""
Issue a book to a member
Steps:
1. Check if book exists and has available copies
2. Check if member exists
3. Check if member already has 3 books (limit)
4. Update book's issued_copies (+1)
5. Add book_id to member's books_issued list
6. Add transaction tuple to transactions list
7. Return success/failure message
"""
```

**Test:**

```python
books = [{'book_id': 'B001', 'copies': 5, 'issued_copies': 2}]
members = [{'member_id': 'M001', 'books_issued': []}]
transactions = []
result = issue_book(books, members, transactions, 'M001', 'B001')
# Expected: "Book issued successfully"
# book's issued_copies should be 3
# member's books_issued should have 'B001'
# transactions should have 1 entry
```


***

**11. return_book(books, members, transactions, member_id, book_id)**

```python
"""
Return a book from member
Steps:
1. Check if member has this book
2. Calculate fine (₹10 per day if overdue - assume 7 days limit)
3. Update book's issued_copies (-1)
4. Remove book_id from member's books_issued
5. Add fine to member's fine_amount if overdue
6. Add transaction tuple
7. Return message with fine details
"""
```

**Test:**

```python
books = [{'book_id': 'B001', 'issued_copies': 3}]
members = [{'member_id': 'M001', 'books_issued': ['B001'], 'fine_amount': 0}]
transactions = []
result = return_book(books, members, transactions, 'M001', 'B001')
# Expected: "Book returned successfully. Fine: ₹0"
# book's issued_copies should be 2
# member's books_issued should be empty
```


***

**12. get_transaction_history(transactions, member_id)**

```python
"""
Get all transactions for a specific member
- Filter transactions list by member_id
- Return list of tuples
"""
```

**Test:**

```python
transactions = [
    ('M001', 'B001', 'Issue', '2024-12-01'),
    ('M002', 'B002', 'Issue', '2024-12-02'),
    ('M001', 'B003', 'Return', '2024-12-03')
]
result = get_transaction_history(transactions, 'M001')
# Expected: [('M001', 'B001', 'Issue', '2024-12-01'), ('M001', 'B003', 'Return', '2024-12-03')]
```


***

#### **Section D: Analytics \& Reports (3 functions)**

**13. generate_library_report(books, members, transactions)**

```python
"""
Generate a formatted string report with:
- Total books in library
- Total available books
- Total members
- Total books issued currently
- Total transactions
- Most issued book (from transactions)

Use string formatting and loops
"""
```

**Test:**

```python
books = [
    {'copies': 5, 'issued_copies': 2},
    {'copies': 3, 'issued_copies': 1}
]
members = [{'member_id': 'M001'}, {'member_id': 'M002'}]
transactions = [('M001', 'B001', 'Issue', '2024-12-01')]

result = generate_library_report(books, members, transactions)
# Expected: Multi-line string with all stats
"""
===== LIBRARY REPORT =====
Total Books: 2
Available Books: 2
Total Members: 2
Books Issued: 3
Total Transactions: 1
==========================
"""
```


***

**14. get_category_statistics(books)**

```python
"""
Return statistics per category:
- Dictionary with category as key
- Value: {'count': X, 'total_copies': Y, 'avg_price': Z}
- Use loops and dictionaries
"""
```

**Test:**

```python
books = [
    {'category': 'Technology', 'copies': 5, 'price': 500},
    {'category': 'Technology', 'copies': 3, 'price': 400},
    {'category': 'Fiction', 'copies': 2, 'price': 300}
]
result = get_category_statistics(books)
# Expected: {
#   'Technology': {'count': 2, 'total_copies': 8, 'avg_price': 450},
#   'Fiction': {'count': 1, 'total_copies': 2, 'avg_price': 300}
# }
```


***

**15. find_overdue_books(members, transactions, current_date)**

```python
"""
Find members with overdue books (issued more than 7 days ago)
Parameters:
- members: list of members
- transactions: list of transaction tuples
- current_date: string in format 'YYYY-MM-DD'

Steps:
1. Filter transactions for 'Issue' type
2. Calculate days difference (simple string comparison or manual calculation)
3. If > 7 days, add to overdue list
4. Return list of tuples: (member_id, book_id, days_overdue)
"""
```

**Test:**

```python
members = [{'member_id': 'M001', 'books_issued': ['B001']}]
transactions = [('M001', 'B001', 'Issue', '2024-12-01')]
current_date = '2024-12-10'  # 9 days later

result = find_overdue_books(members, transactions, current_date)
# Expected: [('M001', 'B001', 9)]
```


***

### **Main Program Structure:**

```python
# Initialize data
books = []
members = []
transactions = []

# Sample data
books = [
    {'book_id': 'B001', 'title': 'Python Programming', 'author': 'John Doe', 
     'category': 'Technology', 'price': 500, 'copies': 5, 'issued_copies': 2, 
     'ratings': [4, 5, 4, 5]},
    {'book_id': 'B002', 'title': 'Data Science Basics', 'author': 'Jane Smith', 
     'category': 'Technology', 'price': 600, 'copies': 3, 'issued_copies': 1, 
     'ratings': [5, 5, 4]},
    {'book_id': 'B003', 'title': 'Fiction Story', 'author': 'Alice Brown', 
     'category': 'Fiction', 'price': 300, 'copies': 4, 'issued_copies': 0, 
     'ratings': [3, 4, 3]},
]

members = [
    {'member_id': 'M001', 'name': 'Rahul Sharma', 'age': 25, 
     'books_issued': ['B001'], 'fine_amount': 50, 'membership_type': 'Regular'},
    {'member_id': 'M002', 'name': 'Priya Singh', 'age': 22, 
     'books_issued': [], 'fine_amount': 0, 'membership_type': 'Premium'},
]

transactions = [
    ('M001', 'B001', 'Issue', '2024-12-01'),
    ('M001', 'B002', 'Issue', '2024-12-03'),
    ('M001', 'B002', 'Return', '2024-12-08'),
]

# Menu-driven program
def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Register Member")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Report")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            # Call add_book with user inputs
            pass
        elif choice == '2':
            # Call search_books
            pass
        # ... other options
        elif choice == '7':
            print("Thank you!")
            break
        else:
            print("Invalid choice")

# Run the program
if __name__ == "__main__":
    main()
```


***

### **6 Test Cases:**

```python
# Test Case 1: Add and search books
def test_case_1():
    books = []
    add_book(books, 'B001', 'Python', 'John', 'Tech', 500, 5)
    add_book(books, 'B002', 'Java', 'Smith', 'Tech', 400, 3)
    
    result = search_books(books, 'python')
    assert len(result) == 1
    assert result[^0]['title'] == 'Python'
    print("✓ Test Case 1 Passed")

# Test Case 2: Issue and return book flow
def test_case_2():
    books = [{'book_id': 'B001', 'copies': 5, 'issued_copies': 0}]
    members = [{'member_id': 'M001', 'books_issued': [], 'fine_amount': 0}]
    transactions = []
    
    issue_book(books, members, transactions, 'M001', 'B001')
    assert books[^0]['issued_copies'] == 1
    assert len(members[^0]['books_issued']) == 1
    
    return_book(books, members, transactions, 'M001', 'B001')
    assert books[^0]['issued_copies'] == 0
    assert len(members[^0]['books_issued']) == 0
    print("✓ Test Case 2 Passed")

# Test Case 3: Member fine calculation
def test_case_3():
    members = [
        {'fine_amount': 50}, 
        {'fine_amount': 100}, 
        {'fine_amount': 0}
    ]
    result = get_members_with_fines(members)
    assert len(result) == 2
    assert result[^0]['fine_amount'] == 100  # Sorted descending
    print("✓ Test Case 3 Passed")

# Test Case 4: Top rated books
def test_case_4():
    books = [
        {'title': 'Book1', 'ratings': [5, 5, 5]},  # avg: 5
        {'title': 'Book2', 'ratings': [3, 4]},     # avg: 3.5
        {'title': 'Book3', 'ratings': [4, 4, 5]}   # avg: 4.33
    ]
    result = get_top_rated_books(books, 2)
    assert result[^0]['title'] == 'Book1'
    assert result[^1]['title'] == 'Book3'
    print("✓ Test Case 4 Passed")

# Test Case 5: Category statistics
def test_case_5():
    books = [
        {'category': 'Tech', 'copies': 5, 'price': 500},
        {'category': 'Tech', 'copies': 3, 'price': 400},
        {'category': 'Fiction', 'copies': 2, 'price': 300}
    ]
    result = get_category_statistics(books)
    assert result['Tech']['count'] == 2
    assert result['Tech']['avg_price'] == 450
    print("✓ Test Case 5 Passed")

# Test Case 6: Issue limit check
def test_case_6():
    books = [
        {'book_id': 'B001', 'copies': 5, 'issued_copies': 0},
        {'book_id': 'B002', 'copies': 5, 'issued_copies': 0},
        {'book_id': 'B003', 'copies': 5, 'issued_copies': 0},
        {'book_id': 'B004', 'copies': 5, 'issued_copies': 0}
    ]
    members = [{'member_id': 'M001', 'books_issued': ['B001', 'B002', 'B003']}]
    transactions = []
    
    result = issue_book(books, members, transactions, 'M001', 'B004')
    assert "limit" in result.lower()  # Should fail due to 3 book limit
    print("✓ Test Case 6 Passed")

# Run all tests
def run_all_tests():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    print("\n✅ All Tests Passed!")
```


***

### **Concepts Used (From Your Syllabus):**

✅ **Strings:** `.lower()`, `.upper()`, slicing, formatting, `in` operator
✅ **Lists:** append, remove, slicing, list comprehensions
✅ **Tuples:** Transaction records
✅ **Dictionaries:** Book, member data structures
✅ **Loops:** `for`, `while`, nested loops
✅ **Functions:** All 15 functions
✅ **Conditionals:** `if/elif/else`
✅ **Lambda:** With filter, sorted
✅ **filter():** Filtering books, members
✅ **map():** Can be used for transformations
✅ **sorted():** Sorting with lambda
✅ **sum():** For calculations
✅ **len():** Counting
✅ **enumerate():** For indexing
✅ **range():** For loops

***

### **Deliverables:**

1. **library_system.py** - All 15 functions implemented
2. **test_library.py** - All 6 test cases
3. **README.md** - Usage instructions and examples
4. **sample_output.txt** - Example program runs

***





