def invert_dict(input_dict):
    output_dict = {}
    
    for key, value in input_dict.items():
        if value not in output_dict:
            output_dict[value] = []
        output_dict[value].append(key)
    
    return output_dict


input_dict = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}

output_dict = invert_dict(input_dict)

print(output_dict)
