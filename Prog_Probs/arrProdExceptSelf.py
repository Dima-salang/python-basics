def productExceptSelf(nums):
        answer = []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        answer = [prod for num in range(len(nums))]
        print(answer)
        for i in range(len(answer)):
            answer[i] *= (1/nums[i])
            
        
        return answer


print(productExceptSelf(nums=[1, 2, 3, 4])) 