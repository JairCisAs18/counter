from tkinter import *
from tkinter import ttk
from win32 import win32api as win
import datetime as dt

models = ['CMI-FC048', 'CAD01-H001', 'ROD BASE (ENSAMBLE)', 'AFM-AX231']
r_numbers = {
    'CMI-FC048':'R16-A220',
    'CAD01-H001':'R16-9814',
    'ROD BASE (ENSAMBLE)':'R16-9765',
    'AFM-AX231':'R16-9766'
}
root = Tk()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.title('Contador de piezas')
root.geometry('600x600+450+50')

btn = Button(root, text='Iniciar', width=180, font=('Arial', 18, 'bold'), compound='top', pady=12)
btn.place(x=200, y=350)
close_btn = Button(root, text='Terminar', width=180, font=('Arial', 18, 'bold'), compound='top', pady=12)
icon = PhotoImage(file=r'icon.png')
cancel = PhotoImage(file=r'close.png')
edit_icon = PhotoImage(file=r'pencil.png')
edit_icon = edit_icon.subsample(9, 9)
edit_btn = Button(root, width=30, image=edit_icon, borderwidth=3)
edit_btn.place(x=500, y=10)
icon = icon.subsample(6, 6)
cancel = cancel.subsample(6,6)
accept = PhotoImage(file=r'arrow.png')
accept = accept.subsample(6, 6) 
reject = PhotoImage(file=r'cross.png')
reject = reject.subsample(10, 10)
current = 0
target = -1
diff = 0
rate = 0.0
process = 0
line = 1
ppm = 1
#current = 0
#target = 0
takt_time = 1.5

