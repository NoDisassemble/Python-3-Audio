print('''
=====================================================================================================================================================
__________                        ___.         /\ ________         .__                 ___________.__                 _________        .__
\______   \ _______  __ __________\_ |__      / / \______ \   ____ |  | _____  ___.__. \__    ___/|__| _____   ____   \_   ___ \_____  |  |   ____
 |       _// __ \  \/ // __ \_  __ \ __ \    / /   |    |  \_/ __ \|  | \__  \<   |  |   |    |   |  |/     \_/ __ \  /    \  \/\__  \ |  | _/ ___\\
 |    |   \  ___/\   /\  ___/|  | \/ \_\ \  / /    |    `   \  ___/|  |__/ __ \\\___  |   |    |   |  |  Y Y  \  ___/  \     \____/ __ \|  |_\  \___
 |____|_  /\___  >\_/  \___  >__|  |___  / / /    /_______  /\___  >____(____  / ____|   |____|   |__|__|_|  /\___  >  \______  (____  /____/\___  >
        \/     \/          \/          \/  \/             \/     \/          \/\/                          \/     \/          \/     \/          \/
=====================================================================================================================================================

Description: Calculates Reverb and Delay times in Milliseconds based on BPM input.
Keywords: [Python 3, Delay times, Reverb times, BPM to Milliseconds]
Jan 2017 v1.0
by
NoDisassemble.me
-----------------------------------------------------------------------------------------------------------------------------------------------------
''')

while True:
    try:
        # user input for BPM
        BPM = float(input("Enter BPM: "))
    # catches invalid entry (anything that's not a number)
    except ValueError:
        print("")
        print("[!] Invalid entry. [!]")
        input("    Press Enter to try again:")
        print("")
        continue
    print("")
    # <---------------------Standard Divisions------------------------>
    # calc for quarter note
    quarterNote = 60000 // float(BPM)
    # calc for whole note
    wholeNote = quarterNote * 4
    # calc for half note
    halfNote = quarterNote * 2
    # calc for eighth note
    eighthNote = quarterNote * 0.5
    # calc for sixteenth note
    sixteenthNote = quarterNote * 0.25
    # calc for thirty second note
    thirtySecondNote = quarterNote * 0.125
    # calc for sixty fourth note
    sixtyFourthNote = quarterNote * 0.0625
    # <----------------------Dotted Divisions------------------------>
    # calc for dotted whole note
    dotWholeNote = quarterNote * 6
    # calc for dotted half note
    dotHalfNote = quarterNote * 3
    # calc for dotted quarter note
    dotQuarterNote = quarterNote * 1.5
    # calc for dotted eighth note
    dotEighthNote = quarterNote * 0.75
    # calc for dotted sixteenth note
    dotSixteenthNote = quarterNote * 0.375
    # calc for dotted thirty second note
    dotThirtySecondNote = quarterNote * 0.1875
    # calc for dotted sixty fourth note
    dotSixtyFourthNote = quarterNote * 0.09375
    # <---------------------Triplet Divisions------------------------>
    # calc for whole note triplet
    wholeNoteTriplet = quarterNote * 2.666
    # calc for half note triplet
    halfNoteTriplet = quarterNote * 1.333
    # calc for quarter note triplet
    quarterNoteTriplet = quarterNote * 0.666
    # calc for eighth note triplet
    eighthNoteTriplet = quarterNote * 0.333
    # calc for sixteenth note triplet
    sixteenthNoteTriplet = quarterNote * 0.1665
    # calc for thirty second note triplet
    thirtysecondNoteTriplet = quarterNote * 0.08325
    # calc for sixty fourth note triplet
    sixtyFourthNoteTriplet = quarterNote * 0.041625

    # display calculations for standard divisions
    print('''[+] BPM of %0.1f Standard [+]
    [%0.1f ms] Whole Note
    [%0.1f ms] Half Note
    [%0.1f ms] Quarter Note
    [%0.1f ms] Eighth Note
    [%0.1f ms] Sixteenth Note
    [%0.1f ms] Thirty second Note
    [%0.1f ms] Sixty fourth Note
    ''' % (float(BPM), float(wholeNote), float(halfNote), float(quarterNote), float(eighthNote), float(sixteenthNote),
           float(thirtySecondNote), float(sixtyFourthNote)))

    # display calculations for dotted divisions
    print('''[+] BPM of %0.1f Dotted [+]
    [%0.1f ms] Dotted Whole Note
    [%0.1f ms] Dotted Half Note
    [%0.1f ms] Dotted Quarter Note
    [%0.1f ms] Dotted Eighth Note
    [%0.1f ms] Dotted Sixteenth Note
    [%0.1f ms] Dotted Thirty second Note
    [%0.1f ms] Dotted Sixty fourth Note
    ''' % (float(BPM), float(dotWholeNote), float(dotHalfNote), float(dotQuarterNote), float(dotEighthNote),
           float(dotSixteenthNote), float(dotThirtySecondNote), float(dotSixtyFourthNote)))

    # display calculations for triplet divisions
    print('''[+] BPM of %0.1f Triplet [+]
    [%0.1f ms] Whole Note Triplet
    [%0.1f ms] Half Note Triplet
    [%0.1f ms] Quarter Note Triplet
    [%0.1f ms] Eighth Note Triplet
    [%0.1f ms] Sixteenth Note Triplet
    [%0.1f ms] Thirty second Note Triplet
    [%0.1f ms] Sixty fourth Note Triplet
    ''' % (float(BPM), float(wholeNoteTriplet), float(halfNoteTriplet), float(quarterNoteTriplet),
           float(eighthNoteTriplet), float(sixteenthNoteTriplet), float(thirtysecondNoteTriplet),
           float(sixtyFourthNoteTriplet)))

    input("Press Enter to convert another BPM.")
    print("")
