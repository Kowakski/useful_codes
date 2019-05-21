import pickle
import numpy as np
#
file = open('./multi_block_data.txt')

data_list = []

while  True:
    line = file.readline()
    line = line.strip('\n')
    if not line:
        break
    StrList = line.split(' ')
    int_data_line = [np.int64(value) for value in StrList ]
    data_list.append( int_data_line )

with open("./data.pkl",'wb+') as f:
    pickle.dump(np.array(data_list), f)

with open("./data.pkl", 'rb') as f:
    data_tmep = pickle.load(f)
    print(type(data_tmep),np.shape(data_tmep))
    # print(data_tmep)
# print ("read complete")