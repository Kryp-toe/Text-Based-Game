import random

question = [', WHAT ARE YOU GOING TO DO?']
end = [' THE DOOR YOU ENTERED LED TO A TRAP AND YOU FALL INTO SPIKES AND DIED.', 'RESTART?', 'end game', 'stop', 'end', 'yes', 'restart', 'no']
Inventory = []
directions = ['north', 'south', 'west', 'east'] # These are the directions the user can go
events = [] # checks which events have happend
store=[]
################################################################################################################################
#START THE GAME#
def start():
    name = input('\n' + 'ENTER USERNAME:')
    print('\n' + '\n' +  'HELLO ' + name.upper() + ' WELCOME TO THE WORLD OF TEXT ESCAPE' + '\n')
    entry = input('\n' + 'PRESS START TO BEGIN THE GAME, START (1) > ')
    if(entry.lower()=='1'):
        begin()
    else:
        print('\n' + 'Invalid Input' + '\n')
        start()

################################################################################################################################
#THE GAME BEGINS#
def begin():
    print('\n' + 'YOU FOUND YOURSELF TRAPPED IN A HUNTERS HOUSE WHO IS ALSO A SERIAL KILLER')
    print('YOU WERE UNCONCIOUS AND YOU JUST WOKE UP, NOW YOU MUST FIND A WAY TO ESCAPE' + '\n')
    print('\n' + 'YOU ARE IN A DARK ROOM' + question[0] + '\n')
    entry = input('LOOK AROUND OR REMAIN STILL? > ')
    if(entry.lower() == 'look around'):
        walkAround()
    elif(entry.lower() == 'remain still'):
        deathwish()
    else:
        print('\n' + 'Invalid Input' + '\n')
        begin()

#################################################################################################################################
# THE DECIDED TO WALK AROUND
def walkAround():
    print('\n' + 'YOU FOUND A TORCH THE IS NOW BRIGHT' + question[0]+ '\n')
    entry = (input('LOOK AROUND OR REMAIN STILL? > '))
    if(entry.lower() == 'look around'):
        door()
    elif(entry.lower() == 'remain still'):
        ownerfindsplayer()
    else:
        print('\n' + 'Invalid Input' + '\n')
        walkAround()

#################################################################################################################################
### THE USER NOW SEE THE ROOM AND THINGS
def door():
    print('\n' + 'YOU SEE A DOOR, A BED AND A WINDOW ' + question[0] + '\n')
    entry = (input('WHERE DO YOU WANT TO GO TO THE DOOR, BED OR WINDOW? > '))
    if(entry == 'door'):
        key()
    elif(entry == 'window'):
        window()
    elif(entry.lower()=='bed'):
        bed()()
    else:
        print('\n' + 'Invalid Input' + '\n')
        door()
            
################################################################################################################################
#THE USER IS LOOK FOR THE KEYS#
def key():
    print('\n' + 'THE DOOR IS LOCKED' + question[0] + '\n')
    entry = (input('SEARCH FOR KEYS, LOOK AROUND OR STAY? > '))
    if(entry.lower() == 'search for keys'):
        randomNumber = random.randint(1, 5)
        while(randomNumber != 3):
            print('\n' + 'YOU HAVE NOT FOUND THE KEYS' + question[0] + (' (TYPE SEARCH TO KEEP SEARCHING)' + '\n'))
            entry = input('KEEP SEARCHING OR QUIT THE SEARCH? > ')
            if(entry.lower()=='quit the search'):
                door()
            randomNumber = random.randint(1, 5)
        openDoor()
    elif(entry.lower() == 'stay'):
        hotroom()
    elif(entry.lower()=='look around'):
        door()
    else:
        print('\n' + 'Invalid Input' + '\n')
        key()

