import winsound

print('''
================================================================================================
___________                      ________                                   __
\__    ___/___   ____   ____    /  _____/  ____   ____   ________________ _/  |_  ___________
  |    | /  _ \ /    \_/ __ \  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\\   __\/  _ \_  __ \\
  |    |(  <_> )   |  \  ___/  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
  |____| \____/|___|  /\___  >  \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|
                    \/     \/          \/     \/     \/     \/           \/

-------------------------------------------------------------------------------------------------
Description: Simple program that generates a tone from user input using the winsound.Beep module.
Keywords: [Python 3, Tone Generator, Note Generator, Beep Generator, winsound.Beep]
2016 v2.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------
''')

while True:
    try:
        hertz=int(input("Choose a frequency in hz: 37 - 32767: "))
        if hertz < 37:
            print("")
            print("[!] Invalid entry [!]")
            print("[!] Frequency must be 37 hz or higher [!]")
            print("")
            input("Press Enter to try again")
            print("")
            continue
        if hertz > 32767:
            print("")
            print("[!] Invalid entry [!]")
            print("[!] Frequency cannot exceed 32767 [!]")
            print("")
            input("Press Enter to try again")
            print("")
            continue
        else:
            pass
    except ValueError:
        print("")
        print("Invalid entry:")
        input("Press [Enter] to try again:")
        print("")
    else:
        try:
            duration=int(input("How many Seconds to play? "))
            print("")
        except ValueError:
            print("")
            print("Invalid entry:")
            input("Press [Enter] to try again:")
            print("")
        else:
            x = "-"
            for i in range(1, 41):
                print(x, end="")
            print("")
            print("[!] Generating", hertz,"hz for", duration, "Seconds [!]")
            x = "-"
            for i in range(1, 41):
                print(x, end="")
            print("")
            print("[+] ", hertz, "hz [+]")
            winsound.Beep(int(hertz),int(duration*1000))
            print("")
            print("[+] Tone Complete:")
            print("")
            input("Press [Enter] to generate another tone:")
            print("")
