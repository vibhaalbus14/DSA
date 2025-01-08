def outer(cost):
    res = []
    helper = []

    def climbFrom(index):
        nonlocal res, cost
        if index == len(cost):
            res.append(sum(helper))
            return
        if index > len(cost):
            return
        
        for i in range(1, 3):  # Correct the range to be 1 and 2 steps
            if index + i <= len(cost):  # Ensure we don't go out of bounds
                helper.append(cost[index])
                climbFrom(index + i)
                helper.pop()

    climbFrom(0)  # Start from step 0
    climbFrom(1)  # Start from step 1
    
    return min(res)


cost = [10, 20, 30]
print(outer(cost))  
