# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(w1, w2):
  if(sorted(w1)== sorted(w2)):
    print('True.')
  else:
    print('False.')

w1 ="coronavirus"
w2 ="carnivorous"
find_anagram(w1, w2)
  

