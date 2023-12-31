import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

min_val = 200000000000000
max_val = 400000000000000
point_data = []
for line in lines:
    point_data.append([])
    for data in line.split('@'):
        vector = []
        for num in data.strip().split(','):
            vector.append(int(num))
        point_data[-1].append(tuple(vector))
    point_data[-1] = tuple(point_data[-1])

def get_intersection(p1,p2,p3,p4):
    denom = (p1[0] - p2[0])*(p3[1] - p4[1]) - (p1[1] - p2[1])*(p3[0] - p4[0])
    x_num = (((p1[0]*p2[1]) - (p1[1] * p2[0]))*(p3[0] - p4[0])) - ((p1[0] - p2[0]) * ((p3[0]*p4[1]) - ((p3[1]*p4[0]))))
    y_num = (((p1[0]*p2[1]) - (p1[1] * p2[0]))*(p3[1] - p4[1])) - ((p1[1] - p2[1]) * ((p3[0]*p4[1]) - ((p3[1]*p4[0]))))
    return (x_num/denom, y_num/denom)

num_collisions = 0
for i in range(len(point_data)):
    p,v1 = point_data[i]
    p1 = p[:2]
    p2 = (p1[0] + v1[0], p1[1] + v1[1])
    for j in range(i + 1, len(point_data)):
        p,v2 = point_data[j]
        p3 = p[:2]
        p4 = (p3[0] + v2[0], p3[1] + v2[1])
        try:
            x,y = get_intersection(p1,p2,p3,p4)
            right_direction_x = (x < p1[0]) == (v1[0] < 0) and (x < p3[0]) == (v2[0] < 0)
            right_direction_y = (x < p1[1]) == (v1[1] < 0) and (x < p3[1]) == (v2[1] < 0)
            if min_val <= x <= max_val and min_val <= y <= max_val and right_direction_x:
                num_collisions += 1
        except ZeroDivisionError:
            continue
print(num_collisions)