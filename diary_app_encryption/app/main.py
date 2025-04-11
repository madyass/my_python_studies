###Name-Surname: Muhammet Ahmet Saydam
###ID:150230720

import tkinter as tk
from tkinter import messagebox

class Password:#this class is for password and password operations , password is in password.txt file
    def __init__(self):
        self.numbers = [1,3,9,2]
        with open('password.txt','r') as f:
            self.password = self.decrypt(f.read())
    
    def check_password(self,check):#checks password is true or not 
        if check == self.password:
            return True
        else:
            return False
    
    def change(self,new):#changes password and writes it
        with open('password.txt','w') as f:
            f.write(self.encrypt(new))
            f.close()
        self.password = new #self.password updated
    
    def encrypt(self,word):#the enryption and decryption methods for password are very similar witk main encryption and decryption functions
        i = 0              #but in password cryptology , shift number is changes each time. Therefore break the password became more challenging
        encrypted_word = ""         #these functions are explained in main crpytology functions (at below)
        for char in word:
            shift = self.numbers[i%4]
            if char.isalpha():  
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
                encrypted_word += shifted_char
            elif char.isdigit():
                encrypted_word += str((int(char) + shift) % 10)
            elif char in special_characters:  
                encrypted_word += special_characters[(special_characters.index(char) + shift) % len_special_chars]
            else:
                encrypted_word += char
            i+=1
        return encrypted_word

    def decrypt(self,word):
        i=0
        decrypted_word = ""
        for char in word:
            shift = self.numbers[i%4]
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
                decrypted_word += shifted_char
            elif char.isdigit():
                decrypted_word += str((int(char) - shift) % 10)
            elif char in special_characters:
                decrypted_word += special_characters[(special_characters.index(char) - shift) % len_special_chars]
            else:
                decrypted_word += char
            i+=1
        return decrypted_word
    
pass_number = 7  # this number is for Caesar encryption
diary_file = 'diary.txt'  # diary file
password = Password()  # Initialize the password manager

def date_format(date):  # checks format of entered date
    if len(date) == 10 and date[2] == "/" and date[5] == "/":#checks format DD/MM/YYYY
        try:
            day, month, year = map(int, date.split("/"))
            return True
        except:#if there is a value Error or other errors it returns False
            return False
    return False

def is_date_in(file_name, date):  # checks entered date is in file or not
    if date_format(date):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            encrypted_date = encrypt(date)#all diary and its dates are enrypted , therefore date should be searched as encrypted 
            for line in lines:
                if encrypted_date in line:
                    return True
    return False

special_characters = [  # i used list for encryption of special characters
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
    ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\n'
]

len_special_chars = len(special_characters)

def write_txt(file_name, date, text):  # this function encrypt date and text. then write to file
    encrypted_date = encrypt(date)
    encrypted_text = encrypt(text)
    with open(file_name, 'a') as f:#adds encrypted date and encrypted text
        f.write(encrypted_date + '\n')
        f.write(encrypted_text + '\n')

def encrypt(plain_text):
    shift = pass_number
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # for letters , encrypted letter is shifted number based on ASCII table
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        elif char.isdigit():  # i use different encryption method for numbers , i add shift number and look last number of this number
            encrypted_text += str((int(char) + shift) % 10)
        elif char in special_characters:  # shifting is based on special characters list
            encrypted_text += special_characters[(special_characters.index(char) + shift) % len_special_chars]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text):  # inverse function of encrypt function
    shift = pass_number
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            decrypted_text += shifted_char
        elif char.isdigit():
            decrypted_text += str((int(char) - shift) % 10)
        elif char in special_characters:
            decrypted_text += special_characters[(special_characters.index(char) - shift) % len_special_chars]
        else:
            decrypted_text += char
    return decrypted_text

