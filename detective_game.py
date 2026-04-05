import random
suspects=["Ethan", "Chenxuan", "Raymond"]
clues=[]
killer=random.choice(suspects)
while True:
  print("\nWhat would you like to do?")
  print("1. Talk to suspect")
  print("2. Investigate (Still in development)")
  print("3. View clues")
  print("4. Accuse")
  choice=input("Enter the number of what you would like to do: ")
  if choice=="1":
    print("\nSuspects:")
    for i in suspects:
      print("-",i)
    suspect_choice=input("Who would you like to talk to?: ").title()
    if suspect_choice in suspects:
        if suspect_choice!=killer:
         print("I was at school. You can call my teacher to check")
         print("They seem confident and calm")
        else:
          print("Uh...I was at home...I...I think")  
          print("Hmm... They seem nervous")
    else:
        print("Invalid name!")
        continue
  elif choice=="2":
    pass
  elif choice=="3":
    print(f"Clues: {clues}")
  elif choice=="4":  
    accused_suspect=input("\nWho is the killer?: ").title()
    if accused_suspect in suspects:
      if accused_suspect==killer:
       print("You have successfully solved the case!")
       break
      else:
        print("You failed to solve the case!")
        print(f"The killer was actually {killer}")
        break
    else:
      print("Invalid name!")
      continue
