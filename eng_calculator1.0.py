import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
import math



window = tk.Tk()
window.iconbitmap("myIcon1.ico")
window.title('Eng Calculator')

bg = tk.PhotoImage(file = "1gray.png")
  
# Show image using label
label1 = tk.Label(
    master=window,
    image = bg,
)
label1.place(x = 0, y = 0)

frame = tk.Frame(window, bg= 'black')







lb_hist = tk.Listbox(
    master=frame,
    height=5,
    
    bg='#d9ffec',
    font=("Courier New", 10, 'bold' ),
)

sbr_hist = tk.Scrollbar(
    master=frame,
)

lb_hist.config(yscrollcommand=sbr_hist)
sbr_hist.config(command = lb_hist.yview)

lb_hist.grid(row=0, column=0, columnspan=6, sticky='news', pady=5, padx=(5,21))
sbr_hist.grid(row=0, column=5, sticky='ens', pady=5, padx=3)
# frame.geometry('200x150')

lbl_show_result = tk.Label(
    master=frame,
    text='0',
    bg='#d9ffec',
    font=("Lucida Console", 10, 'bold'),
    anchor='w'
)


lbl_show_result.grid(row=1, column=0, columnspan=6, pady=5, padx=5)


i = 1
calc_history = []

def cos(x): 
    return math.cos(math.radians(x))

def sin(x): 
    return math.sin(math.radians(x))

def tan(x): 
    return math.tan(math.radians(x))

def log(x):
    return math.log(x,10)

def ln(x):
    return math.log(x,math.e)

pi = math.pi


e = math.e

def click_equal(current):
    global i
    if current[-1] in ['+','-','*','/','(']:
        current = current[:-1]
    if current [-1] == '.' and not current[-2].isdigit():
        current = current[:-1] +'0.0'
    try:
        current = current.replace('%','/100')
        current = current.replace('²','**2')
        lbl_show_result['text'] = f"{eval(current)}"
    except Exception:
        lbl_show_result['text'] = 'Error'
    finally:
        # calc_history.append((current + ' = ' + lbl_show_result['text']))
        lb_hist.insert(i,(current + ' = ' + lbl_show_result['text']))
        i += 1

def click_percent(current, text='%'):
    test = re.split('\+|\-|\*|\/', current)
    if (('%' in test[-1]) or (test[-1] == '')):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_trigonometry(current, text):
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    elif len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    elif len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_log(current, text):
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_ln(current, text):
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pi(current, text):
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text


def click_e(current, text):
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pow(current, text):
    if not current[-1] in ['+','-','*','/','%','(']:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_point(current, text):
    if not re.split('\+|\-|\*|\/|\%', current)[-1].isdigit():
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_del(current, text):
    if len(lbl_show_result['text']) > 1:
        test = re.split('\+|\-|\*|\/', current)
        check_list = ['sin(','cos(','tan(','log(']
        if any(ele in test[-1][-4:] for ele in check_list):
            lbl_show_result['text'] = lbl_show_result['text'][:-4]
        elif 'ln(' in test[-1][-3:]:
            lbl_show_result['text'] = lbl_show_result['text'][:-3]
        else:
            lbl_show_result['text'] = lbl_show_result['text'][:-1]
    else:
        lbl_show_result['text'] = lbl_show_result['text'][:-1] + '0'

def mouse_left_click(event):
    try:
        j = lb_hist.curselection()[0]
        

        # lb_hist.selection_clear(0,tk.END)
        # lb_hist.selection_set(lb_hist.nearest(event.y))
        # lb_hist.activate(lb_hist.nearest(event.y))
        lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]
    except:
        pass

lb_hist.bind('<ButtonRelease-1>', mouse_left_click)

j=0
def click_up(current, text, lb_hist):
    global j
    try:
        j = lb_hist.curselection()[0]
    except:
        j= lb_hist.size()

    if j != 0:
        value = lb_hist.selection_clear(j)
        j -= 1
        value = lb_hist.selection_set(j)
        lb_hist.see(j)
        lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]


def click_down(current, text, lb_hist):
    global j
    try:
        j = lb_hist.curselection()[0]
    except:
        pass

    if lb_hist.size() != 0:
    
        if  j != lb_hist.size()-1:
            lb_hist.selection_clear(j)
            j += 1
            lb_hist.selection_set(j)
            lb_hist.see(j)
            lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]
        else:
            lb_hist.selection_clear(j)
            lbl_show_result['text'] = '0'

