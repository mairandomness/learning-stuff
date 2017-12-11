"""--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw)."""

def main():
    f = open("input", "r")
    steps = f.read()[:-1].split(",")
    #steps = "ne,ne,s,s".split(",")
    previous_step = ""
    distance = 0
    step_opposite ={
            "n":"s",
            "s":"n",
            "ne":"sw",
            "sw":"ne",
            "nw":"se",
            "se":"nw"}
    step_num ={
            "n":0,
            "ne":0,
            "nw":0}
    for step in steps:
        if step in step_num:
            step_num[step]+=1
        else:
            step_num[step_opposite[step]] -=1
    step_num["ne"] +=step_num["n"]
    step_num["nw"] += step_num["n"]
    step_num["n"] -= step_num["n"]
    if step_num["ne"] * step_num["nw"] > 0:
       print(max([abs(step_num[key]) for key in step_num]))
    else:
        print(abs(step_num["nw"]) + step_num["ne"])

if __name__ == "__main__":
    main()
