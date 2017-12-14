"""--- Part Two ---

Now, you need to pass through the firewall without being caught - easier said than done.

You can't control the speed of the packet, but you can delay it any number of picoseconds. For each picosecond you delay the packet before beginning your trip, all security scanners move one step. You're not in the firewall during this time; you don't enter layer 0 until you stop delaying the packet.

In the example above, if you delay 10 picoseconds (picoseconds 0 - 9), you won't get caught:

State after delaying:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

Picosecond 10:
 0   1   2   3   4   5   6
( ) [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 11:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[S] (S) ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 12:
 0   1   2   3   4   5   6
[S] [S] (.) ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 13:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 14:
 0   1   2   3   4   5   6
[ ] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 15:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... ... [ ] (.) [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 16:
 0   1   2   3   4   5   6
[S] [S] ... ... [ ] ... ( )
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]
Because all smaller delays would get you caught, the fewest number of picoseconds you would need to delay to get through safely is 10.

What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?"""

import copy

def reset_wall(int_lst, last_layer):
    wall =[]
    i=0
    j=0
    while i <= last_layer:
        cur_layer = int_lst[j][0]
        layer_depth = int_lst[j][1]

        if i == cur_layer:
            wall.append([" " for i in range(0, layer_depth)])
            j += 1
        else:
            wall.append(".")
        i += 1
    for line in wall:
        if len(line) > 1:
            line[0] = "S"
    return wall


def move_scanners(wall, move_direction):
    for j in range(len(wall)):
        layer = wall[j]
        for i in range(len(layer)):
            if layer[i] == 'S':
                if 0<= i+move_direction[j] < len(layer):
                    layer[i+move_direction[j]] = 'S'
                    layer[i] = ' '
                else:
                    layer[i] = ' '
                    move_direction[j] = move_direction[j] * -1
                    layer[i+move_direction[j]] = 'S'
                break
    return (wall, move_direction)

def main():
    #get input
    f = open("input", "r")
    text = (f.read()[:-1]).split("\n")
    input_lst = [line.split(": ") for line in text]
    int_lst = [[int(line[0]),int(line[1])] for line in input_lst]
    last_layer = int_lst[-1:][0][0:][0]

    #set up the wall

    # now we do the traveling
    wall = reset_wall(int_lst, last_layer)
    last_wall = copy.deepcopy(wall)
    delay = 0
    position = 0
    move_direction = [1 for j in range(len(wall))][:]
    last_move_direction = move_direction[:]
    found = False
    while not found:
        if delay % 1000 ==0:
            print(delay)
        position = 0
        if delay % len(wall[0]) == 0:
            (last_wall, last_move_direction) = move_scanners(last_wall, last_move_direction)
            delay +=1
            continue
        if delay != 0:

            (wall, move_direction) = (copy.deepcopy(last_wall), last_move_direction[:])
            (wall, move_direction) = move_scanners(wall, move_direction)
            (last_wall, last_move_direction) = (copy.deepcopy(wall), move_direction[:])
        position = 0
        while position <= last_layer:
            if position == last_layer and wall[position][0] != 'S':
                found = True
            if wall[position][0] == 'S':
                break
            (wall, move_direction) = move_scanners(wall, move_direction)
            position +=1
        delay +=1

    print(delay-1)



if __name__ == "__main__":
    main()
