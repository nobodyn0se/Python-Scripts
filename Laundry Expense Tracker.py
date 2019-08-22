import os


class Laundry:
    first = 'C:/Users/'
    dirt = '/Desktop/Laundry/'
    final = ''.join([dirt, 'Laundry.txt'])
    wght = ''.join([dirt, 'Weight.txt'])
    user = os.getlogin()
    path = first + user + final
    path_dir = ''.join([first, user, dirt])
    path_w = ''.join([first, user, wght])

    @staticmethod
    def get_value():
        s = input("What was your latest laundry cost?\n")
        if s == "":
            return 0
        return s

    def first_time(self):
        try:
            f = open(self.path, 'r')
            f.close()

        except FileNotFoundError:
            print("Creating storage file for the first time\n")
            os.mkdir(self.path_dir)
            with open(self.path, 'w') as f:
                f.write('0')
            with open(self.path_w, 'w') as r:
                r.write('0')

    def track_add(self, s):
        with open(self.path, 'r') as h:
            val = h.read()
        sum1 = 0
        sum1 += int(val) + int(s)
        with open(self.path, 'w+') as f:
            f.write(str(sum1))

    def read_file(self):
        with open(self.path, 'r') as a:
            amount = a.read()
        print("Your total laundry expenditure so far is Rs. {}".format(amount))
        print("{:0.2f}% of Rs. 7080 used".format(int(amount)/7080 * 100))

        with open(self.path_w, 'r') as p:
            amount2 = p.read()
        print("Total weight laundered so far {} kg(s)".format(amount2))
        print("{:0.2f}% of 90 kg(s) used".format(float(amount2)/90 * 100))

    def add_weight(self):
        # Writes the weight in a separate text file
        n = input("What was the latest weight (in kg)?\n")
        if n == "":
            n = 0.0
        sum2 = 0
        with open(self.path_w, 'r') as w:
            val = w.read()
        sum2 += float(val) + float(n)
        with open(self.path_w, 'w+') as k:
            k.write(str(sum2))


def main():
    l1 = Laundry()
    l1.first_time()
    fin = l1.get_value()
    l1.track_add(fin)
    l1.add_weight()
    l1.read_file()


if __name__ == '__main__':
    main()