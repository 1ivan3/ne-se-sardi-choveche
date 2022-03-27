from glob import glob
from os import times_result
import time
import random
from re import X
import turtle, time
pionka_1 = -600
bot = -600
zar = 0
HOD_NA_PROTIVNIKA = 1
HOD_NA_PIONKATA = 2
HVURLQNE_NA_ZAR = 3
PROVERKA_POZICIYA = 4
kray_na_igrata = False
sledvashta_stupka = HVURLQNE_NA_ZAR
# Create screen
sc = turtle.Screen()
sc.title("nssch")
sc.bgcolor("#D63230")
sc.setup(width=1366, height=600)

text = turtle.Turtle()
text.speed(0)
text.color("#D8973C")
text.shapesize(stretch_wid=1, stretch_len=1)
text.penup()
text.goto(0, 100)
text.hideturtle()
text.write("Здрасти!",
             align="center", font=("Courier", 24, "bold"))


text.goto(0, -100)
text.write("Натисни space, за да хвърлиш заровете",
             align="center", font=("Courier", 24, "bold"))

kvadrtche1 = turtle.Turtle()
kvadrtche1.speed(0)
kvadrtche1.shape("square")
kvadrtche1.color("#700353")
kvadrtche1.shapesize(stretch_wid=2, stretch_len=2)
kvadrtche1.penup()
kvadrtche1.goto(-550, 0)


pionka_1 = turtle.Turtle()
pionka_1.speed(0)
pionka_1.shape("circle")
pionka_1.color("green")
pionka_1.shapesize(stretch_wid=2, stretch_len=2)
pionka_1.penup()
pionka_1.poziciya = 0
pionka_1.goto(-600 + pionka_1.poziciya * 50, 0)




bot = turtle.Turtle()
bot.speed(0)
bot.shape("circle")
bot.color("red")
bot.shapesize(stretch_wid=2, stretch_len=2)
bot.penup()
bot.poziciya = 0
bot.goto(-600 + bot.poziciya * 50, 0)




x = -600
daljina_pole = 1
while x < 500:
        
        x = x + 50
        daljina_pole = daljina_pole + 1
        kvadrtche1.stamp()
        kvadrtche1.goto(x, 0)
        

           

def movesquare1(x, y):
    kvadrtche1.goto(x, y)


def hvarli_zar():
    global sledvashta_stupka
    if sledvashta_stupka != HVURLQNE_NA_ZAR:
        return

    #polezna rabota
    print("space key callback")
    global zar
    zar = random.randint(1, 6)
    sledvashta_stupka = PROVERKA_POZICIYA

    text.clear()
    text.write("падна ти се зар " + str(zar),
                    align="center", font=("Courier", 24, "bold"))
    time.sleep(1)
    if pionka_1.poziciya == 0:
        if zar == 6:
            text.clear()
            text.write("влизаш в полето.", 
                        align="center", font=("Courier", 24, "bold"))
            time.sleep(1)
            sledvashta_stupka = HOD_NA_PIONKATA
        else:
            text.clear()
            text.write("опитай другия път.", 
                        align="center", font=("Courier", 24, "bold"))
            time.sleep(2)
            sledvashta_stupka = HOD_NA_PROTIVNIKA
    else:
        text.clear()
        text.write("Натисни наляво или надясно за да се преместиш",
                        align="center", font=("Courier", 24, "bold"))
        sledvashta_stupka = HOD_NA_PIONKATA
    

    

def proverka_vtoro_hvurlqne():
    global sledvashta_stupka
    global zar
    if zar == 6:
        text.clear()
        text.write("Падна ти се зар 6!Имаш право на второ хвърляне!Натисни space за хвърляне.", 
                     align="center", font=("Courier", 24, "bold"))
        
        sledvashta_stupka = HVURLQNE_NA_ZAR
    else:
        sledvashta_stupka = HOD_NA_PROTIVNIKA


def hod_nazad():
    global sledvashta_stupka
    if sledvashta_stupka != HOD_NA_PIONKATA:
        return
    
    # polezna rabota 
    global zar
    if pionka_1.poziciya + zar <= daljina_pole:
        pionka_1.poziciya = pionka_1.poziciya - zar
        pionka_1.goto(-600 + pionka_1.poziciya * 50, 0)


    if pionka_1.poziciya == bot.poziciya:
        bot.poziciya = 0
        bot.goto(-600, 0)

    proverka_vtoro_hvurlqne()


def hod_napred():
    global sledvashta_stupka
    if sledvashta_stupka != HOD_NA_PIONKATA:
        return
    
    # polezna rabota 
    global zar
    if pionka_1.poziciya + zar <= daljina_pole:
        pionka_1.poziciya = pionka_1.poziciya + zar
        pionka_1.goto(-600 + pionka_1.poziciya * 50, 0)


    if pionka_1.poziciya == bot.poziciya:
        bot.poziciya = 0
        bot.goto(-600, 0)
    proverka_vtoro_hvurlqne()
    


def hod_na_bota():
    global zar
    global sledvashta_stupka
    
    if sledvashta_stupka != HOD_NA_PROTIVNIKA:
        return


    # polezna rabota
    zar = random.randint(1, 6)
    if bot.poziciya == 0:
        if zar == 6:
            time.sleep(1)
            sledvashta_stupka = HOD_NA_PROTIVNIKA
        else:
            time.sleep(1)
            sledvashta_stupka = HOD_NA_PIONKATA
    else:
        sledvashta_stupka = HOD_NA_PROTIVNIKA
    text.clear()
    text.write("противника ходи със зар " + str(zar), 
    align="center", font=("Courier", 24, "bold"))

    time.sleep(1)
    if bot.poziciya + zar <= daljina_pole:
        bot.poziciya = bot.poziciya + zar
        bot.goto(-600 + bot.poziciya * 50, 0)

    if zar == 6:
        sledvashta_stupka = HOD_NA_PROTIVNIKA
    else:
        sledvashta_stupka = HVURLQNE_NA_ZAR

    if bot.poziciya == pionka_1.poziciya:
        pionka_1.poziciya = 0
        pionka_1.goto(-600, 0)

    text.clear()
    text.write("ти си на ход.", 
    align="center", font=("Courier", 24, "bold"))


kvadrtche1.ondrag(movesquare1)


sc.listen()
sc.onkeypress(hvarli_zar, "space")
sc.onkeypress(hod_nazad, "Left")
sc.onkeypress(hod_napred, "Right")

while True:
    if sledvashta_stupka == HOD_NA_PROTIVNIKA: 
        hod_na_bota()

    sc.update()

    # TODO check kray na igrata 
    if bot.poziciya == daljina_pole:
        kray_na_igrata = True

    if pionka_1.poziciya == daljina_pole:
        kray_na_igrata = True

    if kray_na_igrata == True:
        print("kray na igrata")
        text.clear()
        text.goto(0, 100)
        text.write("Край на играта!",
                    align="center", font=("Courier", 24, "bold"))

        time.sleep(2)
        break
