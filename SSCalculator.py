
def print_ss_comma(alist, last):
    for e in alist:
        print(e, end="")
    if not last:
        print(",", end=" ")

samples = ["0", "1", "2"]
ss_size = 3

s_space = []
gs_space = []

#prep lists
for x in range(ss_size):
    s_space.append(samples[0])
    gs_space.append(samples[-1])

#last sample number
lsnum = len(samples) - 1

while s_space != gs_space:
    print_ss_comma(s_space, False)
    #counting logic
    increase = False
    focus = ss_size - 1

    while not increase:
        if s_space[focus] == samples[lsnum]:
            focus = focus - 1
        else:
            i_in = samples.index(s_space[focus]) + 1
            s_space[focus] =  samples[i_in]
            
            while focus != ss_size - 1:
                focus = focus + 1
                s_space[focus] = samples[0]

            increase = True

print_ss_comma(s_space, True)
