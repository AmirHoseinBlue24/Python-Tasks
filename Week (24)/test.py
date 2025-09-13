def count_pairs(arr):
    count = 0
    for i in arr:
        for j in arr:
            count += 1
    return count

# تست
nums = list(range(10000))  # 1000 عنصر
print(count_pairs(nums))
