nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nums1)
print(nums2)

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]==nums2[j]:
            print(nums2[j+1])