from email.policy import default


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


def AddPerson(personList, idVar, error):
    error = False;
    firstName = "temp"
    lastName = "temp"

    print("\n\n\nDodawanie nowej osoby do biblioteki: ");
    print("Imie: ")
    
    while True:
        firstName = str(input())
        if(firstName == None):
            print("Imie nie moze byc puste, podaj prawdziwa wartosc: ")
        else: break;
    
    while True:
        lastName = str(input())
        if(lastName == None):
            print("Imie nie moze byc puste, podaj prawdziwa wartosc: ")
        else: break;

    firstName = firstName.lower()
    lastName = lastName.lower()

    nameTemp = MemberName(firstName, lastName)
    personTemp = Member(nameTemp, idVar, borrowList = None)
    personList.append(personTemp)


def SearchPerson(personList, error, idVar = -1, firstName = "", lastName = ""):
    error = False

    firstName = firstName.lower()
    lastName = lastName.lower()

    if(idVar != 1):
        for person in personList:
            if(person.Id == idVar):
                memberTemp = person
                break

        if(memberTemp == None):
            error = True
    return memberTemp

def SearchBook(bookList, bookId, error):
    error = False
    bookTemp = Book(-1,"","",-1)

    for book in bookList:
        if(book.Id == bookId):
            bookTemp = book

    if(bookTemp.Year == -1):
        error = True

    return bookTemp

def AddBook(bookToAdd, personBorrowing, error):
    error = False
    if(personBorrowing != None):
        personBorrowing.BorrowList.append(bookToAdd)
    else: error = True;


def RemoveBook(bookToRemove, personBorrowing, error):
    error = False
    personBorrowing.BorrowList.remove(bookToRemove)

error = False
hasBooks = True

memberList = Member(None)
bookList = Book(None)


idVar = 0
input1 = -1;
input2 = -1;
input3 = -1;
input4 = -1;
personIdSearch = -1
bookIdSearch = -1

bookList.append(0, "the vanishing half", "brit bennett", 2020)
bookList.append(1, "the september house", "carissa orlando", 2023)
bookList.append(2, "harry potter and the philosopher's stone", "j.k. rowling", 1997)

