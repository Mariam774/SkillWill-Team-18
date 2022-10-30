import math
import re
def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val


def is_roman_number(num):

    pattern = re.compile(r"""   
                                ^M{0,3}
                                (CM|CD|D?C{0,3})?
                                (XC|XL|L?X{0,3})?
                                (IX|IV|V?I{0,3})?$
            """, re.VERBOSE)

    if re.match(pattern, num):
        return True

    return False
def int_to_roman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }
    div = 1
    while A >= div:
        div *= 10
    div /= 10
    res = ""
    while A:
        lastNum = int(A / div)
        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                    romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
                    (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                    romansDict[div * 10])
        A = math.floor(A % div)
        div /= 10
    return res
text = ""
operation = ["+", "-", "/", "*"]
opFlag = False
while True:
    entered_text = input()
    entered_text = entered_text.strip()
    if entered_text == "exit":
        break
    if not (is_roman_number(entered_text) or entered_text in operation) :
        print("roman number is not correct please enter valid one  ")
        continue
    if entered_text in operation:
        text += entered_text
        opFlag = True
    else:
        text += str(roman_to_int(entered_text))
        if opFlag == True:
            text = str(eval(text))
            opFlag = False
if text[-1] in operation:
    text = text[:-1]
print(text)
result = eval(text)
result = int_to_roman(result)
print(result)
