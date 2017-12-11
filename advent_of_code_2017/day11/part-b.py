"""How many steps away is the furthest he ever got from his starting position?"""

def get_distance(step_num):
    step_num["ne"] +=step_num["n"]
    step_num["nw"] += step_num["n"]
    step_num["n"] -= step_num["n"]
    if step_num["ne"] * step_num["nw"] > 0:
        return(max([abs(step_num[key]) for key in step_num]))
    else:
        return(abs(step_num["nw"]) + step_num["ne"])



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
    max_distance=0
    for step in steps:
        if step in step_num:
            step_num[step]+=1
        else:
            step_num[step_opposite[step]] -=1
        if max_distance < get_distance(step_num):
            max_distance = get_distance(step_num)

    print(max_distance)


if __name__ == "__main__":
    main()
