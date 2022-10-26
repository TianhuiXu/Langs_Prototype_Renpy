# all gaming scripts

# define the characters in the game
define v = Character("大妈", color="#c8ffc8")
define m = Character("你", color="#c8c8ff")
define c = Character("Cultural Tips", color="#ffc8c8")
define h = Character("Hint", color="#ffc1c1")
default money = 30
default pomelo = 1
default peach = 5

# label - give a name to a place in the game
# when users click start game



label start:
    # defines the background
    scene bg market
    show opening:
        zoom 1.2
        yzoom 1.15
    "Continue"
    hide opening
    show task1:
        zoom 1.3
        yzoom 1.2
    "Continue"
    hide task1
    show task2:
        zoom 1.3
        yzoom 1.2
    "Continue"
    hide task2
    show task3:
        zoom 1.3
        yzoom 1.2
    "Continue"
    hide task3
    show task4:
        zoom 1.3
        yzoom 1.2
    "Continue"
    hide task4
    show task5:
        zoom 1.3
        yzoom 1.2
    "Continue"
    hide task5
    # defines the character and display on top of background
    show vendor happy at left
    show screen task_reminder
    call screen fruits
    #show pomelo at Position(xpos = 0.7, xanchor=0.5, ypos=0.5,
 #yanchor=0.5)

    screen fruits:
        imagebutton:
            xpos 0.6
            xanchor 0.5
            ypos 0.5
            yanchor 0.5
            idle im.FactorScale("pomelo.png", 0.7)
            # to be replaced with hovered image
            # hover "pomelo_hover.png"
            hovered Show("displayTextPomelo", displayText = "柚子 Pomelo")
            unhovered Hide("displayTextPomelo")
            action [Hide("displayTextPomelo"), Jump("choice_A")]

        imagebutton:
            xpos 0.8
            xanchor 0.5
            ypos 0.5
            yanchor 0.5
            idle im.FactorScale("peach.png", 0.7)
            # to be replaced with hovered image
            # hover "pomelo_hover.png"
            hovered Show("displayTextPeach", displayText = "水蜜桃 Peach")
            unhovered Hide("displayTextPeach")
            action [Hide("displayTextPeach"), Jump("choice_B1")]

    
    screen displayTextPomelo:
        default displayText = ""
        vbox:
            xalign 0.6
            yalign 0.7
            frame:
                text displayText

    screen displayTextPeach:
        default displayText = ""
        vbox:
            xalign 0.8
            yalign 0.7
            frame:
                text displayText

    screen task_reminder:
        text "Your task: "
        text "柚子 Pomelo * [pomelo] & 水蜜桃 Peach * [peach]":
            ypos 0.05
        text "Your money: [money]元":
            ypos 0.1

    screen choice_A:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.2
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/一斤多少钱啊.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.29
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/一斤柚子多少钱啊.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.38
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/好呀.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.47
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/来个.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.56
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要.mp3")]
        

    label choice_A:
        # start dialogue
        play sound "audio/Vendor/来来来，刚到的柚子，小姑娘，要不要来个.mp3"
        v "来来来，刚到的柚子，小伙子/小姑娘，要不要来个？"
        stop sound

        show screen choice_A
        
        # create menu of choice responses
        menu:
            "一斤多少钱啊？":
                hide screen choice_A
                jump tip_A1
            
            "一斤柚子多少钱啊？":
                hide screen choice_A
                jump tip_A1

            "好呀":
                hide screen choice_A
                jump choice_A3
            
            "来个":
                hide screen choice_A
                jump choice_A3

            "要":
                hide screen choice_A
                jump choice_A3


    label h_1:
        h "You can walk away and explore other stalls."
        if money > 0 and pomelo <= 0 and peach <= 0:
            "You've completed the task!"
        else:
            "Try and bargain harder to get all the fruits :)"
        return 


    label tip_A1:
        c "In China, we usually use '斤' as the unit of measurement in wet markets, which is 500 grams. 
        One kilogram(一公斤) is 两斤(two '斤')."

        jump choice_A2

    label tip_A2:
        c "In daily conversations, we usually use '块' rather than '元' as the currency unit. E.g. 
        we would say '两块五' rather than '两元五毛'"

        show screen tip_A2

        menu:
            "有点贵，便宜点呗":
                hide screen tip_A2
                jump choice_A6

            "来一个":
                hide screen tip_A2
                jump choice_A7

    screen tip_A2:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/有点贵，便宜点呗.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.42
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/来一个.mp3")]
    
    label tip_A3:
        c "When vendors say how good their fruits are, don't always trust them. 
        Even though they cut a fruit and show you (which they often do to convince buyers), 
        do not always trust them without questioning. "


        show screen tip_A3

        menu:
            "别的地方只要两块钱一斤":
                hide screen tip_A3
                jump choice_A8

            "那拿一个吧":
                hide screen tip_A3
                jump choice_A7

    screen tip_A3:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/别的地方只要两块钱一斤.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.42
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/那拿一个吧.mp3")]

    label tip_A4:
        c "Some vendors might weigh the fruits more to take advantage of you. 
        It is not uncommon that vendors intentionally adjust the weighting machines to always let it weigh more. 
        It is hard to avoid this so you should always try to bargain to lower the costs."

        "￥-10, 柚子+1"
        $ money -= 10
        $ pomelo -= 1

        jump choice_A11

    label tip_A5:
        c "Although there is price competition in the same market, vendors are usually friends, 
        especially with the ones nearby, some may even be relatives. So they will help each other in sales. "

        jump h_1

    label tip_B1:
        c "Some vendors are friendly like this 大妈, some are not.  To take advantage of foreigners, 
        some vendors might put in one or two bad ones when you are not noticing. When they choose the fruits for you, 
        always watch out for the quality. Or you can choose the fruits yourself."
        jump choice_B4

    label tip_B2:
        c "Sometimes vendors would propose to add in one or two more fruits to make it into an integer weight so that 
        they don't need to give you changes in '毛'(10 cents). If you don't want more, you can always reject. 
        But if you don't mind, you can accept and it's also easier for you to pay."
        
        show screen tip_B2

        menu:
            "好":
                hide screen tip_B2
                "￥-9, 水蜜桃+6"
                $ money -= 9
                $ peach -= 6
                jump h_1

            "不用了，就五个就行":
                hide screen tip_B2
                "￥-8.5, 水蜜桃+5"
                $ money -= 8.5
                $ peach -= 5
                jump h_1

    screen tip_B2:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/好.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.42
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/不用了，就五个就行.mp3")]
        

    label choice_A2:
        play sound "audio/Vendor/一斤柚子两块五.mp3"
        v "一斤柚子两块五。"
        stop sound
        
        jump tip_A2

    label choice_A3:
        play sound "audio/Vendor/要几个.mp3"
        v "要几个？"
        stop sound

        show screen choice_A3

        menu:
            "要一个":
                hide screen choice_A3
                jump choice_A2

            "要两斤":
                hide screen choice_A3
                h "We don't use '斤' in counting 柚子，we use '个'"
                jump choice_A3

            "不要柚子":
                hide screen choice_A3
                jump choice_A4

    screen choice_A3:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.29
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要一个.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.38
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要两斤.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.46
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/不要柚子.mp3")]

    label choice_A4:
        play sound "audio/Vendor/其他水果要不要.mp3"
        v "其他水果要不要？"
        stop sound

        show screen choice_A4

        menu:
            "要水蜜桃":
                hide screen choice_A4
                jump choice_B1

            "要甘蔗":
                hide screen choice_A4
                jump choice_A5

            "不要":
                hide screen choice_A4
                jump h_1

    screen choice_A4:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.29
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要水蜜桃.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.38
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要甘蔗.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.46
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/不要.mp3")]

    label choice_A5:
        jump tip_A5



    label choice_A6:
        play sound "audio/Vendor/我这里柚子水分足，好吃，比别的地方的好.mp3"
        v "我这里柚子水分足，好吃，比别的地方的好"
        stop sound

        jump tip_A3

    label choice_A7:
        play sound "audio/Vendor/差不多两公斤，十块钱.mp3"
        v "差不多两公斤，十块钱"
        stop sound

        jump tip_A4
    
    label choice_A8:
        play sound "audio/Vendor/你再买一个吧，算你两块钱一斤.mp3"
        v "你再买一个吧，算你两块钱一斤"
        stop sound

        show screen choice_A8

        menu:
            "我买两个吃不掉呀，一个就够了":
                hide screen choice_A8
                jump choice_A9
            
            "行，那拿两个吧":
                hide screen choice_A8
                jump choice_A10

    screen choice_A8:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/我买两个吃不掉呀，一个就够了.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.42
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/行，那拿两个吧.mp3")]

    label choice_A9:
        play sound "audio/Vendor/行吧，一共两公斤，八块.mp3"
        v "行吧，一共两公斤，八块"
        stop sound

        "￥-8, 柚子+1"
        $ money -= 8
        $ pomelo -= 1

        jump choice_A11

    label choice_A10:
        play sound "audio/Vendor/四公斤，十六块钱.mp3"
        v "四公斤，十六块钱"
        stop sound

        "￥-16, 柚子+2"
        $ money -= 16
        $ pomelo -= 2

        jump choice_A11

    label choice_A11:
        play sound "audio/Vendor/还要什么其他的吗.mp3"
        v "还要什么其他的吗？"
        stop sound
        
        show screen choice_A11

        menu:
            "不用了":
                hide screen choice_A11
                jump h_1
                # where does this lead to?

            "水蜜桃有吗？":
                hide screen choice_A11
                jump choice_B1

            "还要一个甘蔗":
                hide screen choice_A11
                jump choice_A5

    screen choice_A11:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.29
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/不用了.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.38
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/水蜜桃有吗.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.46
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/还要一个甘蔗.mp3")]

    label choice_B1:
        play sound "audio/Vendor/小姑娘，要买水蜜桃吗.mp3"
        v "小姑娘，要买水蜜桃吗？"
        stop sound

        show screen choice_B1

        menu:
            "水蜜桃多少钱一斤？":
                hide screen choice_B1
                jump choice_B2
            
            "要五个":
                hide screen choice_B1
                jump choice_B3

    screen choice_B1:
        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/水蜜桃多少钱一斤.mp3")]

        imagebutton:
            xpos 0.85
            xanchor 0.5
            ypos 0.42
            yanchor 0.5
            idle im.FactorScale("sound.png", 0.05)
            action [Play("sound", "audio/User/要五个.mp3")]

    label choice_B2:
        play sound "audio/Vendor/四块五一斤.mp3"
        v "四块五一斤"
        stop sound
        play sound "audio/User/要五个.mp3"
        m "要五个"
        stop sound
        jump choice_B3

    label choice_B3:
        play sound "audio/Vendor/我给你挑哈.mp3"
        v "我给你挑哈"
        stop sound
        jump tip_B1

    label choice_B4:
        play sound "audio/Vendor/差一点到两斤，再给你拿一个到两斤呗.mp3"
        v "差一点到两斤，再给你拿一个到两斤呗"
        stop sound
        jump tip_B2


    return
