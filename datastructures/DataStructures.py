class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


# Singly LinkedList
class LinkedList:
	__len = 0

	def __init__(self):
		self.head = None

	def append(self, element):
		if not self.head:
			self.head = Node(element)
			self.__len = self.__len + 1
			return True
		current = self.head
		while current.next:
			current = current.next
		new_node = Node(element)
		current.next = new_node
		self.__len = self.__len + 1
		return True

	def add_at_front(self, element):
		if not self.head:
			self.head = Node(element)
			self.__len = self.__len + 1
			return True
		new_node = Node(element)
		new_node.next = self.head
		self.head = new_node
		self.__len = self.__len + 1
		return True

	def print(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next

	def size(self):
		return self.__len

	def is_empty(self):
		return self.__len == 0

	def get(self, index=None):
		if not index:
			index = 0
		if self.is_empty():
			raise Exception("list is empty")
		current = self.head
		i = 0
		while i < index:
			current = current.next
			i = i + 1
		return current.data

	def remove(self, index=None):
		if not index:
			index = self.__len - 1
		if not self.head or self.is_empty():
			raise Exception("list is empty")
		# have to traverse upto before last element and remove link
		current = self.head
		i = 0
		while i < index - 1:
			current = current.next
			i = i + 1
		# got last before element
		to_be_added = current.next.next
		current.next = to_be_added
		self.__len = self.__len - 1
		return True

	def current_head(self):
		return self.head.data


class DoubleNode:
	def __init__(self, data, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, element):
		if not element:
			raise ValueError("None cannot be added to list")
		if not self.head:
			self.head = DoubleNode(element)
			self.tail = self.head
			return True
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		current_node.next = DoubleNode(element, prev=current_node)
		self.tail = current_node.next
		return True

	def remove_first(self):
		self.head = self.head.next
		self.head.prev = None

	def print(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next

	def get(self, index=None):
		if not index:
			index = 0
		pass


class Stack:
	def __init__(self):
		self.arr = []
		self.top = -1
		self.len = 0

	def push(self, element):
		self.arr.append(element)
		self.top += 1
		self.len += 1

	def pop(self):
		element = self.arr[self.top]
		del self.arr[self.top]
		self.top -= 1
		self.len -= 1
		return element

	def print(self):
		for item in self.arr:
			print(item)


s = Stack()
s.push("maran")
s.push(1)
s.push("preethi")
s.print()
print('-------------')
s.pop()
s.print()
