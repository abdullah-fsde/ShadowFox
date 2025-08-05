def arguments(number,type):
    return format(number,type)#changes the format of the number in octal form as we passed argument as 'o' for change
a = arguments(145,'o')
print(f"The resultant formatted ouput is : {a}")