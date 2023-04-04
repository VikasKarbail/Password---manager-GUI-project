from tkinter import *
import random
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate_fun():
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

    passwordsn = "".join(password_list)
    password_entry.insert(0, passwordsn)
    pyperclip.copy(passwordsn)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_n = website_entry.get()
    e = email_entry.get()
    pa_w = password_entry.get()

    if len(website_n)==0 or len(pa_w)==0:
        messagebox.showinfo(title="OOPS", message="please eneter all box")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \n Email: {e} "
                                                              f"\n Password:{password}\n Is it ok to Save")
        if is_ok:
            data_e = open("data.txt", "a")
            # or
            # with open("data.txt", "a") as data_e
            data_e.write(f"{website_n} | {e} | {pa_w} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
#canvas.grid(column=1, row=1)
canvas.grid(row=0, column=1)

#label
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)


#Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()



email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vikaskarbail@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buton

generate_button = Button(text="Generate Password", command=password_generate_fun)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