# for write , edit and search functions, first date screen appear , after submitting date own pages will open
def write():
    def writing_page():
        def save_entry():  # saves text to file
            entry = text.get("1.0", tk.END).strip()
            write_txt(diary_file, user_date, entry)  # writes to txt file
            messagebox.showinfo("Success", "Entry saved successfully!")
            write_window.destroy()
        
        user_date = date.get()

        if not date_format(user_date):
            messagebox.showerror("Error", "Wrong Date Format!\nPlease enter in this format -> DD/MM/YYYY")
        elif is_date_in(diary_file, user_date):
            messagebox.showerror("Error", "This date is already entered. Please enter another date.")
        else:
            window.destroy()
            write_window = tk.Tk()
            write_window.title("Writing Page")
            
            text = tk.Text(write_window, wrap='word')
            text.pack(expand=True, fill='both')
            
            save_button = tk.Button(write_window, text="Save", command=save_entry)
            save_button.pack(pady=10)
            
    window = tk.Tk()
    window.title("Enter Date")
    window.geometry("300x350")
    
    tk.Label(window, text="Enter Date:\nPlease enter in this format -> DD/MM/YYYY").pack()
    date = tk.Entry(window)
    date.pack(pady=5,padx=5)
    
    date_button = tk.Button(window, text="Submit", command=writing_page)
    date_button.pack(pady=5,padx=5)
    window.mainloop()

def edit():#edit function is similar with write function 
    def editing_page():
        def save_entry():
            entry = text.get("1.0", tk.END).strip()
            lines = []
            with open(diary_file, 'r') as f:
                lines = f.readlines()        #lines veriable is list of texts
            encrypted_date = encrypt(user_date)
            for i in range(len(lines)):
                if encrypted_date in lines[i]:         #search date
                    lines[i + 1] = encrypt(entry) + '\n'       #edit new entry
                    break
            with open(diary_file, 'w') as f:
                f.writelines(lines)         # updates diary_file
            messagebox.showinfo("Success", "Entry edited successfully!")
            edit_window.destroy()
        
        user_date = date.get()#date operations are similar for each function
        if not date_format(user_date):
            messagebox.showerror("Error", "Wrong Date Format! (DD/MM/YYYY)")
        elif not is_date_in(diary_file, user_date):
            messagebox.showerror("Error", "This date is not found. Please enter another date.")
        else:
            window.destroy()
            edit_window = tk.Tk()
            edit_window.title("Editing Page")
            
            text = tk.Text(edit_window, wrap='word')
            text.pack(expand=True, fill='both')
            
            encrypted_date = encrypt(user_date) #enrypt date to find text which is wanted for editing
            with open(diary_file, 'r') as f:
                lines = f.readlines()
            for i in range(len(lines)):
                if encrypted_date in lines[i]: #search entered date 
                    text.insert(tk.END, decrypt(lines[i + 1][:-1])) #shows the text which is wanted for editing , removes last character.
                    break                                           #when i run the code and app saves a entry it adds '_' at the last item.
                                                                    #this caused a bug. so , i remove the last character in edit and in search functions.
            
            save_button = tk.Button(edit_window, text="Save", command=save_entry)
            save_button.pack(pady=10)
            
    window = tk.Tk()
    window.title("Enter Date")
    window.geometry("300x350")
    
    tk.Label(window, text="Enter Date:\nPlease enter in this format ->DD/MM/YYYY").pack()
    date = tk.Entry(window)
    date.pack(padx=5,pady=5)
    
    date_button = tk.Button(window, text="Submit", command=editing_page)
    date_button.pack(pady=5,padx=5)
    window.mainloop()

def search():
    def searching_page():#date operations are similar for each function
        user_date = date.get()
        if not date_format(user_date):
            messagebox.showerror("Error", "Wrong Date Format\nPlease enter in this format->DD/MM/YYYY")
        elif not is_date_in(diary_file, user_date):
            messagebox.showerror("Error", "This date is not found.")
        else:
            search_window.destroy()
            search_results = tk.Tk()
            search_results.title("Search Results")
            
            encrypted_date = encrypt(user_date)
            with open(diary_file, 'r') as f:
                lines = f.readlines()
            for i in range(len(lines)):
                if encrypted_date in lines[i]:
                    tk.Label(search_results, text=decrypt(lines[i + 1][:-1])).pack() #removes last character
                    break
            
    search_window = tk.Tk()
    search_window.title("Enter Date to Search")
    search_window.geometry("300x350")
    
    tk.Label(search_window, text="Enter Date:\nPlease enter in this format->DD/MM/YYYY").pack()
    date = tk.Entry(search_window)
    date.pack(padx=5,pady=5)
    
    date_button = tk.Button(search_window, text="Submit", command=searching_page)
    date_button.pack(padx=5,pady=5)
    search_window.mainloop()

