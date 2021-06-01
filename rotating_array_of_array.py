num_of_list = int(input("Enter the number of rows:"))
element_per_list = int(input("Enter the number of columns:"))
input_list = [[int(input()) for x in range (element_per_list)] for y in range(num_of_list)] # Press Enter after each element
print("\nDesired Input \n",input_list, end="\n")
# output_list = list(map(list,(zip(*reversed(input_list))))) # This is the solution using Map Function
output_list = [list(a) for a in zip(*reversed(input_list))]  # This solution uses List Comprehension
print("\nExpected Output \n",output_list)
