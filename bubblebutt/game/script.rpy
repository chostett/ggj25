# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[realName]")
define b = Character("BubbleButt")
define l = Character("Bubleigh")

# Declaring scene names.

image bedroom cutscene = "cutscene_bedroom_good.png"
image bedroom good = "bedroom_good.png"


# The game starts here.

label start:
    $ goodEnd = 0
    $ badEnd = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom cutscene

    # These display lines of dialogue.

    "I was born with a thicc juicy butt."

    "I don't understand why people make fun of me."

    python:
        realName = renpy.input("What's my name again?", length=25)
        realName = realName.strip()

        if not realName:
            realName = "Naoto"

    m "Oh yeah...[realName]. I haven't heard that name in ages."

    b "Most people call me BubbleButt."

    scene bedroom good

    "Choice 1..."

    menu:
        "Yes":
            $ goodEnd += 1
            jump good1

        "No":
            $ badEnd += 1
            jump bad1
    
    label good1:
        b "I think I made a good choice."

        b "Now onto choice two..."

        jump choice2

    label bad1:
        b "I think I made a bad choice."

        b "Now onto choice two..."

        jump choice2
    
    label choice2:
        "Choice 2..."

    menu:
        "Yes":
            $ goodEnd += 1
            jump good2
        
        "No":
            $ badEnd += 1
            jump bad2
    
    label good2:
        b "I think I made a good choice."

        b "Now onto choice three..."

        jump choice3

    label bad2:
        b "I think I made a bad choice."

        b "Now onto choice three..."

        jump choice3
    
    label choice3:
        "Choice 3..."

    menu: 
        "Yes":
            $ goodEnd += 1
            jump good3

        "No":
            $ badEnd += 1
            jump bad3
    
    label good3:
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
