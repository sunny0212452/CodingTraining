# -*- coding:utf-8 -*-
# 题目描述：数组中存储了一堆小于10的非负整数，整个数组从左到右代表一个正整数（如数组[0,1,3,2]代表正整数132）。
# 现给出一个正整数K，要求经过K次数组相邻位置元素交换（必须完成K次交换），使得这个数组代表的数字最大。
 
##是否是最大值
def isbig(i, array, K):
	# print i
	# print array
	# print K
	if (K+1)<len(array):
		if array[i] == max(array[0:K+1]):
			return True
		else:
			return False
	else:
		if array[i] == max(array[0:]):
			return True
		else:
			return False
 
##从最大值向前面逐个交换
def new_trans_k(array,index_max,k):
    for i in range(k):
        t=array[index_max]
        array[index_max]=array[index_max-1]
        array[index_max - 1]=t
        index_max-=1
        # print i,":",array
    return array

 
#数组转换
def trans(array, K):
    for i in range(K):
		# print 'i=',i
		# print 'K=',K
		if (K+1)<len(array):
			if isbig(i, array, K):
				continue
			else:
				max_num = max(array[i:i+K+1])
				index_max = array.index(max_num)
				c = index_max - i
				K = K - c
				array = new_trans_k(array, index_max, c)
		else:
			if i<len(array):
				if isbig(i, array, K):
					continue
				else:
					max_num = max(array[i:])
					index_max = array.index(max_num)
					c = index_max - i
					K = K - c
					array = new_trans_k(array, index_max, c)
			else:
				break

    return array
 
 
T = int(raw_input())  ##T次测试用例
string_list = []  ##输出列表
 
for i in range(0, T):
    K = int(raw_input())  ###K次变换
    N =  int(raw_input())  ###输入列表array的长度
    array = []
    array = map(int, raw_input().strip().split(" "))
    array = trans(array, K)
    num_list_string = " ".join(map(str,array))
    print num_list_string
 