def show_info():
    global prod_field, shift_field, start_field, end_field, takt_time
    # current = 0
    # target = -1
    # diff = 0
    # rate = 0.0
    root.protocol('WM_DELETE_WINDOW', lambda:None)
    model = selected.get()
    r_number = r_numbers.get(model)
    plan = int(prod_field.get())
    shift = shift_field.get()
    start = start_field.get()
    end = end_field.get()
    btn.place_forget()
    close_btn.place(x=200, y=350)
    display = win.EnumDisplayMonitors()[1][2]
    x = display[0]
    y = display[1]
    screen_width = display[2] - x
    screen_height = display[3] - y- 80
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    x_separation = screen_width/3
    y_separation = screen_height/5
    window = Toplevel(root)
    window.title('Información')
    date = dt.date.today()

    def place_target(t:int, label: Label):
        if len(str(t)) == 1:
            label.place(x=x_separation*1.45, y=y_separation*1.2)
        elif len(str(t)) == 2:
            label.place(x=x_separation*1.4, y=y_separation*1.2)
        elif len(str(t)) == 3:
            label.place(x=x_separation*1.35, y=y_separation*1.2)
        elif len(str(t)) == 4:
            label.place(x=x_separation*1.3, y=y_separation*1.2)

    def place_diff(diff: int, label: Label):
        if(diff < 0):
            label.config(fg='red')
        else:
            label.config(fg='cyan')
        if len(str(diff)) == 1:
            label.place(x=x_separation*1.45, y=y_separation*3.2)
        elif len(str(diff)) == 2:
            label.place(x=x_separation*1.4, y=y_separation*3.2)
        elif len(str(diff)) == 3:
            label.place(x=x_separation*1.35, y=y_separation*3.2)
        elif len(str(diff)) == 4:
            label.place(x=x_separation*1.3, y=y_separation*3.2)

    def place_rate(r: float, t:str, label: Label):
        if r >= 100:
            label.config(fg='cyan')
        else:
            label.config(fg='red')
        if len(t) == 4:
            label.place(x=x_separation*1.3, y=y_separation*4.2)
        elif len(t) == 5:
            label.place(x=x_separation*1.25, y=y_separation*4.2)
        elif len(t) == 6:
            label.place(x=x_separation*1.2, y=y_separation*4.2)

    def set_time():
        time = dt.datetime.now()
        time_label.config(text=f'{time:%H:%M:%S}')
        canvas.after(1000, set_time)

    def set_target():
        global target, current, diff, rate
        nonlocal diff_label, target_label, rate_label
        target += 1
        target_label.config(text=f'{target}')
        diff = current - target
        diff_label.config(text=f'{diff}')
        if target > 0:
            rate = round(current/target*100, 1)
            rate_str = str(rate) + '%'
            rate_label.config(text=rate_str)
            place_rate(rate, rate_str, rate_label)
        place_diff(diff, diff_label)
        #place_rate(rate, rate_str, rate_label)
        place_target(target, target_label)
        # if len(str(target)) == 1:
        #     target_label.place(x=x_separation*1.45, y=y_separation*1.2)
        # elif len(str(target)) == 2:
        #     target_label.place(x=x_separation*1.4, y=y_separation*1.2)
        # elif len(str(target)) == 3:
        #     target_label.place(x=x_separation*1.35, y=y_separation*1.2)
        # elif len(str(target)) == 4:
        #     target_label.place(x=x_separation*1.3, y=y_separation*1.2)
        canvas.after(int(takt_time*1000), set_target)

    def hide_info():
        close_btn.place_forget()
        btn.place(x=200, y=350)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        window.destroy()
        window.update()
         
    def update_counter(event):
        global current, diff, target, rate
        nonlocal current_label, diff_label, target_label, rate_label
        if event.keysym == 'space':
            current += 1
            current_label.config(text=f'{current}')
            diff = current - target
            diff_label.config(text=f'{diff}')
            target_label.config(text=f'{target}')
            if target > 0:
                rate = round(current/target*100, 1)
                rate_str = str(rate) + '%'
                rate_label.config(text=rate_str)
                place_rate(rate, rate_str, rate_label)
            place_diff(diff, diff_label)
            place_target(target, target_label)
            if len(str(current)) == 1:
                current_label.place(x=x_separation*1.45, y=y_separation*2.2)
            elif len(str(current)) == 2:
                current_label.place(x=x_separation*1.4, y=y_separation*2.2)
            elif len(str(current)) == 3:
                current_label.place(x=x_separation*1.35, y=y_separation*2.2)
            elif len(str(current)) == 4:
                current_label.place(x=x_separation*1.3, y=y_separation*2.2)
    window.bind('<Key>', update_counter)
    window.focus_set()
    #window.attributes('-fullscreen', True)
    close_btn.config(image=cancel, command=hide_info)
    window.geometry(f'{screen_width}x{screen_height}+{x}+{y}')
    canvas = Canvas(window, width=screen_width, height=screen_height, bg='black')
    canvas.pack()
    canvas.create_line(x_separation, 0, x_separation, screen_height, fill='white', width=2)
    canvas.create_line(x_separation*2, 0, x_separation*2, screen_height, fill='white', width=2)
    canvas.create_line(x_separation*2.5, 0, x_separation*2.5, screen_height, fill='white', width=2)
    canvas.create_line(0, y_separation, screen_width, y_separation, fill='white', width=2)
    canvas.create_line(0, y_separation*2, screen_width, y_separation*2, fill='white', width=2)
    canvas.create_line(0, y_separation*3, screen_width, y_separation*3, fill='white', width=2)
    canvas.create_line(0, y_separation*4, screen_width, y_separation*4, fill='white', width=2)
    canvas.create_line(x_separation*2, y_separation*0.5, screen_width, y_separation*0.5, fill='white', width=2)
    canvas.create_line(x_separation*2, y_separation*1.5, screen_width, y_separation*1.5, fill='white', width=2)
    canvas.create_line(x_separation*2, y_separation*2.5, screen_width, y_separation*2.5, fill='white', width=2)
    canvas.create_line(x_separation*2, y_separation*3.5, screen_width, y_separation*3.5, fill='white', width=2)
    canvas.create_line(x_separation*2, y_separation*4.5, screen_width, y_separation*4.5, fill='white', width=2)
    Label (canvas, text='PLAN', font=('Arial', 60, 'bold'), bg='black', fg='white').place(x=x_separation/3.5, y=y_separation/4)
    Label (canvas, text='TARGET', font=('Arial', 60, 'bold'), bg='black', fg='white').place(x=x_separation/4.5, y=y_separation*1.25)
    Label (canvas, text='ACTUAL', font=('Arial', 60, 'bold'), bg='black', fg='white').place(x=x_separation/4.5, y=y_separation*2.25)
    Label (canvas, text='DIFFERENCE', font=('Arial', 50, 'bold'), bg='black', fg='white').place(x=x_separation/6, y=y_separation*3.25)
    Label (canvas, text='ACHIEVEMENT RATE', font=('Arial', 40, 'bold'), bg='black', fg='white').place(x=50, y=y_separation*4.25)
    Label (canvas, text='PROD DATE', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2+20, y=25)
    Label (canvas, text='TIME', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.15, y=y_separation*0.5+25)
    Label (canvas, text='R-NO.', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.15, y=y_separation+25)
    Label (canvas, text='LINE NO.', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.1, y=y_separation*1.5+25)
    Label (canvas, text='PROD TIME', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2+20, y=y_separation*2+25)
    Label (canvas, text='SHIFT', font=('Arial' , 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.15, y=y_separation*2.5+25)
    Label (canvas, text='TAKT TIME', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2+25, y=y_separation*3+25)
    Label (canvas, text='REJECT RATE', font=('Arial', 30, 'bold'), bg='black', fg='white').place(x=x_separation*2+20, y=y_separation*3.5+25)
    Label (canvas, text='LENGTH', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.1, y=y_separation*4+25)
    Label (canvas, text=f'{plan}', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation/5)
    target_label = Label (canvas, text='0', font=('Arial', 80, 'bold'), bg='black', fg='cyan')
    #Label (canvas, text=f'{actual}', font=('Arial', 80, 'bold'), bg='black', fg='lime green').place(x=x_separation*1.45, y=y_separation*2.2)
    diff_label = Label (canvas, text=f'{diff}', font=('Arial', 80, 'bold'), bg='black', fg='cyan')
    rate_label = Label (canvas, text=f'{rate}%', font=('Arial', 80, 'bold'), bg='black', fg='red')
    Label (canvas, text=f'{date:%d/%m/%Y}', font=('Arial', 30, 'bold'), bg='black', fg='yellow').place(x=x_separation*2.5+50, y=25)
    Label (canvas, text=r_number, font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.5+55, y=y_separation+25)
    Label (canvas, text='12', font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.7, y=y_separation*1.5+25)
    Label (canvas, text=f'{start} - {end}', font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.5+40, y=y_separation*2+25)
    Label (canvas, text=shift, font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.7+10, y=y_separation*2.5+25)
    Label (canvas, text=f'{takt_time}', font=('Arial', 30, 'bold'), bg='black', fg='cyan').place(x=x_separation*2.66, y=y_separation*3+25)
    Label (canvas, text='1 ppm', font=('Arial', 30, 'bold'), bg='black', fg='red').place(x=x_separation*2.65, y=y_separation*3.5+25)
    time_label = Label (canvas, text='', font=('Arial', 30, 'bold'), bg='black', fg='yellow')
    current_label = Label(canvas, text=f'{current}', font=('Arial', 80, 'bold'), bg='black', fg='lime green')
    set_time()
    set_target()
    time_label.place(x=x_separation*2.6, y=y_separation*0.5+25)
    target_label.place(x=x_separation*1.45, y=y_separation*1.2)
    current_label.place(x=x_separation*1.45, y=y_separation*2.2)
    diff_label.place(x=x_separation*1.45, y=y_separation*3.2)
    rate_label.place(x=x_separation*1.3, y=y_separation*4.2)
    # if len(str(actual)) == 1:
    #     actual_label.place(x=x_separation*1.45, y=y_separation*2.2)
    # elif len(str(actual)) == 2:
    #     actual_label.place(x=x_separation*1.4, y=y_separation*2.2)
    # elif len(str(actual)) == 3:
    #     actual_label.place(x=x_separation*1.35, y=y_separation*2.2)
    # elif len(str(actual)) == 4:
    #     actual_label.place(x=x_separation*1.3, y=y_separation*2.2)
    # label_test = Label (canvas, text='Prueba', font=('Arial', 35, 'bold'), bg='black', fg='white')
    # def press():
    #     label_test.config(text='Hello')
    # Button(canvas, text='prueba', command=press).place(x=50, y=50)
    # label_test.place(x=x_separation*2.1, y=y_separation*4.5+10)
    #canvas.create_line(0, y_separation*5, screen_width, y_separation*5, fill='white', width=2)

def settings():
    global selected
    set = Toplevel(root)
    set.title('Configuración')
    set.geometry('550x700+480+20')
    headers = ['MODEL_N:', 'RNUMBER:', 'PROCESS_N:', 'LINE:', 'REJECT RATE:', 'TAKT TIME:']
    accept_btn = Button(set, text='Aceptar', width=150, height=100, font=('Arial', 14, 'bold'), image=accept, compound='top', pady=12)
    reject_btn = Button(set, text='Cancelar', width=150, height=100, font=('Arial', 14, 'bold'), image=reject, compound='top', pady=12)

    def confirm():
        global process, line, ppm, takt_time
        process = process_field.get()
        line = process_field.get()
        ppm = int(reject_field.get())
        takt_time = float(takt_field.get())
        set.destroy()
        set.update()

    def close():
        set.destroy()
        set.update()
    dist = 20
    for label in headers:
        Label(set, text=label, font=('Arial', 18, 'bold')).place(x=30, y=dist)
        dist += 60
    model_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    model_field.insert(0, selected.get())
    model_field.place(x=250, y=20)
    r_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    r_field.insert(0, r_numbers.get(selected.get()))
    r_field.place(x=250, y=80)
    process_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    process_field.insert(0,f'{line}')
    process_field.place(x=250, y=140)
    line_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    line_field.insert(0, f'{line}')
    line_field.place(x=250, y=200)
    reject_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    reject_field.insert(0, f'{ppm}')
    reject_field.place(x=250, y=260)
    takt_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    takt_field.insert(0, f'{takt_time}')
    takt_field.place(x=250, y=320)
    accept_btn.config(command=confirm)
    reject_btn.config(command=close)
    accept_btn.place(x=80, y=400)
    reject_btn.place(x=310, y=400)

model_label = Label(root, text='Modelo:', font=('Arial', 18, 'bold'))
model_label.place(x=15, y=10)

selected = StringVar()
selected.set('CMI-FC048')
dropdown = OptionMenu(root, selected, *models)
dropdown.config(width=20, font=('Arial', 14), bg='white', anchor='w', borderwidth=5, activebackground='lightgrey')
dropdown['menu'].config(font=('Arial', 14)) 
dropdown.place(x=150, y=5)

prod_label = Label(root, text='Plan Producción (Piezas):', font=('Arial', 18, 'bold'))
prod_label.place(x=15, y=80)
prod_field = Entry(root)
prod_field.config(width=7, font=('Arial', 14, 'bold'), borderwidth=4)
prod_field.place(x=330, y=80)

shift_label = Label(root, text='TURNO:', font=('Arial', 18, 'bold'))
shift_label.place(x=15, y=155)
shift_field = Entry(root)
shift_field.config(width=22, font=('Arial', 14, 'bold'), borderwidth=3)
shift_field.place(x=170,y=155)

start_label = Label(root, text='Inicio:', font=('Arial', 16, 'bold'))
start_label.place(x=65, y=200)
start_field = Entry(root)
start_field.config(width=18, font=('Arial', 14, 'bold'), borderwidth=3)
start_field.place(x=214, y=200)

end_label = Label(root, text='Fin:', font=('Arial', 16, 'bold'))
end_label.place(x=65, y=240)
end_field = Entry(root)
end_field.config(width=18, font=('Arial', 14, 'bold'), borderwidth=3)
end_field.place(x=214, y=240)

btn.config(image=icon, command=show_info)
edit_btn.config(command=settings)

root.mainloop()