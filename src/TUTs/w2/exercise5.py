
# define a function and recall it to process the string (delete the same ): Remove the same characters and sort the remaining characters.

#input: s = “ajldjlajfdljfddd”--> output: ”adfjl”



def test(s):

    #insert your code
    char_list = [];

    for char in s:
        if char not in char_list:
            char_list.append(char);
        
    char_list.sort()
    return "".join(char_list);

if __name__=='__main__':
    s='ajldjlajfdljfddd'
    output=test(s)
    print(output)
    