#################################################################################################################################
#THE USER HAS FOUND THE KEYS AND HAS TO OPEN THE DOORS#
def openDoor():
    print('\n' + 'YOU HAVE FOUND THE KEYS' + question[0] + '\n')
    entry = (input('OPEN DOOR OR STAY OR LOOK AROUND? > '))
    if(entry.lower() == 'open door'):
        print('\n' + 'YOU ENTERED A ROOM AND YOU SEE THREE DOORS' + question[0] + '\n')
        threedoor()
    elif(entry.lower()=='look around'):
        reminder()
    elif(entry.lower()=='stay'):
        print('\n' + "YOU HAVE DECIDED TO STAY IN THE HOUSE AND YOU RAN OUT OF BREATHE" + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        openDoor()

##################################################################################################################################
#THE USER HAS LEFT THE FIRST ROOM AND HAS TO PICK ONE DOOR#
def threedoor():
    for randomNumber in (1,10):
        entry = input('CHOOSE WHICH DOOR TO OPEN, RED DOOR, GREEN DOOR OR BLUE DOOR? > ')
        if(randomNumber == 3):
            print('\n' + 'THE DOOR YOU ENTERED HAD A TRAP, YOU WERE HIT AND DIED' + '\n')
            restart()
        elif((randomNumber % 2) == 0):
            print('\n' + 'THE DOOR YOU CHOSE LEADS OUTSIDE' + question[0] + '\n')
            entry = input('GO OUTSIDE OR SEARCH THE HOUSE? > ')
            if(entry.lower() == 'go outside'):
                outside()
            elif(entry.lower() == 'search the house'):
                search()
            else:
                print('\n' + 'Invalid Input' + '\n')
                exit()
        else:
            print('\n' + 'THE DOOR YOU CHOSE LEADS TO THE BASEMENT' + question[0] + '\n')
            downstairs()

##################################################################################################################################
#THE USER IS NOW OUTSIDE AND GOES TO THE MAIN GATE FOR THE PIN#
def outside():
    print('\n' + 'OUTSIDE YOU FIND THE MAIN GATE, THE MAIN GATE HAS A LOCK' + question[0] + '\n')
    randomNumber_A = random.randint(1, 9)
    randomNumber_B = random.randint(1, 9)
    randomNumber_C = random.randint(1, 9)
    temp  = [0, 0, 0]
    
    randomNumber_POS_A = random.randint(0, 2)
    temp[randomNumber_POS_A] = randomNumber_A
    
    randomNumber_POS_B = random.randint(0, 2)
    while(randomNumber_POS_A == randomNumber_POS_B):
        randomNumber_POS_B = random.randint(0, 2)
    temp[randomNumber_POS_B] = randomNumber_B
    
    randomNumber_POS_C = random.randint(0, 2)
    while(randomNumber_POS_A == randomNumber_POS_C or randomNumber_POS_C == randomNumber_POS_B):
        randomNumber_POS_C = random.randint(0, 2)
    temp[randomNumber_POS_C] = randomNumber_C
    
    #ask the user to guess the pin
    pin = str(temp[0]) + str(temp[1]) + str(temp[2])
    print(randomNumber_A, randomNumber_B, randomNumber_C)
    entry = input('\n' + 'RE-ARRANGE THE NUMBERS ABOVE TO GUESS THE PIN > ')
    count = 0
    alarm = 'Active'
    while(entry != pin):
        count += 1
        print(randomNumber_A, randomNumber_B, randomNumber_C)
        entry = input('\n' + 'INCORRECT PIN, TRY AGAIN > ')
        
        while((count % 3) and (alarm == 'Active')):
            attempts()
            
    if(entry==pin):
        print('\n' + 'THE PIN YOU ENTERED WAS CORRECT')
        print('\n' + "CONGRADULATIONS, YOU FIND YOUSELF OUT THE YARD.")
        print('\n' + 'YOU MADE IT OUT THE HOUSE' + question[0] + '\n')
        entry = input('EXPLORE THE FOREST OR GO BACK? >')
        if(entry.lower()=='explore the forest'):
            forest()
        elif(entry.lower()=='go back'):
            print('\n' + "THE GATE IS NOW LOCKED " + question[0] + '\n')
            look()

#####################################################################################################################################
#THE USER IS LOOK FOR THE ALARM SWITCH WHICH IS OUTSIDE#
def look():
    print('\n' + "YOU SEE A DOG HOUSE,A ELECTRICITY BOX, BACK ROOM AND MAIN HOUSE FIND THE ROOM WITH THE ALARM SWITCH AND TURN IT OFF" + question[0] + '\n')
    entry = input(' WHERE DO YOU WANT TO GO, DOG HOUSE, ELECTRICITY BOX, BACK ROOM OR MAIN HOUSE? > ')
    if(entry.lower()=='dog house'):
        print('THE DOG HOUSE','\n','UNFORTUNATELY FOR YOU THE DOG WAS AWAKE AND YOU WERE KILLED BY THE DOG')
        restart()
    elif(entry.lower()=='electricity box'):
        electricalbox()
    elif(entry.lower() == 'back room'):
        backroom()
    elif(entry.lower()=='main house'):
        search()
    else:
        print('\n' + 'Invalid Input' + '\n')
        look()

######################################################################################################################################
#RETURNS TO THE HOUSE AFTER FAILING TO OPEN THE GATE#
def search():
    print('\n' + 'YOU RETURNED TO THE MAIN HOUSE, BUT THIS TIME THE WHOLE HOUSE IS DARK' + '\n')
    keepknife()

###################################################################################################################################
#IN THE BASEMENT#
def downstairs():
    print('\n' + 'THE BASEMENT IS SUPER DARK' + question[0] + '\n')
    print('>HINT< YOU STILL HAVE A TOUCH' + question[0] + '\n')
    entry = input('USE TORCH or WALK AROUND? > ')
    
    if(entry.lower() == 'use torch'):
        torchdown()
            
    elif(entry.lower()=='walk around'):
        print( '\n' + 'YOU FELL ON A BROKEN BOOK SHELF AND WERE STABBED BY ITs WOOD AND DIED' + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        downstairs()

###################################################################################################################################
def deathwish():
    print('\n' + 'THE ROOM IS BECAMING VERY HOT','\n''YOU MIGHT RUN OUT OF AIR' + question[0] + '\n')
    entry = input('ESCAPE OR STAY? > ')
    if(entry.lower()=='escape'):
        begin()
    elif(entry.lower()=='stay'):
        print('\n' + 'YOU RAN OUT OF AIR')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        deathwish()

####################################################################################################################
def ownerfindsplayer():
    print('\n' + 'YOU DECIDED TO STAY IN THE ROOM'+ question[0]+ '\n')
    entry = (input('ESCAPE OR STAY FOREVER? > '))
    if(entry.lower()=='escape'):
        walkAround()
    elif(entry.lower()=='stay forever'):
        print('\n' + 'THE OWNER RETURNED AND FOUND YOU IN THE HOUSE AND HE KILLED YOU')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        ownerfindsplayer()

#######################################################################################################
def bed():
    print('\n' + 'YOU ARE NEXT TO THE BED')
    print('\n' + 'ITS AT NIGHT' '\n' 'WILL IT BE WISE TO SLEEP?' + question[0] + '\n')
    entry = (input('LOOK AROUND OR LAY DOWN? > '))
    if(entry.lower()=='look around'):
        door()
    elif(entry.lower()=='lay down'):
        print('\n' + 'THE OWNER OF THE HOUSE FOUND YOU SLEPING AND KILLED YOU')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        bed()

######################################################################################################
def window():
    print('\n' + 'THE WINDOWS IN THIS HOUSE ARE PROTECTED WITH ELECTRICAL BARS' + question[0] + '\n')
    entry = (input('LOOK AROUND OR TRY ESCAPING? > '))
    if(entry.lower()=='look around'):
        door()
    elif(entry.lower()=='try escaping'):
        print('\n' + 'YOU WERE SHOCKED BY THE ELETRICAL BARS AND DIED' + '\n' )
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        window()

#######################################################################################################
def hotroom():
    print('\n' + 'YOU HAVE NOT FOUND THE KEY' + question[0] + '\n')
    entry = input('KEEP LOOKING OR REMAIN STILL? > ')
    if(entry.lower() == 'remain still'):
        hotchoice()   
    elif(entry.lower()=='keep looking'):
        key()
    else:
        print('\n' + 'Invalid Input' + '\n')
        hotroom()

#######################################################################################################
def reminder():
    print('\n' + "THERE IS NOTHING USEFUL IN THE ROOM,REMINDER YOU HAVE TO ESCAPE" + '\n' )
    entry = (input('RETURN TO THE DOOR OR STAY? > '))
    if(entry.lower()=='return to the door'):
        openDoor()
    elif(entry.lower()=='stay'):
        print('\n' + "YOU HAVE DECIDED TO STAY IN THE HOUSE AND YOU RAN OUT OF BREATHE" + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        reminder()

##############################################################################################
def backroom():
    print('\n' + 'YOU HAVE ENTERED THE BACK ROOM' + question[0] + '\n')
    entry = input('LOOK AROUND OR EXIT? > ')
    if(entry.lower()=='look around'):
        print('\n' + 'YOU SEE A LAB ROOM AND A SWITCH BOX' + question[0] + '\n')
        entry = input('WHERE DO YOU WANT TO GO?, SWITCH BOX, LAB ROOM OR EXIT > ')
        if(entry.lower()=='switch box'):
            print('\n' + 'YOU SWITCHED THE ALARM OFF')
            outside()
        elif(entry.lower()=='lab room'):
            print('\n' + 'THE ROOM HAD POISONOUNS CHEMICALS AND YOU ENTERED WITHOUT PROTECTIVE GEAR' + '\n')
            restart()
        elif(entry.lower()=='exit'):
            print('\n' + 'YOU ARE OUTSIDE' + '\n')
            look()
        else:
            print('\n' + 'Invalid Input' + '\n')
            backroom()
    elif(entry.lower()=='exit'):
        print('\n' + 'YOU ARE OUTSIDE' + '\n')
        look()
    else:
        print('\n' + 'Invalid Input' + '\n')
        backroom()

###############################################################################################################
def electricalbox():
    print('\n' + 'YOU ARE NEXT TO THE ELECTRICITY BOX, THE BOX HAS A WARNING SIGN' + question[0] + '\n')
    entry=input('TO OPEN PRESS 1 ,TO READ THE WARNING SIGN PRESS 2 > ')
    if(entry == '1'):
        print('\n' + 'YOU WERE SHOCKED AND DIED' + '\n')
        restart()
    elif(entry== '2'):
        warning()
    else:
        print('\n' + 'Invalid Input' + '\n')
        electricalbox()

########################################################################################################
def warning():
    print('\n' + 'THIS BOX IS VERY DANAGEROUS AND THE USER IS RECOMMENDED TO NOT OPEN'+ question[0] + '\n')
    entry=input('OPEN THE BOX OR LOOK AROUND? > ')
    if(entry.lower()=='open the box'):
        print('\n' + 'YOU WERE SHOCKED AND DIED' + '\n')
        restart()
    elif(entry.lower()=='look around'):
        look() 
    else:
        print('\n' + 'Invalid Input' + '\n')
        warning()

#########################################################################################################
def tunnel():
    print('\n' + 'YOU FELL INTO A TUNNEL, THE TUNNEL LANDS YOU IN THE BASEMENT ' + '\n')
    print('THIS BASEMENT HAS NO WINDOWS '+ question[0] + '\n')
    entry = input('LOOK AROUND OR REMAIN STILL? > ')
    
    if(entry.lower() == 'look around'):
        downstairs()
    elif(entry.lower() == 'remain still'):
        print('\n' + 'YOU RAN OUT OF BREATHE, IT IS TOO HOT HERE' + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        tunnel()

################################################################################################################################
def kitchen():
    print('\n' + 'WHILE SEARCHING YOU FOUND A KITCHEN KNIFE' + question[0] + '\n')
    entry = input('KEEP IT or LEAVE IT? > ')
    if(entry.lower()=='keep it'):
        print('\n' + 'THE KNIFE IS STORED ON YOU,*HINT* REMEMBER IT WHEN YOU NEED IT')
        print('\n' + '_HINT_ REMEMBER IT WHEN YOU NEED IT' + '\n' )
        Inventory.append('Knife')
        search()
    elif(entry.lower()=='leave it'):
        print('\n' + 'LEFT THE KNIFE' + '\n')
        keepknife()
    else:
        print('\n' + 'Invalid Input' + '\n')
        kitchen()

################################################################################################################################
def outofair():
    print('\n' + 'YOU RAN OUT OF BREATHE, IT IS TOO HOT HERE' + '\n' )
    entry=input('DO YOU WANT TO RESTART?, YES OR NO? > ')
    restart()
################################################################################################################################
def objects():
    print('\n' + "YOU SEE BOOST VITAMINS, BROKEN BOOK SHELF, CHEST DRAWER"  + question[0]  + '\n')
    entry = input('WHAT DO YOU WANT TO CHECK? VITAMINS, BOOK SHELF OR CHEST DRAWER? > ')
    if(entry.lower() == 'vitamins'):
        vitamins()
    elif(entry.lower()=='chest drawer'):
        chestdrawer(Inventory)
    elif(entry.lower()=='book shelf'):
        print('\n' + 'ON THE BOOK SHELF THERE IS A BOOK ' + '\n')
        entry = input('TAKE BOOK OR LEAVE IT? > ')
        if entry.lower()=='take book':
            print('\n' + "YOU KEPT THE BOOK") 
            objects()
        elif entry.lower()=='leave it':
            print('\n' + "YOU LEFT THE BOOK") 
            objects()
        else:
            print('\n' + 'Invalid Input' + '\n')
            bookshelf()

    else:
        print('\n' + 'Invalid Input' + '\n')
        objects()

################################################################################################################################
def vitamins():
    print('\n' + 'YOU ARE CHECKING THE VITAMINS'+ question[0] + '\n')
    entry = input('USE THEM OR LEAVE THEM? > ')
    if(entry.lower()=='use them'):
        print('\n' + 'THE VITAMINS HAVE BEEN THERE FOR A LONG TIME,AS A RESULT THEY THEATENED YOUR HEALTH' + '\n')
        entry = input('DO YOU WANT TO RESTART?, YES OR NO? > ')
        if(entry.lower()=='yes'):
            start()
        elif(entry.lower()=='no'):
            print('\n' + 'BYE')
            exit()
        else:
            restart()
    elif(entry.lower()=='leave them'):
        downstairs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        vitamins()

################################################################################################################################
def chestdrawer(store):
    if('book' not in store):
        itemchoice()
    else:
        chestopinion()   

################################################################################################################################
def attempts():
    print('\n' + "YOU HAVE NO ATTEMPTS LEFT,AND THE ALARM IS ON" + question[0] + '\n')
    entry = input( 'LOOK AROUND OR GO TO THE HOUSE? > ')
    if(entry.lower() == 'look around'):
        look()
    elif(entry.lower()=='go to the house'):
        search()
    else:
        print('\n' + 'Invalid Input' + '\n')
        attempts()

################################################################################################################################
def escapebasement():
    print("CONGRADULATIONS, YOU FIND YOUSELF OUT THE YARD.")
    print('\n' + 'YOU MADE IT OUT THE HOUSE' + question[0] + '\n')
    entry = input('EXPLORE THE FOREST OR GO BACK? > ')
    if(entry.lower()=='explore the forest'):
        forest()
    elif(entry.lower()=='go back'):
        print('\n' + 'YOU HAVE RETURN AND HAVE TO SEARCH THE BASEMENT AGAIN' +'\n')
        downstairs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        escapebasement()

################################################################################################################################
#THE USERS CHOICE
def unknownroom():
    print('\n' + 'YOU ENTERED THE ROOM AND THE DOOR BEHIND YOU SHUTS, IT BECOMES DARK ' + question[0] + '\n')
    entry = input('USE TORCH OR WALK AROUND? > ')
    if(entry.lower() == 'use torch'):
        snake()
    elif(entry.lower()=='walk around'):
        print('YOU STANDED ON A SNAKE AND IT BITE YOU AND DIED')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        unknownroom() 

################################################################################################################################
def snake():
    print('\n' + 'THE ROOM IS NOW BRIGHT AND YOU CAN NOW SEE')
    print('\n' + 'NEXT TO YOU SEE A SNAKE' + question[0] + '\n')
    entry = input('RUN PAST,QUICKLY GRAB IT OR WALK SLOWLY PAST? > ')
    if(entry.lower()=='run past'):
        print('\n' + 'THE SNAKE FELT STARTLED AND ATTACKED YOU' + '\n')
        restart()
    elif(entry.lower()=='quickly grab it'):
        print('\n' + 'THE SNAKE FELT PROVOKED AND ATTACKED YOU' + '\n')
        restart()
    elif(entry.lower()=='walk slowly'):
        print('\n' + 'THE SNAKE FELT THREATENED AND ATTACKED YOU' + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        snake()

################################################################################################################################
def map():
    print('\n' + 'ON THE MAP YOU SEE A ROUTE TO AN ESCAPE DOOR, A UNKNOWN ROOM, BACK TO THE HOUSE' + question[0] + '\n')
    entry = input('WHICH ROUTE DO YOU WANT TO TAKE, ESCAPE BASEMENT, UNKNOWN ROOM, BACK TO HOUSE, TRESSURE ISLAND OR RETURN?  > ' + '\n')
    if(entry.lower()=='escape basement'):
        escapebasement()
    elif(entry.lower()=='unknown room'):
        unknownroom()
    elif(entry.lower()=='back to house'):
        search()
    elif(entry.lower()=='tressure island'):
        tressureisland()
    elif(entry.lower()=='return'):
        chestdrawer()
    else:
        print('\n' + 'Invalid Input' + '\n')
        map()

################################################################################################################################
def forest():
    print('\n' + 'YOU ARE NOW IN THE FOREST THE ENTRANCE BACK TO THE HOUSE HAS BEEN SHUT' + question[0] + '\n')
    entry = input('LOOK AROUND, REMAIN STILL OR READ GUIDELINES? > ')
    if(entry.lower()=='look around'):
        outdoorForest()
    elif(entry.lower()=='remain still'):
        forest()
    elif(entry.lower()=='read guidelines'):
        guidelines()
    else:
        print('\n' + 'Invalid Input' + '\n')
        forest()
        
################################################################################################################################
def outdoorForest():
    print('\n' + "YOU ARE FACING THE FOREST AND YOU CANNOT RETURN BACK" + question[0] + '\n')
    print('THERE IS NO CLEAR PATH LEADING TO SAFETY, YOU CAN TAKE EITHER DIRECTION, IN ORDER TO FIND A CLEAR PATH: SOUTH, NORTH, WEST, OR EAST ' + '\n')
    entry = input('WHICH DIRECTION DO YOU WANT TO TAKE? > ')
    if(entry.lower() in directions):
        withinforest()
    else:
        print('\n' + 'Invalid Input' + '\n')
        outdoorForest()
################################################################################################################################
def cabin():
    print('\n' + '' + question[0] + '\n')
    print('')
    entry = input(' > ')

######################################################################################################################################################################
def boar():
    #if('quicksand' in events):
        #print() # Put in a specific scenario where the user has been in quicksand and approaches the boar (Reminder they are still drenched with quicksand)
        
    print('\n' + 'YOU SEE A WILD BEAR A COUPLE OF FEETS AHEAD OF YOU BUT IT HAS NOT NOTICED YOU' + question[0] + '\n')
    entry = input(' AVOID IT OR ATTACK IT? > ')
    randomNumber = random.randint(1, 3)
    if(entry.lower() == 'avoid it') and (randomNumber== 2):
        print('\n' + 'UNFORTUNIATELY THE BEAR SAW YOU AND ITS ADVANCING TOWARDS YOU' + question[0] + '\n')
        bearRun()
    elif(entry.lower() == 'attack it'):
             attactbear()      
    else:
        print('\n' + 'Invalid Input' + '\n')
        boar()

########################################################################################################################################################################
def brokenLeg():
    print('\n' + 'YOU LEGS IS INJURIED AND YOU NEED MEDICAL ' + question[0] + '\n')
    entry = input('DO YOU WANNA CHECK YOUR STORES FOR MEDICAL AIDS, YES OR NO? > ')
    if(entry.lower() == 'yes') and 'medical items' in store:
        brokenchoice()
    elif(entry.lower() == 'no'):
        bearRun()
    elif(entry.lower() == 'yes') and 'medical items'not in store:
        print('\n' + 'YOU DO NOT HAVE ANY MEDICAL AIDS')
        bearRun()
    else:
        print('\n' + 'Invalid Input' + '\n')
        brokenLeg()
    
#########################################################################################################################################################################
def book():
    print('\n' + 'THE TITLE OF THE BOOK IS "LOST IN THE BUSHES GUIDELINES' + '\n')
    dontDo()
    entry = input(' > ')

##########################################################################################################################################################################
def ending():
    print('\n' + 'YOU ARE SEEING A TAR ROAD AT THE END OF THE TREE LINE' + question[0] + '\n')
    entry = input(' PROCEED OR CHANGE DIRECTION ? > ')
    if (entry.lower() == 'proceed'):
        print('\n' + 'CONGRADULATIONS YOU MANEGED TO ESCAPE THE OF HUNTERS HOUSE AND FOUND YOUR WAY OUT OF THE FOREST')
        print('\n' + "YOU ARE A CERTIFIED SURVIVOR!")
        designers()
    elif(entry.lower() == 'change direction'):
        print('\n' + 'YOU CAME ACROSS A GROUP OF WILD ANIMALS AND YOU WERE ATTACKED AND KILLED ')
        print('BUT YOU WERE CLOSED TO MAKING IT OUT, BETTER LUCK NEXT TIME' + '\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        ending()
        
###########################################################################################################################################################################
# This checks if the user has a specific item in their inventory by checking if string is in a specific list
def valueFind(lists, value1):
    if(value1 in lists):
        value = value1
    else:
        value = ''
    return ', '+ value

#############################################################################################################################################################################
# This restarts the game
def restart():
    entry = input('DO YOU WANT TO RESTART?, YES OR NO > ')
    if(entry.lower()=='yes'):
        start()
    elif(entry.lower()=='no'):
        print('\n' + 'BYE')
        exit()
    else:
        print('\n' + 'Invalid Input' + '\n')
        restart()
        
#################################################################################################################################################################################
import random
def withinforest():
    print('\n' + 'YOU ARE IN THE DEPTHS OF THE FOREST, SURROUNDED BY TREES WITHOUT SIGHT OF THE SATETY ' + question[0] + '\n')
    print('DO YOU WANT TO CONTINUE WITH THE DIRECTION YOU CHOSE OR CHANGE THE DIRECTION?' + '\n')
    entry = input('CONTINUE OR CHANGE? > ')
    if(entry.lower()=='continue') or (entry.lower()=='change'):
        randomNumberz = random.randint in range(1,4)

        if(randomNumberz == 3):
            print('\n' + 'YOU ARE STILL IN THE DEPTHS OF THE FOREST WITH NO CLEAR PATH TO TAKE' + question[0] + '\n')
            withinforest()

        elif(randomNumberz == 1):
            print('\n' + 'YOU ARE STARTING TO FEEL LIKE YOU ARE LOST AND WORRIED NOW BECAUSE ITS GETTING LATE' + question[0] + '\n')
            withinforest()
            
        elif(randomNumberz % 2 == 0):
                cabinchoice()

        elif(randomNumberz % 2==0):
             intosand()
    else:
        print('\n' + 'Invalid input' + '\n')
        withinforest()

#######################################################################################################################################################################################
def quicksand():
        print('\n' + 'YOU ARE STILL SINKING BUT SLOWER THAN BEFORE'+ question[0] + '\n')
        entry = input('ESCAPE, ACCEPT FATE OR REMAIN CALM? > ')
        randomNumberFour = random.randint(2, 4)
        if((entry.lower() == 'escape') or (entry.lower() == 'accept fate')):
            print('\n' + 'YOU SUNK AND DROWNED' + '\n')
            forestRestart()
        elif((entry.lower() == 'remain calm') and (randomNumberFour == 3)):
            print('\n' + 'THE SAND HAS STOPPED SINKING AND YOU MANAGED TO ESCAPE THE QUICKSAND'+ question[0] + '\n')
            entry = input('WHICH DIRECTION WOULD YOU LIKE TO MOVE TOWARDS WEST, SOUTH, NORTH OR EAST? > ')
            randomNumberFive = random.randint(1, 10)
            if((entry.lower() in directions) and ((randomNumberFive % 2) == 0)):
                boar()
            elif entry.lower() in directions:
                ending()
        elif(randomNumberFour % 2==0):
            quicksand()
        else:
            print('\n' + 'Invalid Input' + '\n')
            quicksand()

###########################################################################################################################################################################################
def knife():
    print('\n' + 'YOU MOVE TOWARDS THE BEAR READY TO STRIKE' + question[3] + '\n')
    entry = input('WHICH BODY PART DO YOU WANT TO STRIKE: HEAD, LEGS OR TORSO? > ')
    if(entry.lower() == 'head'):
        print('\n' + 'THE BEAR GRABBED YOU ARM AND STRIKED YOU ON NECK AND YOU DIED' + '\n')
        forestRestart()
    elif(entry.lower() == 'torso'):
        print('\n' + 'YOU STRIKE THE BEAR ON THE LEGS AND IT GETs ERRATIC AND STRIKES YOU ON THE LEG' + question[0] + '\n')
        brokenLeg()
    elif(entry.lower()=='legs'):
        print('\n' + 'YOU STRIKE THE BEAR ON THE LEGS AND IT GETs ERRATIC AND STRIKES YOU ON THE LEG' + question[0] + '\n')
        brokenLeg()
    else:
        print('\n' + 'Invalid Input' + '\n')
        knife()
###########################################################################################################################################################################################
def runbear():
    print('\n' + 'THE BEAR REACHED YOU AND STRIKED YOU UNTIL YOU DIED' + '\n')
    forestRestart()

###########################################################################################################################################################################################
def runaway():
    print('\n' + 'THE BEAR IS BEHIND YOU' + question[0] + '\n')
    entry = input('KEEP RUNNING OR GIVE UP? > ')
    if(entry.lower() == 'keep running'):
        runbear()
    elif entry.lower()=='give up':
        runbear()
    else:
        print('\n' + 'Invalid Input' + '\n')
        runaway()
##############################################################################################################################################################################################
def attactbear():
    print('\n' + 'WHAT ARE YOU GOING TO USE TO ATTACK?' + '\n')
    entry = input('Fist ' + valueFind(Inventory, 'machete') + valueFind(Inventory, 'knife'))
        
    if(('machete' in Inventory) and (entry.lower() == 'machete')):
        knife()

    elif(('Knife' in Inventory) and (entry.lower() == 'knife')):
        knife()

    elif(entry.lower() == 'fist'):
         fistbear()
    else:
        print('\n' + 'Invalid Input' + '\n')
        attactbear()
#############################################################################################################################################################################################
def fistbear():
    print('\n' + 'YOU MOVE TOWARDS THE BEAR READY TO STRIKE' + question[3] + '\n')
    entry = input('WHICH BODY PART DO YOU WANT TO STRIKE: HEAD OR TORSO? > ')
    if entry.lower() == 'head' or entry.lower()=='torso':
        print('\n' + 'THE BEAR GRABBED YOU ARM AND STRIKED YOU ON NECK AND YOU DIED' + '\n')
        forestRestart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        fistbear()

###############################################################################################################################################################################################
def escapesand():
    print('\n' + 'YOU ARE STILL SINKING' + question[0] + '\n')
    entry = (input('ACCEPT FATE OR ESCAPE> '))
    if(entry.lower() == 'accept fate'):
        print('\n' + 'YOU SUNK AND DROWNED')
        forestRestart()
    elif entry.lower()=='escape':
        print('\n' + 'YOU FAILED TO ESCAPE AND YOU SUNK')
        forestRestart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        escapesand()

#################################################################################################################################################################################################
def intosand():
    events.append('quicksand')
    print('\n' + 'YOU WALKED INTO A QUICKSAND AND YOU ARE STUCK' + question[0] + '\n')
    print('ARE YOU GOING TO TRY ESCAPING, REMAIN CALM OR ACCEPT FATE?' + '\n')
    entry = (input('ESCAPE, REMAIN CALM OR ACCEPT FATE? > '))
    randomNumberThree = random.randint(1, 4)
    if(entry.lower() == 'escape'):
        for i in range(randomNumberThree):
            escapesand()
    elif(entry.lower() == 'accept fate'):
        print('\n' + 'YOU SUNK AND DROWNED'+ '\n')
        forestRestart()
    elif(entry.lower() == 'remain calm'):
        quicksand()
    else:
        print('\n' + 'Invalid input' + '\n')
        intosand()

#########################################################################################################################################
def cabinchoice():
    print('\n' + 'YOU FINALLY SEE SOMETHING, YOU SEE AN ABAONDONED CABIN' + question[0] + '\n')
    entry = (input('WHAT DO YOU WHAT TO DO? ENTER THE CABIN, CONITUNE WALKING OR WALK AROUND CABIN? > '))
    if(entry.lower() == 'enter the cabin'):
        cabin()
    elif(entry.lower()=='coniitune walking'):
        boar()
    elif(entry.lower()=='walk around cabin'):
        intosand()
    else:
        print('\n' + 'Invalid input' + '\n')
        cabinchoice()

########################################################################################################################################
def upstairs():
    print('\n' + "YOU ARE UPSTAIRS IN THE HALLWAY AND YOU SEE A DOOR LEADING OUTSIDE AND STAIRS TO THE BASEMENT" + question[0]  + '\n')
    entry=input('GO DOWNSTAIRS OR GO OUTSIDE? > ')
    if entry.lower() == 'go outside':
        outside()
    elif entry.lower() == 'go downstairs':
        downstairs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        upstairs()
##########################################################################################################################################
def keepknife():
    print('_HINT_ YOU ARE SOMEWHERE IN THE KITCHEN'+ question[0] + '\n')
    entry = (input('SEARCH KITCHEN OR WALK AROUND THE HOUSE? > '))
    if(entry.lower() == 'search kitchen'):
        kitchen()
    elif(entry.lower() == 'walk around the house'):
        tunnel()
    else:
        print('\n' + 'Invalid Input' + '\n')
        search()

##########################################################################################################################################
def torchdown():
    print('\n' + 'THE BASEMENT IS NOW BRIGHT AND YOU CAN NOW SEE' + question[0] + '\n')
    entry = input('LOOK AROUND OR STAY HERE? > ')
    if(entry.lower() == 'look around'):
        objects()
    elif(entry.lower()=='stay here'):
        outofair()
    else:
        print('\n' + 'Invalid Input' + '\n')
        torchdown()
        
#############################################################################################################################
def bookshelf():
    print('\n' + 'ON THE BOOK SHELF THERE IS A BOOK ' + '\n')
    entry = input('TAKE BOOK OR LEAVE IT? > ')
    if entry.lower()=='take book':
            bookread()
    elif entry.lower()=='leave it':
        print('\n' + "YOU LEFT THE BOOK") 
        objects()
    else:
        print('\n' + 'Invalid Input' + '\n')
        bookshelf()

##############################################################################################################################
def itemchoice():
    print('\n' + "THE CHEST IS OPEN AND YOU SEE,'A MAP', 'A MACHETE', 'MEDICAL ITEMS'"  + question[0]  + '\n')
    entry=input('WHAT DO YOU WANT TO TAKE: ITEMS, MAP, LOOK AROUND OR GO UPSTAIRS? > ')
    if entry.lower()=='map':
        map()
    elif entry.lower()=='items':
        store.append('Map')
        store.append('Machete')
        store.append('Medical Items')
        print('\n' + "YOU HAVE STORED THE ITEMS")
        itemchoice()
    elif entry.lower()=='go upstairs':
        upstairs()
    elif entry.lower()=='look around':
        objects()
    else:
        print('\n' + 'Invalid Input' + '\n')
        itemchoice()

##############################################################################################################################
def bookread():
    print('\n' + "YOU TOOK THE BOOK" + '\n')
    entry = input('READ NOW OR READ LATER? > ')
    if entry.lower()=='read now':
        book()
    elif entry.lower()=='read now':
        print('\n' + "THE BOOK IS STORED ON YOU INVENTORY")
        Inventory.append('book')
        objects()
    else:
        print('\n' + 'Invalid Input' + '\n')
        bookread()

#####################################################################################################################################
def guidelines():
    if ('book'in Inventory):
        book()
    elif('book'not in Inventory):
        print('YOU DO NOT HAVE A BOOK ON YOUR INVENTORY' + '\n')
        forest()
    else:
        print('\n' + 'Invalid Input' + '\n')
        guidelines()

####################################################################################################################################
def dontDo():
    print('NEVER MOVE TOWARDS UNKNOWN SOUNDS' + '\n')
    print('NEVER FEED THE WILD ANIMALS' + '\n')
    print('BEAR ARE ONE THE MOST DANAGEROUS ANIMALS BE AWARE OF THEM' + '\n')
    print('DO NOT SLEEP ON THE GROUND' + '\n')
    print('USE YOU MEDICAL KIT WISELY' + '\n')
    print('CERTAIN PLANTS MAKE CAUSE YOU BE CAREFUL OF WHAT YOU EAT' + '\n')
    print('COLLECT ITEMS THAT MIGHT BE USEFULL' + '\n')
    entry = input('PRESS(1) TO CLOSE THE GUIDELINES > ')
    if entry.lower()=='1':
        print('\n' + 'WE HOPE THE GUIDELINES WILL ASSIST YOU' + '\n')
        forest()
######################################################################################################################################
def bearRun():
    entry = input('\n' + 'RUN AWAY OR ATTACK IT? > ')
    if(entry.lower() == 'run away'):
            runaway() 
    elif(entry.lower() == 'attack it'):
        attactbear()
#########################################################################################################################################
def brokenchoice():
    print('\n' + 'YOU HAVE MANAGED TO STOP THE BLEEDING IN YOUR LEG AND COVER IT')
    print('\n' + 'THE BEAR IS STILL IN FRONT OF YOU ' + question[0] + '\n')
    entry = input('STAND UP OR LAY DOWN? > ')
    if(entry.lower() == 'stand up'):
        bearRun()
    elif(entry.lower() == 'lay down'):
        bearLaydown()
    else:
        print('\n' + 'Invalid Input' + '\n')
        brokenchoice()
#####################################################################################################################################
def tressureisland():
    print('\n' + 'YOU HAVE ENTERED THE CRACKED TUNNEL THAT LEADS TO THE TRESSURE' + question[0] + '\n')
    entry = input('PROCEED OR GO BACK ? > ' + '\n')
    if(entry.lower() == 'proceed'):
        Tworoutes()
    elif(entry.lower() == 'go back'):
        print('\n' + 'YOU HAVE RETURNED AND HAVE TO CHOOSE A ROUTE AGAIN' +'\n')
        map()
    else:
        print('\n' + 'Invalid Input')
        tressureisland()

###########################################################################################################################
def Tworoutes():
    print('\n' + 'WHLIE WALKING YOU SEE TWO MISTY ROUTES.' + '\n')
    print('\n' + 'THERES A LONGER ROUTE AND A SHORTER ROUTE,' + '\n')
    entry = input(' WHICH ONE DO YOU TAKE ? LONGER  ROUTE OR SHORTER ROUTE? > ')
    if(entry.lower() == 'shorter route'):
        print('\n' + 'YOU HAVE CHOOSEN THE BRIGHT ROUTE' +'\n')
        shorterroute()
    elif(entry.lower() == 'longer route'):
        print('\n' + 'YOU HAVE CHOOSEN THE SHADED ROUTE' +'\n')
        longerroute()
    else:
        print('\n' + 'Invalid Input' + '\n')
        Tworoutes()
############################################################################################################################
import random
def shorterroute():
    print('\n' + 'THE ROUTE LEADS TO A MISTY PIECE OF LAND AND HALFWAY THROUGH YOU HEAR WOLFS HOULLING BEHIND YOU' + question[0] + '\n')
    entry = input('RUN OR IGNORE THE HOULINGS ? > ')
    randomNumber = random.randint(1,3)
    if(entry.lower() == 'run') and (randomNumber == 3):
        river()
    elif(entry.lower() == 'run') and (randomNumber == 1):
        wolfs()
    elif(entry.lower() == 'run') and (randomNumber == 2):
        river()
    elif(entry.lower() == 'ignore the houlings'):
        wolfs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        shorterroute()
############################################################################################################################
def wolfs():
    print('\n' + '\n' + 'THE WOLFS HAVE CAUGHT UP TO YOU AND KILLED YOU' + '\n')
    restart()
#####################################################################################################################################################################################################
def river():
    print('\n' + 'YOU MANAGED TO OUTRUN THE WOLFS') 
    print('\n' + 'BUT DUE TO LACK OF CLEAR SITE YOU FALL INTO A TOUTBULANT AND ROCKY RIVER' + '\n')
    riverchoice()
##################################################################################################################################
def forestRestart():
    entry = input('DO YOU WANT TO RESTART?, YES OR NO? > ')
    if(entry.lower()=='yes'):
        forest()
    elif(entry.lower()=='no'):
        print('\n' + 'BYE')
        exit()
    else:
        print('\n' + 'Invalid Input' + '\n')
        restart()

####################################################################################################################################
def hotchoice():
    print('\n' + 'THE ROOM IS BECAMING VERY HOT', '\n''YOU MIGHT RUN OUT OF AIR' + question[0]+ '\n' )
    entry = input(' SEARCH OR STAY? > ')
    if(entry.lower()=='search'):
        key()
    elif(entry.lower()=='stay'):
        print('YOU RAN OUT OF AIR')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        hotchoice()
#######################################################################################################################################
# def longroute():
#     print('xxxxx')

#########################################################################################################################################
def choice():
    print('\n' + 'WOULD YOU LIKE TO PRCOCEED?'  + '\n')
    entry = input('YES OR NO? > ')
    if (entry.lower() == 'yes'):
        tressurechest()
    elif (entry.lower() == 'no'):
        choiceno()
    else:
        print('\n' + 'Invalid Input' + '\n')
        choice()
########################################################################################################################################
def choiceno():
    print('\n' + 'WARNING ONE OF THE WOLFs IS SWIMMINING TOWARDS YOU ' + question[0]  + '\n')
    entry = input('RUN OR STAY' + '\n')
    if (entry.lower() == 'run'):
        tressurechest()
    elif (entry.lower() == 'stay'):
        wolfs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        choiceno()
##########################################################################################################################################
def tressurechest():
    print('\n' + 'FROM A DISTANCE YOU see A SILIVER TRESSURE BOX ' + question[0] + '\n')
    print('ON THE BOX YOU SEE A LABEL AND IT READS: SOUTH AFRICAN GOLD RESERVES' + '\n')
    entry = input('GO LOOK INSIDE OR CONTINUE DIRECTION? > ')
    if (entry.lower() == 'go look inside'):
        print('\n' + 'OH OH! YOU HAVE STEPPED ON A MINE FIELD' + '\n')
        minefield()
    elif (entry.lower() == 'continue direction'):
        tresDirec()
    else:
        print('\n' + 'Invalid Input' + '\n')
        tressurechest()

##################################################################################################################################
def minefield():
    print('\n' +'IF YOU MOVE THE MINE FIELD DETENATES' + '\n')
    print('DEACTIVATING THE WHOLE MINE FIELD REQUIRES YOU TO SOLVE A RIDDLE' + question[0] + '\n')
    entry = input('MOVE OR SOLVE THE RIDDLE ? > ')
    if (entry.lower() == 'move'):
        print('\n' + 'THE MINE FIELD DETINATED, YOU DIED' + '\n')
        restart()
    elif (entry.lower() == 'solve the riddle'):
        print('\n' + 'SOLVE THE FOLLOWING RIDDLE' + '\n')
        riddles()
    else:
        print('\n' + 'Invalid Input' + '\n')
        minefield()
        
#########################################################################################################################################
def riddles():
    print('\n' + 'NOTE YOU ONLY HAVE ONE ATTEMPT' + '\n')
    randomNumber = random.randint(1,6)
    if (randomNumber == 1):
        entry = input('WHAT ALWAYS APPROACHES BUT NEVER ARRIVES ? >')
        if (entry.lower() == 'tommorow'):
          print('\n' + 'CORRECT YOU HAVE DEACTIVATED THE MINEFIELD AND AQUIRED THE TRESSURECHEST' + '\n')
          nextstep()
        else:
            print('\n' + 'WRONG! THE MINEFIELD DETINATED, YOU DIED' + '\n')
            restart() 
    elif (randomNumber == 2):
        entry = input('\n' + 'WHAT COMES ONCE IN A MINUTE, TWICE IN A MOMENT,BUT NEVER IN A THOUSAND YEARS? > ')
        if (entry.lower() == 'm'):
            print('\n' + 'CORRECT YOU HAVE DEACTIVATED THE MINEFIELD AND AQUIRED THE TRESSURECHEST' + '\n')
            nextstep()
        else:
           print('\n' + 'WRONG! THE MINEFIELD DETINATED, YOU DIED' + '\n')
           restart() 
    elif (randomNumber == 3):
        entry = input('\n' + 'IT IS TALL WHEN ITs YOUNG,AND SHORT WHEN IT IS OLD WHAT IS IT? > ')
        if (entry.lower() == 'candle'):
            print('\n' + 'CORRECT YOU HAVE DEACTIVATED THE MINEFIELD AND AQUIRED THE TRESSURECHEST' + '\n')
            nextstep()
        else:
            print('\n' + 'WRONG! THE MINEFIELD DETINATED, YOU DIED' + '\n')
            restart() 
    elif (randomNumber == 4):
        entry = input('\n' + 'WHAT HAS MANY KEYS BUT CAN NOT OPEN A SINGLE LOCK? > ')
        if (entry.lower() == 'piano'):
            print('\n' + 'CORRECT YOU HAVE DEACTIVATED THE MINEFIELD AND AQUIRED THE TRESSURECHEST' + '\n')
            nextstep()
        else:
            print('\n' + 'WRONG! THE MINEFIELD DETINATED, YOU DIED' + '\n')
            restart() 
    elif(randomNumber == 5):
            entry = input('\n' + 'WHAT HAS A HEAD,A TAIL AND HAS NO LEGS AND DOES NOT BREATH? > ')
            if (entry.lower() == 'coin'):
                print('\n' + 'CORRECT YOU HAVE DEACTIVATED THE MINEFIELD AND AQUIRED THE TRESSURECHEST' + '\n')
                nextstep()
    else:
        print('\n' + 'WRONG! THE MINEFIELD DETINATED, YOU DIED' + '\n')
        restart()

########################################################################################################################################## 
def nextstep():
    print('\n' + 'THE MINEFIELD WILL DETINATED AUTOMATICALLY IN A FEW MOMENTS AFTER THE TRESSURECHEST HAS BEEN MOVED ' + question[0] + '\n')
    entry = input('\n' + 'CONITINUE DIRECTION OR CALM DOWN ? >')
    if (entry.lower() == 'calm down'):
        print('\n' + 'YOU TOOK LONG TO LEAVE THE MINEFIELD DETINATED, YOU DIED' + '\n')
        restart()
    elif (entry.lower() == 'continue direction'):
        print('\n' + 'CONGRADULATIONS YOU HAVE AQUIRE THE TRESSURECHEST SURVIVED THIS STAGE' + '\n')
        ending()
    else:
      print('\n' + 'Invalid Input' + '\n')
      nextstep()

############################################################################################################################################
def tresDirec():
    print('\n' + 'YOU WILL NEVER KNOW WHAT WAS IN THE BOX' + '\n')
    entry = input('RETURN OR CONTINUE DIRECTION ? > ')
    if (entry.lower() == 'return'):
        tressurechest()
    elif(entry.lower() == 'continue direction'):
        ending()
    else:
        print('\n' + 'Invalid Input' + '\n')
        tresDirec()

#####################################################################################################################################
def bearLaydown():
    print('\n' + 'THE BEAR THOUGHT YOU WERE DIED AND LEFT' + question[0] + '\n')
    entry = input('CONTINUE DIRECTION OR CHANGE DIRECTION? > ')
    if(entry.lower() == 'continue direction') or (entry.lower() =='change direction'):
        Tworoutes()
    else:
        print('\n' + 'Invalid Input' + '\n')
        bearLaydown()

#######################################################################################################################################
def riverchoice():
    print('YOU ARE NOW IN THE RIVER' + question[0]+ '\n' )
    entry = input('SWIM OR FLOW? > ')
    if(entry.lower() == 'swim'):
        randomNumber = random.randint(1,9)
        if ((randomNumber % 2) == 0 ):
           print('\n' + 'YOU HIT A ROCK WITH YOUR HEAD, YOU HAVE DIED' +'\n')
           restart()
        elif ((randomNumber % 3) == 0) and (randomNumber !=6):
            print('\n' + 'YOU COULD NOT HANDLE THE FLOW OF THE WATER, YOU DROWNED AND DIED' +'\n')
            restart()
        elif ((randomNumber % 2) != 0) and ((randomNumber % 3) != 0):
            print('\n' + 'LUCKLY YOU MANAGED TO MAKE IT OUT OF THE RIVER' +'\n')
            choice()
    elif(entry.lower() == 'flow'):
        print('\n' + 'YOU COULD NOT HANDLE THE FLOW OF THE WATER, YOU DROWNED AND DIED' +'\n')
        restart()
    else:
        print('\n' + 'Invalid Input' + '\n')
        riverchoice()

#######################################################################################################################################################    
def longerroute():
    print('\n' + 'THIS ROUTE LEADS YOU INTO A STRIGHT TUNNEL' + '\n')   
    print('\n' + 'HALFWAY THROUGH THE WIND BLOWS STRONG AND YOU HEAR THE ROCKS ABOVE YOU SHAKING' + question[0] + '\n')  
    entry = input('PROCEED OR GO BACK? > ')
    if (entry.lower() == 'proceed'):
       rockslide()
    elif (entry.lower() == 'go back'):
       print('\n' + 'YOU ARE NOW BACK AT THE TWO DIFFENT ROUTES' + '\n')
       Tworoutes()
    else:
       print('\n' + 'INVAlid INPUT' + '\n')
       longerroute()
##########################################################################################################################################################
def rockslide():
    print('\n' + 'YOU HEAR A ROCKSLIDE APPROACHING BEHIND YOU' + question[0] + '\n')
    entry = input('\n' + 'RUN OR IGNORE THE ROCKSLIDE ? >')
    if (entry.lower() == 'run'):
       randomNumber = random.randint(1,5)
       if (randomNumber == 2):
           print('\n' + 'BECAUSE OF EXHAUSTION FROM THE WALKING THE ROCKSLIDE CAUGHT UP AND KILLED YOU ' + '\n')
           Tworoutes()
       else:
           print('\n' + 'YOU OUTRAN THE ROCKSLIDE AND HAVE NOW LOCATED THE TRESSURECHEST ' + '\n')
           tressurechest()
    elif (entry.lower() == 'ignore'):
       print('\n' + 'THE ROCKSLIDE CAUGHT UP AND KILLED YOU' + '\n')
       restart()
    else:
       print('\n' + 'INVAlid INPUT' + '\n')
       rockslide()

##########################################################################################################################################
def chestopinion():
    print('\n' + "THE CHEST IS EMPTY"  + question[0]  + '\n')
    entry=input('GO UPSTAIRS OR LOOK AROUND? > ')
    if entry.lower()=='go upstairs':
        chestup()
    elif(entry.lower()=='look around'):
            objects()
    else:
        print('\n' + 'Invalid Input' + '\n')
        chestopinion()

##########################################################################################################################################
def chestup():
    print('\n' + "YOU ARE UPSTAIRS IN THE HALLWAY AND CAN SEE THE DOOR GOING OUTSIDE"  + question[0]  + '\n')
    entry=input('GO DOWNSTAIRS OR GO OUTSIDE? > ') 
    if entry.lower() == 'go outside':
        outside()
    elif entry.lower() == 'go downstairs':
        downstairs()
    else:
        print('\n' + 'Invalid Input' + '\n')
        chestup()

###################################################################################################################################
def designers():
    print('\n' + 'THIS GAME WAS DESIGNED BY:' + '\n')
    print('ABDULLAH MAYET' + '\n')
    print('BULELA MDINGI' + '\n')
    print('ISAIAH MUHUMUZA' + '\n')
    print('BONGA CHILOANE' + '\n')
    print('UNDER JBS GRITLAD BOOTCAMP' + '\n')
    print('GAME OVER' + '\n')
    exit()
########################################################################################################################################
start()
#####################################################################################################################################################################################################