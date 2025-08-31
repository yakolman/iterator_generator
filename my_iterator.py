class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.external_list=0
        self.item_list=0

    def __iter__(self):
        return self

    def __next__(self):
        while self.external_list<len(self.list_of_list):
            current_list = self.list_of_list[self.external_list]
            if self.item_list<len(current_list):
                item = current_list[self.item_list]
                self.item_list+=1
                return item
            else:
                self.external_list+=1
                self.item_list = 0

        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()