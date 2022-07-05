nums1 = input().split()
nums2 = input().split()
s = set(nums1)
s1 = list()
for i in s:
    if i in nums2:
        s1.append(i)
print(s1)