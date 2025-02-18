# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0 for i in range(n)]

        for start, end, seats in bookings:
            answer[start - 1] += seats
            if end < n:
                answer[end] -= seats
        
        for i in range(1, n):
            answer[i] = answer[i - 1] + answer[i]
        
        return answer