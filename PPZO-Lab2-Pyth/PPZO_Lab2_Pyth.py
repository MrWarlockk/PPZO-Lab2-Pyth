

class MemberName:
    def __init__(self, FirstName, LastName):
        if (FirstName != None):
            self.FirstName = FirstName
        else:
            self.FirstName = ""

        if (LastName != None):
            self.LastName = LastName
        else:
            self.LastName = ""

class Book:
        def __init__(self, Id = None, Title = None, Author = None, Year = None):
            if (Id != None):
                self.Id = Id
            else:
                self.Id = -1

            if (Title != None):
                self.Title = Title
            else:
                self.Title = ""

            if (Author != None):
                self.Author = Author
            else:
                self.Author = ""

            if (Year != None):
                self.Year = Year
            else:
                self.Year = -1

class Member:
    def __init__(self, Name=None, Id=None, BorrowList = None):
        if (Name != None):
            self.Name = Name
        else:
            self.Name = MemberName(None, None)

        if (Id != None):
            self.Id = Id
        else:
            self.Id = -1

        if (BorrowList != None):
            self.BorrowList = BorrowList
        else:
            self.BorrowList = []


def AddPerson(personList, idVar):
    firstName = ""
    lastName = ""

    print("\nDodawanie nowej osoby do biblioteki: ");
    firstName = input("Imie: ")
    lastName = input("Nazwisko: ")

    firstName = firstName.lower()
    lastName = lastName.lower()

    borrowList = []

    nameTemp = MemberName(firstName, lastName)
    personTemp = Member(nameTemp, idVar)
    personList.append(personTemp)
    idVar = idVar+1
    
    return idVar

def SearchPerson(personList, idVar = -1, firstName = "", lastName = ""):
    memberTemp = Member()
    firstName = firstName.lower()
    lastName = lastName.lower()

    if(idVar != -1):
        for person in personList:
            if(person.Id == idVar):
                memberTemp = person
                break

    else:
        for person in personList:
            if(person.Name.FirstName == firstName and person.Name.LastName == lastName):
                memberTemp = person
                break

    if(memberTemp.Id == -1 or memberTemp.Name.FirstName == ""):
        print ("Osoby nie znaleziono\n\n")
        return Member();



    return memberTemp

def SearchBook(bookList, bookId):

    for book in bookList:
        if(book.Id == bookId):
            bookTemp = book
            return bookTemp

    print ("Ksiazki nie znaleziono\n\n")
    return Book()

def AddBook(bookToAdd, personBorrowing):
    if(personBorrowing != None):
        personBorrowing.BorrowList.append(bookToAdd)
    else:
        print("Nie udalo sie dodac ksiazki\n\n")


def RemoveBook(bookToRemove, personBorrowing):
    if(personBorrowing != None and bookToRemove in personBorrowing.BorrowList):
        personBorrowing.BorrowList.remove(bookToRemove)
        return True

    else:
        print("Nie udalo sie usunac ksiazki\n\n")
        return False

hasBooks = True

memberList = [Member()]
bookList = [Book()]


idVar = 0
input1 = -1;
input2 = -1;
input3 = -1;
input4 = -1;
personIdSearch = -1
bookIdSearch = -1

bookList.append(Book(0, "the vanishing half", "brit bennett", 2020))
bookList.append(Book(1, "the september house", "carissa orlando", 2023))
bookList.append(Book(2, "harry potter and the philosopher's stone", "j.k. rowling", 1997))

