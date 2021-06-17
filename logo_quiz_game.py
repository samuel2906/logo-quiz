from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import os




#root variables
root = Tk()
root.geometry("700x700")
root.resizable(0,0)
root.title("Logo Quiz")

canvas_rule = Canvas(root)
canvas_game = Canvas(root)
canvas_start = Canvas(root)
canvas_new_user = Canvas(root)
canvas_login_user = Canvas(root)
canvas_users= Canvas(root)
anylevel_frame = Canvas(root)

number_pic = 0




photo_bg = ImageTk.PhotoImage(Image.open("apps.20660.14434946597921362.9f02a0b5-6441-476c-9378-148e87e39b74.png").resize((696,696)))


#fonts
font_label = font.Font(size = 70, family = "Arial Black")
button_labels = font.Font(family = "Times Bold", size = 30)
back_button_font = font.Font(family = "Times Bold", size = 20)
canvas_rules_label = font.Font(family = "Times Bold", size = 60)
level_font = font.Font(family = "Times Bold", size = 10)
correct_font = font.Font(size = 60, family = "Arial Black")

#functions

def rules_window():
    global global_status_canvas
    global_status_canvas.pack_forget()
    canvas_rule.pack(expand = True, fill = BOTH)
    

    #global
    global_status_canvas = canvas_rule
    
    canvas_rule.create_image(350,350,image = photo_bg)
    canvas_rule.create_rectangle(60,60,650,650, fill = "white",stipple = "gray50")
    canvas_rule.create_text(360, 120, text = "RULES", font = canvas_rules_label)
    rules = """
Welcome!! This game is about
guessing the logos shown.
1)There are 6 levels, when
starting only level 1 will be
accessible

2)Continue guessing logos
and you can unlock new levels
            ENJOY!
"""
    canvas_rule.create_text(360,350, text = rules, font = button_labels)
    back_button_rules = Button(text = "←", font = back_button_font, command = back_menu)
    canvas_rule.create_window(30,30, window = back_button_rules)

def back_menu(answer = 0, submit = 0):
    global global_status_canvas
    global_status_canvas.pack_forget()
    root.geometry("700x700")


    if global_status_canvas == canvas_new_user or global_status_canvas == canvas_login_user:
        canvas_users.pack(fill = BOTH, expand = True)
        global_status_canvas = canvas_users
        
    elif global_status_canvas == canvas_rule or global_status_canvas == canvas_game:
        canvas_start.pack(fill = BOTH, expand = True)
        global_status_canvas = canvas_start
    else:
        anylevel_frame.itemconfigure(answer_create, state = "hidden")
        anylevel_frame.itemconfigure(submit_create, state = "hidden")
        canvas_game.pack(fill = BOTH, expand = True)
        global_status_canvas = canvas_game

        
def start_game():
    global global_status_canvas, level1,level2,level3,level4,level5,level6
    canvas_start.pack_forget()
    canvas_game.pack(expand = True, fill = BOTH)


    #global
    global_status_canvas = canvas_game
    
