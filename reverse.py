class Solution(object):
    def reverseWords(self, s):
        s =list(s)     #to convert string into list because strings are immutable 
        n = len(s)
        i = 0 

        while i < n :
            while i < n and s[i] == " ":
                i +=1 
            start = i 

            while i < n and s[i]!=  " ":
                i +=1 
            end = i - 1


            while start < end  :
                s[start] , s[end] = s[end] , s[start]
                start +=1 
                end -=1 
        
        return "".join(s)   #used to convert list back into the string 

        