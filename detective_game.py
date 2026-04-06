import random
suspects=["Ethan", "Chenxuan", "Raymond"]
killer=random.choice(suspects)
investigations_left=4
clues_collected=[]
clues = [f"{killer} was seen near the crime scene", f"The weapon belongs to {killer}", f"{random.choice([s for s in suspects if s != killer])} has a confirmed alibi", f"{random.choice([s for s in suspects if s != killer])} was out of town"]
while True:
  print("\nWhat would you like to do?")
  print("1. Talk to suspect")
  print("2. Investigate")
  print("3. View clues")
  print("4. Accuse")
  choice=input("Enter the number of what you would like to do: ")

  if choice=="1":
    print("\nSuspects:")
    for i in suspects:
      print(" -",i)
    suspect_choice=input("\nWho would you like to talk to?: ").title()
    if suspect_choice in suspects:
        if suspect_choice!=killer:
         print("I have an alibi. Someone can verify it.\n")
        else:
          print("Uh...I was at home... I think.\n")  
    else:
        print("Invalid name!")
        continue
    
  elif choice=="2":
        if investigations_left <= 0:
            print("You have no investigations left!")
        elif len(clues) == 0:
            print("No more clues to find.")
        else:
            clue = random.choice(clues)
            print("\nYou found a clue:")
            print("-", clue)

            clues_collected.append(clue)
            clues.remove(clue)
            investigations_left -= 1

            print(f"Investigations left: {investigations_left}")
            if investigations_left==1:
               print("You feel like time is running out.")

  elif choice=="3":
    if not clues_collected:
      print("No clues yet.")
    else:
      print("\nCollected Clues:")
      for c in clues_collected:
        print(" -", c)

  elif choice=="4":  
    accused_suspect=input("\nWho is the killer?: ").title()
    if accused_suspect in suspects:
      if accused_suspect==killer:
       print("\nYou have successfully solved the case!")
       break
      else:
        print("\nYou failed to solve the case!")
        print(f"The killer was actually {killer}")
        break
    else:
      print("Invalid name!")
      continue