def store_file(fname, root):
    text_list = lb_hist.get(0, tk.END)
    with open(f'{fname}.txt', 'w') as f:
        f.writelines('\n'.join(text_list))
        f.close()
    root.destroy()



def click_save(*args):
    def handle_focus_in(_):
        ent_fname.delete(0, tk.END)
        ent_fname.config(fg='black')

    win2 = tk.Tk()
    win2.iconbitmap("myIcon1.ico")
    win2.title('Save History')
    win2.geometry('220x100')

    label = tk.Label(win2, text='Choose your textfile name:')
    label.grid(row=0, column=0, pady=(5,0))

    ent_fname = tk.Entry(win2, bg='white', width=30, fg='grey')
    ent_fname.grid(row=1, column=0, pady=5, padx=15)

    btn_name_save = ttk.Button(
        master=win2,
        text='Save',
        command= lambda: store_file(ent_fname.get(), win2)
    )
    btn_name_save.grid(row=2, column=0, pady=10)



    ent_fname.insert(0, "Example: textfile")

    ent_fname.bind("<FocusIn>", handle_focus_in)
    # ent_fname.bind("<FocusOut>", handle_focus_out)
    # ent_fname.bind("<Return>", handle_enter)

    win2.mainloop()

def click_exit(*args):
    ask_quit = messagebox.askquestion("Quit",
                           "Do you want to quit?")
    if ask_quit == 'yes':
        window.destroy()


def click_button(text):
    current = lbl_show_result['text']
    if current in ['0', 'Error']:
        if text in ['+','-','*','/','%','.','²']:
            lbl_show_result['text'] = '0' + text
        elif text == 'Del':
            pass
        elif text == '↓':
            click_down(current,text,lb_hist)
        elif text == '↑':
            click_up(current,text,lb_hist)
        else:
            lbl_show_result['text'] = text
    elif text == '=':
        click_equal(current)
    elif (text in ['+','-','*','/'] and current[-1] in ['+','-','*','/']):
        lbl_show_result['text'] = current[:-1] + text
    elif text == '%':
        click_percent(current, text)
    elif text in ['sin(','cos(','tan(']:
        click_trigonometry(current, text)
    elif text == 'log(':
        click_log(current, text)
    elif text == 'ln(':
        click_ln(current, text)
    elif text == 'pi':
        click_pi(current, text)
    elif text == 'e':
        click_e(current, text)
    elif text == '(':
        if not current[-1] in ['+','-','*','/','(']:
            lbl_show_result['text'] = lbl_show_result['text'] + '*' + text
        else:
            lbl_show_result['text'] = lbl_show_result['text'] + text 
    elif text == '²':
        click_pow(current, text)
    elif (text.isdigit() and current[-1] == ['%','sin(']):
        pass
    elif text == '.':
        click_point(current, text)
    elif text == 'Del':
        click_del(current, text)
    elif text =='↑':
        click_up(current, text, lb_hist)
    elif text =='↓':
        click_down(current, text, lb_hist)
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

    # for edit name of AC button to C
    if lbl_show_result['text'] == '0':
        calc_btn_objs[3]['text'] = 'AC'
    else:
        calc_btn_objs[3]['text'] = 'C'

def click_AC_C(text):
    global calc_history, i
    lbl_show_result['text'] = '0'
    if calc_btn_objs[3]['text'] == 'AC':
        # calc_history = []
        lb_hist.delete(0,i)
    else:
        calc_btn_objs[3]['text'] = 'AC'

eng_status = 'off'

calc_btn_eng_keys = [
    {
        'text': 'sin',
        'command': lambda: click_button('sin('),
        'button': '<Alt-s>',
        'bind_command': lambda e: click_button('sin(')
    },
    {
        'text': 'cos',
        'command': lambda: click_button('cos('),
        'button': '<Alt-c>',
        'bind_command': lambda e: click_button('cos(')
    },
    {
        'text': 'tan',
        'command': lambda: click_button('tan('),
        'button': '<Alt-t>',
        'bind_command': lambda e: click_button('tan(')
    },
    {
        'text': 'e',
        'command': lambda: click_button('e'),
        'button': '<Alt-e>',
        'bind_command': lambda e: click_button('e')
    },
    {
        'text': 'π',
        'command': lambda: click_button('pi'),
        'button': '<Alt-p>',
        'bind_command': lambda e: click_button('pi')
    },
    {
        'text': 'log',
        'command': lambda: click_button('log('),
        'button': 'l',
        'bind_command': lambda e: click_button('log(')
    },
    {
        'text': 'ln',
        'command': lambda: click_button('ln('),
        'button': '<Alt-l>',
        'bind_command': lambda e: click_button('ln(')
    },
    {
        'text': '(',
        'command': lambda: click_button('('),
        'button': '(',
        'bind_command': lambda e: click_button('(')
    },
    {
        'text': ')',
        'command': lambda: click_button(')'),
        'button': ')',
        'bind_command': lambda e: click_button(')')
    },
    {
        'text': 'x²',
        'command': lambda: click_button('²'),
        'button': '@',
        'bind_command': lambda e: click_button('²')
    },
]

