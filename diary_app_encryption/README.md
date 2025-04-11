# OVERVIEW OF DIARY APP

This is a simple diary application project based on GUI with using tkinter library. User could save , edit , search and delete entries with their dates. Furthermore, this diary application stores entries of diary and password as encrypted.

## FEATURES OF DIARY APP

- **Password Managment**: For security of this application , there is a password. Password is in 'password.txt' file as a encrypted format. This password can be changed by user.
- **Write Entries**: Write diary entries with specific date. 
- **Edit Entries**: Edit diary entries which are was saved before with specific date.
- **Search Entries**: Search diary entries with specific date.
- **Delete Entries**: Delete diary entries with specific date.
- **Security**: Entries saved in 'diary.txt' as a encrypted format. Cryptology method is caesa cipher method 

### REQUIREMENTS

- Python 3.12.1
- Tkinter 8.6

### HOW TO RUN APPLICATION 

1. Ensure that there are 'main.py' , 'diary.txt' , 'password.txt'.
2. Navigate the folder which include files in step 1.
3. Run the application(write below to terminal):

python main.py diary.txt password.txt

[!WARNING] Do not write date in format (DD/MM/YYYY) in your entries. Just write date in format(DD/MM/YYYY) when program wants to enter date.
[!WARNING] The password is:1234
[!NOTE] Do not forget to change password 
