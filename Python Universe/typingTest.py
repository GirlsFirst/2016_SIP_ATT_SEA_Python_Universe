############################################################################
 #                             //KEYSTROKE//                               #
 #                         //By Arvindcheenu.//                            #
 #                    //2014-15.All rights reserved.//                     #
############################################################################
import sys,time,random
#Human Typing Simulator:
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
#Letter Counter:
def count_letters(word):
    space = " "
    return len([letter for letter in word if letter not in space])
# Conversation Dictionary
convo ={"Type this sentence to fight back":"Type this sentence to fight back",
               "Great, now keep typing":"Great, now keep typing",
               "Type faster to deactivate the bomb":"Type faster to deactivate the bomb",
               "The city is being evacuated now":"The city is being evacuated now",
               "Every keystroke is saving lives":"Every keystroke is saving lives",
               "Oh we have zome kommunication ichues":"Oh we have zome kommunication ichues",
               "Someteng is wronng with the segneal":"Someteng is wronng with the segneal",
               "Can yu styll haer ush?":"Can yu styll haer ush?",
               "Ze boemb iz cosing interrrfearreeences":"Ze boemb iz cosing interrrfearreeences",
               "I thank msoe hackres aer dinog tihs!":"I thank msoe hackres aer dinog tihs",
               "Cam yu ear mey cleerley?! Whet?":"Cam yu ear mey cleerley?! Whet?",
               "Amaznigly skidlled figners!! I sey!":"Amaznigly skidlled figners!! I sey!",
               "What on erth iz habbenning?!":"What on erth iz habbenning?!",
               "The Gevornmant planz to meind-conterol people!!":"The Gevornmant planz to meind-conterol people!!",
               "The Illerminati is Everywhere!! Look back!!":"The Illerminati is Everywhere!! Look back!!",
               "Routing encrypted data from defense satellite...":"Routing encrypted data from defense satellite..."}
