import statistics as sd
def problem4_2(list):
	mean=sd.mean(list)
	deviation=sd.stdev(list)
	print(mean)
	print(deviation)
# import random
# numList = []
# random.seed(150)
# for i in range(0,25):
#     numList.append(round(100*random.random(),1))
# problem4_2(numList)