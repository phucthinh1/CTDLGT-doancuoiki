def sap_xep_chon(nums):
    for i in range(len(nums)):
        so_nho_nhat = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[so_nho_nhat]:
                so_nho_nhat = j
        nums[i],nums[so_nho_nhat] = nums[so_nho_nhat],nums[i]


cho_so = [18,4,19,8,12]
sap_xep_chon(cho_so)
print(cho_so)

