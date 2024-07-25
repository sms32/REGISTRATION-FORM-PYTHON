# Registration Form Using Tkinter
This project implements a simple registration form using Python's Tkinter library. The form collects user information such as name, email, age, gender, and mobile number. When submitted, it displays a success message.

## Code Explanation
### Imports
```Python
from tkinter import *
import tkinter.messagebox
```
- The code begins by importing necessary classes and functions from the tkinter module for creating GUI applications and the tkinter.messagebox for displaying messages.

### Main Window Setup
```Python
w = Tk()
w.geometry('400x500') 
w.title("Registration form")
```
- A Tkinter window (w) is created, with a specified size of 400x500 pixels, and the title "Registration form" is set.

### Title Label
```Python
l1 = Label(w, text="REGISTRATION FORM", font=('Times New Roman', 20, 'bold'))
l1.place(x=57, y=50)
```

- A label is added to the window to display the title "REGISTRATION FORM" with a specific font size and style.

### Input Fields

#### Name Field
```Python
nl = Label(w, text="Name :", width=20, font=('Times New Roman', 15,))
nl.place(x=2, y=130)
ne = Entry(w)
ne.place(x=170, y=130)
```
- A label and an entry field for the user's name are created.

#### Email Field
```Python
el = Label(w, text="Email :", width=20, font=('Times New Roman', 15))
el.place(x=2, y=180)
ee = Entry(w)
ee.place(x=170, y=180)
```
- A label and entry for the user's email.

#### Age Field
```Python
al = Label(w, text="Age :", width=20, font=('Times New Roman', 15))
al.place(x=-6, y=230)
ae = Entry(w)
ae.place(x=170, y=230)
```
- A label and entry for the user's age.
  
#### Gender Selection
```python
gl = Label(w, text="Gender :", width=20, font=('Times New Roman', 14))
gl.place(x=10, y=280)
g = StringVar(value=None)
m = Radiobutton(w, text="Male", variable=g, value="Male", font=('Times New Roman', 10))
m.place(x=165, y=280)
f = Radiobutton(w, text="Female", variable=g, value="Female", font=('Times New Roman', 10))
f.place(x=230, y=280)
```
- A label for gender selection with radio buttons for "Male" and "Female".

#### Mobile Number Field
```Python
ml = Label(w, text="Mobile No.", width=20, font=('Times New Roman', 13))
ml.place(x=28, y=330)
me = Entry(w)
me.place(x=170, y=330)
```
- A label and entry for the user's mobile number.

#### Submit Button
```Python
def submit():
    tkinter.messagebox.showinfo(title="success", message="Registration Successful!!", ANCHOR=CENTER)
    
b = Button(w, text='Submit form', width=20, bg='mediumPurple', fg='white', command=submit)
b.place(x=120, y=380)
```
- A function submit() is defined to show a success message when the button is clicked. The button is styled and placed at the bottom of the form.

#### Main Loop
```Python
w.mainloop()
```

- Finally, w.mainloop() starts the Tkinter event loop, allowing the application to wait for user interaction.

### Conclusion
- This simple registration form serves as a foundational example for creating GUI applications in Python. You can expand upon this by adding more features, such as data validation, saving the input to a file, or integrating with a database.

<img src="https://github.com/user-attachments/assets/45712989-c946-4475-b20e-c9e5e1d9e400" alt="ARDUINO UNO"  width="50%">
<br>
<br>
<img src="https://github.com/user-attachments/assets/44a20471-577e-49b1-a428-681ae70f6828" alt="ARDUINO UNO"  width="50%">
