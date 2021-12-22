nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:
    def __init__(self, spisok):
        self.spisok = spisok
        self.row_position = 0
        self.col_position = -1

    def __iter__(self):
        return self
    
    def __next__(self):      
        self.col_position += 1
        
        if self.col_position == len(self.spisok[self.row_position]):
            self.row_position += 1
            self.col_position = 0

        if self.row_position == len(self.spisok):
            raise StopIteration

        return self.spisok[self.row_position][self.col_position]



for item in FlatIterator(nested_list):
	print(item)


def flat_generator(spisok):
    pass