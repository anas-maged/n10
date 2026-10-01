import random
hb = 3
score = 0
print("welcome! you are now in the [castale of secrerts game] came and try your luck") 
while True :
    wri = input("write the [next] to explain the game: ").lower()
    if wri == "next" :
        print('you are now a warrior with 3 health points and 0 luck points')
        print("you lose if yur health points reach 0, and you win if your luck points reach 30.")
        print("each time,six options will appear, and you will choose one")
        print("you don't know what the options are, so you woll choose randomly from the six options behind the doors")
        print("one of those thing might appear to you: ")
        print("1. a bomb will expode and take one health point from you.")
        print("2. Doctor,and he will give you one health points.")
        print("3. you will face a monster, and yhen you will lose one luck point.")
        print("4. you won't find any thing, and then you will earn one luck point.")
        print("5. a thief will appear and tale 1 your heallth points and 1 your luck points")
        print("6. you will find treasure and receive 20 lucky points")
        print("7 .the golden door: if you choose it, the system will gianone health point and one luck point,\n if you guess incorrectly, you will lose 1 health point and 1 luck point")
    else: 
        print("what did?")
        break
    while True :
        us1 = int(input("choose one of the doors[1 - 2 - 3 - 4 - 5 - 6 - 7]: "))
        if us1 == 1 :
                us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                if us_ran == "boobm":
                    hb = hb - 1
                    print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                elif us_ran == "Doctor":
                    hb = hb + 1
                    print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                elif us_ran == "mondter":
                    score = score - 1
                    print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                elif us_ran == "nothing":
                    score = score + 1
                    print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                elif us_ran == "thief":
                    score = score - 1
                    hb = hb -1
                    print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                elif us_ran == "treadure":
                    score = score + 20
                    print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                else:
                    ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                    ran = random.randint(1,3)
                    if ch_us == ran :
                        hb = hb + 1 
                        score =score + 1
                        print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                    else:
                        hb = hb - 1 
                        score = score - 1
                        print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}")
        elif us1 == 2 :
                        us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                        if us_ran == "boobm":
                            hb = hb - 1
                            print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                        elif us_ran == "Doctor":
                            hb = hb + 1
                            print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                        elif us_ran == "mondter":
                            score = score - 1
                            print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                        elif us_ran == "nothing":
                            score = score + 1
                            print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                        elif us_ran == "thief":
                            score = score - 1
                            hb = hb -1
                            print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                        elif us_ran == "treadure":
                            score = score + 20
                            print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                        else:
                            ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                            ran = random.randint(1,3)
                            if ch_us == ran :
                                hb = hb + 1 
                                score =score + 1
                                print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                            else:
                                hb = hb - 1 
                                score = score - 1
                                print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}")
        elif us1 == 3 :
                                    us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                                    if us_ran == "boobm":
                                        hb = hb - 1
                                        print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                                    elif us_ran == "Doctor":
                                        hb = hb + 1
                                        print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                                    elif us_ran == "mondter":
                                        score = score - 1
                                        print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                                    elif us_ran == "nothing":
                                        score = score + 1
                                        print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                                    elif us_ran == "thief":
                                        score = score - 1
                                        hb = hb -1
                                        print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                                    elif us_ran == "treadure":
                                        score = score + 20
                                        print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                                    else:
                                        ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                                        ran = random.randint(1,3)
                                        if ch_us == ran :
                                            hb = hb + 1 
                                            score =score + 1
                                            print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                                        else:
                                            hb = hb - 1 
                                            score = score - 1
                                            print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}") 
        elif us1 == 4 :
                                us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                                if us_ran == "boobm":
                                    hb = hb - 1
                                    print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                                elif us_ran == "Doctor":
                                    hb = hb + 1
                                    print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                                elif us_ran == "mondter":
                                    score = score - 1
                                    print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                                elif us_ran == "nothing":
                                    score = score + 1
                                    print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                                elif us_ran == "thief":
                                    score = score - 1
                                    hb = hb -1
                                    print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                                elif us_ran == "treadure":
                                    score = score + 20
                                    print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                                else:
                                    ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                                    ran = random.randint(1,3)
                                    if ch_us == ran :
                                        hb = hb + 1 
                                        score =score + 1
                                        print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                                    else:
                                        hb = hb - 1 
                                        score = score - 1
                                        print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}")
        elif us1 == 5 :
                        us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                        if us_ran == "boobm":
                            hb = hb - 1
                            print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                        elif us_ran == "Doctor":
                            hb = hb + 1
                            print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                        elif us_ran == "mondter":
                            score = score - 1
                            print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                        elif us_ran == "nothing":
                            score = score + 1
                            print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                        elif us_ran == "thief":
                            score = score - 1
                            hb = hb -1
                            print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                        elif us_ran == "treadure":
                            score = score + 20
                            print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                        else:
                            ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                            ran = random.randint(1,3)
                            if ch_us == ran :
                                hb = hb + 1 
                                score =score + 1
                                print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                            else:
                                hb = hb - 1 
                                score = score - 1
                                print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}")
        elif us1 == 6 :
                                us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                                if us_ran == "boobm":
                                    hb = hb - 1
                                    print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                                elif us_ran == "Doctor":
                                    hb = hb + 1
                                    print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                                elif us_ran == "mondter":
                                    score = score - 1
                                    print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                                elif us_ran == "nothing":
                                    score = score + 1
                                    print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                                elif us_ran == "thief":
                                    score = score - 1
                                    hb = hb -1
                                    print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                                elif us_ran == "treadure":
                                    score = score + 20
                                    print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                                else:
                                    ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                                    ran = random.randint(1,3)
                                    if ch_us == ran :
                                        hb = hb + 1 
                                        score =score + 1
                                        print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                                    else:
                                        hb = hb - 1 
                                        score = score - 1
                                        print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}") 
        elif us1 == 7 :
                                us_ran = random.choice(["boobm", "Doctor","monster", "nothing","thief","treadure","golden door"])
                                if us_ran == "boobm":
                                    hb = hb - 1
                                    print(f"you revealed abomb and lost -1- HB pnint your current point: {hb} score: {score}")
                                elif us_ran == "Doctor":
                                    hb = hb + 1
                                    print(f"A doctot has appered, and you have gained -1- HB point your current point: {hb} score: {score}")
                                elif us_ran == "mondter":
                                    score = score - 1
                                    print(f"A monster has appered, and you have lost -1- luck point your current points score: {score} HB: {hb}")            
                                elif us_ran == "nothing":
                                    score = score + 1
                                    print(f"you didn't find anything, you've gined -1- luck point you current point: score: {score} HB: {hb}")
                                elif us_ran == "thief":
                                    score = score - 1
                                    hb = hb -1
                                    print(f"A thief has appeared, ans you have lost -1- luck point and -1- HB point\nand your current points: HB:{hb} - score: {score}")
                                elif us_ran == "treadure":
                                    score = score + 20
                                    print(f"congratulation! you found the treasure and won -20- lucky points\b your current points: {score} HB: {hb}")
                                else:
                                    ch_us = int(input("you have three doors: [ 1 or 2 or 3 ] which one will you choose?"))
                                    ran = random.randint(1,3)
                                    if ch_us == ran :
                                        hb = hb + 1 
                                        score =score + 1
                                        print(f"good you win \n you have earned one health point and one luck point\n hb: {hb}\nscore: {score}")
                                    else:
                                        hb = hb - 1 
                                        score = score - 1
                                        print(f"sorry you lost 1 health point and 1 luck point\nhb: {hb} \nscore: {score}")                                                   
        else:
            print("sorry, return to the beginning and follow the rules.")
        if hb <= 0:
            print(f"your health points have reached {hb} you have lost the game.")
            break
        if score >= 30:
            print(f"congratulations!\n on your luck points: {score} you have won the game!!!!!")                                         
