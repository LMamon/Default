#Define a function called move_to_end() that accepts two arguments: lst and val.
#The function should return a copy of lst with every instance of val moved to the end of the list.

def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return []

  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)
  return result

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))