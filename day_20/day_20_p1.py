from tqdm import tqdm

with open("./day_20.in") as fin:
    lines = fin.read().strip().split("\n")
    nums = list(enumerate(map(int, lines)))


n = len(nums)
og = nums.copy()


def swap(nums, a, b):
    assert (0 <= a < n) and (0 <= b < n)

    nums[a], nums[b] = nums[b], nums[a]
    return nums


for i, x in tqdm(og):
    for idx in range(n):
        if nums[idx][0] == i:
            break

    assert nums[idx][1] == x

    if x < 0:
        cur = idx
        for _ in range(-x):
            nums = swap(nums, cur, (cur - 1) % n)
            cur = (cur - 1) % n

        continue

    if x > 0:
        cur = idx
        for _ in range(x):
            nums = swap(nums, cur, (cur + 1) % n)
            cur = (cur + 1) % n


coords = [1000, 2000, 3000]

ans = 0
for zero_idx in range(n):
    if nums[zero_idx][1] == 0:
        break

for c in coords:
    ans += nums[(zero_idx + c) % n][1]

print(ans)
