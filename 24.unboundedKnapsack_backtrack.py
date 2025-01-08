#time and space complexity same as 0/1 knapsack
from typing import List

def outer(n: int, W: int, values: List[int], weights: List[int]) -> int:
    res = []
    profit = 0
    weights_added = []

    def recFunc(i, profit):
        if i >= n:
            res.append(profit)
        else:
            # Exclude the current item and move to the next
            recFunc(i + 1, profit)
            # Include the current item (stay on the same index for unbounded knapsack)
            if sum(weights_added) + weights[i] <= W:
                weights_added.append(weights[i])
                profit += values[i]
                recFunc(i, profit)
                profit -= values[i]
                weights_added.pop()

    recFunc(0, profit)
    return max(res)

# Test the function
print(outer(2,50,[4, 2],[3, 1]))  # Expected output: 12
