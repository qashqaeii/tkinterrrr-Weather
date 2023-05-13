import pyowm
import tkinter as tk
from tkinter import messagebox

def omw():
    api_key = "f70735bded1ab2742724520cf568ec56"#نوش
    owm_obj = pyowm.OWM(api_key)
    mgr = owm_obj.weather_manager()  # Get the weather manager object
    city_name = city_f.get()

    obs = mgr.weather_at_place(city_name).weather  # Retrieve the weather observation
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



# Create a new window
root = tk.Tk()
root.title("آب و هوا")

# Set the window size and position it in the center of the screen
window_width = 150
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create label for entering city name
tk.Label(root, text="اسم شهر را وارد کنید").grid(column=1, row=0)

# Create entry box for entering city name
city_f = tk.Entry(root, width=20)
city_f.grid(column=1, row=1)

def on_button_click():
    omw()

# Create button for getting weather information
button = tk.Button(root, text="بررسی آب و هوا", command=on_button_click)
button.grid(column=1, row=2)

#craetor : qashqaeii.ps4@gmail.com
tk.Label(root, text="C r e a t e d By QashQaei © ").grid(column=1, row=5)

root.mainloop()