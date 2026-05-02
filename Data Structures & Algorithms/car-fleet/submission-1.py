class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)),key=lambda x: x[0])
        road_arrivals = [(target-p)/s for p,s in cars]
        for i in range(len(road_arrivals)-2,-1,-1):
            if road_arrivals[i] < road_arrivals[i+1]:
                road_arrivals[i] = road_arrivals[i+1]
        return len(set(road_arrivals))
