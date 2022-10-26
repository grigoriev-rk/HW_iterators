
nested_list = [                                 #Initial nested list with diffrent elements and one nesting level
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:                             #Creating iteration class 


    def __init__(self, lst):                    #Cursor initialization 
        self.lst = lst
        self.cursor = -1                        #Begin from -1 for countig from first element (0 position)
        self.nested_cursor = 0
        self.list_len = len(self.lst)

    def __iter__(self):                         #Count cursor and reset nested_cursor
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):                         #Iteration with checking for an empty nested list
        while self.cursor - self.list_len and self.nested_cursor == len(self.lst[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.nested_cursor += 1     
        return self.lst[self.cursor][self.nested_cursor - 1]


#def flat_generator(list: list) -> list:         #Generator func with one nesting level
#    return [x for sublist in list for x in sublist]

if __name__ == '__main__':                      
    
    for item in FlatIterator(nested_list):      #Output separated elements and flat_list of nested_list
        print(item)  
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    
#    for item in flat_generator(nested_list):    #Output elements from nested_list flatted by generator
#        print(item)

flat_list_1 = [x for sub in nested_list for x in sub]
print(flat_list_1)

