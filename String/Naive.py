#Naive Approch 

from ast import pattern


def naive_approch(text, pattern):
    n= len(text)
    m= len(pattern)
    result =[]

    for i in range(n-m+1):    #possible shifts 
        j=0
        while(j<m) and text [i+j]== pattern[j]:
            j +=1
            if j ==m:            #full match 
                result.append(i)
                return result
text = "AABAACAADAABAAABAA"            
pattern = "AABA"
print("Naive matches at indices: ", naive_approch(text, pattern))