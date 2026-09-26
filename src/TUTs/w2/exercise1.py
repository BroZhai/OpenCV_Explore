# setup matplotlib display
#matplotlib inline

import matplotlib.pyplot as plt     # import matplotlib

# 目标: 统计2-100每个数有多少个因数(可以被多少个数整除), 随后用matplot画出来
#The goal of the program is to count the number of factors (not including 1 and the number itself) for each number between 2 and 100. For example, the number of factors of 2 is 0, and the number of factors for 4 is 1.
#Here are two variables to get you started, xs stores the numbers from 2 to 100, and fs will store the factors for each number in xs.

# INSERT YOUR CODE HERE and DEFINE A FUNCTION NAMELY "numfactor"


def numfactor(n):
    # INSERT YOUR CODE HERE
    countnumber = 0;

    if(n == 2):
        return 0;
    # 解决思路: 用 2 到 当前输入值n 当 '除数', 用n对这些值取余看看是否为0
    for devider_num in range(2,n):
        if(n % devider_num == 0):
            countnumber +=1 # 可以整除, 因数+1

    return countnumber # 返回'总因数数'


if __name__=='__main__':
    xs = range(2,101)   # the number
    fs = []             # store number of factors in this list    
    for num in xs:
        #print(num)
        x=numfactor(num); # 取得当前输入num(n) 返回的'因数'个数
        #print(x)
        fs.append(x) # 将当前输入num(n)的'因数个数'加到列表里
    # print(fs)
    
    #Write code to plot the number of factors (y-axis) vs the number (x-axis). Don’t forget to label your axes!
    # 使用plt.plot()函数画图 (x: 2-101连续数字, y: 每个值对应的'因数个数')
    plt.plot(xs, fs);
    plt.xlabel("Number");
    plt.ylabel("Number of factors")
    plt.show();

    # Next we will plot a histogram of the number of factors.
    # 将上面的图换成'直方图', 用12个区间来表示'因数个数'
    # INSERT YOUR CODE HERE
    plt.hist(fs, bins=range(0,12));
    plt.xlabel("factor bins");
    plt.ylabel("factor counts");
    plt.show();
