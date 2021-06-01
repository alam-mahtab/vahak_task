In this folder i solved 2 questions send by Vahak H.R
Question-1. Balancing Brackets:
    Given an input of brackets (string type). Print 'YES' if all the brackets are balanced with opening and closing. 
    Brackets can be of type {,},[,],(,) Refer to sample input and output for reference
    Input:
    {[()]}
    Output:
    YES
    Input:
    {[(])}
    Output:
    NO 
Solution : solution is in balancing_bracket.py file just run it using command python balancing_bracket.py
Sample Input : ({{[[]{}]}()}), {[({[]})]}, {[(])}, [{([{])}]
output       :     Yes       ,     No    ,  Yes  ,    No

Question 2 : Rotating Matrix:
    Given an array of array as below, rotate the array 90 degrees. 
    Refer to sample input and output for reference:
    Input:
    [
    [1,2,3]
    [4,5,6]
    [7,8,9]
    ]
    Output:
    [
    [7,4,1]
    [8,5,2]
    [9,6,3]
    ]

Overview : Question looks simple but its appraoch is quite hard, because we can't pass input in the form of lists of list.
Approach : We have to create a list of list so we take input as how many numbers of lists we want inside   
           a list, second how many elements want to be stored by each list and third input elements one by one seperated by enter   
Solution : solution is in rotating_array_of_array.py file just run it using command python rotating_array_of_array.py
Sample Input : num_of_lists_in_list =3 ,Enter, 
                elements_in_a_list = 3,Enter, 
                elements=1 , Enter, 2 , Enter ................,9, Enter. you will see the output
Sample Output:
                    [
                    [7,4,1],
                    [8,5,2],
                    [9,6,3],
                    ]
