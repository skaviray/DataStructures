class Heap:
    array = []
    size = len(array)
    def __get_parent(self, index: int) -> int:
        print(index)
        print(int((index - 1 )/ 2))
        return int((index - 1 )/ 2)

    def __get_left(self,index: int) -> int:
        return index * 2  + 1
    
    def __get_right(self,index: int) -> int:
        return index * 2 + 2
    
    def __swap(self, first_index: int, second_index: int) -> None:
        print("swapping")
        tmp = self.array[first_index]
        self.array[first_index] = self.array[second_index]
        self.array[second_index] = tmp

    def __bubble_up(self) -> None:
        # print("bubblingup")
        index = self.size - 1
        print(self.size)
        print(index > 0)
        if index > 0:
         print(self.array[index])
         print(self.array[self.__get_parent(index)])

         print(self.array[index] < self.array[self.__get_parent(index)])
        while(index > 0 and self.array[index] > self.array[self.__get_parent(index)]):
            self.__swap(index, self.__get_parent(index))
            index = self.__get_parent(index)
    
    def insert(self, item: int) -> None:
        self.array.append(item)
        self.size +=1
        self.__bubble_up()
    