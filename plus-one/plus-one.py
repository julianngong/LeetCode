class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i=len(digits)
        while i>0 and ( carry == 1):
            i=i-1
            if digits[i]+carry<10:
                digits[i]=digits[i]+carry
                carry=0
            elif digits[i]+carry==10:
                digits[i]=0
                carry=1
            else:
                digits[i]=1
                carry=1
            print(digits)
            print('carry ',carry)
        if carry ==1:
            digits.insert(0, 1)
        return(digits)
            