class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x=[]
        for n in range(1, n+1):
            if n%3 ==0 and n%5 == 0:
                x.append("FizzBuzz")
            elif n%3 == 0:
                x.append("Fizz")
            elif n%5 == 0:
                x.append("Buzz")
            else:
                x.append(str(n))
                
        return x