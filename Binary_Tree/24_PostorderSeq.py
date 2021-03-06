# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence is None or len(sequence) == 0:
            return False

        root = sequence[-1]
        length = len(sequence)

        for i in range(length):
            if sequence[i] > root:  # 找到右子树最小节点
                break

        for j in range(i, length):  # 判断方法，就是大小关系
            if sequence[j] < root:
                return False

        left = True
        right = True

        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])

        return left and right

        # write code here