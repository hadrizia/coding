pos = input().split()
pos = [int(x) for x in pos]

LEN_WINDOW = 200

pos.sort()

offset_1_end = pos[0] + LEN_WINDOW
offset_2_end = pos[1] + LEN_WINDOW
offset_3_end = pos[2] + LEN_WINDOW

used_area = LEN_WINDOW
if offset_1_end != offset_2_end or offset_2_end != offset_3_end:

  if pos[1] < offset_1_end:
    used_area += offset_2_end - offset_1_end
  else:
    used_area += LEN_WINDOW
  if pos[2] < offset_2_end:
    used_area += offset_3_end - offset_2_end
  else:
    used_area += LEN_WINDOW
    
print(60000 - (used_area * 100))
