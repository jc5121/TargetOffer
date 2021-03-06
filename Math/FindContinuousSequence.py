# -*- coding:utf-8 -*-
# 找出所有和为S的连续正数序列
# 以每个数字开头的满足条件的序列最多只有一个
# sum函数
# 容器是队列


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        result = []
        small = 1  # 序列头
        big = 2  # 序列尾
        middle = (1+tsum) / 2  # 开头数字不可能超过和的一半
        tempresult = [1]  # 作为队列，记录当前序列
        while small < middle:
            if sum(tempresult) == tsum:
                temp = tempresult[:]　# 切片了就会生成新的对象，而不是在原对象上操作
                result.append(temp)
                tempresult.append(big)
                big += 1
            elif sum(tempresult) < tsum:
                tempresult.append(big)
                big += 1
            else:
                tempresult.pop(0)
                small += 1
        return result