#levels
    level1 = Button(canvas_game, text = "1", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level1"))
    level2 = Button(canvas_game, text = "2", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level2"))
    level3 = Button(canvas_game, text = "3", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level3"))
    level4 = Button(canvas_game, text = "4", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level4"))
    level5 = Button(canvas_game, text = "5", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level5"))
    level6 = Button(canvas_game, text = "6", font = button_labels, width = 3, height = 1, state = DISABLED, command = lambda: any_level(canvas_game,anylevel_frame, "level6"))
    
    for i in active_levels:
        button = eval(i)
        button["state"] = NORMAL

    canvas_game.create_window(150,300, window = level1)
    canvas_game.create_window(350,300, window = level2)
    canvas_game.create_window(550,300, window = level3)
    canvas_game.create_window(150,500, window = level4)
    canvas_game.create_window(350,500, window = level5)
    canvas_game.create_window(550,500, window = level6)    

    canvas_game.create_image(350,350,image = photo_bg)
    canvas_game.create_rectangle(60,60,650,650, fill = "white",stipple = "gray50")

    back_button_rules = Button(text = "←", font = back_button_font, command = back_menu)
    canvas_game.create_window(30,30,window = back_button_rules)
    canvas_game.create_text(358,100,text = "LEVELS", font = canvas_rules_label)

def canvas_starting():
    global global_status_canvas
    global_status_canvas.pack_forget()
    root.geometry("700x700")
    
    #canvas_starting
    canvas_start.pack(expand = True, fill = BOTH)

    canvas_start.create_image(350,350,image = photo_bg)

    global_status_canvas = canvas_start
    
    #logoquiz
    canvas_start.create_text(350,205, text = "LOGO QUIZ", font = font_label)


    #buttons
    button_1 = Button(text = "Start", font = button_labels, width = 10, command = start_game)
    button_2 = Button(text = "Rules", font = button_labels, width = 10, command = rules_window)
    button_3 = Button(text = "Quit", font = button_labels, width = 10, command = root.destroy)


    canvas_start.create_window(350,400,window = button_1)
    canvas_start.create_window(350,500,window = button_2)
    canvas_start.create_window(350,600,window = button_3)

 
def new_user():

    global global_status_canvas
    
    global_status_canvas.pack_forget()
    root.geometry("400x400")
    
    canvas_new_user.pack(fill = BOTH, expand = True)
    global_status_canvas = canvas_new_user

    new_username = StringVar()
    new_password = StringVar()

    canvas_new_user.create_text(200,50,text = "New User", font = button_labels)
    user_entry = Entry(textvariable = new_username)
    canvas_new_user.create_window(300, 140, window = user_entry)
    canvas_new_user.create_text(125, 140, text = "Enter Username: ", font = back_button_font)

    pass_entry = Entry(textvariable = new_password)
    canvas_new_user.create_window(300, 225, window = pass_entry)
    canvas_new_user.create_text(125, 225, text = "Enter Password: ", font = back_button_font)

    button_login_new_user= Button(text = "Join", font = back_button_font, width = 8, command = lambda: process_username(new_username.get(),new_password.get()))
    canvas_new_user.create_window(200,350, window = button_login_new_user)

    back_button_rules = Button(text = "←", font = back_button_font, command = back_menu)
    canvas_new_user.create_window(30,30,window = back_button_rules)
    

def process_username(username,password):
    my_file = open("store_data.txt","a")
    text = {username:password,'active_levels':['level1'],'list_correct':[]}
    my_rfile = open("store_data.txt")
    data = (my_rfile.read().split(";"))[0:-1]

    for i in data:
        list_1 = eval(i)
        if username in list(list_1.keys()):
            messagebox.showwarning("Error","Username taken!")
            break
            
    else:
        my_file.writelines(str(text)+";")
        my_file.close()
        my_rfile.close()
        login_user()

    

def login_user():
    global global_status_canvas
    
    global_status_canvas.pack_forget()
    root.geometry("400x400")
    canvas_login_user.pack(fill = BOTH, expand = True)
    global_status_canvas = canvas_login_user

    login_username = StringVar()
    login_password = StringVar()

    
    canvas_login_user.create_text(200,50,text = "Login", font = button_labels)
    user_entry = Entry(textvariable = login_username)
    canvas_login_user.create_window(300, 140, window = user_entry)
    canvas_login_user.create_text(125, 140, text = "Enter Username: ", font = back_button_font)

    pass_entry = Entry(textvariable = login_password)
    canvas_login_user.create_window(300, 225, window = pass_entry)
    canvas_login_user.create_text(125, 225, text = "Enter Password: ", font = back_button_font)

    button_login_login_user= Button(text = "Login", font = back_button_font, width = 8, command = lambda: login_process(login_username.get(),login_password.get()))
    canvas_login_user.create_window(200,350, window = button_login_login_user)

    back_button_rules = Button(text = "←", font = back_button_font, command = back_menu)
    canvas_login_user.create_window(30,30,window = back_button_rules)
    

def login_process(username, password):
    global list_correct, login_username, login_password, active_levels
    
    my_file = open("store_data.txt")
    data = (my_file.read().split(";"))[0:-1]

    for i in data:
        list_1 = eval(i)
        if (username,password) in list_1.items():
            login_username = username
            login_password =password
            list_correct = list_1.get("list_correct")
            active_levels = list_1.get("active_levels")
            canvas_starting()
            break
    else:
        messagebox.showwarning("Error","Wrong login and pass combination")
    my_file.close()


def any_level(frame, anylevel_frame, name_of_level):
    global photo_x, photo_bg_level, number_pic, global_status_canvas, answer, answer_entry, submit_button, answer_create, submit_create, label_correct


    global_status_canvas = anylevel_frame
    answer = StringVar()
    
    number_pic = 0
    frame.pack_forget()
    anylevel_frame.pack(fill = BOTH, expand = True)    
    arr = os.listdir(name_of_level)
    photo_bg_level = ImageTk.PhotoImage(Image.open("Image20210208193839.png").resize((696,696)))
    anylevel_frame.create_image(350,350,image = photo_bg_level)

    photo_x = ImageTk.PhotoImage(Image.open(arr[0]).resize((350,350)))

    label_level = Label(anylevel_frame, image = photo_x)
    label_level.place(x = 180, y = 100)

    answer_entry = Entry(anylevel_frame, text = answer, font = button_labels)

    answer_create = anylevel_frame.create_window(360, 500, window =answer_entry)

    submit_button = Button(anylevel_frame, text = "Submit", font = back_button_font, command = lambda: check_ans(answer.get(),arr))

    submit_create = anylevel_frame.create_window(370, 600, window = submit_button)
                                 
    
    button_next = Button(anylevel_frame, text = "→", font = level_font, command = lambda: picture_next(arr, label_level), height = 20, width = 5)
    button_previous = Button(anylevel_frame, text = "←", font = level_font, command = lambda: picture_prev(arr, label_level), height = 20, width = 5)

    back_button = Button(anylevel_frame, text = "←", font = back_button_font, command = back_menu)

    back_button.place(x = 2, y = 3)
    button_next.place(x = 535, y = 110)
    button_previous.place(x = 130, y = 110)
    label_correct = anylevel_frame.create_text(362,575, text = "CORRECT!",font = correct_font, fill = "dark green")
    correct_ans(arr)

def correct_ans(arr):
    global label_correct
    if arr[number_pic] in list_correct:
        anylevel_frame.itemconfigure(answer_create, state = "hidden")
        anylevel_frame.itemconfigure(submit_create, state = "hidden")
        anylevel_frame.itemconfigure(label_correct, state = "normal")

                
    else:
        anylevel_frame.itemconfigure(answer_create, state = "normal")
        anylevel_frame.itemconfigure(submit_create, state = "normal")
        anylevel_frame.itemconfigure(label_correct, state = "hidden")
def picture_next(arr, label_level):
    global photo_x, number_pic, status
    if number_pic == (len(arr)-1):
        number_pic = 0
    else:
        number_pic+= 1

    if arr[number_pic] in list_correct:
        correct_ans(arr)
    else:
        correct_ans(arr)


    answer_entry.delete(0,"end")
    photo_x = ImageTk.PhotoImage(Image.open(arr[number_pic]).resize((350,350)))
    label_level.config(image = photo_x)

def picture_prev(arr, label_level):
    global photo_x, number_pic

    if number_pic == -(len(arr)-1):
        number_pic = len(arr)-1
    else:
        number_pic-= 1

    if arr[number_pic] in list_correct:
        correct_ans(arr)
    else:
        correct_ans(arr)
    answer_entry.delete(0,"end")
    photo_x = ImageTk.PhotoImage(Image.open(arr[number_pic]).resize((350,350)))
    label_level.config(image = photo_x)

def check_ans(answer, arr):
    global active_levels
    if answer.lower() == ((arr[number_pic])[0:-4]):
        list_correct.append(arr[number_pic])
        file = open("store_data.txt")
        data = ((file.read()).split(";"))[0:-1]
        file.close()

        num = len(list_correct)
        den = 0

        for i in active_levels:
            den+=len(i)
        percent = ((num/den)*100)

        if ((num/den)*100) >= 75:
            if (int((active_levels[-1])[-1])+1) != 7:            
                level = "level"+(str(int((active_levels[-1])[-1])+1))
                active_levels.append(level)
                button = eval(active_levels[-1])
                button["state"] = NORMAL
                messagebox.showinfo("CONGRATS!","New level unlocked!!!")
                                     


        for a in data:
            ind_data = eval(a)
            if (login_username,login_password) in ind_data.items():
                ind_data["list_correct"] = list_correct
                ind_data["active_levels"] = active_levels

                data[data.index(a)] = str(ind_data)


        

        data_1 = (";".join(data))+";"
        file_1 = open("store_data.txt","w")
        file_1.writelines(data_1)
        file_1.close()
        correct_ans(arr)



global_status_canvas = canvas_users
canvas_users.pack(expand = True, fill = BOTH)


canvas_users.create_image(350,350, image = photo_bg)

canvas_users.create_text(350,205, text = "LOGO QUIZ", font = font_label)

button_new_user = Button(text = "New User", font = button_labels, command = new_user)
canvas_users.create_window(350,500,window = button_new_user)

button_login = Button(text = "Login", font = button_labels, width = 8, command = login_user)
canvas_users.create_window(350,400, window = button_login)


root.mainloop()
