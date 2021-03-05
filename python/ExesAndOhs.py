#by Max
def xo(string):
    #split strings into character lists of lower cased chars
    def split(word):
        word = word.lower()
        print(word)
        return [char for char in word]
    string = split(string)
    
    count_of_x = 0
    count_of_o = 0
    
    for letter in string:
        if(letter == 'x'):
            count_of_x += 1
        if(letter == 'o'):
            count_of_o += 1
            
    return(count_of_x == count_of_o)
