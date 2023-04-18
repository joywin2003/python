from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = website_entry.get()

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No datafile exits")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Please enter the website to be searched")
        elif website in data:
            web_data = data[website]
            messagebox.showinfo(title=f"{website}",
                                message=f"Email:{web_data['email']}\nPassword:{web_data['password']}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exits")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # gets the entered info
    website_name = website_entry.get()
    username_name = username_entry.get()
    password_name = password_entry.get()
    data_dict = {
        website_name: {
            "email": username_name,
            "password": password_name
        }
    }

    if len(website_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Oops", message="Please fill every details")
    # else:
    #     # pop up message to confirm your details
    #     is_ok = messagebox.askokcancel(title="website",
    #                                    message=f"There are entered Credentials\nWebsite:{website_name}\n"
    #                                            f"Username:{username_name}\nPassword:{password_name}\n"
    #                                            f"Is it okay?")
    #     # saves the details to the file
    # if is_ok:
    # credentials = f"{website_name}|{username_name}|{password_name}\n"
    else:
        try:
            with open("data.json", "r") as file:
            # # json.dump(data_dict, file, indent=4)
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_dict, file, indent=4)
        else:
            data.update(data_dict)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            # username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# creating a canvas and adding the logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# label for entering website address
website_label = Label(text="website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

# label for entering username and email
username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "joywin@sjec.ac.in")

# label for entering password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# generate password button
generate_button = Button(text="generate password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",width=14,command=search)
search_button.grid(row=1, column=2)
window.mainloop()