print("======================================================================================================")
print_slow( "//KEYSTROKE//")
print("")
print("======================================================================================================")
print ("Press 'I' for instructions")
print ("Press 'D' to choose difficulty")
print ("Press 'Q' to quit")
print("======================================================================================================")
opt=input("> ")
while opt!="Q":
        if opt=="D" or opt=="d":
                print("======================================================================================================")
                print ("Choose Difficulty:")
                print ("1. Novice                 (NOV)")
                print ("2. Rookie                 (ROK)")
                print ("3. Professional           (PRO)")
                print("======================================================================================================")
                dif=input("Enter option code: ")
                print("")
                if dif=="NOV" or dif=="nov":
                        print ("Your difficulty has been set.")
                        print("")
                        play=input( "PRESS 'P' TO PLAY============================================================================ ")
                        if play=="P" or play=="p":
                                print("")
                                print("Get ready...")
                                time.sleep(1)
                                print("Set...")
                                time.sleep(1)
                                print("TYPE!..")
                                time.sleep(1)
                                print("")
                                lifesave_nov=30
                                missile_time_nov= 90.0
                                start_time = time.time()
                                convo_len=int(len(convo))
                                qus=(random.choice( list(convo.keys())))
                                print (qus)
                                ans=input("> ")
                                while qus!=ans:
                                    print ("try again..")
                                    ans=input("> ")
                                    fin_time = time.time() - start_time
                                    fin_time = round(fin_time,2)
                                    end_time = missile_time_nov - fin_time
                                    end_time = int(round(end_time,2))
                                    if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time, "seconds.")
                                        print ("Over",lifesaved," lives saved.")
                                        print ("You are a true hero.")
                                        break
                                while qus==ans:
                                     qus=(random.choice( list(convo.keys())))
                                     print (qus)
                                     ans=input("> ")
                                     lifesaved=((count_letters(ans))*lifesave_nov)
                                     fin_time = time.time() - start_time
                                     fin_time = round(fin_time,2)
                                     end_time = missile_time_nov - fin_time
                                     end_time = int(round(end_time,2))
                                     if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time,"seconds.")
                                        print ("Over",lifesaved,"lives saved.")
                                        print ("You are a true hero.")
                                        break
                                break
                elif dif=="ROK" or dif=="rok":
                        print ("Your difficulty has been set.")
                        print("")
                        play=input( "PRESS 'P' TO PLAY============================================================================ ")
                        if play=="P" or play=="p":
                                print("")
                                print("Get ready...")
                                time.sleep(1)
                                print("Set...")
                                time.sleep(1)
                                print("TYPE!..")
                                time.sleep(1)
                                print("")
                                lifesave_rok=10
                                missile_time_rok= 60.0
                                start_time = time.time()
                                convo_len=int(len(convo))
                                qus=(random.choice( list(convo.keys())))
                                print (qus)
                                ans=input("> ")
                                while qus!=ans:
                                    print ("try again..")
                                    ans=input("> ")
                                    fin_time = time.time() - start_time
                                    fin_time = round(fin_time,2)
                                    end_time = missile_time_rok - fin_time
                                    end_time = int(round(end_time,2))
                                    if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time, "seconds.")
                                        print ("Over",lifesaved," lives saved.")
                                        print ("You are a true hero.")
                                        break
                                while qus==ans:
                                     qus=(random.choice( list(convo.keys())))
                                     print (qus)
                                     ans=input("> ")
                                     lifesaved=((count_letters(ans))*lifesave_rok)
                                     fin_time = time.time() - start_time
                                     fin_time = round(fin_time,2)
                                     end_time = missile_time_rok - fin_time
                                     end_time = int(round(end_time,2))
                                     if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time,"seconds.")
                                        print ("Over",lifesaved,"lives saved.")
                                        print ("You are a true hero.")
                                        break
                                break
                else:
                        print ("Your difficulty has been set.")
                        print("")
                        play=input( "PRESS 'P' TO PLAY============================================================================ ")
                        if play=="P" or play=="p":
                                print("")
                                print("Get ready...")
                                time.sleep(1)
                                print("Set...")
                                time.sleep(1)
                                print("TYPE!..")
                                time.sleep(1)
                                print("")
                                lifesave_pro=5
                                missile_time_pro= 30.0
                                start_time = time.time()
                                convo_len=int(len(convo))
                                qus=(random.choice( list(convo.keys())))
                                print (qus)
                                ans=input("> ")
                                while qus!=ans:
                                    print ("try again..")
                                    ans=input("> ")
                                    fin_time = time.time() - start_time
                                    fin_time = round(fin_time,2)
                                    end_time = missile_time_pro - fin_time
                                    end_time = int(round(end_time,2))
                                    if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time, "seconds.")
                                        print ("Over",lifesaved," lives saved.")
                                        print ("You are a true hero.")
                                        break
                                while qus==ans:
                                     qus=(random.choice( list(convo.keys())))
                                     print (qus)
                                     ans=input("> ")
                                     lifesaved=((count_letters(ans))*lifesave_pro)
                                     fin_time = time.time() - start_time
                                     fin_time = round(fin_time,2)
                                     end_time = missile_time_pro - fin_time
                                     end_time = int(round(end_time,2))
                                     if end_time<=0:
                                        print ("Resistance is futile. City is destroyed.")
                                        print ("The time taken is", fin_time,"seconds.")
                                        print ("Time left for missile to explode is ",end_time,"seconds.")
                                        print ("Over",lifesaved,"lives saved.")
                                        print ("You are a true hero.")
                                        break
                                break 
        else:
                print("--------------------------------------------------//INSTRUCTIONS//----------------------------------------------------")
                print("")
                print("THE POWER TO SAVE LIVES WITH THE PRESS OF A KEY.")
                print("")
                print("The basic rule for the game is to save maximum number of lives possible by typing commands you get in the questions.")
                print("Important note: The answers are case sensitive. It tests your accuracy in typing.")
                print("The number of lives saved and the time of strike of the missile will vary by difficulty of 3 levels.")
                print("Toughest levels will have the least time and the least number of lives saved.")
                print("Though its impossible to save all, reducing casualities must be your priority.")
                print("")
                print("BE A HERO, TYPOMANDO.")
                print("")
                print("Press D to choose difficulty")
                print("---------------------------------------------------------------------------------------------------------------------------------")
        opt=input("> ")
if opt=="Q" or opt=="q":
        print ("Game is quitting...")
        time.sleep(1)
        quit()
input()
