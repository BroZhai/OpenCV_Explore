

# define a class to find the largest value and smallest value from the list L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]


class Test(object):

    def __init__(self):
        # the tesing list
        self.L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]

        self.num = self.L1[0]

    def test_small_num(self, count):
        # insert your code
        cur_min = self.L1[0]
        for cur_num in range(0, count):
            if cur_num < cur_min:
                cur_min = cur_num;
            

    def test_large_num(self, count):
        # insert your code
            cur_max = self.L1[0]
            for cur_num in range(0, count):
                if cur_num > cur_max:
                    cur_max = cur_num;

if __name__=='__main__':
    print(Test().test_large_num())
    print(Test().test_small_num())
