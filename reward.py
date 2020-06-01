def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    
    # initial 
    reward = 1e-3
    
    if progress == 100:
        reward += 20
    
    # Calculate 5 markers that are at varying distances away from the center line
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_0:
        reward += 1.0
    elif distance_from_center <= marker_1:
        reward += 0.5
    elif distance_from_center <= marker_2:
        reward += 0.25
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 0.001  # likely crashed/ close to off track

    if all_wheels_on_track:
        reward += speed*0.05
    else:
        reward -= speed*0.05

    if is_offtrack:
        # penalty if off track
        reward = 1e-3
    else:
        # Give higher reward if the car is fast, but stay center still more important
        reward += speed*0.125
    
    
    return float(reward)
