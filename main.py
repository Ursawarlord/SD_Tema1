from sort_algorithms.skiplist import *
from sort_algorithms.quicksort_mediana import *
from sort_algorithms.quicksort_mediana_din_3 import *
from sort_algorithms.radixsort import *
from sort_algorithms.radixsort16 import *
from sort_algorithms.radixsortb2 import *
from sort_algorithms.bubblesort import *
from sort_algorithms.countsort import *

from random import *
import sys
import time
sys.setrecursionlimit(15000) # evitare RecursionError: maximum recursion depth

def sorteaza_skiplist(lista):
    lst = SkipList(0, 0.5)
    lst.insert_all(lista)
    return lst.return_sorted_List()

def sorteaza_radixsort(lista):
    radixSort(lista)
    return lista

def sorteaza_radixsort16(lista):
    radixSortHex(lista)
    return lista

def sorteaza_radixsortb2(lista):
    return radix_sort_bit(lista)


def sorteaza_quicksort_mediana(lista):
    quicksort_mediana(lista,0,len(lista)-1)
    return lista

def sorteaza_quicksort_mediana_din_3(lista):
    quicksort_mediana_din_3(lista,0,len(lista))
    return lista

def sorteaza_countsort(lista,val_max):
    return counting_sort(lista,val_max)

def sorteaza_bubblesort(lista):
    return bubbleSort(lista)

def genereaza_lista(nr, val_max):
    rez = []
    for i in range(0,nr):
        rez.append(randrange(val_max))
    return rez;

def afiseaza_timp(nume_functie, list,val_max, nume):
    print('\t'+nume)
    print('\t\t' + "Timp executie:", end=" ")
    start = time.time()
    if(nume == "Countsort"):
        nume_functie(list,val_max)
    else:
        nume_functie(list)
    end = time.time()
    print(round(end-start,7), "s")

def sorteaza_native(lista):
    return sorted(lista)

def afiseaza_eroare(nume):
    print(nume + "\n \t\talgoritmul nu poate rula in timp util")

def main():
    f = open("teste.txt", "r")
    nr_teste = int(f.readline())
    ls = []
    for i in range(0,nr_teste):
        nr, val_max = [ int(x) for x in f.readline().split() ]
        print("Testul {}\n(n={},vmax={})".format(i+1,nr,val_max))
        ls = genereaza_lista(nr, val_max)
        if(nr*val_max < 50007000):
            afiseaza_timp(sorteaza_skiplist, ls, val_max, "Skiplist")
        else:
            afiseaza_eroare("Skiplist")
        if (val_max < 100 and nr / val_max < 2000):
            afiseaza_eroare("Quicksort")
        else:
            afiseaza_timp(sorteaza_quicksort_mediana, ls, val_max, "Quicksort cu alegerea pivotului mediana medianelor")
            afiseaza_timp(sorteaza_quicksort_mediana_din_3, ls, val_max, "Quicksort cu alegerea pivotului mediana din 3")
        if(nr<20070):
            afiseaza_timp(sorteaza_bubblesort, ls, val_max, "Bubblesort")
        else:
            afiseaza_eroare("Bubblesort")
        if(val_max<20000500):
            afiseaza_timp(sorteaza_countsort, ls, val_max, "Countsort")
        else:
            print(nume + "\n \t\talgoritmul nu poate rula in timp util")
        if(nr<30700):
            afiseaza_timp(sorteaza_radixsort, ls, val_max, "Radixsort")
        else:
            afiseaza_eroare("Radixsort base-10")
        afiseaza_timp(sorteaza_radixsortb2, ls, val_max, "Radixsort base-2")
        afiseaza_timp(sorteaza_radixsort16, ls, val_max, "Radixsort HEX")
        afiseaza_timp(sorteaza_native, ls, val_max, "Python standard sort")


main()