calc_btn_eng_objs = []

for calc_btn_eng_key in calc_btn_eng_keys:
    btn_eng_calc = tk.Button(
        master=frame,
        text=calc_btn_eng_key['text'],
        relief=tk.GROOVE,
        width=8,
        height=1,
        command=calc_btn_eng_key['command']
        )
    calc_btn_eng_objs.append(btn_eng_calc)
    window.bind(calc_btn_eng_key['button'], calc_btn_eng_key['bind_command'])

    btn_eng_calc.configure(
        fg='white',
        bg='DarkSlateBlue',
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10, ),
    )

manage_btn_keys = [
    {
        'text':'↑',
        'command': lambda: click_button('↑'),
        'button': '<Up>',
        'bind_command': lambda e: click_button('↑'),
    },
    {
        'text':'↓',
        'command': lambda: click_button('↓'),
        'button': '<Down>',
        'bind_command': lambda e: click_button('↓'),
    },
    {
        'text':'Exit',
        'command': lambda: click_exit('Exit'),
        'button': '<Escape>',
        'bind_command': lambda e: click_exit('Exit'),
    },
    {
        'text':'Save',
        'command': lambda: click_save(),
        'button': '<Control-s>',
        'bind_command': click_save,
    },
]
    

manage_btn_objs = []
for manage_btn_key in manage_btn_keys:
    btn_manage = tk.Button(
        master=frame,
        text=manage_btn_key['text'],
        relief=tk.GROOVE,
        command=manage_btn_key['command']
    )

    manage_btn_objs.append(btn_manage)
    window.bind(manage_btn_key['button'], manage_btn_key['bind_command'])
    
    btn_manage.configure(
        fg='white',
        bg='gray10',
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10, ),
    )

manage_btn_objs[0].grid(row=2, column=2, columnspan=3, sticky='news', pady=(3,1), padx=3)
manage_btn_objs[1].grid(row=3, column=2, columnspan=3, sticky='news', pady=(1,3), padx=3)
manage_btn_objs[2].grid(row=2, column=5, rowspan=2, sticky='news', pady=2, padx=3)
manage_btn_objs[3].grid(row=2, column=1, rowspan=2, sticky='news', pady=2, padx=3)

def off_eng():
    global eng_status, manage_btn_objs
    eng_status ='off'
    for calc_btn_eng_obj in calc_btn_eng_objs:
        calc_btn_eng_obj.grid_forget()
    for manage_btn_obj in manage_btn_objs:
        manage_btn_obj.grid_forget()

    calc_btn_objs[15].grid(row=9, column=1, sticky='news')

    manage_btn_objs[0].grid(row=2, column=2, columnspan=3, sticky='news', pady=(3,1), padx=3)
    manage_btn_objs[1].grid(row=3, column=2, columnspan=3, sticky='news', pady=(1,3), padx=3)
    manage_btn_objs[2].grid(row=2, column=5, rowspan=2, sticky='news', pady=2, padx=3)
    manage_btn_objs[3].grid(row=2, column=1, rowspan=2, sticky='news', pady=2, padx=3)


