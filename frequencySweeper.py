import winsound
import time

print('''
===========================================================================================================================
___________                                                          _________
\_   _____/______   ____  ________ __   ____   ____   ____ ___.__.  /   _____/_  _  __ ____   ____ ______   ___________
 |    __) \_  __ \_/ __ \/ ____/  |  \_/ __ \ /    \_/ ___<   |  |  \_____  \\\ \/ \/ // __ \_/ __ \\\____ \_/ __ \_  __ \\
 |     \   |  | \/\  ___< <_|  |  |  /\  ___/|   |  \  \___\___  |  /        \\\     /\  ___/\  ___/|  |_> >  ___/|  | \/
 \___  /   |__|    \___  >__   |____/  \___  >___|  /\___  > ____| /_______  / \/\_/  \___  >\___  >   __/ \___  >__|
     \/                \/   |__|           \/     \/     \/\/              \/             \/     \/|__|        \/

---------------------------------------------------------------------------------------------------------------------------
Description: Simple program that sweeps a fixed frequency range from user input.
Keywords: [Frequency Sweeper, Tone Sweeper, Sound Sweeper, Frequency Range]
2016 v2.0
by
NoDisassemble.me
---------------------------------------------------------------------------------------------------------------------------
''')

while True:
    start=40
    answer=input("Start Frequency Sweep? [Yes or No]: ")

    if answer in ["Yes", "yes", "Y", "y"]:
        try:
            increment = int(input("In What Increments? "))
        except ValueError:
            print("")
            print("[!] Invalid Response:")
            input("Press enter to try again:")
            print("")
            continue
        try:
            wait = float(input("Duration in seconds: "))
        except ValueError:
            print("")
            print("[!] Invalid Response:")
            input("Press enter to try again:")
            print("")
            continue
        else:
            print("")
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print('')
            print("[!] Generating Frequency Sweep [!]")
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")
            while start < 32767:
                winsound.Beep(start,1000)
                print("[+}",start, "hz")
                start = start +int(increment)
                time.sleep(wait)
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")
            print("[!] Frequency Sweep Completed: [!]")
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")
            print("")
            input("Press Enter to do another sweep:")
            print("")
            continue
    if answer in ["No", "no", "N", "n"]:
        print("")
        x = "-"
        for i in range(1, 35):
            print(x, end="")
        print("")
        print("[!] Exiting program...")
        x = "-"
        for i in range(1, 35):
            print(x, end="")
        print("")
        quit()
    else:
        print("")
        print("[!] Invalid Response:")
    input("Press enter to try again:")
    print("")
