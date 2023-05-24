def sap_xep_chen(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        phan_tu_chen = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > phan_tu_chen:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = phan_tu_chen


# Verify it works
chon_so = [9, 1, 15, 28, 6]
sap_xep_chen(chon_so)
print(chon_so)
