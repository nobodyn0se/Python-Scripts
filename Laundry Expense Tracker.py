import os


class Laundry:
    first = 'C:/Users/'
    last = '/Desktop/Laundry.txt'
    user = os.getlogin()
    path = first + user + last

    @staticmethod
    def get_value():
        s = int(input("What was your latest laundry cost?\n"))
        return s

    def first_time(self):
        stime = input("Are you entering data for the first time? (Yes or No) \n")
        if stime.lower() == "yes":
            with open(self.path, 'w') as f:
                f.write('0')
        else:
            pass

    def track_add(self, s):
        with open(self.path, 'r') as h:
            val = h.read()
        sum = 0
        sum += int(val) + s
        with open(self.path, 'w+') as f:
            f.write(str(sum))

    @staticmethod
    def read_file():
        with open('C:/Users/ACER/Desktop/Laundry.txt', 'r') as a:
            amount = a.read()
        print("Your total laundry expenditure so far is Rs. {}".format(amount))
        print("{:0.2f}% of Rs. 7080 used".format(int(amount)/7080 * 100))


def main():
    l1 = Laundry()
    l1.first_time()
    fin = l1.get_value()
    l1.track_add(fin)
    l1.read_file()


if __name__ == '__main__':
    main()

