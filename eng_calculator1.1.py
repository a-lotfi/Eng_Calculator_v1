import tkinter as tk
from tkinter import END, messagebox
from tkinter import ttk
import re
import math

from click import command

# create main window
window = tk.Tk()
# window.iconbitmap(r"..\myIcon1.ico")
window.title('Eng Calculator')
# automatic resize of window
window.resizable(False,False)
# bg = tk.PhotoImage(file = "1gray.png")

window.configure(bg='#ffffff')

# create a frame to place the desired widgets
frame = tk.Frame(window, bg= '#ffffff')

# create listbox for calculation history
lb_hist = tk.Listbox(
    master=frame,
    height=5,
    bg='#d9ffec',
    font=("Courier New", 10, 'bold' ),
)

# create scrollbar for listbox
sbr_hist = tk.Scrollbar(
    master=frame,
)

# link listbox with scrollbar
lb_hist.config(yscrollcommand=sbr_hist)
sbr_hist.config(command = lb_hist.yview)

# grid listbox and scrollbar
lb_hist.grid(row=0, column=0, columnspan=6, sticky='news', pady=5, padx=(5,21))
sbr_hist.grid(row=0, column=5, sticky='ens', pady=5, padx=3)

lbl_show_result = tk.Label(
    master=frame,
    text='0',
    relief="groove",
    bg='#d9ffec',
    font=("Lucida Console", 10, 'bold'),
)

lbl_show_result.grid(row=1, column=0, columnspan=6, pady=5, padx=5)

pi = math.pi
e = math.e


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

def click_equal(current):
    """
    run when user click = button
    
    Args:
        current(str): contexts of lbl_show_result
    """
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
        lb_hist.insert(lb_hist.size()+1,(current + ' = ' + lbl_show_result['text']))

def click_percent(current, text):
    """
    run when user click % button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): %
    """
    test = re.split('\+|\-|\*|\/', current)
    if (('%' in test[-1]) or (test[-1] == '')):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_trigonometry(current, text):
    """
    run when user click sin or cos or tan button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): sin( or cos( or tan(
    """
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
    """
    run when user click log button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): log(
    """
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_ln(current, text):
    """
    run when user click ln button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): ln(
    """
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pi(current, text):
    """
    run when user click π button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): pi
    """
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text


def click_e(current, text):
    """
    run when user click e button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): e
    """
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pow(current, text):
    """
    run when user click power 2 button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): ²
    """
    if not current[-1] in ['+','-','*','/','%','(']:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_point(current, text):
    """
    run when user click . button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): .
    """
    if not re.split('\+|\-|\*|\/|\%', current)[-1].isdigit():
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_del(current):
    """
    run when user click Del button
    
    Args:
        current(str): contexts of lbl_show_result
    """
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

def mouse_left_click(*args):
    """
    run when user use Left click of mouse
    
    Args:
        args : 'nothing'. just used for binding
    """
    try:
        j = lb_hist.curselection()[0]
        lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]
    except:
        pass

lb_hist.bind('<ButtonRelease-1>', mouse_left_click)

def click_up(lb_hist):
    """
    run when user click ↑ button
    
    Args:
        lb_hsit (listbox): lb_hist is the listbox that have calculation history
    """
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

def click_down(lb_hist):
    """
    run when user click ↓ button
    
    Args:
        lb_hsit (listbox): lb_hist is the listbox that have calculation history
    """
    try:
        j = lb_hist.curselection()[0]
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
    except:
        pass

def store_file(fname, root):
    """
    run when user click on Save button in save history window
    
    Args:
        fname(str): name of textfile for storing
        root: window 
    """
    text_list = lb_hist.get(0, tk.END)
    with open(f'{fname}.txt', 'w') as f:
        f.writelines('\n'.join(text_list))
        f.close()
    root.destroy()

def click_save(*args):
    """
    run when user click save button in main window
    
    Args:
        args : 'nothing'. just used for binding
    """
    def handle_focus_in(_):
        """
        delete and replace example text by name of text file
        """
        ent_fname.delete(0, tk.END)
        ent_fname.config(fg='black')

    win2 = tk.Tk()
    # win2.iconbitmap(r"..\myIcon1.ico")
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

    win2.mainloop()

def click_exit(*args):
    """
    run when user click Exit button
    
    Args:
        args : 'nothing'. just used for binding
    """
    ask_quit = messagebox.askquestion("Quit",
                           "Do you want to quit?")
    if ask_quit == 'yes':
        window.destroy()

def click_button(text):
    """
    run when user click some button like numbers and etc.
    
    Args:
        text(str): the string that user entered by click button
    """
    current = lbl_show_result['text']
    if current in ['0', 'Error']:
        if text in ['+','-','*','/','%','.','²']:
            lbl_show_result['text'] = '0' + text
        elif text == 'Del':
            pass
        elif text == '↓':
            click_down(lb_hist)
        elif text == '↑':
            click_up(lb_hist)
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
        click_del(current)
    elif text =='↑':
        click_up(lb_hist)
    elif text =='↓':
        click_down(lb_hist)
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

    # for edit name of AC button to C
    if lbl_show_result['text'] == '0':
        calc_btn_objs[3]['text'] = 'AC'
    else:
        calc_btn_objs[3]['text'] = 'C'

