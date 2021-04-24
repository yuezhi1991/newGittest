class Solution(object):
    def findContentChildren(self, g, s):
        sorted_g=sorted(g)
        sorted_s=sorted(s)
        
        max_content=0
        j_left_pointer=0
        i=0
        j=0
        while(i<len(g) and j<len(s) and j>=j_left_pointer):
            if sorted_g[i]<=sorted_s[j]:
                max_content=max_content+1
                j_left_pointer=j+1
                j=j+1
                i=i+1
            elif sorted_g[i]>sorted_s[j]:
                j=j+1
                
        return(max_content)
