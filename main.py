import tkinter as tk
from tkinter import ttk

FONT = 'Courier'
conversions = ['Binary', 'Octa', 'Hexadecimal', 'Decimal']

tinker = tk.Tk()
tinker.config(width=500, height=500)

label = tk.Label(text="From", font=(FONT, 12, "bold"))
label.place(x=100, y=150)

label = tk.Label(text="To", font=(FONT, 12, "bold"))
label.place(x=300, y=150)

user_input_from = ttk.Combobox(tinker, values=conversions)
user_input_from.place(x=100, y=175)

user_input_to = ttk.Combobox(tinker, values=conversions)
user_input_to.place(x=300, y=175)

user_input = tk.Label(text="Enter a number", font=(FONT, 8, "bold"))
user_input.place(x=100, y=215)

question = tk.Text(width=42, height=1)
question.place(x=100, y=235)

result = tk.Label(text="Result", font=(FONT, 8, "bold"))
result.place(x=100, y=275)

result_box = tk.Text(width=42, height=1)
result_box.place(x=100, y=295)


#Conversions

def binary_to_octal(binary):
    binary = binary.zfill((len(binary) // 3) * 3 + 3)

    octal = ''
    for i in range(0, len(binary), 3):
        # Take groups of 3 bits and convert to octal
        bits = binary[i:i + 3]
        octal_digit = str(int(bits, 2))
        octal += octal_digit

    return octal

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return str(decimal)

def binary_to_hexadecimal(binary):
    binary = binary.zfill((len(binary) // 4) * 4 + 4)

    hexadecimal = ''
    for i in range(0, len(binary), 4):
        # Take groups of 4 bits and convert to hexadecimal
        bits = binary[i:i + 4]
        hexadecimal_digit = hex(int(bits, 2))[2:].upper()
        hexadecimal += hexadecimal_digit

    return hexadecimal

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary string and remove the '0b' prefix
    return binary

def decimal_to_octal(decimal):
    octal = oct(decimal)[2:]  # Convert decimal to octal string and remove the '0o' prefix
    return octal

def decimal_to_hexadecimal(decimal):
    hexa = hex(decimal)[2:]
    return hexa.upper()

def octal_to_binary(octal):
    binary = bin(octal)[2:]
    return binary

def octal_to_decimal(octal):
    decimal_number = 0
    for i in range(len(octal)):
        decimal_number = decimal_number * 8 + int(octal[i])
    return decimal_number

def octal_to_hexadecimal(octal):
    hexa = hex(int(octal, 8))[2:]
    return hexa.upper()

def hexadecimal_to_binary(hexa):
    decimal = int(hexa, 16)
    binary = bin(decimal)[2:]
    return binary

def hexadecimal_to_decimal(hexa):
    decimal = int(hexa, 16)
    return decimal

def hexadecimal_to_octal(hexa):
    hexa = hexadecimal_to_binary(hexa)
    octal = binary_to_octal(hexa)[1:]
    return octal

def convert():

    if user_input_from.get() == 'Binary' and user_input_to.get() == 'Octa':
        number = question.get("1.0", "end-1c")
        converted = binary_to_octal(number)
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Binary' and user_input_to.get() == 'Decimal':
        number = question.get("1.0", "end-1c")
        converted = binary_to_decimal(number)
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Binary' and user_input_to.get() == 'Hexadecimal':
        number = question.get("1.0", "end-1c")
        converted = binary_to_hexadecimal(number)
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Decimal' and user_input_to.get() == 'Binary':
        number = question.get("1.0", "end-1c")
        converted = decimal_to_binary(int(number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Decimal' and user_input_to.get() == 'Octa':
        number = question.get("1.0", "end-1c")
        converted = decimal_to_octal(int(number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Decimal' and user_input_to.get() == 'Hexadecimal':
        number = question.get("1.0", "end-1c")
        converted = decimal_to_hexadecimal(int(number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Octa' and user_input_to.get() == 'Binary':
        number = question.get("1.0", "end-1c")
        converted = octal_to_binary(int(number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Octa' and user_input_to.get() == 'Decimal':
        number = question.get("1.0", "end-1c")
        converted = octal_to_decimal((number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Octa' and user_input_to.get() == 'Hexadecimal':
        number = question.get("1.0", "end-1c")
        converted = octal_to_hexadecimal((number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Hexadecimal' and user_input_to.get() == 'Binary':
        number = question.get("1.0", "end-1c")
        converted = hexadecimal_to_binary((number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Hexadecimal' and user_input_to.get() == 'Decimal':
        number = question.get("1.0", "end-1c")
        converted = hexadecimal_to_decimal((number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == 'Hexadecimal' and user_input_to.get() == 'Octa':
        number = question.get("1.0", "end-1c")
        converted = hexadecimal_to_octal((number))
        result_box.insert("end", str(converted))

    elif user_input_from.get() == user_input_to.get():
        result_box.insert("end", question.get("1.0", "end-1c"))



def clear():
    question.delete("1.0", "end")
    result_box.delete("1.0", "end")

convert_button = tk.Button(text="Convert", command=convert)
convert_button.place(x=100, y=325)

clear_button = tk.Button(text="Clear", command=clear)
clear_button.place(x=200, y=325)



tinker.mainloop()
