from cl import cal


symbl = cal.symbl


def symbl_numb_divider(inpt):
    number = []
    num = ""
    for i in inpt:
        if i not in symbl:
            num = num + i
        elif i in symbl:
            number.append(num)
            num = ""
            number.append(i)
    number.append(num)
    return number


def calculate(inpt):
    new = []
    number_symbl = symbl_numb_divider(inpt)
    ans = 0
    for i in number_symbl:
        if i in symbl:
            aq = number_symbl.index(i)
            if not new:
                new.append(int(number_symbl[aq - 1]))
            num2 = int(number_symbl[aq + 1])
            if i == "+":
                ans = cal.sum(cal(), new[0], num2)
                new[0] = ans
            elif i == "*":
                ans = cal.mult(cal(), new[0], num2)
                new[0] = ans
            elif i == "-":
                ans = cal.sub(cal(), new[0], num2)
                new[0] = ans
            elif i == "/":
                ans = cal.div(cal(), new[0], num2)
                new[0] = ans
    return ans


while True:
    number = input("Enter qutient: ").title()

    print(f"Ans: {calculate(number)}")
