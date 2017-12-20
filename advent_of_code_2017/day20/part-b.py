"""--- Part Two ---

To simplify the problem further, the GPU would like to remove any particles that collide. Particles collide if their positions ever exactly match. Because particles are updated simultaneously, more than two particles can collide at the same time and place. Once particles collide, they are removed and cannot collide with anything else after that tick.

For example:

p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

------destroyed by collision------
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>
In this example, particles 0, 1, and 2 are simultaneously destroyed at the time and place marked X. On the next tick, particle 3 passes through unharmed.

How many particles are left after all collisions are resolved?"""

def remove_duplicates(new_specs):
    to_be_excluded = []
    for i in range(0,len(new_specs)):
        index_lst = []
        if i in index_lst:
            continue
        for j in range(0,len(new_specs)):
            if new_specs[i][0] == new_specs[j][0]:
                index_lst.append(j)

        if len(index_lst) > 1:
            to_be_excluded += index_lst

    if len(to_be_excluded) > 0:
        exclude = sorted(list(set(to_be_excluded)))
        i = len(exclude) -1
        while i >= 0:
            idx = exclude[i]
            del new_specs[idx]
            i -= 1
    return new_specs

def remove_divergent(new_specs):
    scaped_now = []
    pos_x = [line[0][0] for line in new_specs]
    vec_x = [line[1][0] for line in new_specs]
    acc_x = [line[2][0] for line in new_specs]


    for i in range(len(new_specs)):
        line = new_specs[i]
        if line[0][0] == max(pos_x) and line[2][0] == max(acc_x) and line[1][0] == max(vec_x):
            scaped_now.append(i)

        if  line[0][0] == min(pos_x) and line[2][0] == min(acc_x) and line[1][0] == min(vec_x):
            scaped_now.append(i)

    scaped_now = sorted(list(set(scaped_now)))
    if len(scaped_now) > 0:
            i = len(scaped_now) -1
            while i >= 0:
                idx = scaped_now[i]
                del new_specs[idx]
                i -= 1
    return (new_specs, scaped_now)




def move(input_lst, escaped):
    input_lst = remove_duplicates(input_lst)
    (input_lst, scaped_now) = remove_divergent(input_lst)
    new_specs = []
    for line in input_lst:
        position = line[0]
        velocity = line[1]
        acceleration = line[2]
        for i in range(3):
            velocity[i] += acceleration[i]

        for i in range(3):
            position[i] += velocity[i]

        new_specs.append([position, velocity, acceleration])


    escaped += scaped_now


    return (new_specs, escaped)



def main():

    f = open("input", "r")
    text = f.read()[:-1].split("\n")
    text2 = [line.split(", ") for line in text]
    text3 = [[(elem[:-1])[3:].split(",") for elem in line] for line in text2]
    input_lst = [[[int(num) for num in coord] for coord in line] for line in text3]



    last_len = len(input_lst)
    escaped = []

    while len(input_lst)>0:
        (input_lst, escaped) = move(input_lst, escaped)

    print("escaped", len(escaped))

if __name__ == "__main__":
    main()
