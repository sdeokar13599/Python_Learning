import os
# name=input("Enter you name")
# print("Hello",name)

# code uppercase or lowercase the string the string--.

# name='sHubham'
# choice=input("Enter what u want to ")

# def c_upper(name):
#     print(name.upper())

# def c_lower(name):
#     print(name.lower())   

# if choice=='u':
#     c_upper(name)
# else:
#     c_lower(name)



##Write a code to work on how many digit,alphbet and special charcter present in string also print them


# Message="S1@h3# "

# alpha_count=0
# num_count=0
# spl_count=0



# for word in Message:
#     if word.isalpha():
#         alpha_count+=1
#     elif(word.isdigit()):
#         num_count+=1
#     else:
#         spl_count+=1


# print(alpha_count)   
# print(num_count)   
# print(spl_count)



         
#####   Write a code to find the occurance of chacter in given chacrcter in the given string  ######

# Name='aaabbbcc'
# count_dict={}

# for word in Name:
#     if word in count_dict:
#         count_dict[word]+=1
#     else:
#         count_dict[word]=1



# print("Printing the occurance of char in the string")
# for key,values in  count_dict.items():
#     print(key,values)


### Write a python code to give print a2b3c1   o/p should be aabbbc

# input_string="a2b3c1"
# output_string=""



# for i in input_string:
#     if (i.isalpha()):
#         char=i
#     else:
#         count=int(i)
#         output_string+=char*count

# print(output_string)


        

##Write program to replace charcter from the string with another word


# Original_word="Hello Shubham,How are you Bhai"
# replace_word=input("Enter the word u want to replace it with")
# substitute_word=input('Enter the Subtitute word u wnat to enter')

# print("Out")
# print(Original_word.replace(replace_word,substitute_word))

#Write prgramm to find out count of vowles in the string

# vowles=['a','e','i','o','u']

# Demo="Sahebihoau"
# v_count=0

# for i in Demo:
#     if i in vowles:
#         v_count+=1

# print(v_count)        


# #Write prgramm to find out count of vowles each  in the string

# vowles=['a','e','i','o','u']
# v_count={}

# Demo="Sahebihoau"

# for i in Demo:
#     if (i in vowles and i in v_count):
#         v_count[i]+=1
#     elif(i in vowles):
#      v_count[i]=1


# for key,values in v_count.items():
#    print(key,values)


        
        
##Write a Programm to reverse a sring 

# demo="Shubham"
# print(demo[::-1])

#String Slicing--->
# demo="Shubham"
# print(demo[0:4])  # 0 is exclusive and  4 is inclusive

##anagram means sorted comparison and reverse means reverse comparision
# str1 = "listen"
# str2 = "silent"

# if(sorted(str1)==sorted(str1)):
#     print("Anagrm")
# else:
#     print("It is not an anagram")    

#above string is anagram 

###Palindrome code

# Demo="madam"

# if(Demo==Demo[::-1]):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")    


# ##Capitalize the first letter of the string 

# Demo="hello my name is shubham deokar"

# print(Demo.title())



## Wirte a code to remove the duplicates from string 

# Demo="aabbccdd"
# demo2=""

# for char in Demo:
#     if char not in demo2:
#         demo2+=char

# print(demo2)


#Replace all spaces in a string with a given character (e.g., “%20”).

# Name="My Name is Shubham "
# repl=Name.replace(" ","%2D")
# print(repl)


## complete the string once then start on other conepts once this is done.

        










