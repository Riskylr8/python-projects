﻿print
Welcome to Lukis Castle!

print(r"""
                                   ]=I==II==I=[
                                    \\__||__//                 ]=I==II==I=[
               ]=I==II==I=[          |.. ` *|                   \\__||__//
                \\__||__//           |. /\ #|                    |-_ []#|
                 | []   |            |  ## *|                    |      |
                 |    ..|            | . , #|                  ]=I==II==I=[
 ___   ____  ___ |   .. |         __ |..__.*| __                \\__||__//
 ] I---I  I--I [ |..    |        |  ||_|  |_|| |                 |    _*|
 ]_____________[ | .. []|         \--\-|-|--/-//                 |   _ #|
  \_\| |_| |/_/  |_   _ | _   _   _|      ' *|                   |`    *|
   |  .     |'-'-` '-` '-` '-` '-` | []     #|-|--|-_-_-_-_ _ _ _|_'   #|
   |     '  |=-=-=-=-=-=-=-=-=-=-=-|      []*|-----________` ` `   ]   *|
   |  ` ` []|      _-_-_-_-_  '    |-       #|      ,    ' ```````['  _#|
   | '  `  '|   [] | | | | |  []`  |  []    *|   `          . `   |'  I*|
   |      - |    ` | | | | | `     | ;  '   #|     .  |        '  |    #|
  /_'_-_-___-\__,__|_|_|_|_|_______|   `  , *|    _______+___,__,-/._.._.\
              _,--'    __,-'      /,_,_v_Y_,_v\\-'   -""")

print("Welcome to Lukis Castle!")
print("Your mission is to find Lukis Castle hidden on Fairy Island!")

choice1 = input('You are at the beginning of your journey. There are two paths in front of you.\n'
                'Type "forest" to go through the dense forest.'
                'Type "mountain" to climb the rocky mountain.\n').lower()

if choice1 == "forest":
    choice2 = input('You\'ve entered the forest. '
                    'You hear strange noises and see a river blocking your path.\n '
                    'Type "bridge" to cross the old wooden bridge.\n '
                    'Type "raft" to build a raft and cross the river.\n').lower()
    if choice2 == "bridge":
        choice3 = input("You safely crossed the bridge.\n "
                        "Ahead, you see three caves. One with shimmering lights,\n "
                        "one with soft music, and one that is dark and silent.\n "
                        "Which cave do you enter? "
                        'Type "lights", "music", or "dark".\n').lower()
        if choice3 == "lights":
            print("The cave is filled with illusions. You lose your way. Game Over.")
            print(r"""
                _ _
              _(9(9)__        __/^\/^\__
             /o o   \/_     __\_\_/\_/_/_
             \___,   \/_   _\.'       './_      _/\_
              `---`\  \/_ _\/           \/_   _|.'_/
                    \  \/_\/      /      \/_  |/ /
                     \  `-'      |        ';_:' /
                     /|          \      \     .'
                    /_/   |,___.-`',    /`'---`
                  jgs    /___/`       /____/
            """)
        elif choice3 == "music":
            print("You find a magical portal that teleports you to Lukis Castle. You Win!")
            print(r"""
                     .-.     __
                    /   \   /  '.
                    \    \ |    /
                   __\_   \    /
                 .'    \   \  / sSS2z
                  \      \   \  sS/ .(           .-.   __
                   '.__   \   \s2z  _/     _  _ /   \ /  \
                       \_  '.  \s -\______// / \|   |/   |
                     .'  '-._'._\ ____.---' :   \   /  _/_
                     '._,__.--|  _/         _\_  \_|_.'   '.
                            .', /          :   '-(  )_____.' 
                           ( (  \           '.__/'--\   \
                           /  \  \             /  |  \   )
                          /  / \. )           /   /  |'-:
                         / .'  / /            '--'\__/ \ \
                       _/ /   /.'                       \ \
                      ( '/   (_~-.                       \ \
                      / /      '-'                        \ \
                      ;/   snd                             ) )
                                                          / Picture
            """)
        elif choice3 == "dark":
            print("A wild beast attacks you in the darkness. Game Over.")
            print(r"""
                _ _
              _(9(9)__        __/^\/^\__
             /o o   \/_     __\_\_/\_/_/_
             \___,   \/_   _\.'       './_      _/\_
              `---`\  \/_ _\/           \/_   _|.'_/
                    \  \/_\/      /      \/_  |/ /
                     \  `-'      |        ';_:' /
                     /|          \      \     .'
                    /_/   |,___.-`',    /`'---`
                  jgs    /___/`       /____/
            """)
    elif choice2 == "raft":
        print("The raft breaks apart in the strong current. Game Over.")
else:
    print("You take a wrong turn and end up at a dead end. Game Over.")
