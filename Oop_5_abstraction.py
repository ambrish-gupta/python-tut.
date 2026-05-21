### ✨ Abstraction ✨
'''abstaction meaning is "hiddn" , it means hiding internal details and showing only what is nexessary to the user.'''
from abc import ABC ,abstractmethod
class BankApp(ABC):

    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass
    
# security implemente, how , it is hidden
# yha security implemented hai jo nhi dikh rhi jo abstractmethod ke andar hai
class MobileApp(BankApp):

    def mobile_login(self):
        print('login into mobile')

    def security(self):
        print('mobile security')

    def display(self):
        print('display')

mob = MobileApp()
mob.security()
mob.database()
mob.display()

'''in the building of application and websites we want that the app or website is sequre
then we can uh that abstraction method, after using this method another cannot use that without adding the abstract method.
(kisi website ya app ko safe rankne ya koi aur chiz ho jo hum bnate hai hum chahenge ku wo safe rhe isliye wha hum @abstraction method ka use kar sakte hai.)'''
### we cannot make object of abstract class.