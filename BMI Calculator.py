from tkinter import Tk, Label, Entry, Button, messagebox

win = Tk()
width = 600
height = 300
win.minsize(width=width, height=height)
win.title("BMI CALCULATOR")

label_1 = Label(text="Enter Your Mass")
label_2 = Label(text="Enter Your Height")
label_3 = Label(text=" ")

entry_1 = Entry()
entry_2 = Entry()

def get_BMI():
    yazi = ""
    user_input1 = entry_1.get()
    user_input2 = entry_2.get()
    try:
        mass = float(user_input1)
        height = float(user_input2)
        sonuc = int(mass / ((height / 100) ** 2))

        if sonuc < 16:
            yazi = "Severe Thinness"
        elif 16 < sonuc < 17:
            yazi = "Moderate Thinness"
        elif 17 < sonuc < 18.5:
            yazi = "Mild Thinness"
        elif 16 < sonuc < 25:
            yazi = "Normal"
        elif 16 < sonuc < 30:
            yazi = "Overweight"
        elif 16 < sonuc < 35:
            yazi = "Obese Class I"
        elif 16 < sonuc < 40:
            yazi = "Obese Class II"
        elif sonuc > 40:
            yazi = " Obese Class III"

        label_3.config(text=f"Your BMI= {sonuc}, {yazi}")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

button = Button(padx=10, pady=10, text="Hesapla", command=get_BMI)
xx = width // 2 - 50
yy = 10
label_1.place(x=xx, y=yy, width=100, height=30)
entry_1.place(x=xx, y=yy + 35, width=100, height=30)
label_2.place(x=xx, y=yy + 70, width=100, height=30)
entry_2.place(x=xx, y=yy + 105, width=100, height=30)
button.place(x=xx, y=yy + 140, width=100, height=30)
label_3.place(x=xx - 200, y=yy + 175, width=500, height=30)

win.mainloop()
