# def longestPalindrome(self, s: str) -> str:
def longestPalindrome(s: str) -> str:
    # s="ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    def isPalindrome(s):
        return s == s[::-1]

    if isPalindrome(s):
        return s

    length = len(s)
    lcs=s[0]
    for i in range(length):
        for j in range(i,length):
            cs=s[i:j+1]
            l=len(cs)
            if isPalindrome(cs) and l>len(lcs):
               lcs=cs

    return lcs

    # if s == s[::-1]:
    #     return s
    # res = [test_str[i: j] for i in range(len(test_str))
    #        for j in range(i + 1, len(test_str) + 1)]
    #
    # alist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    # blist = []
    # # for i in s:
    # #     if i not in alist:
    # #         alist.append(i)
    # # lcs = s[0]
    # while True:
    #     for i in alist:
    #         for j in alist:
    #             if i == j:
    #                 if len(i + j) < 1001 and i + j not in alist and i + j not in blist:
    #                     blist.append(i + j)
    #                     # if len(lcs) < len(i + j):
    #                     #     lcs = i + j
    #                 # else:
    #                 #     continue
    #                 # if i+j in s and len(lcs)<len(i+j):
    #                 #         lcs=i+j
    #
    #             # else:
    #             if len(i + j + i) < 1001 and i + j + i not in alist and i + j + i not in blist:
    #                 blist.append(i + j + i)
    #                 # if len(lcs) < len(i + j + i):
    #                 #     lcs = i + j + i
    #                 # else:
    #                 #     continue
    #             if len(j + i + j) < 1001 and j + i + j not in alist and j + i + j not in blist:
    #                 blist.append(j + i + j)
    #                 # if len(lcs) < len(j + i + j):
    #                 #     lcs = j + i + j
    #                 # else:
    #                 #     continue
    #                 # alist.append(i + j + i)
    #                 # alist.append(j + i + j)
    #             # if i+j+i in s and len(lcs)<len(i+j+i):
    #             #     lcs=i+j+i
    #
    #             # if j + i + j in s and len(lcs)<len(j + i + j):
    #             #     lcs=j + i + j
    #     if len(blist) == 0:
    #         break
    #     else:
    #         print(len(blist))
    #         alist.extend(blist)
    #         blist = []
    #
    # return lcs


# longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
#
#
#
#
# # def longestPalindrome(self, s: str) -> str:
# def longestPalindrome(s: str) -> str:
#     # s="ccc"
#     # def isPalindrome(s):
#     #     return s == s[::-1]
#
#     # if s == s[::-1]:
#     #     return s
#
#     alist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
#     blist = []
#     # for i in s:
#     #     if i not in alist:
#     #         alist.append(i)
#     # lcs = s[0]
#     while True:
#         for i in alist:
#             for j in alist:
#                 if i == j:
#                     if len(i + j) < 1001 and i + j not in alist and i + j not in blist and i + j in s:
#                         blist.append(i + j)
#                         if len(lcs) < len(i + j):
#                             lcs = i + j
#                     # else:
#                     #     continue
#                     # if i+j in s and len(lcs)<len(i+j):
#                     #         lcs=i+j
#
#                 # else:
#                 if len(i + j + i) < 1001 and i + j + i not in alist and i + j + i not in blist and i + j + i in s:
#                     blist.append(i + j + i)
#                     if len(lcs) < len(i + j + i):
#                         lcs = i + j + i
#                     # else:
#                     #     continue
#                 if len(j + i + j) < 1001 and j + i + j not in alist and j + i + j not in blist and j + i + j in s:
#                     blist.append(j + i + j)
#                     if len(lcs) < len(j + i + j):
#                         lcs = j + i + j
#                     # else:
#                     #     continue
#                     # alist.append(i + j + i)
#                     # alist.append(j + i + j)
#                 # if i+j+i in s and len(lcs)<len(i+j+i):
#                 #     lcs=i+j+i
#
#                 # if j + i + j in s and len(lcs)<len(j + i + j):
#                 #     lcs=j + i + j
#         if len(blist) == 0:
#             break
#         else:
#             alist.extend(blist)
#             blist = []
#
#     return lcs
#
#
# longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
