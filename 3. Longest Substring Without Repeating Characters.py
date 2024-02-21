def lengthOfLongestSubstring(s: str) -> int:
    lcs = ''
    s = " 6^7:"
    # d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    #      'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    size = len(s)
    substrlist = []
    for i in range(0, size):
        # d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        #      'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        print(i)
        lcs=''
        lcs += s[i]
        substrlist.append(len(lcs))
        # d[s[i]] = 1
        for j in range(i + 1, size):
            if i == j:
                break
            # if s[i] != 1:
            #     lcs += s[i]
            #     d[s[i]] = 1
            # else:
            #     substrlist.append(len(lcs))
            #     d[s[i]] = 0
            #     lcs = ''
            # if d[s[j]] != 1:
            if s[j] not in lcs:
                lcs += s[j]
                substrlist.append(len(lcs))
                # d[s[j]] = 1
            else:
                substrlist.append(len(lcs))

                # print(lcs)
                # d[s[j]] = 0
                # d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                #      'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                #      'y': 0, 'z': 0}
                lcs = ''
                break
    if len(substrlist) == 0:
        return 0
    return max(substrlist)
