# %%
import aocd

data = aocd.get_data(day=1, year=2015)
data

# %%
left_count = data.count('(')
right_count = data.count(')')

print(left_count - right_count)

# %%
position = 1
floor = 0

for char in data:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    
    if floor < 0:
        print(position)
        break

    position += 1

print(position)

# %%



