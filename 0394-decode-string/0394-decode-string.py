class Solution:
    def decodeString(self, s: str) -> str:
        st1=[]
        for i in s:
            if i!=']':
                st1.append(i)
            else:
                curstr=""
                while st1[-1]!='[':
                    curstr=st1.pop()+curstr
                st1.pop()
                curr_num = ""
                while st1 and st1[-1].isdigit():
                    curr_num = st1.pop() + curr_num
                curstr = int(curr_num) * curstr
                st1.append(curstr)

        return "".join(st1)
                
                
            

        