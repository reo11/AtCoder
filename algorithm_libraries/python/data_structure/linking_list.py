from typing import List

class LinkList:
    def __init__(self, array: List):
        self.values = dict()
        for value in array:
            self.

    def add(self, value, pre_value=None, next_value=None):
        if pre_value is not None:
            if pre_value in self.values:
                self.values[pre_value].next = value
            else:
                raise ValueError(f"{pre_value} is not in the list.")
        self.values[value] =

    def remove(self, value):
        if self.next is not None:
            if self.next.value == value:
                self.next = self.next.next
            else:
                self.next.remove(value)

    def get(self):
        # 全要素のListを返す
