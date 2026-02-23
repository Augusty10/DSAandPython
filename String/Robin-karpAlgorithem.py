

from ast import pattern
import math as m
from pydoc import text


def simple_hash(s):
    ''' hash = sum of Ascii values of charchters '''
    return sum(ord(ch)for ch in s)

def rabin_karp(text, pattern):
     n, m = len(text), len(pattern)
     results= []

     #Complete hash of pattern and first window 
     pattern_hash= simple_hash(pattern)
     window_hash= simple_hash(text[:m])

     #Slide over the text 
     for i in range(n-m+1):
          #Check hash match 
          if pattern_hash == window_hash:
               #Verify actual match (to handle hash collisions)
               if text[i:i+m] == pattern:
                    results.append(i)
          #Update window hash (remove first char, add last char)
          if i < n-m:
               window_hash = window_hash - ord(text[i]) + ord(text[i+m])
     
     return results

#Example 
text = "AABAACAADAABAAABAA"
pattern ="AABA"
print(rabin_karp(text, pattern))

