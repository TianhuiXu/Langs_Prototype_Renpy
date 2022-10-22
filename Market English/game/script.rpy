# all gaming scripts

#init python:
#    style.default.font = "YRDZST Medium.ttf"
#    style.default.language = "eastasian"

translate chinese style default:
    font "YRDZST Medium.ttf"

# define the characters in the game
define v = Character("大妈", color="#c8ffc8")
define m = Character("你", color="#c8c8ff")

# label - give a name to a place in the game
# when users click start game
label start:
    # defines the background
    scene bg market
    
    # defines the character and display on top of background
    show vendor happy at left
    image pomelo = im.FactorScale("pomelo.png", 0.7)
    show pomelo at Position(xpos = 0.7, xanchor=0.5, ypos=0.5,
 yanchor=0.5)

    # start dialogue
    v "来来来，刚到的柚子，小伙子/小姑娘，要不要来个？"

    # 
    menu:

        "一斤多少钱啊？":
            jump choiceB_1

        "柚子多少钱啊？":
            jump choiceB_1
        
        "一斤柚子多少钱啊？":
            jump choiceB_1

        "好呀":
            jump choiceB_1
        
        "来（要）":
            jump choiceB_1

        "walk away":
            jump choiceB_2

    label choiceB_1:

        v "一斤柚子两块五。"

        jump choice2

    label choice1_2:

        # ... the game continues here.
    
    label choice2:
        menu:
            "有点儿贵，便宜一点儿，行吗?":
                jump choice2_1

            "好的，来两斤":
                jump choice2_2

    label choice2_1:
        v "很新鲜的，不贵"

    label choice2_2:
        v "好嘞"


    # 此处为游戏结尾。

    return
