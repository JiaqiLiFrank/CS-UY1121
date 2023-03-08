# Author: <Frank Li>
# Assignment / Part: HW3
# Date due: 2023-02-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the # NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

class Account:
    def __init__(self):
        self.account_lst = []

    def account(self, name, num):
        self.account_lst.append([num, name, 0, []])

    def deposit(self, num, value):
        for account in self.account_lst:
            if num == account[1]:
                account[2] += float(value)
                account[3].append(float("+" + str(value)))
            else:
                continue

    def withdraw(self, num, value):
        for account in self.account_lst:
            if num == account[1]:
                account[2] -= float(value)
                account[3].append(float("-" + str(value)))
            else:
                continue

    def print(self, num):
        output_txt = "Account: "
        for account in self.account_lst:
            if num == account[1]:
                output_txt += (account[1] + " (" + account[0] + "), $" + str(account[2]) + ", " + str(account[3]))
            else:
                continue
        return output_txt


def load_data():
    try:
        file_name = input("Please Enter the File Name: ")
        # transactions.txt
        file = open(file_name, "r")
        output = []
        for words in file.readlines():
            output.append(words.strip().split())
        for command in output:
            if command[0] == "Account":
                command.insert(1, command[2])
                command.pop(3)
        file.close()
        return output
    except FileNotFoundError:
        return "The File is Not Found"


def main():
    input_file = load_data()
    single_account = Account()
    for command in input_file:
        if command[0] == "Account":
            single_account.account(command[1], command[2])
        if command[0] == "Deposit":
            single_account.deposit(command[1], command[2])
        if command[0] == "Withdraw":
            single_account.withdraw(command[1], command[2])
        if command[0] == "Print":
            print(single_account.print(command[1]))


if __name__ == "__main__":
    main()
