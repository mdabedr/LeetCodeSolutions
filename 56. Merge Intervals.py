def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    l=[]
    for i in intervals:
        l.append(list(range(i.pop(0),(i.pop(0)+1))))

    new_intervals=[]

    for i in l:
        for j in l:
            if i==j:
                continue

        i_set = set(i)
        j_set = set(j)
        if len(i_set.intersection(j_set)) > 0:
            new_intervals.append()
        #     return (True)
        # return (False)
