from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        #pick one skip and keep doing that#skip? because we pop out
        #dont spend time calculating mis, going over it and reversing the order in case of odd or even

        trackIndex=[i for i in range(len(deck))]
        dq=deque(trackIndex)
        res=[0 for _ in range(len(deck))]

        for card in deck:
            res[dq.popleft()]=card
            if dq:
                dq.append(dq.popleft())
        return res


