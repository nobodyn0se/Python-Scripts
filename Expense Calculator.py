import os


class Expense:
    first = 'C:/Users/'
    last = '/Desktop/Expense.txt'
    user = os.getlogin()
    path = ''.join([first, user, last])

    @staticmethod
    def getdata():
        i = input("What was your latest expense?\n")
        if i == "":
            return 0
        return int(i)

    def first_time(self):
        # Checks if a stored expense file already exists
        try:
            f = open(self.path, 'r')
            f.close()

        except FileNotFoundError:
            print("Creating storage file for the first time\n")
            with open(self.path, 'w') as f:
                f.write('0')

    def expense(self, par):
        # Calculates the expense and stores it to a file
        with open(self.path, 'r') as h:
            val = h.read()
        summ = 0
        summ += int(val) + par
        with open(self.path, 'w+') as f:
            f.write(str(summ))

    def read_file(self):
        with open(self.path, 'r') as a:
            amount = a.read()
        print("Your total expenditure so far is Rs. {}".format(amount))
        print("{:0.2f}% of Rs. 10000 used".format(int(amount)/100))


def main():
    e1 = Expense()
    e1.first_time()
    ex = e1.getdata()
    e1.expense(ex)
    e1.read_file()


if __name__ == '__main__':
    main()



