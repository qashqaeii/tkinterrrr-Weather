import pyowm
import tkinter as tk
from tkinter import messagebox

def omw(): #فرستادن درخواست از طریق Api
    api_key = "f70735bded1ab2742724520cf568ec56"#نوش
    owm_obj = pyowm.OWM(api_key)
    mgr = owm_obj.weather_manager()  
    city_name = city_f.get()

    obs = mgr.weather_at_place(city_name).weather  
    if obs is not None:
        temp = obs.temperature('celsius')
        status = obs.detailed_status
        wind = obs.wind()
        humidity = obs.humidity

        messagebox.showinfo("آب و هوا", 
                            f"درجه حرارت: {temp['temp']}°C\n"
                            f"وضعیت: {status}\n"
                            f"سرعت باد: {wind['speed']} m/s\n"
                            f"رطوبت: {humidity}%")
    elif obs is None:
        messagebox.showerror("خطا", "این شهر پیدا نشد")



# ایجاد یک پنجره جدید
root = tk.Tk()
root.title("آب و هوا")

# ست کردن سایز پنجره و همچنین ست کردن لوکیشن پنجره در وسط صفحه
window_width = 150
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ساخت لیبل 
tk.Label(root, text="اسم شهر را وارد کنید").grid(column=1, row=0)

# ساخت تکست باکس
city_f = tk.Entry(root, width=20)
city_f.grid(column=1, row=1)

def on_button_click():
    omw()

# دکمه بررسی آب و هوا
button = tk.Button(root, text="بررسی آب و هوا", command=on_button_click)
button.grid(column=1, row=2)

#لیبل سازنده : qashqaeii.ps4@gmail.com
tk.Label(root, text="C r e a t e d By QashQaei © ").grid(column=1, row=5)

root.mainloop()