class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        for front in range(len(numbers)-1):
            if numbers[front]!=numbers[front-1]:
                back=front+1
                while back<len(numbers):
                    if numbers[front]+numbers[back]==target:
                        return([front+1,back+1])
                    elif numbers[front]+numbers[back]<target:
                        back+=1
                    else:
                        back=len(numbers)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front=0
        back=len(numbers)-1
        while front<back:
            if numbers[front]+numbers[back]==target:
                return([front+1,back+1])
            elif numbers[front]+numbers[back]<target:
                front+=1
            else:
                back-=1

                