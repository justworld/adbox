# coding: utf-8
def kmp(t, w):
    """
    KMP算法是一种改进的字符串匹配算法，由D.E.Knuth，J.H.Morris和V.R.Pratt提出的
    利用匹配失败后的信息，尽量减少模式串与主串的匹配次数
    时间复杂度O(m+n)
    """