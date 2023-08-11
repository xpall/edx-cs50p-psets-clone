class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return '🍪' * self.size


    def deposit(self, n):
        if (self.size + n) < self.capacity:
            self._size += n
        else:
            raise ValueError('Jar is full')


    def withdraw(self, n):
        if (self.size - n) > 0:
            self._size -= n
        else:
            raise ValueError('Jar is empty')


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


def main():
    only_jar = Jar(50)
    only_jar.deposit(40)
    only_jar.withdraw(25)
    print(only_jar.size)
    print(only_jar)


if __name__ == "__main__":
    main()