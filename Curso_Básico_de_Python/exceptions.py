
def divide_elements_on_list(list,divisor):
    try:
        return [i/divisor for i in list]

    except ZeroDivisionError as e:
        print(e)
        return list

list= list(range(10))
divisor=0

print(divide_elements_on_list(list,divisor))