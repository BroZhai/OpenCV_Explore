import pickle
#matplotlib inline
import matplotlib.pyplot as plt     # import matplotlib


#Next you will practice using pickle to load data from the file “data1.pickle”. The pickle is storing an nd array object (numpy multi-dimensional array). Load the pickle file and save its contents into a variable called mydata.

#Inspecting the shape of the array, we see that there are 120 samples (rows). Each sample is a 2-dimensional vector (the number of columns).

#Finally, let’s visualise the data with a plot. Treat the 1st dimension of the samples as the x-variable, and the 2nd dimension as the y-variable. In other words, plot the 1st column of the data vs. the 2nd column of the data.

# 这里的pickle_file是一个'二维Numpy数组', 我们的目标是用matplot去把每个'一维数组中的x,y'数据画出来
pickle_file=open("./data1.pickle","rb")
mydata=pickle.load(pickle_file)
# print(mydata)

# INSERT YOUR CODE HERE
x = mydata[:,0] # 用Numpy的'特色摘取': 取到二维数组中的'所有元素' (一维数组), 随后取到'一维数组'中的所有'第0个元素'
y = mydata[:,1] # 同理, 取所有'一维数组'中的'第一个元素'
plt.plot(x,y);
plt.show(); # 画出来了一个奇妙的'hello'
