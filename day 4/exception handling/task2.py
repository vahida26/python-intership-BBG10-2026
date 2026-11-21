def get_value(my_list,index):
    try:
        return my_list[index]
    except IndexError:
        return None
    
animal=["dog","cat","tiger"]
print(get_value(animal,0))
print(get_value(animal,4))