#Program to perform operation on tuples
#creating a Tuple

my_tuple = (10,20,30,40,50)
print("Original Tuples:",my_tuple)

#1.  Indexing
print("Element at index 2: ", my_tuple[2])

#2.  Slicing
print("Tuple from index 1 to 3:",my_tuple[1:4])

#3.  Concatentaion
new_tuple = my_tuple + (60,70)
print("After Concatentaion:", new_tuple)

#4.  Repetition
repeated_tuple = my_tuple * 2
print("After Repetition: ",repeated_tuple)

#5.   Nested Tuple
nested_tuple = ((1,2),(2,3,4),(True, False))
print(nested_tuple)