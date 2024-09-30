import customtkinter as ctk
from PIL import Image, ImageTk
import sys
import os
import subprocess
import ctypes
from CTkMessagebox import CTkMessagebox

def show_checkmark():
    CTkMessagebox(message="Windows Updated Successfully!.",
                  icon="check", option_1="Close", fg_color = '#6552a2', title = 'Done!', bg_color = 'black', button_hover_color = '#884494', button_color = '#6552a2')

def show_checkmark_for_defender():
    CTkMessagebox(message="Defender Updated Successfully!.",
                  icon="check", option_1="Close", fg_color = '#6552a2', title = 'Done!', bg_color = 'black', button_hover_color = '#884494', button_color = '#6552a2')

def button_callback():
    sys.exit()

def shutdown_system():
    os.system("shutdown /s /t 0")

def reboot_system():
    os.system("shutdown /r /t 0")

def clean_trash():
    os.system('powershell.exe Clear-RecycleBin -Force')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def update_windows_():
    os.system("powershell Install-WindowsUpdate -AcceptAll -AutoReboot")
    show_checkmark()
    print('Done!')


def update_windows():
    if is_admin():
        print('Updating Windows...')
        update_windows_()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def update_defender():
    print("Updating Windows Defender...")
    os.system("powershell Update-MpSignature")
    show_checkmark_for_defender()
    print('Done!')

def lock_system():
    os.system('rundll32.exe user32.dll, LockWorkStation')

app = ctk.CTk()
app.corner_radius = 40
app.geometry('1000x600')
app.wm_iconname('rocket.ico')
app.title('Linux')
app._set_appearance_mode('dark')
app.overrideredirect(True)
app.configure(fg_color = 'black', bg_color = '#E6E6FA')

def start_move(event):
    app.x = event.x
    app.y = event.y

def stop_move(event):
    app.x = None
    app.y = None

def on_motion(event):
    x = event.x_root - app.x
    y = event.y_root - app.y
    app.geometry(f"+{x}+{y}")
def switch_to_monitoring():
    subprocess.Popen(['python', 'monitor.py'])
    sys.exit()

app.bind('<Button-1>', start_move)
app.bind('<ButtonRelease-1>', stop_move)
app.bind('<B1-Motion>', on_motion)

shutdown_image = Image.open("power.png").convert("RGBA")
background_image_shutdown = ImageTk.PhotoImage(shutdown_image.resize((120, 120)))

lock_image = Image.open("lock.png").convert("RGBA")
background_image_lock = ImageTk.PhotoImage(lock_image.resize((120, 120)))


reboot_image = Image.open("reboot.png").convert("RGBA")
background_image_reboot = ImageTk.PhotoImage(reboot_image.resize((120, 120)))

clean_trash_image = Image.open("trash.png").convert("RGBA")
background_image_clean_trash = ImageTk.PhotoImage(clean_trash_image.resize((120, 120)))

clean_system_image = Image.open("update_windows.png").convert("RGBA")
background_image_clean_system = ImageTk.PhotoImage(clean_system_image.resize((120, 120)))

clean_yay_image = Image.open("update_defender.png").convert("RGBA")
background_image_clean_yay = ImageTk.PhotoImage(clean_yay_image.resize((120, 120)))

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

button_tab1 = ctk.CTkButton(app, text = 'System', width = 100, fg_color = '#6F42C1', hover_color = '#6C757D')
button_tab1.grid(row = 0, column = 1, columnspan = 2)

button_tab2 = ctk.CTkButton(app, text = 'Monitoring', width = 100, command = switch_to_monitoring, fg_color = '#3ab3b6')
button_tab2.grid(row = 0, column = 0, columnspan = 2)

label1 = ctk.CTkLabel(app, text='', image=background_image_shutdown, fg_color = 'black')
label1.grid(row=1, column=0, padx=20, pady=20)

button1 = ctk.CTkButton(app, text='ShutDown', command=shutdown_system, bg_color='black', text_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button1.grid(row=2, column=0, padx=20, pady=20)

label2 = ctk.CTkLabel(app, text='', image=background_image_clean_trash, fg_color = 'black')
label2.grid(row=3, column=0, padx=20, pady=20)

button2 = ctk.CTkButton(app, text='Clean Trash', command=clean_trash, text_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button2.grid(row=4, column=0, padx=20, pady=20)

label3 = ctk.CTkLabel(app, text='', image=background_image_reboot, fg_color='black')
label3.grid(row=1, column=1, padx=20, pady=20)

button3 = ctk.CTkButton(app, text='Reboot', command=reboot_system, text_color = 'black', bg_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button3.grid(row=2, column=1, padx=20, pady=20)

label4 = ctk.CTkLabel(app, text='', image=background_image_clean_system, fg_color = 'black')
label4.grid(row=3, column=1, padx=20, pady=20)

button4 = ctk.CTkButton(app, text='Update Windows', command=update_windows, bg_color='black', text_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button4.grid(row=4, column=1, padx=20, pady=20)

label5 = ctk.CTkLabel(app, text='', image=background_image_lock, fg_color='black')
label5.grid(row=1, column=2, padx=20, pady=20)

button5 = ctk.CTkButton(app, text='Lock', command=lock_system, bg_color='black', text_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button5.grid(row=2, column=2, padx=20, pady=20)

label6 = ctk.CTkLabel(app, text='', image=background_image_clean_yay, bg_color='black')
label6.grid(row=3, column=2, padx=20, pady=20)

os.system('cls')

button6 = ctk.CTkButton(app, text='Update Defender', command=update_defender, bg_color='black', text_color = 'black', fg_color = '#6552a2', hover_color = '#884494')
button6.grid(row=4, column=2, padx=20, pady=20)

exit_button = ctk.CTkButton(app, text = 'Exit Program', command = button_callback, fg_color = 'purple', hover_color = 'darkred')
exit_button.grid(row=0, column=0, columnspan=3, pady=20)

app.mainloop()