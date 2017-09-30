area_cent = float(input())
area_meters = area_cent * 100
bed_length = 25
bed_width = 15

free_area = int(area_meters - (bed_length * bed_width))

print(free_area) if free_area > 0 else print(0)