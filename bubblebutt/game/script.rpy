# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MC")
define c = Character("NPC")
define h = Character("Hot Guy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "I was born with a thicc juicy butt."

    m "I don't understand why people make fun of me."

    m "I can't help I was born so fine!!!!"

    c "You're one to talk! How can you walk around looking like that?"

    menu:
        "Accept the insult":
            jump accept

        "Fight back":
            jump fight
    
    label fight:
        "I clench my fists."

        m "I can't help that I was born this way!"

        c "Geez, don't be so sensitive."

        "It's always this way. It's so frustrating. What am I supposed to do?"

        h "Hey. The way you stood up for yourself is really cool. I respect that."

        m "Thanks..."

        h "Wanna go out for coffee sometime?"

        m "...yeah!"

        "GOOD END"

        jump end

    label accept:
        "Even though I can't help it...even though it stings..."

        "I can't fight back."

        m "Whatever..."

        c "Yeah, that's right!"

        "Man, this sucks. I don't want to be like this anymore."

        "In the end, I never did find acceptance. People were still mean to me."

        "BAD END"

        jump end

    # This ends the game.
    label end:

    return
