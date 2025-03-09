def prefix_sum(arr,queries):
    N = len(arr)

    prefix = [0] * N
    prefix[0] = arr[0]

    for i in range(1, N):
        prefix[i] = prefix[i-1]+arr[i]

    results=[]
    for l, r in queries:
        if l==0:
            results.append(prefix[r])
        else:
            results.append(prefix[r]-prefix[l-1])
        
    return results

arr=[3,1,4,1,5,9]
queries=[(1,3),(0,2),(2,5)]
print(prefix_sum(arr,queries))
