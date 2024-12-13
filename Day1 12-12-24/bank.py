class Bank:
    accbal=25000
    t_count=0
    def deposit(self):
        amount=int(input('Enter amount to be deposited'))
        if amount<100:
            print('minimum amount should be 100')
        elif amount>50000:
            print('Amount should be below 50000' )
        else:
            if (amount%100)!=0:
                print('Amount should be multiples of 100')
            else:
                self.accbal += amount
                print(self.accbal)


    def withdraw(self):
            if(self.t_count<3):
                amount = int(input('Enter amount to withdraw'))
                flag=True
                if amount > self.accbal:
                    print('Amount should be below account balance')
                    flag = False
                if amount < 100:
                    print('minimum amount should be 100')
                    flag=False
                if (amount % 100) != 0:
                    print('Amount should be multiples of 100')
                    flag = False
                if self.accbal-amount < 500:
                    print('You should maintain min 500')
                    flag = False
                if amount>20000:
                    print('Limit exceeded')
                    flag=False
                if flag:
                    self.accbal-=amount
                    self.t_count+=1
                    print('balance',self.accbal)
            if self.t_count==3:
                print('transaction limit exceeded')
    def balance(self):
        print(self.accbal)
    def viewOptions(self):
        option=1
        while(option!=0):
            print('1.Deposit\n2.Withdraw\n3.Balance Enquiry\n4.Exit' )
            option=int(input('Choose the option'))
            if option==1:
                obj.deposit()
            elif option==2:
                obj.withdraw()
            elif option==3:
                obj.balance()
            elif option==4:
                print('You are exitted')
                exit(0)
            else:
                print('correct option')
    def validate(self):
        count = 0
        while (count < 3):
            pin = int(input('Enter pin number'))
            if pin == 1234:
                obj.viewOptions()
                break
            else:
                count += 1
                print('Invalid pin , try again')
        if count==3:
            print('chances are completed')
obj=Bank()
obj.validate()