def on_eng():
    global eng_status, manage_btn_objs
    eng_status = 'on'

    for i, calc_btn_eng_obj in enumerate(calc_btn_eng_objs[:-1]):

        if i >=4:
            calc_btn_eng_obj.grid(row=(i//13)+5, column=(i%5)+1, sticky='news', pady=3, padx=3)
        else:
            calc_btn_eng_obj.grid(row=(i%4)+5, column=0, sticky='news', pady=3, padx=3)
    calc_btn_objs[15].grid(row=9, column=0, sticky='news', pady=3, padx=3)
    calc_btn_eng_objs[-1].grid(row=9, column=1, sticky='news', pady=3, padx=3)
    
    manage_btn_objs[0].grid(row=2, column=2, columnspan=2, sticky='news', pady=(3,1), padx=3)
    manage_btn_objs[1].grid(row=3, column=2, columnspan=2, sticky='news', pady=(1,3), padx=3)
    manage_btn_objs[2].grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', pady=3, padx=3)
    manage_btn_objs[3].grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', pady=3, padx=3)
    
    
def click_eng(text):
    global eng_status
    if eng_status == 'on':
        off_eng()
        
    else:
        on_eng()

calc_btn_keys = [
    {
        'text': '7',
        'command': lambda : click_button('7'),
        'button': '7',
        'bind_command': lambda e: click_button('7'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '8',
        'command': lambda : click_button('8'),
        'button': '8',
        'bind_command': lambda e: click_button('8'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '9',
        'command': lambda : click_button('9'),
        'button': '9',
        'bind_command': lambda e: click_button('9'),
        'bg': 'gray20',
        'fg': 'white'
    },
        {
        'text': 'AC',
        'command': lambda : click_AC_C('AC'),
        'button': 'c',
        'bind_command': lambda e: click_AC_C('AC'),
        'bg': 'orange',
        'fg': 'black'
    },
    {
        'text': 'Del',
        'command': lambda : click_button('Del'),
        'button': '<Delete>',
        'bind_command': lambda e: click_button('Del'),
        'bg': 'orange',
        'fg': 'black'
    },
    {
        'text': '4',
        'command': lambda : click_button('4'),
        'button': '4',
        'bind_command': lambda e: click_button('4'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '5',
        'command': lambda : click_button('5'),
        'button': '5',
        'bind_command': lambda e: click_button('5'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '6',
        'command': lambda : click_button('6'),
        'button': '6',
        'bind_command': lambda e: click_button('6'),
        'bg': 'gray20',
        'fg': 'white'
    },
        {
        'text': '*',
        'command': lambda : click_button('*'),
        'button': '<*>',
        'bind_command': lambda e: click_button('*'),
        'bg': 'gray20',
        'fg': 'white'
    },
        {
        'text': '/',
        'command': lambda : click_button('/'),
        'button': '/',
        'bind_command': lambda e: click_button('/'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '1',
        'command': lambda : click_button('1'),
        'button': '1',
        'bind_command': lambda e: click_button('1'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '2',
        'command': lambda : click_button('2'),
        'button': '2',
        'bind_command': lambda e: click_button('2'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '3',
        'command': lambda : click_button('3'),
        'button': '3',
        'bind_command': lambda e: click_button('3'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '+',
        'command': lambda : click_button('+'),
        'button': '<+>',
        'bind_command': lambda e: click_button('+'),
        'bg': 'gray20',
        'fg': 'white'
    },
        {
        'text': '-',
        'command': lambda : click_button('-'),
        'button': '-',
        'bind_command': lambda e: click_button('-'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': 'Eng',
        'command': lambda : click_eng('Eng'),
        'button': 'e',
        'bind_command': lambda e: click_eng('Eng'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '0',
        'command': lambda : click_button('0'),
        'button': '0',
        'bind_command': lambda e: click_button('0'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '.',
        'command': lambda : click_button('.'),
        'button': '.',
        'bind_command': lambda e: click_button('.'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '%',
        'command': lambda : click_button('%'),
        'button': '<%>',
        'bind_command': lambda e: click_button('%'),
        'bg': 'gray20',
        'fg': 'white'
    },
    {
        'text': '=',
        'command': lambda : click_button('='),
        'button': '<Return>',
        'bind_command': lambda e: click_button('='),
        'bg': 'gray20',
        'fg': 'white'
    },
]

calc_btn_objs = []
for calc_btn_key in calc_btn_keys:
    btn_calc = tk.Button(
        master=frame,
        text=calc_btn_key['text'],
        relief=tk.GROOVE,
        width=8,
        height=1,
        command=calc_btn_key['command'],
    )
    btn_calc.configure(
        fg=calc_btn_key['fg'],
        bg=calc_btn_key['bg'],
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10 ),
    )
    
    calc_btn_objs.append(btn_calc)
    window.bind(calc_btn_key['button'], calc_btn_key['bind_command'])

for i, calc_btn_obj in enumerate(calc_btn_objs):
    calc_btn_obj.grid(row=(i//5)+6, column=(i%5)+1, sticky='news', pady=3, padx=3)

frame.grid(padx=10, pady=10)

window.protocol("WM_DELETE_WINDOW", click_exit)
window.mainloop()