entries = input().split()
entries = [float(x) for x in entries]

alcohol_cost = entries[2] / entries[0]
gas_cost = entries[3] / entries[1]

print(gas_cost, alcohol_cost)
if gas_cost >= alcohol_cost:
  print('G')

else:
  print('A')