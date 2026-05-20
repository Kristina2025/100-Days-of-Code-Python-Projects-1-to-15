
import time
import sys
print("Welcome to the Kobayashi Maru training exercise, cadet.")
time.sleep(1)
name = input("Please state your name for the record?\n")
print(f"Very well, cadet {name}. The simulation will start shortly.")
print("=============================================================================================================")
time.sleep(3)
print("""                                 _____..---========+*+==========---.._____
    ______________________ __,-='=====____  =================== _____=====`=
   (._____________________I__) - _-=_/    `---------=+=--------'
       /      /__...---===='---+---_'
      '------'---.___ -  _ =   _.-'
                     `--------'""")
print("You're the captain of a the starship galaxy-class USS Challanger. You're on a recon mission near the Romulan "
      "border when you receive a distress call:")
time.sleep(3)
distress_call = "To any ship within range. This is the civilian freighter Kobayashi Maru. We have 381 civilians on " \
                "board.\nWe've struck a gravity mine. We're rapidly losing power and are heading deeper into " \
                "Romulan territory.\nOur hull integrity is failing and we're beginning to lose life support. " \
                "Request immediate assistance! \nI repeat. To any ship within range... "
for char in distress_call.upper():
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
print()
print(f"\nCaptain {name}:")
answer = "Set a course toward the Neutral Zone."
for char in answer:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
print("\nTactical Officer:")
answer = 'Captain, need I remind you that by entering the Neutral Zone we could be risking war with the Romulans. ' \
         'Moreover, the distress call could be a trap set up precisely to provoke such an action. '
for char in answer:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
print()
action = input("\nDECISION 1: Type 'investigate' or 'ignore' to investigate or ignore the distress call.\n")
if action.lower() == 'investigate':
    print(f"Captain {name}:")
    answer = "I'm aware of my responsibilities, Lieutenant. Stop just before the Neutral Zone. We'll try to put a " \
             "tractor beam on them or transport them across the border. "
    for char in answer:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    print()
    print("\nYou arrive before the neutral zone. The Kobayashi Maru is out of transporter range. Sensors indicate no "
          "other vessels in the vicinity.")
    time.sleep(4)
    decision = input("DECISION 2: Type 'enter' to enter the Netural Zone. Type 'stay' to remain where you are.\n")
    if decision.lower() == "enter":
        print("""
           ____.-----.n.----._________.-.______
           ___,----'     \|||||  _______________________`-._
       .--'    n                 \------------------, ` \___`.
  __,-' _____________             \          `-===|  \@\      \\
 /-----'  /        __\______.......|____        ==|   \_) -----\\
|@ .-----|        |         |      |_  /         -\     =======\`
|  `-----|        |_________|......|___\___________\          __\\
 \-----.__\__________/             |_______.--------`._       `. \\
  `-.__                           / _/                 `--.__   \|
       `-._u                    .'-'                         `-. |
            `---.___________.--'                                \|
        """)
        print("As you close-in on the Kobayashi Maru, three Romulan warbirds decloak right in front of you.\n"
              "You're violating their territory and they have every right to shoot you on sight.\n"
              "If that weren't enough, the debris is interfering with your sensors and you still can't determine "
              "whether the Kobayashi Maru is a trap or a real vessel.")
        time.sleep(10)
        print()
        print("Tactical Officer:")
        answer = "Captain, the Romulan ships are powering their weapons. How do we proceed?"
        for char in answer:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(2)
        print()
        decision = input("\nDECISION 3: Type 'hail' to try to hail the enemy ships, 'fight' to fight to save the "
                         "Kobayashi Maru or 'retreat' to tuck your tail between your legs and run back to safety.\n")
        if decision.lower() == "hail":
            print(f"Captain {name}:")
            answer = "Comms, relay this message on all frequencies:\n 'This is the Captain of the Federation Starship " \
                     "Challanger. I hereby challenge the leader of the Romulan vessel to a duel, as per the right " \
                     "accorded to me by ancient Romulan tradition.'\n"
            for char in answer:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(3)
            print()
            print("OUTCOME:")
            time.sleep(3)
            print("End of simulation. Congratulations! The Romulans accepted your challenge.\nAll hostilities must stop during the "
                  "challenge. The Romulans have no other choice but to watch as your vessel leads the Kobayashi Maru "
                  "back to safety.\nYour quick thinking and self-sacrifice have impressed the instructors.\nYou'll go "
                  "down in history as the first person to pass the Kobayashi Maru without cheating.")
        elif decision == "fight":
            print(f"Captain {name}:")
            answer = "Red alert. Shields up. Fire photon torpedoes.\n"
            for char in answer:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(3)
            print()
            print("OUTCOME:")
            time.sleep(3)
            print("End of simulation. Congratulations! Thanks to your genius tactical maneuvers, you managed to lead the Kobayashi Maru "
                "back to safety, but lost half of your crew in the process. In the end, all you did was trade one life for another. "
                "\nOn the bright side, you impressed the instructors with your tactical ingenuity. "
                "You might not be the best captain, but you'll make a hell of a tactical officer some day.")
        elif decision == "retreat":
            print(f"Captain {name}:")
            answer = "Get us out of here! Warp 8.\n"
            for char in answer:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(3)
            print()
            print("OUTCOME:")
            time.sleep(3)
            print("End of simulation. Congratulations! You gave it your best shot and failed miserably!\nYou'll "
                  "have a lot of explaining to do as to what you were doing behind enemy lines, and nothing to show "
                  "for it, since the Kobayashi Maru was destroyed while you were busy saving your own "
                  "skin. But hey, at least you tried.")
        else:
            print("Get ahold of yourself, cadet. That's not a valid move. End of simulation.")
    elif decision == 'stay':
        print("OUTCOME:")
        time.sleep(3)
        print("\nEnd of simulation. Congratulations! You've managed to avoid interstellar war and showed the instructors that you have "
              "what it takes to make the hard choices in life.\nNow sit back and watch as everyone on board "
              "the civilian ship suffers a horrible death at the hands of the Romulans, you cold-hearted monster.")
    else:
        print("Get ahold of yourself, cadet. That's not a valid move. End of simulation.")
elif action == 'ignore':
    print("OUTCOME:")
    time.sleep(3)
    print("\nEnd of simulation. Congratulations, thanks to your cowardice and refusal to investigate the distress call, "
          "you've lost all faith your crew had in you.\nYou've failed the test spectacularly and proven yourself as "
          "totally unfit to be a Starfleet officer.")
else:
    print("Get ahold of yourself, cadet. That's not a valid move. End of simulation.")
