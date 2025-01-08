def eraseOverlapIntervals(intervals):
    intervals.sort(key= lambda item: item[1])
    #sort the intervals in ascending order of end limit to save shorter range 
    prev_end=float('-inf')
    remove_count=0
    for item in intervals:
        if item[0]<prev_end:
            remove_count+=1#removing the one that has largest range
        else:
            prev_end=item[1]
    
    return remove_count

print(eraseOverlapIntervals([[1, 4], [2, 5], [5, 6], [3, 4]]))
    

    