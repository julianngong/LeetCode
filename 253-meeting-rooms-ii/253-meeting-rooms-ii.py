import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        endtimesheap = [] # we then only care about the smallest end time
        intervals.sort()
        for interval in intervals:
            if endtimesheap!=[] and interval[0] >= endtimesheap[0]: # if the heap is not empty aka not at the start or mainly for if the start time of the current interval is greater or equal to the earliest end time then we have to remove a room as a meeting can start due to teh earliest finishing meeting being done
                heapq.heappop(endtimesheap)
            #if not then add this end time of this meeting to the heap of the current running meeting end times
            heapq.heappush(endtimesheap,interval[1]) # this will essentially be replacing the old meeting which had expired with the current meeting 
        return(len(endtimesheap)) #the length of the heap at the end are all the meeting rooms which needed to be used. we only add a meeting to the heap if an extra meeting room is needed due to all the curent ones not finishing before it needs to start. each time we decrease one room by popping the list we replace it with a newer one so this is always non decreasing hence lenght of heap is number of rooms needed
                

            
