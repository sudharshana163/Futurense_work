# ------------- Dictionary----------------
import json
# var={"name":"dhoni"}
# print(var)

# adding two dic's

# var={"name":"charu"}
# var1={"age":"44"}
# print(var+var1)            #it throws an error

# another way
# var={"name":"charu"}
# var1={"age":44}
# output=(**var, **var1)        # it gives output as output={"name":"charu","age":44}
# print(output)

#update method
# var={"name":"charu"}
# var1={"age":44}
# var.update(var1)        # it gives output as output={"name":"charu","age":44}
# print(var)

#----------

# var={"name":2,("a,b"):1,6.0:33,True:"q"}    # the things which are immutable they can use as keys in dict
# print(var)
#
# var={[1,2,3]:"chaeyr"}
# print(var)                 # it gives an error like """ unhashable type: 'list' """


# dict are mutable

# var={"name":"chary"}
# var["name"]="sadhana"
# print(var)

# ---------------------

#var={"name":"rama","age":22,"team":"Moghals","born_year":2000}
# var1=dict(sorted(var.items()))      #optimised way
# print(var1)

# keys=[]
# for key in var.keys():
#     keys.append(key)
# print(keys)
# sorted_keys=sorted(keys)
# print(sorted_keys)
#
# sorted_dict={}
# for key_values in sorted_keys:
#     sorted_dict[key_values]=var[key_values]
# print(sorted_dict)

 # comphransive code for sorting dict
#
# sorted_dict={key_values:var[key_values] for key_values in sorted([key for key in var.keys()])}
# print(sorted_dict)

# ---------
# sort() and sorted()

# sort()
#var=["ramadevi","na","chary","sudharshana","sai"]
# var.sort()
# print(var)

#sorted()
# var=["ramadevi","na","chary","sudharshana","sai"]
# output=sorted(var,reverse=True,key=len)
# print(output)

# ---------
# var='{"name":"chary","age":33}'
# # var_dict=json.loads(var)
# # print(var_dict)
#
# var_dict=json.dumps(var)
# print(var_dict)
# print(type(var_dict))

# ------------------
#removing last data in list and dict
#dict
#var={"name":"chary","age":33}
# var.popitem()
# print(var)     # it gives the output as {"name":"chary"}

#list
# list=["name","age","team"]
# list.pop()
# print(list)



# -- bangels project-------

def string_compare(secret_string, guess_string):
    exclude = []
    output = []
    if secret_string == guess_string:
        return 'You guessed it right'
    for i in range(len(secret_string)):
        if secret_string[i] == guess_string[i]:
            output.append('Fermi')
            exclude.append(i)
    for i in range(len(secret_string)):
        if i not in exclude:
            for char in secret_string:
                if guess_string[i] == char:
                    output.append('Pico')
                    exclude.append(i)
                    break
    if len(output) == 0:
        output.append('bagels')
    return output


import random


# def

def start_bagels():
    # x = int(input('Enter number of digits of secret number: ')) # len of secret number
    print("""Game Rules:
 When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.""")
    x = 3
    secret_number = random.randrange(10 ** (x - 1), 10 ** (x), x)
    print('I have decided the secret number you have 10 guess.')
    num_guess = 1
    while num_guess <= 10:
        guess_number = input('Enter 3 digit number: ')
        sc = string_compare(str(secret_number), guess_number)
        if sc == 'You guessed it right':
            print(sc)
            break
        else:
            print(sc)
            num_guess += 1
    else:
        print('You turn is up, I won and the secret number is: ', secret_number)


start_bagels()