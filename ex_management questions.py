#Hospital management system
'''
class hospital():
    def ptadmission(self):
        ward=input('Enter type of ward: ').lower()
        ward_assign=f'Patient admitted to {ward.upper()} ward'
        if ward == "icu":
            return ward_assign
        elif ward == "general":
            return ward_assign
        elif ward == "maternity":
            return ward_assign
        else:
            print("patient came here for consultation only")

    
    def doc_appt(self):
        print('Type 1 for cardiologist','\nType 2 for Dermatologist','\nType 3 for Neurologist', '\nType 4 for Orthopedic')
        specialist=int(input('Enter type of specialization: '))
        if specialist == 1:
            return 'Cardiologist appointment'
        elif specialist == 2:
            return 'Dermatologist appointment'
        elif specialist == 3:
            return 'Neurologist appointment'
        elif specialist == 4:
            return 'Orthopedic appointment'
        else:
            return 'No doctor available'

    
    def medicine_stocks(self):
        num_medicines=int(input("Enter the number of medicines: "))
        stock_level=[]
        for i in range(num_medicines):

            stock=int(input(f"Enter stocks for medicine {i+1}:"))
            stock_level.append(stock)
        #print('/n medicine stock status:')
        print(stock_level)
        result=[]
        for i in range(len(stock_level)):
            if stock_level[i]>500:
                status='Overstocked'
            elif 200<=stock_level[i]<=500:
                status='Sufficient Stock'
            else:
                status='Restock Needed'
            result.append(f"Medicine {i+1}: {status}")

        return result

    
    def billing(self):
        print('Enter 1 for General consulatation','\nEnter 2 for X-Ray', '\nEnter 3 for Surgery', '\nEnter 4 for ICU stay')
        treatment = int(input("Enter type of treatment: "))

        if treatment == 1:
            return "Treatment type is General consultation and final bill is Rs.500"
        elif treatment == 2:
            return "Treatment type is X-Ray and final bill is Rs.1500"
        elif treatment == 3:
            return "Treatment type is Surgery and final bill is Rs.50000"
        elif treatment == 4:
            num_stays=int(input("Enter number of days in hospitalization: "))
            return "Treatment type is ICU and final bill is ", num_stays*10000
    
hms = hospital()
print(hms.ptadmission())
print(hms.doc_appt())
print(hms.medicine_stocks())
print(hms.billing())'''

#Library Management system

'''class library():
    print("Membership types are premium, regular and guest")
    
    def __init__(self):
        
        self.membership = input('Enter Type of Membership: ').lower()
        self.bookcount = int(input('Enter number of books borrowed:'))
        self.month_count = int(input("Enter number of months:"))
        self.n = int(input("Enter number of days delayed to return the book: "))
        self.num_books=int(input("Enter the number of books for stocks: "))
        
    def book_borrow(self):
        
        if self.membership == "premium":
            
            if self.bookcount <= 5:
                return 'Books allowed for 30 days only'
            else:
                return 'More than 5 books are not allowed'
            
        elif self.membership == "regular":
            
            if self.bookcount <= 3:
                return 'Books allowed for 15 days'
            else:
                return 'More than 3 books are not allowed'
            
        elif self.membership == "guest":
            
            if self.bookcount <= 1:
                return 'Book allowed for 7 days'
            else:
                return 'More than 1 book is not allowed'
            
        else:
            print("Please check membership type!")

    def book_return(self):
        
        if self.n == 0:
            return "No fine"
        elif 1 < self.n <= 5:
            return "Fine amount is",self.n*10
        else:
            return "Fine amount is",self.n*20
        
    def book_stock(self):
        
        stock_level=[]
        
        for i in range(self.num_books):

            stock=int(input(f"Enter stocks for book {i+1}:"))
            stock_level.append(stock)
        print(stock_level)
        result=[]
        
        for i in range(len(stock_level)):
            if stock_level[i]>100:
                status='Overstocked'
            elif 50<=stock_level[i]<=100:
                status='Sufficient'
            else:
                status='Restock Needed'
            result.append(f"Book {i+1}: {status}")

        return result
    
    def membership_fee(self):
        
        if self.membership == "premium":
            return "Membership fee:", 5000/12*self.month_count
        elif self.membership == "regular":
            return "Membership fee:", 2500/12*self.month_count
        elif self.membership == "guest":
            return "Membership fee:", 500/12*self.month_count
        else:
            return "No other membership types are available"

lms = library()

print(lms.book_borrow())
print(lms.book_return())
print(lms.book_stock())
print(lms.membership_fee())

'''

