def computeBinary(digit, result):
  if (digit == 0):
    return result

  result = str(digit % 2) + result
  return computeBinary(digit // 2, result)

if __name__ == '__main__':
  result = computeBinary(200, "")
  print(result)
