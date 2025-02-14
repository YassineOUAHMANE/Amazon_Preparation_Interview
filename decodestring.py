def decodestring(s):
    stack_letters = []
    stack_numbers = []
    word = ""
    number = 0
    for el in s:
        if el.isdigit():
            number = number * 10 + int(el)
        elif el == "[":
            stack_letters.append(word)
            stack_numbers.append(number)
            number = 0 
            word = ""
            
        elif el == "]":
            num = stack_numbers.pop()
            prevword = stack_letters.pop()
            word = prevword + word * num
        else:
            word += el
    return word