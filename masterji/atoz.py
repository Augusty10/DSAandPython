class Solution(object):
    def minTimeToType(self, word):
        time = 0
        current = 'a'
        
        for char in word:
            diff = abs(ord(char) - ord(current))
            move = min(diff, 26 - diff)
            time += move + 1   # +1 for typing
            
            current = char
        
        return time