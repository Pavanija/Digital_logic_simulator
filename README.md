# Digital_Logic_Simulator

## Introduction

Digital logic circuits have numerous applications across various industries and fields due to their ability to process binary data using logical operations.
These logic circuits are composed of interconnected digital components, such as logic gates, flip-flops, multiplexers, and other building blocks of digital electronics
Digital logic simulation play a vital role to validate the correctness and analyze the behavior of digital logic circuits before physically implementing them.
It helps catch errors and design flaws early in the development process.
This repository presents design of a digital logic simulator for a combinational circuit in Python 
It gives a good visualization to the mechanisms behind circuits using logic gates and the interaction between gates.

## Implementation details
Design of a digital logic simulator for a combinational circuit(using logic gates such as NOT , AND , OR , XOR , NOR , NAND , XNOR) in Python with HSpice circuit description file as input.
Outputs for the circuit are determined by considering the whole circuit as a graph and leveling the graph.In this repo an example combinational logic circuit of HALF ADDER is used to check the logic simulator working

![logic_simulator](https://github.com/Pavanija/Digital_logic_simulator/assets/140067158/09c9e826-1bc9-4108-94ce-d56f33ec0549)
## Key concepts 
### Representing Circuit as a Graph
In digital logic design, circuits can be represented as graphs ,where logic gates are mapped as nodes, and the connections between these gates are edges. 
Each node represents a logical operation  that processes input signals and produces an output.
### Leveling the Graph
Leveling the Graph refers to the process of organizing the components of the circuit into different levels based on their dependencies and the order in which their outputs are needed
By organizing components into levels,  ensures dependencies are satisfied i.e, components at a lower level produce outputs that can be used as inputs for components at higher levels.
### Determining Outputs
Once the graph is leveled, starting from the input nodes and proceed through the levels, calculating the outputs of each component based on the inputs provided to them. 
Since the components are organized in a way that ensures dependencies are satisfied, you can propagate the calculated outputs through the circuit to determine the final outputs.

## Verification
The accuracy of the  Logic Simulator output is verified by comparing its results with manual analysis output for combinational logc circuits. 
The results ensured that the simulator functions correctly and produces expected results





 
