class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=max(len(a),len(b))
        a, b = a.zfill(n),b.zfill(n)
        carry=0
        output=''
        for i in range(n-1,-1,-1):
            if int(a[i])+int(b[i])+int(carry)==3:
                output = '1' + output 
            elif int(a[i])+int(b[i])+int(carry)==2:
                output = '0'+output
                carry=1
            elif int(a[i])+int(b[i])+int(carry)==1:
                output = '1'+output
                carry=0
            else:
                output = '0'+output
        if carry==1:
            output = '1'+output
        return(output)
            

