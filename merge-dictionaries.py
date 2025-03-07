def input_dictionary():
    dic={}
    while(True):
        key=input("enter key or type exit to stop : ")
        if key.lower() == 'exit':
            break
        value=input("enter value of the key:")
        dic[key]=value
    return dic

def merge_dictionaries(dict1, dict2):
    merge_dic= dict1.copy()
    merge_dic.update(dict2)
    return merge_dic

print("Input User1 Info: ")
usr1dic = input_dictionary()
print("User1 Dictionary: ", usr1dic)


print("Input User2 Info: ")
usr2dic = input_dictionary()
print("User2 Dictionary: ", usr2dic)

merged_result = merge_dictionaries(usr1dic, usr2dic)
print("Merged Users:", merged_result)