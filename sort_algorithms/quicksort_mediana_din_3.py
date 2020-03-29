def compareswap(L,a,b):
    L[a], L[b] = min(L[a],L[b]),max(L[a],L[b])

def medianfirst(L,a,b,c):
    compareswap(L,b,a) # L[b]<=L[a]
    compareswap(L,b,c) # L[b]<=L[c] i.e L[b] smallest
    compareswap(L,a,c) # L[a]<=L[c] i.e L[c] largest

def quicksort_mediana_din_3(L, low, high):
    if low < high:
        pivot_location = Partition(L, low, high)
        quicksort_mediana_din_3(L,low,pivot_location)
        quicksort_mediana_din_3(L,pivot_location + 1, high)

def Partition(L, low, high):
    middle = (low+high-1)//2
    medianfirst(L,low,middle,high-1)
    pivot = L[low]
    i = low + 1
    for j in range(low + 1,high,1):
        if L[j] < pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
    L[low],L[i-1] = L[i-1],L[low]
    return i - 1

# c = [2148,9058,7742,3153,6324,609,7628,5469,7017,504]
# print(c)
# quicksort_mediana_din_3(c, 0, len(c))
# print(c)
