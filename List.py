# Python lists are:

# Ordered: Items retain their sequence and can be accessed via zero-based indices.

# Mutable: You can modify, add, or remove elements after creating the list.

# Allow duplicates and can contain mixed data types—even other lists.

# They grow and shrink dynamically to fit your data.

#list=[1,2,3,4,5,6]
# print(list[0])
#print(list[-1])

# # for i in list:
# #     print(i)

# Creating lists with different types

# fruits = ["apple", "banana", "cherry"]
# mixed = [1, "hello", 3.14, False, [1, 2, 3]]
# print(mixed)

# #print(fruits)

# ##Modify the exisisting elemenst
# nums=[1,2,3,4,5,6]

# # nums[2]=5

# # print(nums)

# nums.insert(3,5)  # required inedex and value
# nums.append(7)  # it will going to add at the last
# print(nums)
# nums.extend([10,11,12])
# print(nums)


# #Write a programm to revers a list 

# a =[1,2,4,5,6]
# print(a[::-1])


# ##Write a programm to max and min element in the list 

# a=[1,2,3,5,6]
# print(max(a))
# print(min(a))

##Write a code to find out the occurance of elements inside the list

# list_1=[1,1,2,2,3,3,4]

# for x in set(list_1):
#     print(x,":",list_1.count(x))

##inbuid method inside the list which will help to get the count of each element.

##Write a code to remove the duplciate elements from the list 

# list_1=[1,1,2,2,3,3,4]
# print(list(set(list_1)))

###Write a Programm to merge two list

# list_1=[1,2,3]
# list_2=[4,5,6]

# list_3=list_1+list_2
# print(list_3)

##Write a programm find even and odd numbers from list.(using normal method)

# list_a=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]

# for i in list_a:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even",even)
# print("Odd",odd)           
## List comprehension(we can  create list from one list uisng below technique)
# list_a=[1,2,3,4,5,6,7,8,9,10]
# list_c= [x for x  in list_a]
# print(list_c)

##Write a programm to find the square of numbers in list

# list_a=[1,2,3,4,5,6,7,8,9,10]
# list_sq=[x**2 for x in list_a]
# print(list_sq)


##Write a programm to find even and odd numbers uisng List Comprehension

# list_a=[1,2,3,4,5,6,7,8,9,10]
# even=[x for x in list_a if x%2==0]
# odd=[x for x in list_a if x%2!=0]
# print(even)
# print(odd)



# ##Find the second largest number in the String

# list_a=[1,2,3,4,5,6,7,8,9,10]
# print(list_a[-2])

# #falttern the list

# list_a=[[1,2],[3,4],[5,6]]
# list_flat=[x for sub in list_a for x in sub]
# print(list_flat)

# #Extract numbers from a string into a list
# text = "Customer123 has 4 orders and 56 items"
# nums=[x for x in text if x.isdigit()]
# print(nums)