# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[realName]")
define b = Character("BubbleButt")
define l = Character("Bubleigh")
define a = Character("Bubblina")
define o = Character("Elderly Woman")
define s = Character("Agent")
define p1 = Character("Random Person 1")
define p2 = Character("Random Person 2")


# Declaring scene names.

image bedroom cutscene = "cutscene_bedroom_good.png"
image bedroom good = "bedroom_good.png"
image street1 = "street_1.png"
image street2 = "street_2.png"

# Declaring sprite names.

image bubble flat = "BB_FlatNeutral.png"
image bubble neutral = "BB_Neutral.png"
image bubble bored = "BB_Bored.png"

init:
# Sprite Positions
    define center = Position(xalign=0.5)
    define left = Position(xalign=0.2)
    define right = Position(xalign=0.8)
    define centerleft = Position(xalign=0.4)


# The game starts here.

label start:
    $ goodEnd = 0
    $ badEnd = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/neutral.mp3" volume 0.4

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

    play sound "audio/b_ooh.ogg" volume 1.0

    m "Look at her, I wish I was with her. My life would be so much better, more well-rounded you know?"

    scene bedroom good

    show bubble flat at left

    play sound "audio/a_happy.ogg" volume 1.0

    a "Did I hear someone say {i}well-rounded?{/i} I can make that happen you know."

    play sound "audio/b_what.ogg" volume 1.0

    m "Whaaaaaaa?! Who are you? What are you? Why are you here?"

    a "My name is Bubbleina. I've been sent here to give you that well-rounded life you seek..."

    m "Did... did you hear my wishes? Can you really help me out?"

    # show Bubbleina mischievous

    play sound "audio/a_happy.ogg" volume 1.0

    a "Bubblenia Of course I can! All it takes is a wave of my wand and a..."

    a "Few"

    a "{i}magic{/i}"

    a "words..."

    m "Then do it! Give me the well-rounded life I crave!"

    # show Bubbleina mischievous

    a "...mumble mumble big mumble mumble butt mumble mumble..."

    hide bubble flat

    show bubble neutral at left

    m "Something feels bigger...more cushiony...wait...it's my butt!"

    play sound "audio/b_what.ogg" volume 1.0
    
    m "It's huge! What did you do to it?!"

    # show Bubbleina mischievous

    play sound "audio/a_evil.ogg" volume 1.0

    a "I'm sorry, is this not what you asked for? You wanted a well-rounded life and I gave it to you!"
    
    a "...in curse form!"

    # show BB surprised

    m "But how am I supposed to do that with this giant butt?!"

    # show Bubbleina happy

    a "That's up to you to find out!"

    play sound "audio/a_evil.ogg" volume 1.0
    
    a "By the way, you have 24 hours to figure this out or that big bouncy bubble butt of yours stays with you forever soooooooo good luck!"

    a "...[realName],"

    a "Or should I say..."

    a "BubbleButt!"

    play sound "audio/b_no.ogg" volume 1.0

    b "Nooooooooooo!"

    scene street1
    show bubble bored at left

    b "I'm so glad I had my stretchy pants."
    
    b "Now to get out and figure out how to stop this stupid curse and shrink my stupid butt back back down to normal."

    # show BB determined

    play sound "audio/b_sigh.ogg" volume 1.0

    b "Ok, just act normal. You don't have a giant dumpy attached to you. Just keep walking everything is cool."

    # show Illustration 1

    play sound "audio/OMG.ogg" volume 2.0

    p1 "Oh my god, look at their butt!"

    play sound "audio/Cake.ogg" volume 2.0

    p2 "Are you a bakery? Cuz that's some serious cake son!"

    # show BB sad/defeated

    b "Oh my god they're all looking at me. I can't hide this thing!"

    play sound "audio/MeanLaugh.ogg" volume 2.0
    
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
        # show BB determined 

        b "Wait why do I care?"
        
        b "I don't even know them, I'll probably never even see them again? I've got bigger things to worry about."

        # show BB happy

        play sound "audio/b_haha.ogg" volume 1.0

        b "Yeah that's right, it's my butt and its a big one!"
        
        b "Keep laughing, take pics! Don't forget to tag me though!"

        jump choice2

    label bad1:
        # show BB sad

        b "They think i'm a freak! A big caked up bootylicious freak."

        play sound "audio/b_sigh.ogg" volume 1.0
        
        b "I can't do this. I can't go outside again. I need to go back."
        
        b "I can never show my cheeks again. I'm going home!"

        jump choice2
    
    label choice2:
        scene street2
        show bubble neutral at left

        "On their way down the street, our bootylicious protagonist stops to think."

        play sound "audio/b_hm.ogg" volume 1.0

        b "Well-rounded life... well-rounded. I mean I got that but how can I make my life fulfilled in 24 hours?"
        
        b "This sucks, this is booty cheeks... literally."

        # scene illustration 2
        #show BB surprised

        "And what a sight! A nearsighted elderly woman, crossing the street..."
        
        "But that car is speeding right through that signal!"

        play sound "audio/b_what.ogg" volume 1.0

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
        # show BB determined
        b "Stop the carrrrrrrr!!!!! Work butt work!"

        o "Young man...lady...sir. Thank you!"
        
        o "You saved me. You and your... big butt."

        play sound "audio/Hero.ogg" volume 2.5

        p1 "That young person's butt saved that woman. They're a true hero!"

        play sound "audio/VOD.ogg" volume 2.0

        p2 "Yo, who's got the VOD?"

        jump choice3

    label bad2:
        play sound "audio/b_no.ogg" volume 1.0

        b "I can't do it!"
        
        b "I'm sorry!! Someone else help her please!"

        p1 "The car stopped thank god."
        
        p2 "You were {i}right{/i} there. What the heck?"

        o "Thanks for nothing! Especially you Cheeks McGee!"

        play sound "audio/b_sigh.ogg" volume 1.0

        b "I'm so useless..."

        jump choice3
    
    label choice3:
        # scene city street 3

        # show BB neutral

        "Even after all that, our protagonist is starting to panic."

        b "I'm running out of time! I need to figure out how to break the curse."

        play sound "audio/b_sigh.ogg" volume 1.0
        
        b "I take back everything I said! I just want things to be normal again!"

        b "I wanna be [realName] again!"

        # show Illustration 3

        "A black car pulls up. BubbleButt is surprised when two men dressed in black suits approach them. They look serious."

        s "Are you the citizen with the butt? The big one."

        # show BB surprised

        play sound "audio/b_hm.ogg" volume 1.0

        b "I uh, I guess that's me. Unless there's a bigger butt around here but I doubt that..."

        b "Word gets around fast huh..."

        s "Was that supposed to be a joke?"

        b "..."

        s "We need your help, its a matter of national security."

        b "Are you kidding me? How could someone like me help you out?"

    menu: 
        "Stop the assteroid and save the world":
            $ goodEnd += 1
            jump good3

        "On second thought...":
            $ badEnd += 1
            jump bad3
    
    label good3:
        play sound "audio/b_ooh.ogg" volume 1.0

        b "I think I made a good choice."

        b "Now onto the final result..."

        jump final
    
    label bad3:
        b "I think I made a bad choice."

        b "Now onto the final result..."

        jump final
    
    label final:
        "It's time for the final result."

        if goodEnd > badEnd:
            "You got the good end."

            b "Do I keep the butt or no?"

            menu:
                "Keep the butt":
                    b "I'm happy with how I am."
                    jump keepButt

                "Return the butt":
                    b "I think I'd be happier without it."
                    jump returnButt
        else:
            "You got the bad end."
            jump theBadEnd
    
    label keepButt:
        "I kept my butt. I'm happy with the way I am."
        
        "Good End - Keep"

        jump end
    
    label returnButt:
        "I returned my butt. I'm happier without it."

        "Good End - Return"

        jump end
    
    label theBadEnd:
        "Man, this ending sucks."

    # This ends the game.
    label end:

    return
