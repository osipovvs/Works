area_cent = float(input())
area_meters = area_cent * 100
bed_length = 25
bed_width = 15
bed_area = bed_length * bed_width

free_area = int(area_meters % bed_area)

print(free_area)