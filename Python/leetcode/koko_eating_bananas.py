def cal_time(speed, piles):
       time=0
       for pile_size in piles:
                     time+=(pile_size+speed-1) // speed
       return time

def minEatingSpeed(piles, h):
       low = 1
       high = max(piles)
       ans = max(piles)
       while low<=high:
              mid = (low+high)//2
              time_taken = cal_time(mid, piles)
              if time_taken > h:
                     low = mid + 1
              else:
                     ans = mid
                     high = mid-1
       return ans
