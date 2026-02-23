 # Check Anagram 

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False 
    #Convert frequency yof charcters  manually 
    count1={}
    count2={}
    for char in str1:
        count1[char]=count1.get(char, 0)+1

    for char in str2:
        count2[char]=count2.get(char, 0)+1

    return count1 == count2 
# Example usage 
str1 = "Listen"
str2 = "Silent"

print(is_anagram(str1, str2))
