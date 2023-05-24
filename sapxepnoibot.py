def sap_xep_noi_bot(nums):
    chuyen = True
    while chuyen:
        chuyen = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                chuyen = True


# Verify it works
chon_so = [5, 2, 1, 8, 4]
sap_xep_noi_bot(chon_so)
print(chon_so)
