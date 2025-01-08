'''
When using bitwise operators in Python, the following sequence happens:

Binary Representation for Operations: Python temporarily works with the binary (bit-level) representation 
of the integers during the operation.This allows bitwise operators like &, |, ^, <<, and >> to
manipulate the individual bits directly.

Immediate Return to Decimal Representation: Once the operation is complete, Python immediately returns 
the result as a regular integer in decimal form. So, even though the bit manipulation happens in binary form,
Python displays and stores the result as a standard integer.

This process is seamless, so you don't have to manually convert integers to binary or back to decimal. 
Python handles everything internally, making it efficient and user-friendly for bitwise operations.

'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        i=0
        while n!=0 :
            curr=n&1
            res=res | curr<<31-i
            i+=1
            n=n>>1
        return res

