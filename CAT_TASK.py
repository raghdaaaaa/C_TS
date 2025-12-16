# TASK (1)
def rem_and_rev(list):
    sett = []
    for item in list:
        if item not in sett:
            sett.append(item)
    sett.reverse()
    return sett

data = [1, 2, 3, 2, 4, 1, 5]
result = rem_and_rev(data)
print(result)

#############################################

# TASK (2)
def is_palindrome(number):
    num_str = str(number)
    rev_str = num_str[::-1]

    if num_str == rev_str:
        return True
    else:
        return False

print(is_palindrome(1221))   
print(is_palindrome(4554))   
print(is_palindrome(1234))   

################################################

# TASK (3)
def caesar_cipher(text, shift):

    alp_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alp_lower = "abcdefghijklmnopqrstuvwxyz"
    
    enc_text = ""
    
    for char in text:
        if char in alp_upper:
            old_index = alp_upper.index(char)
            new_index = (old_index + shift) % 26
            enc_text += alp_upper[new_index]
            
        elif char in alp_lower:
            old_index = alp_lower.index(char)
            new_index = (old_index + shift) % 26
            enc_text += alp_lower[new_index]
        
        else:
            enc_text += char
            
    return enc_text 

print(caesar_cipher("q", 1))  
print(caesar_cipher("j", 5))
print(caesar_cipher("RaghDaa", 3))    




