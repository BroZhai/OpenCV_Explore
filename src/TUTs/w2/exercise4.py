

# define a class to find the largest value and smallest value from the list L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
# 目标: 从一个无序数列中找到'最小值' & '最大值', 思路: 留存'局部最小 & 最大'和每一个后面的数进行比较, 直至结尾时再"返回找到的'最小/大'值"

class Test(object):

    def __init__(self):
        # the tesing list
        self.L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
        self.num = self.L1[0]

    def test_small_num(self, count): # 找最小值
        # insert your code
        cur_min = self.L1[0]
        for cur_num in self.L1:
            if cur_num < cur_min:
                cur_min = cur_num;
        return cur_min;

    def test_large_num(self, count): # 找最大值
        # insert your code
            cur_max = self.L1[0]
            for cur_num in self.L1:
                if cur_num > cur_max:
                    cur_max = cur_num;
            return cur_max;

if __name__=='__main__':
    print(Test().test_large_num(len(Test().L1)));
    print(Test().test_small_num(len(Test().L1)));
