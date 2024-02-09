class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  
  def __str__(self):
    cur = self.head
    result = []
    while cur:
      result.append(str(cur.data))
      cur = cur.next
    return ','.join(result)

  def reversed(self):
    cur = self.head
    list = LinkedList()
    while cur:
      list.insert_at_beginning(cur.data)
      cur = cur.next
    return list

  def insertion_sort(self):
      if not self.head or not self.head.next:
           return

      sorted_list = LinkedList()
      cur = self.head

      while cur:
        next_node = cur.next
        sorted_list.insert_sorted(cur)
        cur = next_node

      self.head = sorted_list.head
  
  def insert_sorted(self, new_node):
    if not self.head or self.head.data >= new_node.data:
      new_node.next = self.head
      self.head = new_node
    else:
      cur = self.head
      while cur.next and cur.next.data < new_node.data:
        cur = cur.next
      new_node.next = cur.next
      cur.next = new_node
  
  def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    cur1, cur2 = list1.head, list2.head

    while cur1 or cur2:
        if not cur1:
            merged_list.insert_at_beginning(cur2.data)
            cur2 = cur2.next
        elif not cur2:
            merged_list.insert_at_beginning(cur1.data)
            cur1 = cur1.next
        elif cur1.data < cur2.data:
            merged_list.insert_at_beginning(cur1.data)
            cur1 = cur1.next
        else:
            merged_list.insert_at_beginning(cur2.data)
            cur2 = cur2.next

    merged_list.insertion_sort()
    return merged_list

 

def main():
  list = LinkedList()
  for i in [47, 32, 68, 23, 56, 89, 14, 79, 51, 36]:
    list.insert_at_beginning(i)

  print(f'прямий порядок: {list}')
  list = list.reversed()
  print(f'зворотній порядок: {list}')

  list.insertion_sort()
  print(f'сортований: {list}')

  list1 = LinkedList()
  for i in [1, 77, 37, 32]:
    list1.insert_at_beginning(i)

  list.merge_sorted_lists(list1)
  print(f'злитий: {list}')

def __main__():
  main()