def delete():
    def deleting():#date operations are similar for each function
        user_date = date.get()
        if not date_format(user_date):
            messagebox.showerror("Error", "Wrong Date Format\nPlease enter in this format->DD/MM/YYYY")
        elif not is_date_in(diary_file, user_date):
            messagebox.showerror("Error", "This date is not found. Please enter another date.")
        else:
            lines = []
            with open(diary_file, 'r') as f:
                lines = f.readlines()
            encrypted_date = encrypt(user_date)
            for i in range(len(lines)):
                if encrypted_date in lines[i]:
                    del lines[i:i + 2]
                    break
            with open(diary_file, 'w') as f:
                f.writelines(lines)
            messagebox.showinfo("Success", "Entry is deleted")
            delete_window.destroy()
    
    delete_window = tk.Tk()
    delete_window.title("Enter Date")
    delete_window.geometry("300x350")
    
    tk.Label(delete_window, text="Enter Date:\nPlease enter in this format->DD/MM/YYYY").pack()
    date = tk.Entry(delete_window)
    date.pack(padx=5,pady=5)
    
    date_button = tk.Button(delete_window, text="Submit", command=deleting)
    date_button.pack(padx=5,pady=5)
    delete_window.mainloop()

def main():#this is screen for password and password operations
    enter = tk.Tk()
    enter.title("Diary App")
    
    def change_password_menu():#when user click change password , this screen appear
        def change_password():#this function changes passwords
            if not password.check_password(old_password.get()):#checks passwords are matched
                messagebox.showerror("Error", "Old password does not match!")
            else:
                password.change(new_password.get())         #then changes password
                messagebox.showinfo("Success", "Password changed successfully!")
                change.destroy()
        
        change = tk.Tk()
        change.title("Change Password")
        change.geometry("300x350")
        
        tk.Label(change, text="Old Password:").pack()
        old_password = tk.Entry(change, show="*")
        old_password.pack(padx=5,pady=5)
        
        tk.Label(change, text="New Password:").pack()
        new_password = tk.Entry(change, show="*")
        new_password.pack(padx=5,pady=5)
        
        change_button = tk.Button(change, text="Submit", command=change_password)
        change_button.pack(padx=5,pady=5)
        
    def check_password():
        if password.check_password(password_entry.get()):
            enter.destroy()
            main_menu()
        else:
            messagebox.showerror("Error", "Incorrect Password. Please try again!")
            
    tk.Label(enter, text="Password:").pack()
    password_entry = tk.Entry(enter, show="*")
    password_entry.pack(padx=5,pady=5)
    
    submit_button = tk.Button(enter, text="Enter", command=check_password)
    submit_button.pack(padx=5,pady=5)            
    
    change_button_menu = tk.Button(enter, text="Change Password", command=change_password_menu)
    change_button_menu.pack(padx=5,pady=5)
    
    enter.mainloop()
    
def main_menu():#this is main menu which include write , edit , search and delete functions.
    def exit_app():
        menu.destroy()
        
    menu = tk.Tk()
    menu.title("Diary App")
    menu.geometry("500x400")
    
    tk.Label(menu, text="Welcome to the Diary App!").pack()
    
    write_button = tk.Button(menu, text="Write", command=write)
    write_button.pack(padx=20,pady=20)            
    
    edit_button = tk.Button(menu, text="Edit", command=edit)
    edit_button.pack(padx=20,pady=20)            
    
    search_button = tk.Button(menu, text="Search", command=search)
    search_button.pack(padx=20,pady=20)            
    
    delete_button = tk.Button(menu, text="Delete", command=delete)
    delete_button.pack(padx=20,pady=20)
    
    exit_button = tk.Button(menu, text="Exit", command=exit_app)
    exit_button.pack(padx=20,pady=20)
       
    menu.mainloop()

if __name__ == "__main__":
    main()
    
