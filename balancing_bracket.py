def check_is_bracket_balanced(bracket):
      
    open_bracket = tuple('({[')
    close_bracket = tuple(')}]')
    map = dict(zip(open_bracket, close_bracket))
    queue = []
  
    for i in bracket:
        if i in open_bracket:
            queue.append(map[i])
        elif i in close_bracket:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Yes"
    else:
        return "No"

user_input = str(input("Enter bracket: "))
print(check_is_bracket_balanced(user_input))