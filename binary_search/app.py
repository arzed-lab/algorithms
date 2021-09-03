list = []

for x in range(128):
    list.append(x)

class BinarySearch:
    def __init__(self,list, item):
        self.list = list
        self.item = item
    def searching(self):
        times = 0
        low = 0
        high = len(list) - 1
        while low <= high:
            times += 1
            mid = (low + high) // 2
            guess = self.list[mid]
            if guess == self.item:
                return guess, times
            elif guess > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None

if __name__ == '__main__':
    search_item = int(input('Input the int(0 < 128): '))
    result = BinarySearch(list, search_item).searching()
    print(f'Result: {result[0]}, Times: {result[1]} ')