# logic_simulator 

##########################################################
# Description:
#  Provides digital circuit logic output based on given
# circuit and input vector. Circuits in the standard text
# text file format for representing digital circuits. 
# 
# Assuming basic gates are NAND, NOR, AND, OR, INV, BUF
# Level of each node is calculated and printed.
# Max level of circuit is found
# Later nodes are evaluated based on their level
#
# Usage: python3 main.py <circuit_name> <input_vector>
#  Eg:- python3 main.py Netlist inputlogic
# 
##########################################################
import itertools

inpvec = []
PI = []
PO = []

f1 = open('inputvector.txt', 'r')
input_file = f1.readline()
line = input_file.strip()
inpvec_str = line.split()
print("Input vector is:", inpvec_str)

for i in inpvec_str:
    if (int(i) > 1):
        print("Please enter a binary input vector or dont care")
        exit()

inpvec = [int(val) for val in inpvec_str]
print('given input vector in binary:',inpvec)


f = open('Netlist.txt', "r")

num_of_nets = 0

num_of_lines = 0

for line in f:
    line = line.strip()
    data = line.split()
    gate = data[0]
    net_indices_str = data[1:-1]
    if gate == 'INPUT':
        PI = list(map(int, net_indices_str))

        if (len(PI) != len(inpvec_str)):
            print("Please input a",len(PI),"element long vector")
            exit()
    if gate == 'OUTPUT':
        PO = list(map(int, net_indices_str))

    net_indices = list(map(int, net_indices_str))
    if (num_of_nets < max(net_indices)):
        num_of_nets = max(net_indices)
    num_of_lines = num_of_lines + 1
f.close()

logic_values = [0] * (num_of_nets)

f = open('Netlist.txt', "r")
lines = f.readlines()
f.close()

nets_done = []
line_no = 0
completion = [0] * (num_of_lines)

for i in range(len(PI)):
    logic_values[PI[i] - 1] = inpvec[i]

for line in itertools.cycle(lines):
    data = line.split()
    gate = data[0]
    net_indices = []
    net_indices_str = []

    if (gate == 'INPUT' or gate == 'OUTPUT'):
        net_indices_str = data[1:-1]
        net_indices = list(map(int, net_indices_str))
    else:
        net_indices_str = data[1:]
        net_indices = list(map(int, net_indices_str))


    nets_done = PI

    if gate == 'INV':
        if (net_indices[0] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[1] - 1] = int(not logic_values[net_indices[0] - 1])
            completion[line_no] = 1
            nets_done.append(net_indices[1])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            print("line", line_no + 1, "-", gate, "done")

    if gate == 'BUF':
        if (net_indices[0] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[1] - 1] = int(logic_values[net_indices[0] - 1])
            completion[line_no] = 1
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[1])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])

    if gate == 'AND':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[2] - 1] = int(
                logic_values[net_indices[0] - 1] and logic_values[net_indices[1] - 1])
            completion[line_no] = 1
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'NOR':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[2] - 1] = int(
                not ((logic_values[net_indices[0] - 1]) or (logic_values[net_indices[1] - 1])))
            completion[line_no] = 1
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'NAND':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[2] - 1] = int(not (logic_values[net_indices[0] - 1] and logic_values[net_indices[1] - 1]))
            completion[line_no] = 1
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'OR':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            logic_values[net_indices[2] - 1] = int(logic_values[net_indices[0] - 1] or logic_values[net_indices[1] - 1])
            completion[line_no] = 1
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'XOR':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            completion[line_no] = 1
            logic_values[net_indices[2] - 1] = int(((not (logic_values[net_indices[0] - 1]) and (
            logic_values[net_indices[1] - 1])) or ((logic_values[net_indices[0] - 1]) and (not ((logic_values[net_indices[1] - 1]))))))
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'XNOR':
        if (net_indices[0] in nets_done) and (net_indices[1] in nets_done) and (completion[line_no] == 0):
            completion[line_no] = 1
            logic_values[net_indices[2] - 1] = int(((not (logic_values[net_indices[0] - 1]) and (
                not (logic_values[net_indices[1] - 1]))) or ((logic_values[net_indices[0] - 1]) and (logic_values[net_indices[1] - 1]))))
            print("line", line_no + 1, "-", gate, "done")
            nets_done.append(net_indices[2])
            if (net_indices[0] not in nets_done):
                nets_done.append(net_indices[0])
            if (net_indices[1] not in nets_done):
                nets_done.append(net_indices[1])

    if gate == 'INPUT':
        completion[line_no] = 1

    if gate == 'OUTPUT':
        completion[line_no] = 1

    line_no += 1

    if line_no == (num_of_lines):
        print("--------------------------------------------------")
        line_no = 0

    output_vector = [logic_values[indx - 1] for indx in PO]
    if completion.count(1) == (num_of_lines):
        print("Output logic_values are:", output_vector)
        break

