import math

class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1

    def addElt(self, elt):

        """this"""
        self.data.append(elt)
        self.n += 1
        self.siftUp(self.n)
        """this"""


    def siftUp(self, i):
        while i >=2:

            """this"""
            k = i // 2 

            if self.data[k] >= self.data[i]:
                return

            self.data[k], self.data[i] = self.data[i], self.data[k]

            i = k
            """this"""

    def siftDown(self, i):

        """this"""
        m = self.data[i]
        a = i
        key_bool = False

        while a * 2 <= self.n and not key_bool:
            
            if a * 2 < self.n and self.data[a*2] < self.data[a * 2 + 1]:
                key = a *2 +1
            else:
                key = a * 2
            
            if m < self.data[key]:
                self.data[a] = self.data[key]
                a = key
                
            else:
                key_bool = True
        self.data[a] = m
        """this"""

    def makeHeap2(self):

        """this"""
        for b in range(self.n //2, 0, -1):
            self.siftDown(b)
        """this"""

    def root(self):

        if(self.n >0):

            """this"""
            keyout = self.data[1]
            self.data[1] = self.data[self.n]
            self.n -= 1
            self.siftDown(1)
            """this"""
            
            return keyout

    def removeKeys(self):

        """this"""
        c = list()
        for i in range(self.n):
            c.append(self.root())
        
        return c
        """this"""

    def heapSort(a):
        
        """this"""
        d = Heap(a)
        d.makeHeap2()

        return d.removeKeys()
        """this"""



a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s = Heap.heapSort(a)
print(s)    