def click_AC_C(*args):
    """
    run when user click AC/C button
    
    Args:
        args : 'nothing'. just used for binding
    """
    lbl_show_result['text'] = '0'
    if calc_btn_objs[3]['text'] == 'AC':
        lb_hist.delete(0,END)
    else:
        calc_btn_objs[3]['text'] = 'AC'

def off_eng(*args):
    """
    off Eng button 
    """
    for calc_btn_eng_obj in calc_btn_eng_objs:
        calc_btn_eng_obj.grid_forget()
    for manage_btn_obj in calc_manage_btn_objs:
        manage_btn_obj.grid_forget()

    calc_manage_btn_objs[0].grid(row=2, column=2, columnspan=3, sticky='news', pady=(3,1), padx=3)
    calc_manage_btn_objs[1].grid(row=3, column=2, columnspan=3, sticky='news', pady=(1,3), padx=3)
    calc_manage_btn_objs[2].grid(row=2, column=5, rowspan=2, sticky='news', pady=2, padx=3)
    calc_manage_btn_objs[3].grid(row=2, column=1, rowspan=2, sticky='news', pady=2, padx=3)

    calc_btn_objs[15].configure(command=on_eng)
    window.bind('e', on_eng)

def on_eng(*args):
    """
    on Eng button
    """
    for i, calc_btn_eng_obj in enumerate(calc_btn_eng_objs):

        if i >=5:
            calc_btn_eng_obj.grid(row=(i//10)+5, column=(i%5)+1, sticky='news', pady=3, padx=3)
        else:
            calc_btn_eng_obj.grid(row=(i%5)+5, column=0, sticky='news', pady=3, padx=3)
    
    calc_manage_btn_objs[0].grid(row=2, column=2, columnspan=2, sticky='news', pady=(3,1), padx=3)
    calc_manage_btn_objs[1].grid(row=3, column=2, columnspan=2, sticky='news', pady=(1,3), padx=3)
    calc_manage_btn_objs[2].grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news', pady=3, padx=3)
    calc_manage_btn_objs[3].grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news', pady=3, padx=3)
    
    calc_btn_objs[15].configure(command=off_eng)
    window.bind('e', off_eng)


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

calc_manage_btn_keys = [
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
        'command': lambda: click_exit(),
        'button': '<Escape>',
        'bind_command': lambda e: click_exit(),
    },
    {
        'text':'Save',
        'command': lambda: click_save(),
        'button': '<Control-s>',
        'bind_command': click_save,
    },
]

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
        'command': on_eng,
        'button': 'e',
        'bind_command': lambda e: on_eng(),
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

# create engineering calculator button by for loop
calc_btn_eng_objs = []
for calc_btn_eng_key in calc_btn_eng_keys:
    btn_eng_calc = tk.Button(
        master=frame,
        text=calc_btn_eng_key['text'],
        relief=tk.GROOVE,
        width=8,
        height=1,
        command=calc_btn_eng_key['command'],
        fg='white',
        bg='DarkSlateBlue',
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10, ),
        )
    calc_btn_eng_objs.append(btn_eng_calc)
    window.bind(calc_btn_eng_key['button'], calc_btn_eng_key['bind_command'])

# create management button of calculator by for loop
calc_manage_btn_objs = []
for calc_manage_btn_key in calc_manage_btn_keys:
    btn_manage = tk.Button(
        master=frame,
        text=calc_manage_btn_key['text'],
        relief=tk.GROOVE,
        command=calc_manage_btn_key['command'],
        fg='white',
        bg='gray10',
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10, ),
    )

    calc_manage_btn_objs.append(btn_manage)
    window.bind(calc_manage_btn_key['button'], calc_manage_btn_key['bind_command'])

# grid management button of calculator like save and exit button
calc_manage_btn_objs[0].grid(row=2, column=2, columnspan=3, sticky='news', pady=(3,1), padx=3)
calc_manage_btn_objs[1].grid(row=3, column=2, columnspan=3, sticky='news', pady=(1,3), padx=3)
calc_manage_btn_objs[2].grid(row=2, column=5, rowspan=2, sticky='news', pady=2, padx=3)
calc_manage_btn_objs[3].grid(row=2, column=1, rowspan=2, sticky='news', pady=2, padx=3)

calc_btn_objs = []
for calc_btn_key in calc_btn_keys:
    btn_calc = tk.Button(
        master=frame,
        text=calc_btn_key['text'],
        relief=tk.GROOVE,
        width=8,
        height=1,
        command=calc_btn_key['command'],
        fg=calc_btn_key['fg'],
        bg=calc_btn_key['bg'],
        activebackground='gray71',
        activeforeground='gray71',
        font=("Comic Sans MS", 10 ),
    )
    
    calc_btn_objs.append(btn_calc)
    window.bind(calc_btn_key['button'], calc_btn_key['bind_command'])

# grid simple button of calculator like numbers and */-+ etc.
for i, calc_btn_obj in enumerate(calc_btn_objs):
    calc_btn_obj.grid(row=(i//5)+6, column=(i%5)+1, sticky='news', pady=3, padx=3)

frame.grid(padx=12, pady=12)



# show warning when exit 
window.protocol("WM_DELETE_WINDOW", click_exit)
window.mainloop()