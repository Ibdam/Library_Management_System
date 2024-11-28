"""This is Library Management system that monitors all books, transactions and members information in the library."""

"""DEVELOPED BY DAMILOLA IBRAHIM"""

"""Defining the book class to manage all book information"""
 
class Book:
    def __init__(self, name, author, isbn):
        self.name= name
        self.author= author
        self.isbn= isbn

    """This function display the information of the book"""

    def display_info(self):
        print(f'Title: {self.name}, Author: {self.author}, ISBN: {self.isbn}')

"""Defining class for a library to manage all libraries information"""

class Library(Book):
    def __init__(self, name, author, isbn, availability= 'Available'):
        """This call the constructor of the parent class Book"""
        super().__init__(name, author, isbn)
        self.availability= availability
    
    book={'Name':[], 'Author': [], 'ISBN': [], 'Status': []}

    """This method can be used add book to the library"""

    def add_book (self):
        self.book['Name'].append(self.name)
        self.book['Author'].append(self.author)
        self.book['ISBN'].append(self.isbn)
        self.book['Status'].append(self.availability)
        print(f'Book name: {self.name} is succesfully added, here is the information of the book you added')
        

    """This method can be used to borrow book from the library and give output if no book is found in the library"""

    def borrow_book(self, borrow_name):

        if borrow_name in self.book['Name']:
            borrow_index= self.book['Name'].index(borrow_name)
            self.book['Name'].pop(borrow_index)
            self.book['Author'].pop(borrow_index)
            self.book['ISBN'].pop(borrow_index)
            self.book['Status'].pop(borrow_index)
            print(f'Book: {borrow_name} is successfully borrowed')
      
        else:
            print(f'Book name: {borrow_name} you are trying to find in not available')

    """This method can be used to check all the available books present in the library and give output if no books is found in the library"""

    def available_books(self):
        if self.book:
            print('Here are the available books')
            name_list= list(self.book['Name'])
            author_list= list(self.book['Author'])
            isbn_list= list(self.book['ISBN'])
            status_list= list(self.book['Status'])
            for index, (name_list, author_list, isbn_list, status_list) in enumerate(zip(name_list, author_list, isbn_list, status_list), start= 1):
                print(f'{index}. Title: {name_list}, Author: {author_list}, ISBN: {isbn_list}, Status: {status_list}')
        
        else:
            print('No book is available, kindly check back later')

    """This method is to search for a book in the library and give output if the book is not found"""

    def book_search(self, search_name):
        if search_name in self.book['Name']:
            search_index= self.book['Name'].index(search_name)
            v1= self.book['Author'][search_index]
            v2= self.book['ISBN'][search_index]
            print(f'Title: {search_name} Author: {v1}, ISBN: {v2}, Status: {self.availability}')
        else:
            print('The book you are trying to find is not available')

"""This class manage the library member information"""

class Member:
    def __init__(self, name, age, department):
        self.name= name
        self.age= age
        self.department= department

    """This method display library member information"""

    def member_info(self):
        return f'Name: {self.name}, Age: {self.age}, Department: {self.department}'
    
    """This method is to add member to the library"""

    members= {'Name': [], 'Age': [], 'Department': []}
    def add_member(self):
        self.members['Name'].append(self.name)
        self.members['Age'].append(self.age)
        self.members['Department'].append(self.department)
        print(f'{self.member_info()} is successfully added')

    """This method is to check for a member and give output of the member is not found in the library"""

    def check_member(self, check_name):
        if check_name in self.members['Name']:
            check_index= self.members['Name'].index(check_name)
            v3= self.members['Age'][check_index]
            v4= self.members['Department'][check_index]
            print(f'Name: {check_name}, Age: {v3}, Department: {v4}')

        else:
            print('The member you tried to check is not available')
        
    """This method is to view all the members in the library"""

    def all_members(self):
        name_list= list(self.members['Name'])
        age_list= list(self.members['Age'])
        department_list= list(self.members['Department'])
        for index, (name_list, age_list, department_list) in enumerate(zip (name_list, age_list, department_list), start= 1):
            print(f'{index}. Name: {name_list}, Age: {age_list}, Department: {department_list}')

    """This class can be used to run the library system"""

class LibraryManagementSystem:

    """This method is to run the system"""

    def run(self):
        pass
        while True:
            try:
                print('\nWelcome to our library, kindly enjoy our operation')
                print('1. Add book to the library')
                print('2. Borrow book from the library')
                print('3. Return book to the library')
                print('4. Search for a book')
                print('5. Check all available books')
                print('6. Add member to the library')
                print('7. Search for a member')
                print('8. All available members')
                print('9. Exit')

                option= int(input('Enter the operation to perform: ').strip())
                if option == 1 or option == 3:
                    name= input('Enter name: ').strip().capitalize()
                    author= input('Enter author: ').strip().capitalize()
                    isbn= input('Enter ISBN number: ').strip().capitalize()
                    library= Library(name, author, isbn)
                    library.add_book()
                    library.display_info()

                elif option == 2:
                    borrow_name= input('Enter the name of the book to borrow: ').capitalize()
                    library.borrow_book(borrow_name)

                elif option == 4:
                    search_name= input('Enter the name of the book to search: ').capitalize()
                    library.book_search(search_name)


                elif option == 5:
                    library.available_books()
                
                elif option == 6:
                    name= input('Enter your name: ').strip().capitalize()
                    age= int(input('Enter your age: ').strip())
                    department= input('Enter your department: ').strip().capitalize()
                    member= Member(name, age, department)
                    member.add_member()

                elif option == 7:
                    search_name= input('Enter the name of the member you are trying to check: ').capitalize( )
                    member.check_member(search_name)

                elif option == 8:
                    member.all_members()

                elif option == 9:
                    print('Thank you for using our library system, have a nice day')
                    break

                else:
                    break

            except NameError:
                print('No book or member in the library, kindly add book or member to the library.')

            except ValueError:
                print('Please input the correct value')

if __name__== '__main__':
    library= LibraryManagementSystem()
    library.run()
