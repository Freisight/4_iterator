nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

# 1
 
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

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# 2 

def flat_generator(spisok):
    spisok = [ob for item in spisok for ob in item]
    count = 0
    while count < len(spisok):
        yield spisok[count]
        count += 1

for item in  flat_generator(nested_list):
	print(item)