while (input !=-6):
    print("Co Chcesz zrobic? Wybierz odpowiedni numer:")
    print("1: Dodaj osobe do biblioteki")
    print("2: Wyszukaj osobe")
    print("3: Dodaj ksiazke do osoby")
    print("4: Usun ksiazke od osoby")
    print("5: Wyswietl wszystkie osoby oraz wypozyczone ksiazki")
    print("6: Wyjdz z programu\n")

    print("Wybor: ")
    try:
        input1 = int(input())
    except:
        print("Nieprawidlowy input\n\n")


        if(input1 == 1):
            AddPerson(memberList, idVar, error)
            print(f"Osoba dodana pomyslnie (Id: {idVar - 1})")
            break
        if(input1 == 2):
            print("Wybierz odpowiedni numer wyszukiwania:")
            print("1: Imie i nazwisko")
            print("2: Id\n")
            print("Wybor: ")
            try:
                input1 = int(input())
            except:
                print("Nieprawidlowy input\n\n")

                if(input2 == 1):
                        print("\n\n\nWyszukiwanie po imieniu i nazwisku: \n")
                        print("Imie: ")
                        firstNameSearch = input()
                        print("Nazwisko: ")
                        lastNameSearch = input()
                        personTemp = SearchPerson(memberList, error, -1, firstNameSearch, lastNameSearch)

                        if(error == False and personTemp != None):
                            print("Informacje osoby wyszukiwanej:\n")
                            print((f"Id: {personTemp.Id}    Imie: {personTemp.Name.FirstName}    Nazwisko: {personTemp.Name.LastName}\n"))
                            hasBooks = False
                            for book in personTemp.BorrowList:
                                print(f"Autor:  {book.Author}    Id:  << {book.Id} <<    Tytul:  << {book.Title} <<    Rok: << {book.Year}")
                                hasBooks = True
                            if(hasBooks == False):
                                print("Brak wypozyczonych ksiazek")
                            else:
                                print("BLAD PODCZAS WYSZUKIWANIA")
                                error = False
                        print("\n\n\n")
                        personTemp = None
                        break

                if(input2 == 2):
                        print("\n\n\nWyszukiwanie Id: \n")
                        print("Id: ")
                        try:
                            personIdSearch = int(input())
                        except:
                            print("Nieprawidlowy input\n")
                        personTemp = SearchPerson(memberList, error, personIdSearch, "", "")

                        if(error == False and personTemp != None):
                            print("Informacje osoby wyszukiwanej:\n")
                            print((f"Id: {personTemp.Id}    Imie: {personTemp.Name.FirstName}    Nazwisko: {personTemp.Name.LastName}\n"))
                            hasBooks = False
                            for book in personTemp.BorrowList:
                                print(f"Autor:  {book.Author}    Id:  << {book.Id} <<    Tytul:  << {book.Title} <<    Rok: << {book.Year}")
                                hasBooks = True
                            if(hasBooks == False):
                                print("Brak wypozyczonych ksiazek")
                            else:
                                print("BLAD PODCZAS WYSZUKIWANIA")
                                error = False
                        print("\n\n\n")
                        personTemp = None
                        break
        if(input1 == 3):
            print("Wybierz odpowiedni sposob wyszukiwania wypozyczajacego:")
            print("1: Imie i nazwisko")
            print("2: Id\n")
            print("Wybor: ")
            try:
                input3 = int(input())
            except:
                print("Nieprawidlowy input\n")

                if(input3 == 1):
                    print("\n\n\nImie i nazwisko wypozycajacego: ")
                    print("Imie: ")
                    firstNameSearch = input()
                    print("Nazwisko: ")
                    lastNameSearch = input()
                    print("Id ksiazki: ")
                    try:
                        bookIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n")
                        break
                    personTemp = SearchPerson(memberList, error, -1, firstNameSearch, lastNameSearch)
                    bookTemp = SearchBook(bookList, bookIdSearch, error)

                    if(error == False and bookTemp != None and personTemp != None):
                        AddBook(bookTemp, personTemp, error)
                        print("Ksiazka dodana pomyslnie\n\n\n\n")
                    else:
                        print("BLAD PODCZAS WYSZUKIWANIA OSOBY LUB KSIAZKI\n\n\n\n")
                        error = False

                    personTemp = None
                    bookTemp = None
                    break

                if(input3 == 2):
                    print("\n\n\nId wypozyczajacego: \n")
                    try:
                        personIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n\n")
                        break
                    print("\n\n\nId ksiazki: \n")
                    try:
                        bookIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n\n")
                        break

                    personTemp = SearchPerson(memberList, error, personIdSearch, "", "")
                    bookTemp = SearchBook(bookList, bookIdSearch, error)

                    if(error == False and bookTemp != None and personTemp != None):
                        AddBook(bookTemp, personTemp, error)
                        print("Ksiazka dodana pomyslnie\n\n\n\n")
                    else:
                        print("BLAD PODCZAS WYSZUKIWANIA OSOBY LUB KSIAZKI\n\n\n\n")
                        error = False

                    personTemp = None
                    bookTemp = None
                    break
        if(input1 == 4):
            print("Wybierz odpowiedni sposob wyszukiwania wypozyczajacego:")
            print("1: Imie i nazwisko")
            print("2: Id\n")
            print("Wybor: ")
            try:
                input3 = int(input())
            except:
                print("Nieprawidlowy input\n")

                if(input4 == 1):
                    print("\n\n\nImie i nazwisko wypozycajacego: ")
                    print("Imie: ")
                    firstNameSearch = input()
                    print("Nazwisko: ")
                    lastNameSearch = input()
                    print("Id ksiazki: ")
                    try:
                        bookIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n")
                        break
                    personTemp = SearchPerson(memberList, error, -1, firstNameSearch, lastNameSearch)
                    bookTemp = SearchBook(bookList, bookIdSearch, error)

                    if(error == False and bookTemp != None and personTemp != None):
                        RemoveBook(bookTemp, personTemp, error)
                        print("Ksiazka usunieta pomyslnie\n\n\n\n")
                    else:
                        print("BLAD PODCZAS WYSZUKIWANIA OSOBY LUB KSIAZKI\n\n\n\n")
                        error = False

                    personTemp = None
                    bookTemp = None
                    break

                if(input4 == 2):
                    print("\n\n\nId wypozyczajacego: \n")
                    try:
                        personIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n\n")
                        break
                    print("\n\n\nId ksiazki: \n")
                    try:
                        bookIdSearch = int(input())
                    except:
                        print("Nieprawidlowy input\n\n")
                        break

                    personTemp = SearchPerson(memberList, error, personIdSearch, "", "")
                    bookTemp = SearchBook(bookList, bookIdSearch, error)

                    if(error == False and bookTemp != None and personTemp != None):
                        RemoveBook(bookTemp, personTemp, error)
                        print("Ksiazka usunieta pomyslnie\n\n\n\n")
                    else:
                        print("BLAD PODCZAS WYSZUKIWANIA OSOBY LUB KSIAZKI\n\n\n\n")
                        error = False

                    personTemp = None
                    bookTemp = None
                    break
        if(input1 == 5):
            for person in memberList:
                print("Informacje osoby wyszukiwanej:\n ")
                print(f"id:   {person.Id}     Imie:   {person.Name.FirstName}     Nazwisko:   {person.Name.LastName}  \n")
                print("Wypozyczone ksiazki:\n\n ")
                hasBooks = False

                for book in person.BorrowList:
                    print(f"Autor:   {book.Author}     id:   {book.Id}     Tytul:   {book.Title}     Rok:   {book.Year}")
                    hasBooks = True

                if(hasBooks == False):
                    print("Brak wypozyczonych ksiazek")

            print("\n\n\n")
            break