#hotel booking and management system
'''
class hotel():
    print("Our Hotel provides three types of rooms: Luxury, Deluxe and Standard")
    print()
    print("Service Request Dial Numbers: 1 for Room cleaning, 2 for Laundry service, 3 for Food Delivery and 4 for Taxi Service")
    print()
    #def __init__(self):
        
        #self.room_type = input('Enter Type of Room: ').lower()
        #self.service_request = int(input('Enter number for service request: '))
        #self.days = int(input("How many nights needed: "))
    def room_booking(self):
        
        if self.room_type == "luxury":
            return f"Luxury room charges for {self.days} day(s) is", self.days*10000
            
        elif self.room_type == "deluxe":
            return f"Deluxe room charges for {self.days} day(s) is", self.days*7000
            
        elif self.room_type == "standard":
            return f"Standard room charges for {self.days} day(s) is", self.days*5000
            
        else:
            print("Service Not Available")

    def service_req(self):
        if self.service_request == 1:
            return "Room Cleaning"
        elif self.service_request == 2:
            return "laundry Service"
        elif self.service_request == 3:
            return "Food Delivery"
        elif self.service_request == 4:
            return "Taxi Service"
        else:
            return "Service Not Available"
            '''
        
'''def room_availability(self):
        #no.of rooms from user, if it's available show the room types and price
        num_rooms = int(input("Enter number of rooms: "))
        room_data = {
            'luxury':{'room_available':5, 'price': 10000},
            'deluxe':{'room_available':10, 'price':7000},
            'standard':{'room_available':7, 'price': 5000}
            }
        for key, room_info in room_data.items():
           # print(key,room_info)
            #if key == self.room_type in key:
            if num_rooms <= room_info['room_available']:
                return f"ROOM TYPE: {key}, PRICE: {room_info['price']}"
            else:
                return "Sorry, not enough rooms availble"
            
            return "Invalid room type"
                    '''

    
'''    def membership_fee(self):
        
        
            '''
#hotelmanagement = hotel()
#print(hotelmanagement.room_booking())
#print(hotelmanagement.room_availability())

#employee management system
'''
class employee():
    #A company wants an employee management system to track salaries, leave requests, performance, and promotions.
    
    def __init__(self):
        self.role = input('Enter name of the role: ')
        self.num_leaves = int(input("Enter number of days requesting for leave: "))
        self.performance_score = int(input('Enter number of performance evaluated annually: '))
        self.Exp = float(input('Enter number of years of experience: '))
        print()
    def sal_calc(self):
        if self.role == 'manager':
            return f"Salary for {self.role.capitalize()} is 100000 per month"
        elif self.role == 'software engineer':
            return f"Salary for {self.role.capitalize()} is 80000 per month"
        elif self.role == 'hr':
            return f"Salary for {self.role.upper()} is 60000 per month"
        elif self.role == 'intern':
            return f"Salary for {self.role.capitalize()} is 25000 per month"
        else:
            return "Invalid entry. Please check the spelling"
            
    def leave_req(self):
        if 1 < self.num_leaves < 3:
            return "Leave Approved"
        elif 4 < self.num_leaves < 7:
            return "Manager Approval Required for Leave"
        elif self.num_leaves >7:
            return "HR Approval Required for Leave"
        else:
            return "Leave Not Approved"
            
    def performance(self):
        appraisal_ratings = []
        for i in range(self.performance_score):
            score = int(input(f"Enter performance score for every quarterly{i+1}: "))
            appraisal_ratings.append(score)
        print(appraisal_ratings)
        
        global total_Score
        total_Score = 0
        for j in appraisal_ratings:
            total_Score = total_Score + j

        if total_Score > 90:
            return "Your performance in the last year was EXCELLANT"
        elif 70 <= total_Score <= 90:
            return "Your performance in the last year was GOOD"
        elif 50 <= total_Score <= 70:
            return "Your performance in the last year was NEED IMPROVEMENT"
        elif total_Score < 50:
            return "Your performance in the last year was PROBATION"

    def promotion(self):
        if self.Exp > 3 and total_Score> 80:
            return "Eligible for Promotion"
        else:
            return "No Promotion"
        
emp = employee()

print(emp.sal_calc())

print(emp.performance())

print(emp.leave_req())

print(emp.promotion())
'''

#5.school management system
class school():
    def __init__(self):
        self.grade = int(input("Enter Grade: "))
        self.marks = int(input("Enter marks: "))
        self.attendance = int(input("Enter number of days present: "))
        print('Fee for primary secion is 30000 per year, \nFee for middle section is 50000 per year, \nFee for senior section is 75000 per year')
        self.fee = input("FEE PAID OR NOT? ").lower()
    def std_Adm(self):
        if 1 <= self.grade <=5:
            return "Primary Section"
        elif 6 <= self.grade <= 10:
            return "Middle Section"
        elif 11 <= self.grade <=12:
            return "Senior Section"
        else:
            return "Please enter Grade between 1 and 12"

    def grade_calc(self):
        if self.marks >= 90:
            return "A Grade"
        elif 80 <= self.marks < 90:
            return "B Grade"
        elif 70 <= self.marks < 80:
            return "C Grade"
        else:
            return "Fail"

    def attd_track(self):
        attd = (self.attendance / 180) * 100
        if attd > 75:
            return "Eligible for Exams"
        elif 50 <= attd <= 75:
            return "Warning to attend Exams"
        else:
            return "Not Eligible for Exams"

    def fee_management(self):
        if self.fee == 'fully paid':
            return "No balance to show, fully paid"
        elif self.fee == "partially paid":
            paid amount
    
