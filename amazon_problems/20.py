# trapping_rain_water

'''
the first and last bars cannot trap any water becuase they do not have boundaries on both sides

> ideally, we want get the maximum value on the left side and the maximum value on the right side of the current unit
> why max value of both right and left side, because  these both will act potential boundaies to trap the water
> once we have left_max and right_max for a bar at index i, the water level that can be sustained above this bar 
is limited by the shorter of these two maximum heights: min(left_max, right_max)
>If this water_level is greater than the height of the current bar (height[i]), it means water can be trapped. 
The amount of water trapped above this bar is the difference between the water_level and the height[i]: water_level - height[i]

'''
def trapping_water(height):
    if not height:
        return 0 #if the input list is empty, no water can be trapped
    
    n = len(height) # gets the number of bars in the elevation map
    trapped_water = 0 # initialize a variable to store the total amount of trapped water
    
    # iterate through each bar in the elevation map, excluding height of bars to left and right of the current bar
    for i in range(1, n-1):
        # initialize variables to find the maximum height of bars to the left and right
        left_max = 0
        right_max = 0
        
        # find the max height of the bars to the left of the current bar
        for j in range(i):
            left_max = max(left_max, height[j])
        
        # find the max height of the bars to the right of the current bar
        for j in range(i+1, n):
            right_max = max(right_max, height[j])
        
        # The amount of water that can be held above the current bar is determined by the
        # shorter of the tallest bars on its left and right. This forms the "water level"
        water_level = min(left_max, right_max)
        
        # If the calculated water level is higher than the current bar's height,
        # then water can be trapped above it
        if water_level > height[i]:
           # The amount of water trapped above the current bar is the difference
            # between the water level and the height of the current bar
            trapped_water += water_level - height[i]
    return trapped_water 