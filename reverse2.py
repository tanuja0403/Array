class Solution(object):
    def reverseWords(self, s):
        s = list(s)
        n = len(s)
        i = 0
        j = len(s)-1

        while i < j :
            s[i] , s[j] = s[j] , s[i]
            i +=1 
            j -=1 
        # return "".join(s)
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
        res = "".join(s)
        return " ".join(res.split())
       