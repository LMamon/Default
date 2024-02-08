#Define a function called wrap_string(), the function should return a copy of str with n number of '<' and '>' prepended and appended to it, respectively.
#Example:

#Input: wrap_string("Pearl", 3)
#Output: "<<<Pearl>>>"

def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"
  return result
# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)