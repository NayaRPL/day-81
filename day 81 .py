from lib2to3.pytree import Node


class node:
    def __init__(self,element,next=None):
        self._element= element
        self._next=next
        
class linkedlist :
    def _init_(self):
        #referensi yang menunjukkkan ke simpul pertama
        self.head=None
        #referensi yang menunjukkan ke simpul terakhir 
        self.tail=None
        self.tail=0  # mula_mula list kosong
    # memriksa ukuran list
    def isempty(self):
        return self.zise == 0
    # menambah simpul pada posisi pertama
    def addfirst(self,element):
        #membuat simpul baru (newnode.next menunjuk ke head)
        newnode = Node
        # head mwnunjuk ke simpul baru 
        self.head= newnode
        #jika list hanya berisi satu simpul 
        if self.tail== self.head:
            self.tail = self.head
