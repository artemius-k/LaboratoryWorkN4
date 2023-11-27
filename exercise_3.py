class List:
    def __init__(self):
        self.my_list = list()

    def append_list(self, something):
        self.my_list.append(something)

    def pop_list(self):
        self.my_list.pop()

    def sort_list(self):
        self.my_list.sort()

    def count_in_list(self, something):
        return self.my_list.count(something)

    def reverse_list(self):
        self.my_list.reverse()
