'''HW_BookWorm '''
def worm():
    '''return max read book'''
    term = input()
    for i in range(term):
        minute = input()
        book = input()
        lists = []
        count = 0
        books = 0
        for _ in range(book):
            time = input()
            lists.append(time)
        lists.sort()
        for j in lists:
            if  books+j <= minute:
                books += j
                count += 1
        print count
worm()
