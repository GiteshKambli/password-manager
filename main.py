import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_pass():
    website = website_tf.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message="Password not saved")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No file found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password_tf.delete(0, END)
    password_tf.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_tf.get()
    email = email_tf.get()
    password = password_tf.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Some fields are empty:")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details Entered:\nEmail: {email}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_tf.delete(0, END)
                password_tf.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_tf = Entry(width=35)
website_tf.focus()
website_tf.grid(column=1, row=1, sticky="ew", padx=3, pady=3)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_tf = Entry(width=35)
email_tf.insert(0, "gkambli2002@gmail.com")
email_tf.grid(column=1, row=2, columnspan=2, sticky="ew", padx=3, pady=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_tf = Entry(width=21)
password_tf.grid(column=1, row=3, sticky="ew", padx=3, pady=3)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3, sticky="ew", padx=3, pady=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=3, pady=3)

search_button = Button(text="Search", command=search_pass)
search_button.grid(column=2, row=1, sticky="ew", padx=3, pady=3)

window.mainloop()
