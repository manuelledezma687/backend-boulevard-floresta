class Account:
    id = int
    Name = str
    Surname = str
    Document = int
    Country = str
    state = str
    Nickname = str
    phone_number = int
    email = str
    password = str
    Address = str

class user (Account):
     def __init__(self,id,Name, Adress):
        super.__init__(id,Name,Adress)
        

class salesperson(Account):
    def __init__(self,id,Name,store,Adress):
        super.__init__(id,Name,Adress)
        self.store = store
