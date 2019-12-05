import random
import numpy as np

# 集団
group = np.random.randint(0, 2, (100, 100))

for k in range(0, 2000):

    #集団評価
    group_evaluation = []
    group_evaluation = np.mean(group, axis=1)

    #平均
    average = np.sum(group_evaluation[0:100])/100
    average1 = np.sum(group_evaluation[0:50])/50

    #並び替え
    sorted_result = sorted(group, reverse=True, key = lambda x: sum(x))

    #スライス
    for i in range(0, 50, 2):
        j = random.randrange(0, 95)
        sorted_result[i][j:j+5], sorted_result[i+1][j:j+5] = sorted_result[i+1][j:j+5], sorted_result[i][j:j+5].copy()

    #突然変異
    i = random.randint(24,50)
    if sum(sorted_result[i]) > average:
        j = random.randint(0,50)
        sorted_result[i][j:j+50] = np.random.randint(0, 2, (1, 50))


    #新世代
    for i in range(50, 100):
        sorted_result[i] = np.random.randint(0, 2, (1, 100))

    #引継ぎ
    for i in range(0, 100):
        group[i] = sorted_result[i].copy()

    #k世代の優勢列
    print('=====================================')
    print('第'+str(k)+'世代の優勢列')
    print(sorted_result[0])
    print('average')
    print(average1)

