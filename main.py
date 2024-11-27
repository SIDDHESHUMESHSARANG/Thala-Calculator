#THALA FOR A REASON Calculator by SIDDHESH UMESH SARANG

# STRING:-
def check_input(userInput):
    userInput = userInput.lower()

    if len(userInput) == 7:
        print("THALA FOR A REASON")
    elif "seven" in userInput:
        print("THALA FOR A REASON")
    elif "7" in userInput:
        print("THALA FOR A REASON")
    elif sum(ord(c) for c in userInput) == 7:
        print("THALA FOR A REASON")
    elif len(userInput.split()) == 7:
        print("THALA FOR A REASON")
    elif "dhoni" in userInput:
        print("THALA FOR A REASON")
    elif "ms" in userInput:
        print("THALA FOR A REASON")
    elif "thala" in userInput:
        print("THALA FOR A REASON")
    else:
        print("NO THALA FOUND, KINDLY ENTER A DIFFERENT STRING")
userInput = input("ENTER THE STRING HERE: ")
check_input(userInput) 

# GUI(Under Development):-
# import tkinter as tk

# root = tk.Tk()
# root.title("THALA Calculator")

# entry = tk.Entry(root, width=40)
# entry.pack(pady=10)

# check_button = tk.Button(root, text="Check", command=check_input)
# check_button.pack(pady=5)

# result_label = tk.Label(root, text="", width=40, height=2)
# result_label.pack(pady=20)

# root.mainloop()




