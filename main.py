import pandas

# ---------------------------- CONSTANTS ------------------------------- #
greenLight = "#96bb7c"
lightOrange = "#ecb390"
orange = "#df7861"
beigeLight = "#fcf8e8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checksText = ""
timer = None

pythonTime = 0
algorithmsTime = 0
gitTime = 0
invertedTime = {"Activity": ["Python", "Algorithm", "Git"], "Time": [pythonTime,algorithmsTime,algorithmsTime,]}

# ---------------------------- INFO - TIME ------------------------------- # 
def selection_work():
    global pythonTime, algorithmsTime, gitTime
    if (varOption.get()) != "":
        index = invertedTime["Activity"].index(varOption.get())
        invertedTime["Time"][index] += 30
    
def convertionCSV(dictionary):
    dataFrameTime = pandas.DataFrame(dictionary)
    dataFrameTime.to_csv
    



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checksText
    global reps

    window.after_cancel(timer)
    titleLabel.config(text = "WORK", fg = orange)
    canva.itemconfig(minutes, text = "00:00")
    checksText == ""
    reps = 1
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work)
        titleLabel.config(text = "WORK", fg = orange)
    elif reps % 8 == 0:
        count_down(long_break)
        titleLabel.config(text = "LONG BREAK", fg = lightOrange)
    elif reps % 2 == 0:
        count_down(short_break)
        titleLabel.config(text = "BREAK", fg = greenLight)

    reps += 1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checksText
    global timer

    count_minutes = count // 60
    count_seconds = count % 60
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canva.itemconfig(minutes, text = f"{count_minutes}:{count_seconds}")
    if count>0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checksText += "✔"
            checkLabel.config(text = checksText)
            selection_work()
            
# ---------------------------- UI SETUP ------------------------------- #
'''Foreground = font color in Label'''
import tkinter as tk

window = tk.Tk()
window.title("Pomodoro")
window.config(padx = 100, pady= 50, bg = beigeLight)

tomatoDirection = r"C:\Users\cesar\OneDrive\programacion\python\Pythonparteteorica\librerias\tkinter\pomodoro\pomodoro-start\tomato.png"
tomatoImage = tk.PhotoImage(file = tomatoDirection)
titleLabel = tk.Label(text = "Timer", bg = beigeLight, font = (FONT_NAME, 35, "bold"), foreground = orange)
titleLabel.grid(column = 1, row = 0)

canva = tk.Canvas(width = 200, height = 224, bg = beigeLight, highlightthickness = 0)
canva.create_image(99,112, image = tomatoImage)
minutes = canva.create_text(107, 130,text = "00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canva.grid(column = 1, row = 1)

buttonStart = tk.Button(command = start_timer,text = "START" , bg = orange, foreground = "white", bd = 0, font = (FONT_NAME, 10, "bold"))
buttonStart.config(padx = 10, pady = 10)
buttonStart.grid(column = 0, row = 2)

buttonReset = tk.Button(command = reset_timer, text = "Reset" , bg = orange, foreground = "white", bd = 0, font = (FONT_NAME, 10, "bold"))
buttonReset.config(padx = 10, pady = 10)
buttonReset.grid(column = 2, row = 2)

checkLabel = tk.Label(text = checksText, bg = beigeLight, font = (FONT_NAME, 20, "bold"), foreground = greenLight)
checkLabel.grid(column = 1, row = 3)


varOption = tk.StringVar()


option1 = tk.Radiobutton(window, text='Python',variable=varOption, value = "Python",bg = beigeLight)
option1.grid(column = 0, row = 3)
option2 = tk.Radiobutton(window, text='Alghorithms',variable=varOption, value = "Algorithm", bg = beigeLight)
option2.grid(column = 1, row = 3)
option3 = tk.Radiobutton(window, text='GIT-PROJECTS',variable=varOption, value = "Git", bg = beigeLight)
option3.grid(column = 2, row = 3)
 
window.mainloop()
