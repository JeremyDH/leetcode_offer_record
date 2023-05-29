#物品重量和价值
weight = [1, 3, 4]
value = [15, 20, 30]
#背包重量
bagweight = 4 
#初始DP数组
dp = [[0] * (bagweight+1) for i in range(len(weight))]
for j in range(weight[0],bagweight+1, 1):
    dp[0][j] = value[0]
    
#开始循环
for i in range(1, len(weight)):
    for j in range(bagweight+1):
        if (j < weight[i]): dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i]] + value[i])
 #打印结果
print(dp[len(weight) - 1][bagweight])
