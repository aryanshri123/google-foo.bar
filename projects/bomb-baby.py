def solution(x, y):
  # general strategy:
  # reduce down to 1, 1
  x = int(x)
  y = int(y)
  count = 0
  while x + y > 2:
      if x == 1:
          return str(count + (y-1))
      elif y == 1:
          return str(count + (x-1))
      if x % y == 0 or y % x == 0:
          return 'impossible'
      if x > y:
          factor = int(x/y)
          x -= factor * y
          count += factor
      elif x < y:
          factor = int(y/x)
          y -= factor * x
          count += factor
      else:
          return 'impossible'
  return str(count)

