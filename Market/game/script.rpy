# all gaming scripts

# define the characters in the game
define v = Character("大妈", color="#c8ffc8")
define m = Character("你", color="#c8c8ff")
define c = Character("Cultural Tips", color="#ffc8c8")
define h = Character("Hint", color="#ffc1c1")

# label - give a name to a place in the game
# when users click start game
label start:
    # defines the background
    scene bg market
    
    # defines the character and display on top of background
    show vendor happy at left
    call screen fruits
    #show pomelo at Position(xpos = 0.7, xanchor=0.5, ypos=0.5,
 #yanchor=0.5)

    screen fruits:
        imagebutton:
            xpos 0.7
            xanchor 0.5
            ypos 0.5
            yanchor 0.5
            idle im.FactorScale("pomelo.png", 0.7)
            # to be replaced with hovered image
            # hover "pomelo_hover.png"
            hovered Show("displayTextPomelo", displayText = "柚子 Pomelo")
            unhovered Hide("displayTextPomelo")
            action [Hide("displayTextPomelo"), Jump("choice_A")]

    
    screen displayTextPomelo:
        default displayText = ""
        vbox:
            xalign 0.7
            yalign 0.7
            frame:
                text displayText

    label choice_A:
        # start dialogue
        v "来来来，刚到的柚子，小伙子/小姑娘，要不要来个？"
        # create menu of choice responses
        menu:

            "一斤多少钱啊？":
                jump tip_A1

            "柚子多少钱啊？":
                jump tip_A1
            
            "一斤柚子多少钱啊？":
                jump tip_A1

            "好呀":
                jump choice_A3
            
            "来个":
                jump choice_A3

            "要":
                jump choice_A3

    label h_1:
        h "You can walk away and explore other stalls."


    label tip_A1:
        c "In China, we usually use '斤' as the unit of measurement in wet markets, which is 500 grams. 
        One kilogram(一公斤) is 两斤(two '斤')."

        jump choice_A2

    label tip_A2:
        c "In daily conversations, we usually use '块' rather than '元' as the currency unit. E.g. 
        we would say '两块五' rather than '两元五毛'"

        menu:
            "有点贵，便宜点呗":
                jump choice_A6

            "来一个":
                jump choice_A7
    
    label tip_A3:
        c "When vendors say how good their fruits are, don't always trust them. 
        Even though they cut a fruit and show you (which they often do to convince buyers), 
        do not always trust them without questioning. "

        menu:
            "别的地方只要两块钱一斤":
                jump choice_A8

            "那拿一个吧":
                jump choice_A7

    label tip_A4:
        c "Some vendors might weigh the fruits more to take advantage of you. 
        It is not uncommon that vendors intentionally adjust the weighting machines to always let it weigh more. 
        It is hard to avoid this so you should always try to bargain to lower the costs."

        "￥-10, 柚子+1"

        jump choice_A11

    label tip_B1:
        c "Although there is price competition in the same market, vendors are usually friends, 
        especially with the ones nearby, some may even be relatives. So they will help each other in sales. "

        jump h_1

    label choice_A2:

        v "一斤柚子两块五。"
        jump tip_A2

    label choice_A3:
        v "要几个？"

        menu:
            "要一个":
                jump choice_A2

            "要两斤":
                h "We don't use '斤' in counting 柚子，we use '个'"
                jump choice_A3

            "不要柚子":
                jump choice_A4

    label choice_A4:
        v "其它水果要不要？"

        menu:
            "要水蜜桃":
                jump choice_B1

            "要甘蔗":
                jump choice_A5

            "不要":
                jump h_1

    label choice_A5:
        jump tip_B1



    label choice_A6:
        v "我这里柚子水分足，好吃，比别的地方的好"

        jump tip_A3

    label choice_A7:
        v "差不多两公斤，十块钱"

        jump tip_A4
    
    label choice_A8:
        v "你再买一个吧，算你两块钱一斤"

        menu:
            "我买两个吃不掉呀，一个就够了":
                jump choice_A9
            
            "行，那拿两个吧":
                jump choice_A10

    label choice_A9:
        v "行吧，一共两公斤，八块"

        "￥-8, 柚子+1"

        jump choice_A9

    label choice_A10:
        v "四公斤，十六块钱"

        "￥-16, 柚子+2"

        jump choice_A11

    label choice_A11:
        v "还要什么其它的吗？"

        menu:
            "不用了":
                jump h_1
                # where does this lead to?

            "水蜜桃有吗？":
                jump choice_B1

            "还要一个甘蔗":
                jump choice_A5


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
