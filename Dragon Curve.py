import copy, turtle, math, os, time, datetime

"""
color = [
    "DarkRed", "Red", "OrangeRed", "DarkOrange", "Orange", "Gold", "Yellow",
    "GreenYellow", "Green", "Chartreuse", "LimeGreen", "ForestGreen", "Green",
    "SeaGreen", "MediumSeaGreen", "MediumAquamarine", "LightSeaGreen", "Teal",
    "RoyalBlue", "Blue", "Navy", "MidnightBlue", "SlateBlue", "DarkSlateBlue",
    "Indigo", "Purple", "DarkViolet", "BlueViolet", "DarkOrchid",
    "MediumOrchid", "Orchid", "Violet", "Pink", "HotPink", "DeepPink"
         ]
"""
#"DarkGray" and "DarkGrey" Removed
color = ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige",
         "Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown",
         "BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral",
         "CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan",
         "DarkGoldenRod","DarkGreen","DarkKhaki",
         "DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed",
         "DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray",
         "DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue",
         "DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite",
         "ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod",
         "Gray","Grey","Green","GreenYellow","HoneyDew","HotPink","IndianRed",
         "Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen",
         "LemonChiffon","LightBlue","LightCoral","LightCyan",
         "LightGoldenRodYellow","LightGray","LightGrey","LightGreen",
         "LightPink","LightSalmon","LightSeaGreen","LightSkyBlue",
         "LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow",
         "Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine",
         "MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen",
         "MediumSlateBlue","MediumSpringGreen","MediumTurquoise",
         "MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin",
         "NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange",
         "OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise",
         "PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum",
         "PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown",
         "Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver",
         "SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen",
         "SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet",
         "Wheat","White","WhiteSmoke","Yellow","YellowGreen"]

def check(i):
    #Used to check library of finished sequences
    #If sequence doesn't exist, create one by using the sequence before that (Recursively)
    file = "G:/Users/Jozhus/Documents/Python/Dragon/" + str(i) + ".txt"
    #My path for stored sequences
    if not os.path.isfile(file):
        if i == 0:
            return dragon('1', 0)
        index = open(file, 'w')
        index.write(dragon(check(i - 1), 1))
        index.close()
    index = open(file, 'r')
    return index.read()

def dragon(seq, i):
    #Recursively generates a sequence of turns, denoted by right = 1 and left = 0, to create a dragon curve
    if i == 0:
        return seq
    old = copy.deepcopy(seq)
    seq += '0'
    seq = ''.join(['1' if x == '0' else '0' for x in seq])
    seq = seq[::-1]
    return (dragon(old + seq, i - 1))

def draw(seq, length):
    #Interprets a list of '1's and '0's and draws it
    turtle.resizemode("Auto")
    turtle.bgcolor("DarkGray")
    turtle.speed(0)
    turtle.ht()
    time.clock()
    counter, rights, lefts = 0, 0, 0
    for x in seq:        
        turtle.pencolor(color[math.floor(counter / len(seq) * len(color)) % len(color)])
        counter += 1
        os.system('cls')
        print (loadingbar(counter, len(seq), 20), "| Current color: ", turtle.pencolor(), '\n', "Rights: ", rights, '\n', "Lefts:  ", lefts, '\n', "Time:   ", datetime.timedelta(seconds = int(time.clock())))
        if x == '1':
            turtle.right(90) 
            rights += 1
        else:
            turtle.left(90)
            lefts += 1
        turtle.forward(length)
    return turtle.update()

def loadingbar(curr, total, spaces):
    #Creates a fancy little dynamic loading bar
    bar = []
    perc = math.floor(curr / total * spaces)
    for x in range(spaces):
        if x < perc:
            bar.append('#')
        else:
            bar.append('_')
    bar = '[', ''.join(bar), ']', curr, '/', total, '(', int(curr / total * 100), '%)'
    return ' '.join(str(x) for x in bar)

draw(check(int(input("Iterations: "))), int(input("Size: ")))
turtle.mainloop()
