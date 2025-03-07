def input_dictionary():
    dic={}
    while(True):
        key=input("enter key or type exit to stop : ")
        if key.lower() == 'exit':
            break
        value=input("enter value of the key:")
        dic[key]=value
    return dic


usrdic = input_dictionary()
print("Your Dictionary: ", usrdic)


