#!/usr/bin/python3

# A function that prints x elements of a list

def safe_print_list(my_list=[], x=0):

    count = 0

    for count in range(x):
        try:
            print(f"{my_list[count]}", end="")
            count += 1
        except IndexError:
            break
    print()
    return(count)
