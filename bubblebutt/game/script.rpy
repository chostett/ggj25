# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[realName]")
define b = Character("BubbleButt")
define l = Character("Bubleigh", who_color="#e44519")
define a = Character("Bubbleina", who_color="#9010eb")
define o = Character("Elderly Woman", who_color="#4d485f")
define s = Character("Agent", who_color="#139d4d")
define p1 = Character("Random Person 1", who_color="#4d485f")
define p2 = Character("Random Person 2", who_color="#4d485f")
define p = Character("President", who_color="#147ceb")
define sc = Character("Important Scientist", who_color="#4d485f")


# Declaring scene names.

image bedroom cutscene = "cutscene_bedroom_good.png"
image instagram = "instagram.png"
image bedroom cutscene bad = "cutscene_bedroom_bad.png"
image street cutscene 1 = "cutscene_street_1.png"
image street cutscene 2 = "cutscene_street_2.png"
image asteroid 1 = "cutscene_asteroid_1.png"
image asteroid 2 = "cutscene_asteroid_2.png"
image asteroid 3 = "cutscene_asteroid_3.png"
image asteroid bad = "cutscene_asteroid_bad.png"

# Declaring backgrounds.

image bedroom good = "bedroom.png"
image bedroom bad = "bedroom_bad.png"
image street1 = "street_1.png"
image street2 = "street_2.png"
image street3 = "street_3.png"

# Declaring ending screens. Good end, keep butt. Good end, return butt. Bad end + universal ending screen.

image bedroom cutscene bad = "cutscene_bedroom_bad.png"
image keep butt = "cutscene_keep_good.png"
image nokeep butt = "cutscene_return_good.png"
image bad end 1 = "cutscene_badend_1.png"
image bad end 2 = "cutscene_badend_2.png"
image endscreen = "EndScreen.png"

# Declaring sprite names.

image bubble flat = "BB_FlatNeutral.png"
image bubble flat determined = "BB_FlatDetermined.png"
image bubble flat surprised = "BB_FlatSurprised.png"
image bubble neutral = "BB_Neutral.png"
image bubble bored = "BB_Bored.png"
image bubble determined = "BB_Determined.png"
image bubble happy = "BB_Happy.png"
image bubble noo = "BB_Noo.png"
image bubble runaway = "BB_RunAway.png"
image bubble sad = "BB_Sad.png"
image bubble surprised = "BB_Surprised.png"
image fairy neutral = "Bubbleina_Neutral.png"
image fairy happy = "Bubbleina_Happy.png"
image fairy mis = "Bubbleina_Mischievous.png"
image leigh = "Bubbleigh_Neutral.png"
image agents = "Agents_Neutral.png"

# Define audio for ease of calling later. A = Bubbleina, B = BubbleButt/Player, l = Bubbleigh, p = Random People.

define audio.a_evil = "audio/a_evil.ogg"
define audio.a_happy = "audio/a_happy.ogg"
define audio.b_haha = "audio/b_haha.ogg"
define audio.b_hm = "audio/b_hm.ogg"
define audio.b_no = "audio/b_no.ogg"
define audio.b_ooh = "audio/b_ooh.ogg"
define audio.b_sigh = "audio/b_sigh.ogg"
define audio.b_what = "audio/b_what.ogg"
define audio.l_laugh = "audio/l_laugh.ogg"
define audio.l_ooh = "audio/l_ooh.ogg"
define audio.p_cake = "audio/Cake.ogg"
define audio.p_hero = "audio/Hero.ogg"
define audio.meanlaugh = "audio/MeanLaugh.ogg"
define audio.p_omg = "audio/OMG.ogg"
define audio.p_vod = "audio/VOD.ogg"
define audio.thankyou = "audio/thankyou_woman.ogg"

define audio.car = "audio/car.ogg"
define audio.crash = "audio/crash.ogg"
define audio.sparklesin = "audio/FairySparkles1.ogg"
define audio.sparklesout = "audio/FairySparkles2.ogg"

# Define songs - good end, bad end and neutral.
define audio.bad = "audio/bad.mp3"
define audio.good = "audio/good.mp3"
define audio.neutral = "audio/neutral.mp3"

init:
# Sprite Positions
    define center = Position(xalign=0.5)
    define left = Position(xalign=0.1)
    define right = Position(xalign=0.8)
    define upperRight = Position(xalign=0.8, yalign=0.2)
    define centerleft = Position(xalign=0.4)

# animation, shaking
    transform shaking:
        linear 0.1 xoffset -5 yoffset 5 
        linear 0.1 xoffset 6 yoffset -6 
        linear 0.1 xoffset 5 yoffset -5
        linear 0.1 xoffset -6 yoffset 6
        linear 0.1 xoffset 0 yoffset 0
        repeat

