#iterate through text and set a variable match_count equal to 0.

#Then, for each index of the text, iterates through the pattern to check for matching characters.
#If found, increments match_count. Otherwise, the search breaks the pattern iteration and moves onto the next index in text.

#Each time the pattern iteration is completed, the match_count is compared to the length of the pattern to determine if a match is found.

def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0
    for char in range(len(pattern)):
      print("Pattern Index:", char)
      if pattern[char] == text[index + char]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)