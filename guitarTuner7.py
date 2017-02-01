import winsound

print('''
===========================================================================================
  ________      .__  __                 ___________                          _________
 /  _____/ __ __|__|/  |______ _______  \__    ___/_ __  ____   ___________  \______  \\
/   \  ___|  |  \  \   __\__  \\\_  __ \   |    | |  |  \/    \_/ __ \_  __ \     /    /
\    \_\  \  |  /  ||  |  / __ \|  | \/   |    | |  |  /   |  \  ___/|  | \/    /    /
 \______  /____/|__||__| (____  /__|      |____| |____/|___|  /\___  >__|      /____/
        \/                    \/                            \/     \/
===========================================================================================

Description: A simple Python 3 text based 7 string guitar tuner using winsound. PC only =(
Keywords: [Python 3, Simple Guitar Tuner]
Jan 2017 v1.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------''')


# play low B string
def lowBstring():
    print("[!] Playing Low B String [!]")
    winsound.Beep(248, 5000)


# play low E string
def lowEstring():
    print("[!] Playing Low E String [!]")
    winsound.Beep(328, 5000)


# play A string
def Astring():
    print("[!] Playing A String [!]")
    winsound.Beep(440, 5000)


# play D string
def Dstring():
    print("[!] Playing D String [!]")
    winsound.Beep(588, 5000)


# play G string
def Gstring():
    print("[!] Playing G String [!]")
    winsound.Beep(784, 5000)


# play B string
def Bstring():
    print("[!] Playing B String [!]")
    winsound.Beep(988, 5000)


# play high E string
def highEstring():
    print("[!] Playing High E String [!]")
    winsound.Beep(1320, 5000)


# cath all for invalid entry
def invalOpt():
    print("[!] Invalid Choice [!]")
    input("Press Enter to try again")
    print("")

# Begin program actual
while True:
    # display strings
    print('''
    e|:------------
    b|:------------
    g|:------------
    d|:------------
    a|:------------
    E|:------------
    B|:------------
    ''')
    # user input for string to play
    string = input("Choose String: ")
    print("")
    # if low B string is chosen
    if string == "B":
        lowBstring()
        continue
    # if low E string is chosen
    if string == "E":
        lowEstring()
        continue
    # if A string is chosen
    if string == "a":
        Astring()
        continue
    # if D string is chosen
    if string == "d":
        Dstring()
        continue
    # if G string is chosen
    if string == "g":
        Gstring()
        continue
    # if B string is chosen
    if string == "b":
        Bstring()
        continue
    # if high E string is chosen
    if string == "e":
        highEstring()
        continue
    # catch all for invalid entrys
    else:
        invalOpt()
        continue
