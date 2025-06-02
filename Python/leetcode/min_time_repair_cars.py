def repairCars(ranks, cars):
    def can_repair(time):
        total_cars_repaired = 0
        for rank in ranks:
            cars_by_mechanic = int((time / rank) ** 0.5)
            total_cars_repaired += cars_by_mechanic
        
        return total_cars_repaired >= cars
    left = 1  
    right = min(ranks) * cars * cars  
    
    while left < right:
        mid = (left + right) // 2
        if can_repair(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