while (input !=-6):
    print("Co Chcesz zrobic? Wybierz odpowiedni numer:")
    print("1: Dodaj osobe do biblioteki")
    print("2: Wyszukaj osobe")
    print("3: Dodaj ksiazke do osoby")
    print("4: Usun ksiazke od osoby")
    print("5: Wyswietl wszystkie osoby oraz wypozyczone ksiazki")
    print("6: Wyjdz z programu\n")

    try:
        input1 = int(input("Wybor: "))
    except ValueError:
        print("Nieprawidlowy input\n\n")

    while True:
            if(input1 == 1):
                idVar = AddPerson(memberList, idVar)
                print(f"Osoba dodana pomyslnie (Id: {idVar - 1})\n\n")
                break
            if(input1 == 2):
                print("Wybierz odpowiedni numer wyszukiwania:")
                print("1: Imie i nazwisko")
                print("2: Id\n")
                try:
                    input2 = int(input("Wybor: "))
                except ValueError:
                    print("Nieprawidlowy input\n\n")

                if(input2 == 1):
                    print("\nWyszukiwanie po imieniu i nazwisku: \n")
                    firstNameSearch = input("Imie: ")
                    lastNameSearch = input("Nazwisko: ")
                    personTemp = SearchPerson(memberList, -1, firstNameSearch, lastNameSearch)

                    if(personTemp.Id != -1):
                        print("Informacje osoby wyszukiwanej:\n")
                        print((f"Id: {personTemp.Id}    Imie: {personTemp.Name.FirstName}    Nazwisko: {personTemp.Name.LastName}\n"))
                        hasBooks = False
                        for book in personTemp.BorrowList:
                            print(f"Autor:  {book.Author}    Id:   {book.Id}     Tytul:   {book.Title}     Rok:  {book.Year}")
                            hasBooks = True
                        if(hasBooks == False):
                            print("Brak wypozyczonych ksiazek")
                    personTemp = None
                    break

                if(input2 == 2):
                    print("\nWyszukiwanie po Id: \n")
                    try:
                        personIdSearch = int(input("Id: "))
                    except ValueError:
                        print("Nieprawidlowy input\n")
                    personTemp = SearchPerson(memberList, personIdSearch, "", "")

                    if(personTemp != None and personTemp.Name.FirstName != "" and personTemp.Id != -1):
                        print("Informacje osoby wyszukiwanej:\n")
                        print((f"Id: {personTemp.Id}    Imie: {personTemp.Name.FirstName}    Nazwisko: {personTemp.Name.LastName}\n"))
                        hasBooks = False
                        for book in personTemp.BorrowList:
                            print(f"Autor:  {book.Author}    Id:   {book.Id}     Tytul:   {book.Title}     Rok:  {book.Year}")
                            hasBooks = True
                        if(hasBooks == False):
                            print("Brak wypozyczonych ksiazek")
                    personTemp = None
                    break
                else: break
            
            if(input1 == 3):
                print("Wybierz odpowiedni sposob wyszukiwania wypozyczajacego:")
                print("1: Imie i nazwisko")
                print("2: Id\n")
                try:
                    input3 = int(input("Wybor: "))
                except ValueError:
                    print("Nieprawidlowy input\n")

                if(input3 == 1):
                    print("\nImie i nazwisko wypozycajacego: ")
                    firstNameSearch = input("Imie: ")
                    lastNameSearch = input("Nazwisko: ")
                    try:
                        bookIdSearch = int(input("Id ksiazki: "))
                    except ValueError:
                        print("Nieprawidlowy input\n")
                        break
                    personTemp = SearchPerson(memberList, -1, firstNameSearch, lastNameSearch)
                    bookTemp = SearchBook(bookList, bookIdSearch)

                    if(bookTemp.Id != -1 and personTemp.Id != -1 and personTemp.Name.FirstName != ""):
                        AddBook(bookTemp, personTemp)
                        print("Ksiazka dodana pomyslnie\n\n")

                    personTemp = None
                    bookTemp = None
                    break

                if(input3 == 2):
                    try:
                        personIdSearch = int(input("\nId wypozyczajacego: "))
                    except ValueError:
                        print("Nieprawidlowy input\n\n")
                        break
                    try:
                        bookIdSearch = int(input("\nId ksiazki: "))
                    except ValueError:
                        print("Nieprawidlowy input\n\n")
                        break

                    personTemp = SearchPerson(memberList, personIdSearch, "", "")
                    bookTemp = SearchBook(bookList, bookIdSearch)

                    if(bookTemp.Id != -1 and personTemp.Id != -1 and personTemp.Name.FirstName != ""):
                        AddBook(bookTemp, personTemp)
                        print("Ksiazka dodana pomyslnie\n\n")

                    personTemp = None
                    bookTemp = None
                    break
                else:
                    break
            if(input1 == 4):
                print("Wybierz odpowiedni sposob wyszukiwania wypozyczajacego:")
                print("1: Imie i nazwisko")
                print("2: Id\n")
                try:
                    input4 = int(input("Wybor: "))
                except ValueError:
                    print("Nieprawidlowy input\n")

                if(input4 == 1):
                    print("\nImie i nazwisko wypozycajacego: ")
                    firstNameSearch = input("Imie: ")
                    lastNameSearch = input("Nazwisko: ")
                    try:
                        bookIdSearch = int(input("Id ksiazki: "))
                    except ValueError:
                        print("Nieprawidlowy input\n")
                        break
                    personTemp = SearchPerson(memberList, -1, firstNameSearch, lastNameSearch)
                    bookTemp = SearchBook(bookList, bookIdSearch)

                    if(bookTemp.Id != -1 and personTemp.Id != -1 and personTemp.Name.FirstName != ""):
                        RemoveBook(bookTemp, personTemp)
                        if(removeBookOutcome == True):
                            print("Ksiazka usunieta pomyslnie\n\n")

                    personTemp = None
                    bookTemp = None
                    break

                if(input4 == 2):
                    try:
                        personIdSearch = int(input("\nId wypozyczajacego: "))
                    except ValueError:
                        print("Nieprawidlowy input\n\n")
                        break
                    try:
                        bookIdSearch = int(input("\nId ksiazki: "))
                    except ValueError:
                        print("Nieprawidlowy input\n\n")
                        break

                    personTemp = SearchPerson(memberList, personIdSearch, "", "")
                    bookTemp = SearchBook(bookList, bookIdSearch)

                    if(bookTemp.Id != -1 and personTemp.Id != -1 and personTemp.Name.FirstName != ""):
                        removeBookOutcome = RemoveBook(bookTemp, personTemp)
                        if(removeBookOutcome == True):
                            print("Ksiazka usunieta pomyslnie\n\n")


                    personTemp = None
                    bookTemp = None
                    break
                else:
                    break
            if(input1 == 5):
                for person in memberList:
                    if(person.Id != -1): 
                        print("\nInformacje osoby wyszukiwanej:\n ")
                        print(f"id:   {person.Id}     Imie:   {person.Name.FirstName}     Nazwisko:   {person.Name.LastName}  \n")
                        print("Wypozyczone ksiazki:\n\n ")
                        hasBooks = False

                        for book in person.BorrowList:
                            print(f"Autor:   {book.Author}     id:   {book.Id}     Tytul:   {book.Title}     Rok:   {book.Year}")
                            hasBooks = True

                        if(hasBooks == False):
                            print("Brak wypozyczonych ksiazek")
                    print("\n\n")

                break
            else:
                break