class PhoneBook:
    def __init__(self):
        self.book = dict()

    def add(self, number, name):
        self.book[number] = name

    def find(self, number):
        try:
            print(self.book[number])
        except:
            print('not found')

    def delete(self, number):
        if number in self.book:
            del self.book[number]

book = PhoneBook()
n = int(input())
for i in range(n):
    line = input()
    params = line.split()
    if params[0] == 'add':
        book.add(params[1], params[2])
    elif params[0] == 'find':
        book.find(params[1])
    elif params[0] == 'del':
        book.delete(params[1])


