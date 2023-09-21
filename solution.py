def solution(R):
    max_pothole_indicator = 0 
    current_group_depth = 0   
    current_group_size = 0   
    for segment in R:
        if segment == 0:
            max_pothole_indicator = max(max_pothole_indicator, current_group_depth * current_group_size)
            current_group_depth = 0 
            current_group_size = 0   
        else:
          
            current_group_depth = max(current_group_depth, segment)
            current_group_size += 1

   
    max_pothole_indicator = max(max_pothole_indicator, current_group_depth * current_group_size)
    return max_pothole_indicator
