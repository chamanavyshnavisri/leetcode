class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        gre=defaultdict(lambda:-1)
        for i in nums2:
            while st and st[-1]<i:
                gre[st.pop()]=i
            st.append(i)
        res=[]
        for j in nums1:
            res.append(gre[j])
        return res


        
        