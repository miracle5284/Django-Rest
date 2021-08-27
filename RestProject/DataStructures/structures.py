from concurrent.futures import ProcessPoolExecutor


class Node:

    def __init__(self, data=None, next=None, prev=None):

        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        nex = self.next.data if self.next is not None else self.next
        prev = self.prev.data if self.prev is not None else self.prev
        return '%s %s %s,' % (self.data, nex, prev)


def levels(self, top_level=False):

    if not self:
        return self.level
    results = []
    for items in self:
        if items.childrens:
            with ProcessPoolExecutor() as executor:
                results.append(max(executor.map(levels, items.childrens)))

        else:
            results.append(items.level)

    return max(results) - (self.level if top_level else 0)


class Node2:

    def __init__(self, data=None, _next=None):

        self.data = data
        self.next = _next

    def __str__(self):
        nex = self.next.data if self.next is not None else self.next
        return '%s %s,' % (self.data, nex)


class LinkedList2:

    def __init__(self):

        self.head = None
        self.len = 0
        self.end = None

    def __str__(self):

        if self.head is None:
            return None
        string, itr = '', self.head

        while itr:
            if string:
                string += '--> %s' % itr.data
            else:
                string += str(itr.data)
            itr = itr.next

        return string

    def insert(self, *data, index=None):
        if index and not 0 <= index < self.len:
            raise IndexError
        _data_ = None
        for count, _data in enumerate(data):

            _data = Node(_data, None, _data_)
            _data_ = _data
            if _data.prev is not None:
                _data.prev.next = _data

            if not count:
                node = _data
        end_node = _data
        length = self.len + len(data)
        #print(node, end_node, length, self.end)

        if self.head is None:
            self.head = node
            self.end = end_node
        elif not index and self.end is not None:
            node.prev = self.end
            self.end.next = node
            self.end = end_node
        else:
            count, itr = 0, self.head
            while True:
                end = itr.next
                print(itr.data)
                if count == index-1:
                    node.prev = itr
                    itr.next = node
                    if end is not None:
                        end.prev = end_node
                        end.prev.next = end
                    break
                itr = itr.next
                count += 1
        self.len = length


class LinkedList:

    def __init__(self, *args):

        self.head = None
        self.len = 0
        self.end = None

        if args:

            self.insert_many(*args)

    def __str__(self):

        if self.head is None:
            return None
        string, itr = '', self.head

        while itr:
            if string:
                string += '--> %s' % itr.data
            else:
                string += str(itr.data)
            itr = itr.next

        return string

    def insert(self, index, data):
        count, itr = 0, self.head
        while True:
            if count == index-1:
                itr.next = Node2(data, itr.next)

                break
            itr = itr.next
            count += 1
        self.len += 1

    def insert_many(self, *data, index=None):
        if index and not 0 <= index < self.len:
            raise IndexError
        _data_ = None
        for count, _data in enumerate(data):

            _data = Node2(_data, None)

            if _data_ is not None:
                _data_.next = _data

            _data_ = _data

            if not count:
                node = _data

        end_node = _data
        length = self.len + len(data)
        print(node, end_node, length, self.end)

        if self.head is None:
            self.head = node
            self.end = end_node
        elif not index and self.end is not None:
            self.end.next = node
            self.end = end_node
        else:
            count, itr = 0, self.head
            while True:
                end = itr.next
                print(itr.data)
                if count == index-1:
                    itr.next = node
                    if end is not None:
                        end_node.next = end
                        self.end.next = None

                    break
                itr = itr.next
                count += 1
        self.len = length

        print(self.end.next)

    def __iter__(self):
        itr = self.head

        while itr:
            yield itr.data
            itr = itr.next

    def __getitem__(self, item):

        for count, items in enumerate(self):
            if count == item:
                return items
        else:
            raise IndexError

    def __setitem__(self, key, value):

        count, itr = 0, self.head
        while itr:
            if count == key:
                itr.data = value
                break
            itr = itr.next
            count += 1

    def __delitem__(self, key):

        self.pop(key)

    def __bool__(self):
        return bool(self.len)

    def pop(self, key):

        if not 0 <= key < len(self):
            raise IndexError('')

        count, itr = 0, self.head

        while True:

            if count == key - 1:
                item = itr.next.data
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
        self.len -= 1

        return item

    def remove(self, item):

        count, itr, prev = 0, self.head, None
        while itr:

            if itr.data == item:
                if prev is None:
                    self.head = itr.next
                    return
                prev.next = itr.next
                self.len -= 1
                return

            itr, prev = itr.next, itr

        raise ValueError('%s not present' % item)

    def __contains__(self, item):

        count, itr, prev = 0, self.head, None
        while itr:

            if itr.data == item:
                return True

            itr, prev = itr.next, itr

        return False

    def __len__(self):
        return self.len

    __repr__ = __str__


class Tree:

    def __init__(self, data):

        self.data = data
        self.childrens = []
        self.parent = None

    def __str__(self):
        return self.data

    def add_child(self, child):
        if not isinstance(child, Tree):
            child = Tree(child)
        child.parent = self
        self.childrens.append(child)

    def __iter__(self):

        for items in self.childrens:
            yield items

    def children(self):

        for items in self:
            yield items, items.childrens

    def floor(self):
        for items in self.childrens:
            if not items.childrens:
                yield items
            else:
                data = items.floor()
                while True:
                    try:
                        yield next(data)
                    except StopIteration:
                        break

    def __getitem__(self, item):
        for items in self:
            if items.data == item:
                return self.childrens

    def __len__(self):
        return len(self.childrens)

    @property
    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    @property
    def levels(self):
        return levels(self, top_level=True)

    def display(self, sep='|--', tab=3):

        print('%s %s %s' % (
            ' ' * self.level * tab,
            sep,
            self.data
        ))
        for child in self:
            print('%s %s %s' % (
                ' ' * child.level * tab,
                sep,
                child.data
            ))
            for childs in child:
                childs.display(sep=sep, tab=tab)

    def __repr__(self):

        return repr(self.data)

    def __bool__(self):
        return bool(self.childrens)

print('SSSSSS')
Electronics = Tree('Electronics')
Laptop = Tree('Laptop')
Laptop.add_child(Tree('HP'))
Laptop.add_child(Tree('Lenovo'))
Laptop.add_child(Tree('Acer'))
TV = Tree('TV')
TV.add_child(Tree('LG'))
TV.add_child(Tree('Samsung'))
TV.add_child(Tree('Sony'))
Mobiles = Tree('Mobiles')
Tecno = Tree('Tecno')
Camon = Tree('Camon')
Camon.add_child('CamonX')
Tecno.add_child(Camon)
Tecno.add_child('Spark')

Mobiles.add_child(Tecno)
Mobiles.add_child(Tree('Oppo'))
Mobiles.add_child(Tree('Infinix'))
Mobiles.add_child(Tree('Iphone'))
Category = Tree('Category')
Category.add_child('School')
Category.add_child(Mobiles)
Electronics.add_child(Laptop)
Electronics.add_child(TV)
Electronics.add_child(Category)
Electronics.display()
# S = LinkedList()
# print(12345)
# S.insert_many(1,2,3,6)
# S.head
# print(4321)
# print(S)
# print(444324)
# S.insert_many(11, 12, index=1)
