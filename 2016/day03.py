# TO DO
# Deal with p2 input problems since all numbers are not the same amount of characters.
# fix p2 data processing


from aoc_utils import data_import

raw_data = data_import.get_input()
# data_import.preview()

test_data = """5  10 25
2  2  2"""
    
test_data_p2 = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403  03"""

def valid_triangle(triangle:list) -> bool:
    s1 = int(triangle[0])
    s2 = int(triangle[1])
    s3 = int(triangle[2])
    
    if s1 + s2 <= s3:
        return False
    elif s1 + s3 <= s2:
        return False
    elif s2 + s3 <= s1:
        return False
    else:
        return True

def data_prep(raw_data):
    triangles = raw_data.splitlines()
    for i, triangle in enumerate(triangles):
        triangle_cleaned = [char for char in triangle.split(" ") if char != ""]
        triangles[i] = triangle_cleaned
    return triangles

def main_p1(data):
    possible_triangle_count = 0
    for triangle in data:
        if valid_triangle(triangle):
            possible_triangle_count += 1
    print(possible_triangle_count)
        

def main_p2(raw_data):
    triangles = []
    data = raw_data.splitlines()

    for i, num in enumerate(data):
        num_cleaned = [char for char in num.split(" ") if char != ""]
        data[i] = num_cleaned
    print(data)
    
    for row in range(0, len(data), 3):
        triangle = []
        for col in range(0, 3):
            print(row, col)
            triangle.append(data[row][col])    
        triangles.append(triangle)
    # print(triangles)
    
    

if __name__ == "__main__":
    data = data_prep(raw_data)
    # main_p1(data)
    main_p2(test_data_p2)   