# animation, run away: increase linear for more time, increase the negeative number of the xalign is the sprite is still on the screen after the move
    transform offLeft:
        linear 3.0 xalign -0.10 


# The game starts here.

label start:
    $ goodEnd = 0
    $ badEnd = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/neutral.mp3" volume 0.3

    scene bedroom cutscene

    # These display lines of dialogue.

    "Our main protagonist: bored with life, filled with zero aspirations, and nothing to contribute endlessly scrolls through social media, looking at nothing in particular."

    "Maybe you, dear reader, know someone like this."

    python:
        realName = renpy.input("What is their name?", length=25)
        realName = realName.strip()

        if not realName:
            realName = "Naoto"

    m "Life is so.... boring and pointless! I wish I was literally something else, someone else."

    # show instagram scene

    scene instagram
    play sound b_ooh volume 1.2

    m "Look at her, I wish I was with her. My life would be so much better, more well-rounded you know?"

    scene bedroom good

    show bubble flat at left
    show fairy neutral at upperRight
    play sound sparklesin volume 1.0

    a "Did I hear someone say {i}well-rounded?{/i} I can make that happen you know."

    play sound b_what volume 1.2
    hide bubble flat
    show bubble flat surprised at left

    m "Whaaaaaaa?! Who are you? What are you? Why are you here?"

    hide bubble flat surprised
    show bubble flat at left
    hide fairy neutral
    show fairy happy at upperRight

    play sound a_happy volume 1.2

    a "My name is Bubbleina. I've been sent here to give you that well-rounded life you seek..."

    hide fairy happy
    show fairy neutral at upperRight

    m "Did... did you hear my wishes? Can you really help me out?"

    play sound a_happy volume 1.2

    hide fairy neutral
    show fairy happy at upperRight

    a "Of course I can! All it takes is a wave of my wand and a..."

    a "Few"

    hide bubble flat
    show bubble flat surprised at left

    a "{i}magic{/i}"

    a "words..."

    hide bubble flat surprised
    show bubble flat determined at left

    m "Then do it! Give me the well-rounded life I crave!"

    hide fairy happy
    show fairy mis at upperRight
    play sound sparklesout volume 1.0

    a "...mumble mumble big mumble mumble butt mumble mumble..."

    hide bubble flat
    hide fairy mis

    show bubble surprised at left
    show fairy happy at upperRight

    m "Something feels bigger...more cushiony...wait...it's my butt!"

    play sound b_what volume 1.2
    
    m "It's huge! What did you do to it?!"

    play sound a_evil volume 1.2
    
    hide fairy happy
    show fairy mis at upperRight

    hide bubble surprised
    show bubble sad at left

    a "I'm sorry, is this not what you asked for? You wanted a well-rounded life and I gave it to you!"
    
    a "...in curse form!"

    m "But how am I supposed to do that with this giant butt?!"

    # show Bubbleina happy
    hide fairy mis 
    show fairy happy at upperRight

    a "That's up to you to find out!"

    play sound a_evil volume 1.2
    
    a "By the way, you have 24 hours to figure this out or that big bouncy bubble butt of yours stays with you forever soooooooo good luck!"

    a "...[realName],"

    hide fairy happy 
    show fairy mis at upperRight

    a "Or should I say..."

    a "BubbleButt!"

    play sound b_no volume 1.2
    hide bubble sad 
    show bubble noo at left

    b "Nooooooooooo!"

    scene street1 with wiperight
    show bubble bored at left

    b "I'm so glad I had my stretchy pants."

    hide bubble bored
    show bubble sad at left
    
    b "Now to get out and figure out how to stop this stupid curse and shrink my stupid butt back back down to normal."

    hide bubble sad
    show bubble neutral at left

    play sound b_sigh volume 1.2

    b "Ok, just act normal. You don't have a giant dumpy attached to you. Just keep walking everything is cool."

    # show Illustration 1

    play sound p_omg volume 1.5
    hide bubble neutral
    show bubble surprised at left

    p1 "Oh my god, look at their butt!"

    play sound p_cake volume 1.5

    p2 "Are you a bakery? Cuz that's some serious cake son!"

    hide bubble surprised
    show bubble sad at left

    b "Oh my god they're all looking at me. I can't hide this thing!"

    play sound meanlaugh volume 1.5
    hide bubble sad
    show bubble runaway at left
    
    b "Everyone is so mean to me! What am I going to do?"

    # Choice 1...

    menu:
        "Blow them off":
            $ goodEnd += 1
            jump good1

        "Take their words to heart":
            $ badEnd += 1
            jump bad1
    
    label good1:
        hide bubble runaway
        show bubble determined at left 

        b "Wait why do I care?"
        
        b "I don't even know them, I'll probably never even see them again? I've got bigger things to worry about."
        
        hide bubble determined 
        show bubble happy at left

        play sound b_haha volume 1.2

        b "Yeah that's right, it's my butt and its a big one!"
        
        b "Keep laughing, take pics! Don't forget to tag me though!"

        jump choice2

    label bad1:
        hide bubble runaway
        show bubble sad at left

        b "They think i'm a freak! A big caked up bootylicious freak."

        play sound b_sigh volume 1.2
        hide bubble sad
        show bubble runaway at left
        
        b "I can't do this. I can't go outside again. I need to go back."
        
        b "I can never show my cheeks again. I'm going home!"

        show bubble runaway with moveoutleft

        jump choice2
    
    label choice2:
        scene street2 with wiperight
        show bubble neutral at left

        "On their way down the street, our bootylicious protagonist stops to think."

        play sound b_hm volume 1.2
        hide bubble neutral
        show bubble bored at left

        b "Well-rounded life... well-rounded. I mean I got that but how can I make my life fulfilled in 24 hours?"

        hide bubble bored
        show bubble sad at left
        
        b "This sucks, this is booty cheeks... literally."

        hide bubble sad
        show bubble neutral at left

        "And what a sight! A nearsighted elderly woman, crossing the street..."

        play sound car volume 1.0
        hide bubble neutral
        show bubble surprised at left
        
        "But that car is speeding right through that signal!"

        play sound b_what volume 1.2

        b "Hey lady what are you doing?! That car's not stopping!!! Oh god someone help!"

        p1 "Somebody save that poor woman!"

        # Choice 2...

    menu:
        "Stop it with your cheeks":
            $ goodEnd += 1
            jump good2
        
        "It's someone else's problem!":
            $ badEnd += 1
            jump bad2
    
    label good2:
        hide bubble surprised
        show street cutscene 1

        b "Stop the carrrrrrrr!!!!! Work butt work!"

        play sound crash volume 1.2
        hide street cutscene 1
        show street cutscene 2
        play sound thankyou volume 0.5

        o "Young man...lady...sir. Thank you!"
        
        o "You saved me. You and your... big butt."

        hide street cutscene 2
        show bubble happy at left
        play sound p_hero volume 2.5

        p1 "That young person's butt saved that woman. They're a true hero!"

        play sound p_vod volume 2.0

        p2 "Yo, who's got the VOD?"
        hide bubble happy

        jump choice3

    label bad2:
        hide bubble surprised
        show bubble noo at left
        play sound b_no volume 1.2

        b "I can't do it!"

        hide bubble noo
        show bubble runaway at left
        
        b "I'm sorry!! Someone else help her please!"

        p1 "The car stopped...thank god."

        
        p2 "You were {i}right{/i} there. What the heck?"

        o "Thanks for nothing! Especially you Cheeks McGee!"

        play sound b_sigh volume 1.2
        hide bubble runaway
        show bubble sad at left

        b "I'm so useless..."

        jump choice3
    
    label choice3:
        scene street3 with wiperight
        show bubble surprised at left

        "Even after all that, our protagonist is starting to panic."

        b "I'm running out of time! I need to figure out how to break the curse."

        play sound b_sigh volume 1.2
        hide bubble surprised 
        show bubble sad at left
        
        b "I take back everything I said! I just want things to be normal again!"

        b "I wanna be [realName] again!"

        hide bubble sad
        show bubble neutral at left

        "A black car pulls up. BubbleButt is surprised when two men dressed in black suits approach them. They look serious."

        show agents at right

        s "Are you the citizen with the butt? The big one."

        hide bubble neutral
        show bubble surprised at left

        play sound b_hm volume 1.2

        b "I uh, I guess that's me. Unless there's a bigger butt around here but I doubt that..."

        hide bubble surprised
        show bubble neutral at left

        s "We need your help, its a matter of national security."

        s "Your uh, buttocks can provide an effective defense against an incoming spaceborn threat."
        hide agents

        play sound b_what volume 1.2
        hide bubble neutral
        show bubble surprised at left

        b "My butt can...save people?"

        hide bubble surprised
        show bubble determined at left
        
        b "How? I know it's big and perfectly round and honestly looks pretty good on me, but how can that help out?"

        show agents at right
        hide bubble determined
        show bubble neutral at left

        p "Hello, good citizen."
        
        p "It's me, your dearly elected leader and I come before you on behalf of the entire nation."

        hide bubble neutral
        show bubble surprised at left

        p "You see, a giant asteroid is on a collision course with the planet Earth."

        hide bubble surprised
        show bubble bored at left
        
        p "Thanks to lots of super smart, tax-paid scientists, your rear is strong enough to withstand the force of this fast approaching assteroid."
        
        p "Will you help us? Will you help your country?"

        hide bubble bored
        show bubble determined at left

        play sound b_what volume 1.2

        b "My butt...is going to take on an ass...teroid?"

        play sound b_hm volume 1.2
        hide bubble determined
        show bubble sad at left
        
        b "Can I really save these people?"

        p "Have you looked at yourself?"

        hide bubble sad
        show bubble determined at left

        p "We're convinced that thing can take on a black hole. Are you ready to be the hero you were destined to be?"

    menu: 
        "Stop the assteroid and save the world":
            $ goodEnd += 1
            jump good3

        "On second thought...":
            $ badEnd += 1
            jump bad3
    
    label good3:
        hide bubble determined 
        show asteroid 1
        play sound b_haha volume 1.2

        b "Mr. President my butt is in position. I'm ready to take on the incoming assteroid."

        hide asteroid 1
        show asteroid 2

        p "God speed good citizen. The whole nation looks upon you and your patriotic posterior."

        hide asteroid 2
        show asteroid 3 at shaking
        play sound crash volume 1.2

        sc "We have impact!"
        
        sc "It's...a success!!"
        
        sc "The assteroid has made contact with both left and right cheeks and has been destroyed. We're saved!"

        hide asteroid 3
        show asteroid 3

        b "I..did it! I'm this nation's greatest hero! I'm a true government {i}ass{/i}et… hehehe “ass”."

        p "Indeed you are! Stand up, let the nation see you!"

        play sound b_sigh volume 1.2
        hide asteroid 3
        show bubble neutral at left

        b "Stand up...not for a while. Give me a minute..."

        hide agents
        hide bubble neutral

        jump final
    
    label bad3:
        hide bubble determined
        show bubble sad at left
        play sound b_sigh volume 1.2

        b "Mr. President I'm sorry, I'm so sorry. I just can't!"
        
        b "Me, my butt, I can't stop an entire asteroid—that's insane!"

        hide bubble sad
        show bubble runaway at left
        
        b "Ask the scientists to look again! I'm running my ass out of here!"

        hide bubble runaway

        scene asteroid bad

        sc "Mr. President, our defense appears to be running away?"
        
        sc "They're too dummy thicc, we hear what appears to be their cheeks clapping on the open mic."

        sc "Assteroid has made contact with our planet. Currently analyzing damage but it looks catastrophic."

        p "It appears the power of booty has let us and our nation down yet again. I bet I get blamed for this."

        jump final
    
    label final:

        scene bedroom good 

        show bubble neutral at left
            
        b "I'm so tired! My poor butt has butted into so many adventures today...but it's still there."

        hide bubble neutral 
        show bubble bored at left
        
        b "I guess I'm gonna be stuck with this thing forever. I gotta buy new jeans now."

        play sound sparklesin volume 1.0
        show fairy happy at upperRight
        hide bubble bored
        show bubble surprised at left

        a "Oh the problems of the one percent!"
        
        a "Life must be so hard having a perfectly shaped bubble butt. You're the real hero here."

        hide bubble surprised
        show bubble sad at left

        b "You! You turned my behind into a badonkadonk! I want my basic butt back!"

        hide fairy happy 
        show fairy mis at upperRight
        hide bubble sad
        show bubble bored at left

        a "Why do you think I'm here? To ogle my handiwork?"
        
        a "I mean I could but..."

        hide fairy mis
        show fairy happy at upperRight 

        a "No! I'm here to decide your fate."
        
        a "You've been through a lot and made some big choices that really surprised me. Are you ready to accept your destiny?"

        hide bubble bored 
        show bubble determined at left

        b "Can I just say before you judge that I..."

        a "Nope! Be quiet now!"
        hide fairy happy
        hide bubble determined

        if goodEnd > badEnd:
            stop music

            show fairy happy at upperRight
            show bubble happy at left
            play music good volume 0.4

            a "I'm very proud of you!"
            
            a "You truly discovered what it takes to live a happy and fulfilling life. You've carried that weight for long enough."

            play sound a_happy volume 1.2
            
            a "You are free of the curse! Go live a happy life!"

            a "Your name is now restored, [realName]. "

            hide bubble happy
            show bubble determined at left

            m "Thank you. I think I'll..."

            menu:
                "Keep the butt":
                    m "You know something? I was wondering if I could possibly, you know, maybe, just keep what I have?"
                    jump keepButt

                "Return the butt":
                    m "Yes yes please!"
                    jump returnButt
        else:
            scene bedroom bad
            stop music
            show fairy mis at upperRight
            show bubble sad at left
            play music bad volume 0.4
            
            a "You really didn't learn anything did you? I gave you 24 hours and you couldn't learn one simple lesson?"

            jump theBadEnd
    
    label keepButt:
        hide fairy happy
        show fairy mis at upperRight
        a "Wat?"
        
        hide bubble determined
        show bubble happy at left

        m "I feel like during my time with this bubble butt, I learned that accepting who I was was a big part of being happy and finding fulfillment in life."

        hide bubble happy
        show bubble determined at left
        
        m "I want the world to know that yes! This is who I am and that doesn't stop me from being happy!"

        hide bubble determined
        show bubble happy at left
        
        a "Well if that's what you truly want, sure! Enjoy! Less work for me."

        hide fairy mis
        scene keep butt
        
        a "Live your life to the fullest and don't forget to tag me on Insta!"

        m "Thank you Bubbleina! Thank you for showing me that life is truly booty-ful."
        
        m "I'll use this butt only for good I promise!"

        jump end
    
    label returnButt:
        hide fairy happy
        show fairy mis at upperRight
        hide bubble determined
        show bubble happy at left

        m "I'm ready to fit in chairs again! I WANT TO BE FREEEEEEEEEEEEEEE"

        play sound sparklesout volume 1.0

        a "mumble mumble disappear butt mumble mumble back to basics"

        a "Your big cursed bouncy behind is no more. Go forth and be happy."

        hide fairy mis
        show fairy happy at upperRight
        hide bubble happy
        show bubble flat surprised at left

        m "I'm going to go live my life! There's still time in the day."
        
        m "I need to take a walk with a new center of gravity again."

        scene street1 with wiperight
        show bubble flat at left
        show leigh at right

        play sound l_ooh volume 2.0

        l "Um excuse me, hi um, are you that hero the president is talking about on TV?"

        m "Depends on who is asking..."

        hide bubble flat
        show bubble flat surprised at left
        
        m "Wait are you?!"

        play sound l_laugh volume 2.0

        l "Yes! It is me, the one and only big booty influencer and number 2 MOBA streamer, Bubleigh_Boughtie."

        hide bubble flat surprised
        show bubble flat
        
        l "That's my real name."

        play sound b_what volume 1.5
        hide bubble flat
        show bubble flat determined

        m "Oh wow I can't believe it!"
        
        m "I've been watching your streams and liking your posts forever! You shouted me out once on your stream! I can't believe you're standing here!"

        l "Haha no the honor is mine!"

        play sound l_ooh volume 2.0
        hide bubble flat determined
        show bubble flat surprised
        
        l "I was wondering if you were free to go...on...a date with me?"
        
        l "I think you're really cool and want to get to know you better."

        play sound b_ooh volume 1.5
        scene nokeep butt

        m "I mean uh, well, guh, ooohh weee, if you'd like to, then sure!"

        m "I guess Bubbleina was right. Life is booty-ful. Butts are booty-ful."

        m "Here's to living life to the fullest!"

        jump end
    
    label theBadEnd:

        play sound a_evil volume 1.2
        
        a "You need more time to learn a true lesson. You are about to live in a world with your consequences."

        b "Wait what do you mean? I have time to change, just give me more time..."

        a "No! You and the world will learn from your lack of purpose."

        play sound a_evil volume 1.2
        
        a "I mean that 100 percent, 1,000 percent!"

        hide fairy mis
        scene bedroom cutscene bad

        b "The world has become dark."
        
        b "Demons have risen from the depths of hell and run amok. The space bound Arcadian Empire has claimed Earth as their new holy land and has declared war on the demons."
        
        b "Humanity has been cast aside and now fights for scraps. I could have been a hero...maybe, but now I never will."

        scene bad end 1

        b "Oh hey Bubbleigh is streaming! Sweet."

        play sound p_omg volume 2.0
        ## This is the very bad scene.

        p1 "Oh dear god, the acid demons are back!!"

        p2 "Get inside! The Arcadian de-molecular squads are here."

        scene bad end 2

        p1 "It's all because of that big ass kid. I'll never look at a butt ever again!"
        
        p2 "Ahhhhh my leg!!"

    # This ends the game.
    label end:

        scene endscreen

        "Thank you for playing our game! - Kyle, Ceren & CJ"

        "Made for Global Game Jam 2025 - Theme: Bubble"

    return
