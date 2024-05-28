def string_cover(string):
    new_str=""
    for i in range(len(string)):
        if i % 2 == 0:  #index çiftse
            new_str+=string[i].upper()
        else:
            new_str+=string[i].lower()
    return new_str
    
print(string_cover("hi my name is mine"))
            
