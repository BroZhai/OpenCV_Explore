
# define a function and recall it to process the string (delete the same ): Remove the same characters and sort the remaining characters.

#input: s = “ajldjlajfdljfddd”--> output: ”adfjl”

# 处理思路: 新建一个数组, 随后'挨个遍历'原字符串, 插入新数组中'不存在'的数组, 调用数组自带的.sort()方法完成排序

def test(s):

    #insert your code
    char_list = [];

    for char in s:
        if char not in char_list:
            char_list.append(char);
        
    char_list.sort();
    return "".join(char_list);

if __name__=='__main__':
    s='ajldjlajfdljfddd'
    output=test(s)
    print(output)
    
