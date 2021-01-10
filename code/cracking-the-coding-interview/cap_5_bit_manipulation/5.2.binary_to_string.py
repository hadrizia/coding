def float2bin(n):
  if n == 0:
    return [0]

  res = []
  while n != 1 and len(res) < 24:
    prod = n * 2
    n = prod - 1 if prod > 1 else prod
    res.append(int(prod // 1))
  
  if len(res) == 24:
    raise NameError("ERROR")
  else:
    return res

def binary_to_str(n):
  bits = []
  bits.append(".")
  bits_float_part = float2bin(n)
  bits.extend(bits_float_part)
  return ''.join(str(i) for i in bits)

def tests():
  assert binary_to_str(0.75) == ".11"
  assert binary_to_str(0.50) ==  ".1"
  assert binary_to_str(0.25) == ".01"
  try:
    binary_to_str(0.275)
  except:
    print("Raising expected exception: Can't exceed more than 32 bits")
    
if __name__=="__main__":
  tests()