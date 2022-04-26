import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


class MainWindow:
    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self, username):
        self.username = username
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=1, row=0)

        self.website_label = Label(text="Website:")
        self.website_label.grid(column=0, row=1)

        self.website_tf = Entry(width=35)
        self.website_tf.focus()
        self.website_tf.grid(column=1, row=1, sticky="ew", padx=3, pady=3)

        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(column=0, row=2)

        self.email_tf = Entry(width=35)
        self.email_tf.grid(column=1, row=2, columnspan=2, sticky="ew", padx=3, pady=3)

        self.password_label = Label(text="Password:")
        self.password_label.grid(column=0, row=3)

        self.password_tf = Entry(width=21)
        self.password_tf.grid(column=1, row=3, sticky="ew", padx=3, pady=3)

        self.generate_pass = Button(text="Generate Password", command=self.generate_password)
        self.generate_pass.grid(column=2, row=3, sticky="ew", padx=3, pady=3)

        self.add_button = Button(text="Add", width=36, command=self.add_password)
        self.add_button.grid(column=1, row=4, sticky="ew", padx=3, pady=3)

        self.search_button = Button(text="Search", command=self.search_pass)
        self.search_button.grid(column=2, row=1, sticky="ew", padx=3, pady=3)
        
        self.logout_btn = Button(text="Logout", command=self.logout)
        self.logout_btn.grid(column=2, row=4, sticky="ew", padx=3, pady=3)

        self.window.mainloop()

    # ---------------------------- PASSWORD SEARCH ------------------------------- #
    def search_pass(self):
        website = self.website_tf.get()
        try:
            with open("data.json", "r") as file:
                data = json.load(file)[self.username]
                if website in data:
                    email = data[website]['email']
                    password = data[website]['password']
                    pyperclip.copy(password)
                    messagebox.showinfo(title=website,
                                        message=f"Email: {email}\nPassword: {password}\n\nPassword copied to clipboard!")
                else:
                    messagebox.showinfo(title=website, message="Password not saved")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No file found")

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P',
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
        self.password_tf.delete(0, END)
        self.password_tf.insert(0, generated_password)
        pyperclip.copy(generated_password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def add_password(self):
        website = self.website_tf.get()
        email = self.email_tf.get()
        password = self.password_tf.get()
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Some fields are empty:")
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"Details Entered:\nEmail: {email}\nPassword: {password}")
            if is_ok:
                try:
                    with open("data.json", "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    add_data = {
                        self.username: new_data
                    }
                    with open("data.json", "w") as file:
                        json.dump(add_data, file, indent=4)
                else:
                    data[self.username].update(new_data)
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                finally:
                    self.website_tf.delete(0, END)
                    self.password_tf.delete(0, END)
                    
    def logout(self):
        self.window.destroy()
        Login()


class SignUp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=25)

        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.username_label = Label(text="New Username:")
        self.username_label.grid(column=0, row=1)

        self.username_tf = Entry(width=35)
        self.username_tf.focus()
        self.username_tf.grid(column=1, row=1, sticky="ew", padx=3, pady=8, columnspan=2)

        self.newpass_label = Label(text="Enter Password:")
        self.newpass_label.grid(column=0, row=2)

        self.newpass_tf = Entry(width=35)
        self.newpass_tf.grid(column=1, row=2, sticky="ew", padx=3, pady=8, columnspan=2)

        self.conpass_label = Label(text="Confirm Password:")
        self.conpass_label.grid(column=0, row=3)

        self.conpass_tf = Entry(width=35)
        self.conpass_tf.grid(column=1, row=3, sticky="ew", padx=3, pady=8, columnspan=2)

        self.signup_button = Button(text="Sign Up", command=self.sign_up)  # add command here
        self.signup_button.grid(column=2, row=4, sticky="ew", padx=3, pady=30)

        self.login_btn = Button(text="Login", command=self.login)  # add command here
        self.login_btn.grid(column=0, row=4, sticky="ew", padx=3, pady=30)

        self.window.mainloop()

    def sign_up(self):
        user_name = self.username_tf.get()
        new_pass = self.newpass_tf.get()
        con_pass = self.conpass_tf.get()

        new_data = {
            user_name: {
                "password": new_pass
            }
        }
        if len(user_name) == 0 or len(new_pass) == 0 or len(con_pass) == 0:
            messagebox.showinfo(title="Oops", message="Some fields are empty:")
        else:
            if new_pass == con_pass:
                try:
                    with open("data.json") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    with open("data.json", "w") as file:
                        json.dump(new_data, file, indent=4)
                else:
                    if user_name in data:
                        messagebox.showinfo(title="Oops", message="User already exists!")
                    else:
                        data.update(new_data)
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
            else:
                messagebox.showinfo(title="Oops", message="Password doesn't match!")

        self.window.destroy()
        MainWindow(user_name)

    def login(self):
        self.window.destroy()
        Login()


class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=30)

        self.canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=2)

        self.username_label = Label(text="Username:")
        self.username_label.grid(column=0, row=1, sticky="ew", padx=3, pady=3)

        self.username_tf = Entry(width=21)
        self.username_tf.grid(column=1, row=1, sticky="ew", padx=3, pady=3)

        self.pass_label = Label(text="Password:")
        self.pass_label.grid(column=0, row=2, sticky="ew", padx=3, pady=3)

        self.pass_tf = Entry(width=21)
        self.pass_tf.grid(column=1, row=2, sticky="ew", padx=3, pady=3)

        self.login_btn = Button(text="Log in", command=self.user_login)
        self.login_btn.grid(column=1, row=3, padx=8, pady=10, sticky='e')

        self.signup_btn = Button(text="Sign Up", command=self.signup)
        self.signup_btn.grid(column=0, row=3, padx=8, pady=10, sticky='w')

        self.window.mainloop()

    def user_login(self):
        user_name = self.username_tf.get()
        password = self.pass_tf.get()
        with open('data.json', 'r') as file:
            data = json.load(file)
            if user_name in data:
                if password == data[user_name]['password']:
                    self.window.destroy()
                    MainWindow(user_name)

    def signup(self):
        self.window.destroy()
        SignUp()


if __name__ == '__main__':
    Login()
