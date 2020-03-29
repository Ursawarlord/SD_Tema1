# SD_Tema1

Algoritmii de sortare implementați cu succes în acest repository sunt:
- [x] SkiplistSort
- [x] RadixSort
- [x] RadixSort baza 2
- [x] RadixSort HEX
- [x] QuickSort pivot "mediana medianelor"
- [x] QuickSort pivot "mediana din 3"
- [x] BubbleSort
- [x] CountSort

Considerăm fișierul teste.txt
```
9
22000 1700
220000 170
1000 1000
10000 1000
100000 1000
1000000 1000
1000000 100000
10000 10000000
100000 10000000
```

Programul rulează din main.py iar terminalul va afișa astfel:

```
Testul 1
(n=22000,vmax=1700)
	Skiplist
		Timp executie: 17.3580544 s
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 0.4247575 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 0.6516278 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 0.0379777 s
	Radixsort
		Timp executie: 16.2606819 s
	Radixsort base-2
		Timp executie: 2.9283226 s
	Radixsort HEX
		Timp executie: 0.1219292 s
	Python standard sort
		Timp executie: 0.0010002 s
Testul 2
(n=220000,vmax=170)
	Skiplist
		Timp executie: 13.8990366 s
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 33.2879517 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 42.2358246 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 0.182894 s
Radixsort base-10
 		algoritmul nu poate rula in timp util
	Radixsort base-2
		Timp executie: 33.8486063 s
	Radixsort HEX
		Timp executie: 0.8854964 s
	Python standard sort
		Timp executie: 0.0049961 s
Testul 3
(n=1000,vmax=1000)
	Skiplist
		Timp executie: 0.1319354 s
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 0.0069959 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 0.0129926 s
	Bubblesort
		Timp executie: 0.1958768 s
	Countsort
		Timp executie: 0.0009987 s
	Radixsort
		Timp executie: 0.6636283 s
	Radixsort base-2
		Timp executie: 0.1199319 s
	Radixsort HEX
		Timp executie: 0.0049982 s
	Python standard sort
		Timp executie: 0.0 s
Testul 4
(n=10000,vmax=1000)
	Skiplist
		Timp executie: 4.1006422 s
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 0.2178741 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 0.2938318 s
	Bubblesort
		Timp executie: 20.0105326 s
	Countsort
		Timp executie: 0.0060105 s
	Radixsort
		Timp executie: 7.2918079 s
	Radixsort base-2
		Timp executie: 1.3962016 s
	Radixsort HEX
		Timp executie: 0.0599666 s
	Python standard sort
		Timp executie: 0.0 s
Testul 5
(n=100000,vmax=1000)
Skiplist
 		algoritmul nu poate rula in timp util
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 2.0218437 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 3.4240367 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 0.0709612 s
Radixsort base-10
 		algoritmul nu poate rula in timp util
	Radixsort base-2
		Timp executie: 18.3374913 s
	Radixsort HEX
		Timp executie: 0.8864927 s
	Python standard sort
		Timp executie: 0.0020003 s
Testul 6
(n=1000000,vmax=1000)
Skiplist
 		algoritmul nu poate rula in timp util
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 137.9909902 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 140.7659295 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 0.7405765 s
Radixsort base-10
 		algoritmul nu poate rula in timp util
	Radixsort base-2
		Timp executie: 154.4385483 s
	Radixsort HEX
		Timp executie: 7.9734302 s
	Python standard sort
		Timp executie: 0.1009412 s
Testul 7
(n=1000000,vmax=100000)
Skiplist
 		algoritmul nu poate rula in timp util
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 17.9497094 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 22.9228797 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 0.831516 s
Radixsort base-10
 		algoritmul nu poate rula in timp util
	Radixsort base-2
		Timp executie: 151.277324 s
	Radixsort HEX
		Timp executie: 10.7378387 s
	Python standard sort
		Timp executie: 0.0359795 s
Testul 8
(n=10000,vmax=10000000)
Skiplist
 		algoritmul nu poate rula in timp util
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 0.1109383 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 0.1819136 s
	Bubblesort
		Timp executie: 19.4218516 s
	Countsort
		Timp executie: 7.2828276 s
	Radixsort
		Timp executie: 7.5176928 s
	Radixsort base-2
		Timp executie: 1.5351202 s
	Radixsort HEX
		Timp executie: 0.1199319 s
	Python standard sort
		Timp executie: 0.0 s
Testul 9
(n=100000,vmax=10000000)
Skiplist
 		algoritmul nu poate rula in timp util
	Quicksort cu alegerea pivotului mediana medianelor
		Timp executie: 1.4551687 s
	Quicksort cu alegerea pivotului mediana din 3
		Timp executie: 3.6768906 s
Bubblesort
 		algoritmul nu poate rula in timp util
	Countsort
		Timp executie: 7.4097536 s
Radixsort base-10
 		algoritmul nu poate rula in timp util
	Radixsort base-2
		Timp executie: 15.0903752 s
	Radixsort HEX
		Timp executie: 1.5421317 s
	Python standard sort
		Timp executie: 0.0049789 s
```
**RUN**
