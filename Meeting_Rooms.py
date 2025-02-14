from typing import List
class interval:
    def __init__(self,start:int,end:int):
        self.start = start
        self.end = end
class solution:
    def meetingrooms1(self,intervals:List[interval]):
        intervals.sort(key = lambda x:x.start)
        can_attend = True
        prev_meeting = intervals[0]
        for meeting in intervals[1:]:
            if meeting.start < prev_meeting.end:
                can_attend = False
                return can_attend
            prev_meeting = meeting
        return can_attend
    
    def meetingrooms2(self,intervals:List[interval]):
        rooms = 0
        start = sorted([meeting.start for meeting in intervals])
        end   = sorted([meeting.end for meeting in intervals])
        j = 0
        i = 0
        max_rooms = 0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                rooms += 1
            else:
                rooms -= 1
                j += 1
            max_rooms = (max_rooms,rooms)
        return max_rooms
            

            

        

    