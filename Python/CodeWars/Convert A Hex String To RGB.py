def hex_string_to_RGB(hex_string): 
    rgb_vals = [int(hex_string[i: i+2], 16) for i in range(1, 7, 2)]
    return {x : rgb_vals[i] for i, x in enumerate(['r', 'g', 'b'])}

print(hex_string_to_RGB("#FF9933"))