from math import sin, cos, radians
import tkinter as tk
import random


# 1)
canvas = tk.Canvas()
canvas.pack()
x, y = 50, 50 # alebo 120, 10
canvas.create_rectangle(x, y, x+100, y+100, fill='red')
canvas.create_rectangle(x+110, y, x+210, y+100, fill='blue')
canvas.create_text(x+50, y+50, text='červený', font='arial 20', fill='yellow')
canvas.create_text(x+160, y+50, text='modrý', font='arial 20', fill='yellow')

# 2)
canvas = tk.Canvas(bg='navy')
canvas.pack()
n = 200
for i in range(n):
    canvas.create_text(random.randint(5, 370), random.randint(5, 260), text='*', font=f'arial {random.randint(10, 20)}', fill='yellow')

# 3)
canvas = tk.Canvas()
canvas.pack()
x, y = 50, 50     # alebo 140, 20
a1, a2 = 180, 100 # alebo 200, 190
canvas.create_rectangle(x, y, x+a1, y+a1, fill='indian red')
canvas.create_rectangle(x+(a1-a2)/2, y+(a1-a2)/2, x+(a1-a2)/2+a2, y+(a1-a2)/2+a2, fill='light blue')
canvas.create_text(x-10, y-10, text='A')
canvas.create_text(x+a1+10, y-10, text='B')
canvas.create_text(x-10, y+a1+10, text='C')
canvas.create_text(x+a1+10, y+a1+10, text='D')
canvas.create_text(x+a1+10, y+a1/2, text=a1)
canvas.create_text(x+a1/2, y+a1/2+a2/2-10, text=a2)

# 4)
canvas = tk.Canvas()
canvas.pack()
x, y = 150, 150
n = 20
f1, f2, f3 = 'red', 'blue', 'yellow'
for i in range(n*5, 0, -5):
    canvas.create_rectangle(x-i, y-i, x+i, y+i, fill=f1)
    f1, f2, f3 = f2, f3, f1

# 5)
canvas = tk.Canvas()
canvas.pack()
x, y = 20, 20
canvas.create_rectangle(x, y, x+135, y+90, fill='yellow', width=0)
canvas.create_rectangle(x, y, x+135, y+90*2/3, fill='red', width=0)
canvas.create_rectangle(x, y, x+135, y+90/3, fill='black', width=0)
canvas.create_rectangle(x, y, x+135, y+90)
x, y = 200, 20
canvas.create_rectangle(x, y, x+135, y+90, fill='red', width=0)
canvas.create_rectangle(x, y, x+135*2/3, y+90, fill='white', width=0)
canvas.create_rectangle(x, y, x+135/3, y+90, fill='green', width=0)
canvas.create_rectangle(x, y, x+135, y+90)
x, y = 20, 150
canvas.create_rectangle(x, y, x+135, y+90, fill='red', width=0)
canvas.create_rectangle(x, y, x+135*2/3, y+90, fill='white', width=0)
canvas.create_rectangle(x, y, x+135/3, y+90, fill='blue', width=0)
canvas.create_rectangle(x, y, x+135, y+90)
x, y = 200, 150
canvas.create_rectangle(x, y, x+135, y+90, fill='red', width=0)
canvas.create_rectangle(x, y, x+135, y+90*2/3, fill='blue', width=0)
canvas.create_rectangle(x, y, x+135, y+90/3, fill='white', width=0)
canvas.create_rectangle(x, y, x+135, y+90)

# 6)
canvas = tk.Canvas()
canvas.pack()
x, y = 180, 250
sirka = 100
for farba in 'darkgreen', 'green', 'yellowgreen', 'limegreen':
    canvas.create_rectangle(x-sirka, y, x+sirka, y-50, fill=farba)
    sirka -= 25
    y -= 50

# 7)
canvas = tk.Canvas()
canvas.pack()
x, y = 10, 100 # bod zaciatku ciary
n, d = 16, 20
for i in range(n):
    canvas.create_line(x, y, x+abs(d), y+d, width=5, fill='blue')
    x += abs(d)
    y += d
    d = -d

# 8)
canvas = tk.Canvas()
canvas.pack()
x, y = 70, 100 # stred prveho kruhu
r = 50
dx, dy = 120, 60
for farba in 'blue', 'yellow', 'black', 'limegreen', 'red':
    canvas.create_oval(x-r, y-r, x+r, y+r, width=15, outline=farba)
    x += dx/2
    y += dy
    dy = -dy

# 9)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
suma = 0
x, y = 150, 50
for i in range(n):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    canvas.create_rectangle(x, y, x+50, y+20, fill='white')
    canvas.create_text(x+25, y+10, text=f'{hodnota:2} €', font='arial 10')
    suma += hodnota
    y += 20
canvas.create_text(275, 100, text=f'spolu = {suma} €', font='arial 10 bold')

