monthDays = (1900 , 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31)
monthNames = ('/' , 'Jan' , 'Feb' , 'March' , 'Apr' , 'May' , 'Jun' , 'July' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec')
dayNames = ('Saturday','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
class Date:

    def __init__(self):
        self.y = 1900
        self.m = 1
        self.d = 1
    
    def isLeap(self,year: int) -> bool:
        if year % 100 == 0 and year % 400 == 0 :
            return True
        elif year % 100 != 0 and year % 4 == 0 :
            return True
        else :
            return False

    def get(self) -> None:
        print("Enter Date : ")

        self.y = int(input(" Year : "))
        while self.y < 1900 or self.y > 3000 :
            print("Out Of Range ...")
            self.y = int(input("Year : "))
        
        self.m = int ( input ( " Month : ") )
        while self.m < 1 or self.m > 12 :
            print (" Out of Range ...")
            self.m = int ( input ( " Month : ") )
        
        daylimit = monthDays[self.m]
        if self.m == 2 and self.isLeap(self.y) == True :
            daylimit = 29

        self.d = int ( input ( " Day : ") )
        while self.d < 1 or self.d > daylimit :
            print (" Out of Range ...")
            self.d = int ( input ( " Day : ") )

    def showMenu(self) -> None :
        print (" Select Show Mode ")
        print (" 0 = 2/25/2000 ")
        print (" 1 = 25/Feb/2000 ")
        print (" 2 = Friday/25/Feb/2000 ")
        ans = int(input("Enter choise : "))
        if ans == 0 or ans == 1 or ans == 2 :
            self.show(ans)
        else :
            print (" Out of Range ...")
            
    def show(self , selector = 0) -> None :
        if selector == 0 :
            print (self.m,self.d,self.y,sep=monthNames[0])
        elif selector == 1 :
            print (self.d,monthNames[self.m],self.y,sep=monthNames[0])
        elif selector == 2 :
            print (self.dow(),self.d,monthNames[self.m],self.y,sep=monthNames[0])

    def dow(self) -> str :
        month = self.m
        day = self.d
        year = self.y
        if month == 1 :
            month = 13
            year = year - 1
     
        if month == 2 :
            month = 14
            year = year - 1
        q = day
        m = month
        k = year % 100
        j = year // 100
        h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
        h = h % 7
        return dayNames[h]

    def sum(self , day: int) -> None :
        self.d += day
        i = self.m
        while self.d > monthDays[i] :
            if i == 12 :
                self.d -= monthDays[i]
                self.y += 1
                if self.isLeap(self.y) :
                    self.d -= 1
                self.m = 1
                i = 1  
            else :              
                self.d -= monthDays[i]
                self.m += 1
                i += 1
        d.showMenu()

d = Date()
d.get()
d.showMenu()
x = int(input("How Many Days Do U Want To Add ? "))
d.sum(x)