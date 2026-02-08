#Program to perform Opertions on Dictionary

#creating a dictionary
my_dict = {
    "Name": "Rohit",
    "Age" : 19,
    "City": "Pune"
}
print("Original Dictionary:" ,my_dict)

#1.  Accessing Element 
print("Name:" , my_dict["Name"])

#2.  Adding New-value pair
my_dict["Country"]= "India"
print("After adding country:", my_dict)

#3.  Updating Vaule
my_dict["Age"] = 20
print("After updating age:", my_dict)