# 10)
canvas = tk.Canvas()
canvas.pack()
r, n = 20, 30
for i in range(n):
    x, y = random.randint(20, 360), random.randint(20, 240)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=f'#{random.randrange(256**3):06x}')
    canvas.create_text(x, y, text=random.randint(1, 9), font='arial 30')

# 11)
canvas = tk.Canvas()
canvas.pack()
txt = input('zadaj text: ')
x, y = 10, 10
for pismeno in txt:
    canvas.create_rectangle(x, y, x+30, y+30, fill=f'#{random.randrange(256**3):06x}')
    canvas.create_text(x+15, y+15, text=pismeno, font='arial 26', fill=f'#{random.randrange(256**3):06x}')
    x += 30

# 12)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
x, y = 5, 5
sirka = 370//n - 5
for i in range(n):
    canvas.create_rectangle(x, y, x+sirka, y+sirka, fill=f'#{random.randrange(256**3):06x}')
    x += sirka+5

# 13)
canvas = tk.Canvas()
canvas.pack()
x, y = 50, 250
a = 280
canvas.create_polygon(x, y, x+a, y, x+a/2, y-3**(1/2)*a/2, fill='blue')

# 14)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
for i in range(n):
    x, y = random.randint(10, 330), random.randint(50, 210)
    a = random.randint(10, 50)
    canvas.create_polygon(x, y, x+a, y, x+a/2, y-3**(1/2)*a/2, fill=f'#{random.randrange(256**3):06x}')
    canvas.create_rectangle(x, y, x+a, y+a, fill=f'#{random.randrange(256**3):06x}', width=0)

# 15)
canvas = tk.Canvas()
canvas.pack()
sirka, vyska = 300, 200
x, y = 25, 25
canvas.create_rectangle(x, y, x+sirka, y+vyska/2, fill='white', width=0)
canvas.create_rectangle(x, y+vyska/2, x+sirka, y+vyska, fill='red', width=0)
canvas.create_polygon(x, y, x, y+vyska, x+sirka/2, y+vyska/2, fill='navy')
canvas.create_rectangle(x, y, x+sirka, y+vyska)

# 16)
canvas = tk.Canvas()
canvas.pack()
riadky = int(input('zadaj počet riadkov: '))
stlpce = int(input('zadaj počet stĺpcov: '))
vel = 30
farba1, farba2 = 'maroon', 'gold'
x, y = 10, 10
for riadok in range(riadky):
    f1, f2 = farba1, farba2
    for stlpec in range(stlpce):
        canvas.create_rectangle(x, y, x+vel, y+vel, fill=f1)
        f1, f2 = f2, f1
        x += vel+3
    farba1, farba2 = farba2, farba1
    x = 10
    y += vel+3

# 17)
canvas = tk.Canvas(height=250, width=375)
canvas.pack()
x = 0
for i in range(25):
    r = 250 - i * 10
    b = 250 - r
    canvas.create_rectangle(x, 0, x+15, 250, fill=f'#{r:02x}00{b:02x}', width=0)
    x += 15

# 18)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
a = float(input('zadaj dĺžku strany: '))
x, y = 180, 130
r = a / sin(radians(180/n)) / 2
x1, y1 = x+r, y
for i in range(1, n+1):
    x2 = x + r * cos(radians(i*360/n))
    y2 = y + r * sin(radians(i*360/n))
    canvas.create_line(x1, y1, x2, y2, width=3)
    x1, y1 = x2, y2

# 19)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
x, y, r = 180, 130, 125
uhol = 360 / n
for i in range(n):
    for j in range(i+1, n):
        x1 = x + r * cos(radians(uhol*i))
        y1 = y + r * sin(radians(uhol*i))
        x2 = x + r * cos(radians(uhol*j))
        y2 = y + r * sin(radians(uhol*j))
        canvas.create_line(x1, y1, x2, y2)

# 20)
canvas = tk.Canvas()
canvas.pack()
n = int(input('zadaj n: '))
x0, y0, r0 = 180, 130, 80
uhol = 360 / n
r = r0 * sin(radians(uhol/2))
for i in range(n):
    x = x0 + r0 * cos(radians(uhol*i))
    y = y0 + r0 * sin(radians(uhol*i))
    farba = f'#{random.randrange(256**3):06x}'
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

# 21)
canvas = tk.Canvas()
canvas.pack()
x, y = 30, 30
sir, vys = 325, 216
obrazok = tk.PhotoImage(file='sk.png')
canvas.create_rectangle(x, y, x+sir, y+vys, fill='#ee1c25', width=0)
canvas.create_rectangle(x, y, x+sir, y+vys*2/3, fill='#0b4ea2', width=0)
canvas.create_rectangle(x, y, x+sir, y+vys/3, fill='white', width=0)
canvas.create_rectangle(x, y, x+sir, y+vys)
canvas.create_image(x+100, y+vys/2, image=obrazok)

tk.mainloop()