from tkinter import *
from win32 import win32api as win
import datetime as dt

models = ['Modelo 1', 'Modelo 2']

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

def show_info():
    global prod_field, shift_field, start_field, end_field
    root.protocol('WM_DELETE_WINDOW', lambda:None)
    model = selected.get()
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
    def set_time():
        time = dt.datetime.now()
        time_label.config(text=f'{time:%H:%M:%S}')
        canvas.after(1000, set_time)
    def hide_info():
        close_btn.place_forget()
        btn.place(x=200, y=350)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        window.destroy()
        window.update()
    def update_counter(event):
        global current
        nonlocal current_label
        if event.keysym == 'space':
            current += 1
            current_label.config(text=f'{current}')
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
    Label (canvas, text='740', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation*1.2)
    #Label (canvas, text=f'{actual}', font=('Arial', 80, 'bold'), bg='black', fg='lime green').place(x=x_separation*1.45, y=y_separation*2.2)
    Label (canvas, text='756', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation*3.2)
    Label (canvas, text='10.5%', font=('Arial', 80, 'bold'), bg='black', fg='red').place(x=x_separation*1.25, y=y_separation*4.2)
    Label (canvas, text=f'{date:%d/%m/%Y}', font=('Arial', 30, 'bold'), bg='black', fg='yellow').place(x=x_separation*2.5+50, y=25)
    Label (canvas, text=model, font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.5+55, y=y_separation+25)
    Label (canvas, text='12', font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.7, y=y_separation*1.5+25)
    Label (canvas, text=f'{start} - {end}', font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.5+40, y=y_separation*2+25)
    Label (canvas, text=shift, font=('Arial', 30, 'bold'), bg='black', fg='green3').place(x=x_separation*2.7+10, y=y_separation*2.5+25)
    Label (canvas, text='45.00', font=('Arial', 30, 'bold'), bg='black', fg='cyan').place(x=x_separation*2.66, y=y_separation*3+25)
    Label (canvas, text='1 ppm', font=('Arial', 30, 'bold'), bg='black', fg='red').place(x=x_separation*2.65, y=y_separation*3.5+25)
    time_label = Label (canvas, text='', font=('Arial', 30, 'bold'), bg='black', fg='yellow')
    current_label = Label(canvas, text=f'{current}', font=('Arial', 80, 'bold'), bg='black', fg='lime green')
    set_time()
    time_label.place(x=x_separation*2.6, y=y_separation*0.5+25)
    current_label.place(x=x_separation*1.45, y=y_separation*2.2)
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
    set = Toplevel(root)
    set.title('Configuración')
    set.geometry('550x700+480+20')
    headers = ['MODEL_N:', 'RNUMBER:', 'PROCESS_N:', 'LINE:', 'REJECT RATE:', 'TAKT TIME:']
    accept_btn = Button(set, text='Aceptar', width=150, height=100, font=('Arial', 14, 'bold'), image=accept, compound='top', pady=12)
    accept_btn.place(x=80, y=400)
    reject_btn = Button(set, text='Cancelar', width=150, height=100, font=('Arial', 14, 'bold'), image=reject, compound='top', pady=12)
    def close():
        set.destroy()
        set.update()
    dist = 20
    for label in headers:
        Label(set, text=label, font=('Arial', 18, 'bold')).place(x=30, y=dist)
        dist += 60
    model_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    model_field.place(x=250, y=20)
    r_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    r_field.place(x=250, y=80)
    process_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    process_field.place(x=250, y=140)
    line_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    line_field.place(x=250, y=200)
    reject_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    reject_field.place(x=250, y=260)
    takt_field = Entry(set, font=('Arial', 18, 'bold'), width=18, borderwidth=2)
    takt_field.place(x=250, y=320)
    reject_btn.config(command=close)
    reject_btn.place(x=310, y=400)

model_label = Label(root, text='Modelo:', font=('Arial', 18, 'bold'))
model_label.place(x=15, y=10)

selected = StringVar()
selected.set('Modelo 1')
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