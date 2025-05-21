class MemberName:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName

class Book:
        def __init__(self, Id, Title, Author, Year):
            self.Id = Id
            self.Title = Title
            self.Author = Author
            self.Year = Year

class Member:
    def __init__(self, Name=None, Id=None, BorrowList=None):
        if Name != None:
            self.Name = Name
        else:
            self.Name = ("","")
        self.Id = Id
        if BorrowList != None:
            self.BorrowList = BorrowList
        else:
            self.BorrowList = []



            


