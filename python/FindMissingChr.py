# by Max
def find_missing_letter(chars):
    # convert to num ord
    
    prevNum = ord(chars[0])
    print(prevNum)
    
    for char in chars:
        if (ord(char) > prevNum + 1):
            return chr(ord(char) - 1)
        else:
            prevNum = ord(char)

        
        

