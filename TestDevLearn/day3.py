#coding: utf-8

def day3():
    books = [{"name": "三国演义"}, {"name": "西游记"}]
    book = {"name": "水浒传"}
    books.insert(1, book)
    # book = {"name": "红楼梦"}
    book = [23, 34]
    books.append(book)
    print(books)
    books.extend(book)
    print(books)
    print(books[0: 2])
    del book
    print(books.insert(1, 11))
    books.pop(1)
    print("pop移除下标元素:%s"% books)
    books.reverse()
    print("reverse反向元素:%s"% books)
    test = books.copy()
    print("copy的作用：%s"% test)
    books.remove(23)
    print("remove:%s"% books)

def sorts():
    lists =["age", "name", "lss"]
    lists.sort(reverse= True)
    print(lists)

if __name__ == "__main__":
    # day3()
    sorts()



