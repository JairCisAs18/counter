from tkinter import *
from win32 import win32api as win
import datetime as dt

models = ['Modelo 1', 'Modelo 2']

root = Tk()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.title('Contador de piezas')
root.geometry('600x600+450+50')

def show_info():
    display = win.EnumDisplayMonitors()[1][2]
    x = display[0]
    y = display[1]
    screen_width = display[2] - x
    screen_height = display[3] - y - 50
    x_separation = screen_width/3
    y_separation = screen_height/5
    window = Toplevel()
    window.title('Información')
    date = dt.date.today()
    def set_time():
        time = dt.datetime.now()
        time_label.config(text=f'{time:%H:%M:%S}')
        canvas.after(1000, set_time)
    #window.attributes('-fullscreen', True)
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
    Label (canvas, text='REJECT QTY.', font=('Arial', 30, 'bold'), bg='black', fg='white').place(x=x_separation*2+20, y=y_separation*3.5+25)
    Label (canvas, text='REJECT RATE', font=('Arial', 30, 'bold'), bg='black', fg='white').place(x=x_separation*2+20, y=y_separation*4+25)
    Label (canvas, text='LENGTH', font=('Arial', 35, 'bold'), bg='black', fg='white').place(x=x_separation*2.1, y=y_separation*4.5+10)
    Label (canvas, text='600', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation/5)
    Label (canvas, text='740', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation*1.2)
    Label (canvas, text='5', font=('Arial', 80, 'bold'), bg='black', fg='lime green').place(x=x_separation*1.45, y=y_separation*2.2)
    Label (canvas, text='756', font=('Arial', 80, 'bold'), bg='black', fg='cyan').place(x=x_separation*1.35, y=y_separation*3.2)
    Label (canvas, text='10.5%', font=('Arial', 80, 'bold'), bg='black', fg='red').place(x=x_separation*1.25, y=y_separation*4.2)
    Label (canvas, text=f'{date:%d/%m/%Y}', font=('Arial', 30, 'bold'), bg='black', fg='yellow').place(x=x_separation*2.5+50, y=25)
    time_label = Label (canvas, text='', font=('Arial', 30, 'bold'), bg='black', fg='yellow')
    set_time()
    time_label.place(x=x_separation*2.6, y=y_separation*0.5+25)
    # label_test = Label (canvas, text='Prueba', font=('Arial', 35, 'bold'), bg='black', fg='white')
    # def press():
    #     label_test.config(text='Hello')
    # Button(canvas, text='prueba', command=press).place(x=50, y=50)
    # label_test.place(x=x_separation*2.1, y=y_separation*4.5+10)
    #canvas.create_line(0, y_separation*5, screen_width, y_separation*5, fill='white', width=2)

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

icon = PhotoImage(file=r'icon.png')
icon = icon.subsample(6, 6)
btn = Button(root, text='Iniciar', width=180, font=('Arial', 18, 'bold'), image=icon, compound='top', pady=12, command=show_info)
btn.place(x=200, y=350)

root.mainloop()