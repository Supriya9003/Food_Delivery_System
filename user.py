from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id, name, phone, email, password):
        self.__user_id = user_id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password
    

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            print(f'Welcome {self.__name}')
            return True
        print('Invalid Email or Password')
        return False

    def logout(self):
        print(f'Thank You {self.__name}')

    @abstractmethod
    def display_profile(self):
        pass










class Customer:
    def __init__(self,customer_id,customer_name,phone,email,password,address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address

        self.orders = []    

    def get_name(self):
        return self.customer_name  
    
    def login(self,email,password):
        return self.email,self.password
    
    def add_order(self,order):
        self.orders.append(order)
    
    def display_orders(self):
        if not self.orders:
            print("No orders found.")
            return
        
        for order in self.orders:
            print(order)
             
class RestaurantOwner:
    def __init__(self,owner_id,ower_name,phone,email_id,password,restaurant_name):
        self.owner_id = owner_id
        self.owner_name = ower_name
        self.phone = phone
        self.email_id = email_id
        self.password = password
        self.restaurant_name = restaurant_name
        

