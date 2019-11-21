#hello world exmple.
# print("Priyankit")
# print('0----')
# print(' ||||')
# print('*' * 10)

#Data types.
# price=10
# rating=4.5
# name='priyankit'
# is_published=False
# print(price.__str__()+ name)

#Excersize- Take input in colose

# full_name=input('Please enter your name ? ')
# print('Hi '+full_name)
# fav_color=input('Wnat is your fav color ? ')
# print('Hey '+full_name+', your fav color is '+fav_color)

# Type conversion

# birth_year=input('Birth year? ')
# #age=2019-birth_year
# print(type(birth_year))#type return data type
# age=2019-int(birth_year)
# print(type(age))
# print(age)


#Playing with long string

# text='''
# yes hello 'priyankit'
#
# "Whats up"
#
#
# '''
#
# print(text)


#getting string index using 0 to positive from Left to right and -1 to negative if want to use Index right to left

# text='Hello, Priyankit'
# print(text[0] + text[-1])
#
# #sub string
# print (text[0:5])
#
# #Formatted string HCL [Technology] is best
#
# first='HCL'
# last='Technology'
# print(first+ '['+last+' ] '+ 'is best')
#
# print(f'{first} [{last}] is best')
#
# #check the length
# print(len(first))
# print(first.upper())
# print(first.find('C'))

#44.38

# dealing with Int and float

# print(2+2)
#
# print (10/3)
#
# print (10//3) # return only integer part

# modulus return remainder of division.
#print (10%3)
# exponent as power use double star

#print(2**2)

#augmented assignment operator
# x=10
# x=x+10
#
# print(x)
#
# # use it as
#
# y=10
# y+=10
# print(y)

# print (round(4.55))
# print (abs(-4.55 ))

############################### Module section ############
# import Modules
#
# lbs_value=Modules.kilogram_to_lbs(100)
# print(lbs_value)

#import directly the function and use without reference.
import  Modules
from Modules import kilogram_to_lbs


print(kilogram_to_lbs(100))





