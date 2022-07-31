# Capture the BUG –A Design Verification Hackathon

To provide a basic hands-on for design verification, which enhances practical verification knowledge. The verification challenge helps to understand the verification 
intent to detect bugs in designs, understand debugging and fix the buggy designs. It provides a practical exposure to real world design verification activities.

Cocotb is a library for digital logic verification in Python.
Provides Python interface to control standard RTL simulators.
Offers an alternative to using Verilog/SystemVerilog/VHDL framework for verification.


# Introduction 
Design verification is the process of demostrating the functional correctness of the RTL design with respect to design specification. Design Verfication attempts to 
check whether the proposed design what it is intended to do. This is a complex task and takes the majority of time and effort in most large electronic system design 
projects. It is imperative that the design if fumctionaly verified and any potential bug is eliminated at an early stage it is very common that more engineers time 
and expense is spent to verify a designthat the rest of the steps in the ASIC Design Cycle. Even with this large expenditure, most designs are first fabricated with several bugs still in them. So here comes the importance.
Design Verification: Predictive analysis to ensure that the synthesized design, when manufactured, will perform the given I/O function.


# CocoTb

* Cocotb is a library for digital logic verification in Python.
* Coroutine cosimulation testbench.
* Cocotb automatically connects to a variety of HDL simulators (such as Icarus, Modelsim, Questasim, and others) and allows you to control the signals in your 
  design straight from Python. The whole testbench may be written in Python, and automation and randomization are simple to implement, resulting in increased 
  productivity. Cocotb does not necessitate the use of any additional RTL code. In the simulator, the top level is instantiated as the Design Under Test. 
* Python is used to provide simulation to the DUT’s inputs and monitor the outputs. Given that it does not necessitate knowledge of HDLs, it can be of great help to 
  those who are unfamiliar with it. 
* Python is also an object oriented scripting language. Cocotb has certain significant advantages over HDL testing.

## Features of Python for verification:

* Python is an extremely productive language that allows one to write code quickly. 
* Python makes it simple to connect to other languages.
* Python contains a large library of pre-existing code that can be reused.
* Python is an interpreted language, which means that tests can be modified and rerun without having to recompile the design or exit the simulator GUI.
* Python is widely used, significantly more engineers are familiar with it than SystemVerilog or VHDL.


## Architecture of cocotb

A normal cocotb testbench does not necessitate any additional RTL code. Without any wrapper code, the Design Under Test (DUT) is instantiated as the simulator’s 
toplevel. Cocotb applies stimuli to the DUT’s inputs (or lower in the hierarchy) and monitors the outputs directly from Python. Cocotb acts as a bridge between the 
simulator and Python as shown in Figure. Verilog Procedural Interface (VPI) or VHDL Procedural Interface (VHDLPI) is used (VHPI). 

![coctb](https://user-images.githubusercontent.com/88897605/182017611-12399f21-2cd5-4d5e-a2f9-e2d7ff04954b.png)

A test is a Python function. The await keyword indicates when control of execution should be returned to the simulator. A test can start numerous coroutines, permitting 
separate execution flows.

Python testbench code has the ability to:
* Traverse the DUT hierarchy and update values.
* Wait for the simulation timer to run out.
* Wait for a signal’s rising or falling edge


## Design Methodology

The cocotb framework is made to be a goal-directed design verification tool. The following steps are included in the python based verification flow:

1) Capture the IP-level actions needed to create a desired use case, if not already captured.
2) Compose the desired use case in text format.
3) Use cocotb for vector generation: cocotb allows constrained randomization through which all the parameters of the IP core can be randomized.


## Cosimulation

It is the independent simulation of the design and testbench. Communication is accomplished using VPI/VHPI interfaces, which are represented by cocotb ‘triggers’. 
The simulation time does not advance while the Python function is running. When a trigger is delivered, the testbench suspends execution until the triggered condition 
is met before restarting execution.

```
* Timer(time, unit)
* Edge(signal)
* RisingEdge(signal)
* FallingEdge(signal)
* ClockCycles(signal, num)
``` 
  
# Verification Environment
  
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon:

![getting started hackathon](https://user-images.githubusercontent.com/83152452/182035432-8a644483-91fd-4aac-b25e-27db5c35a223.png)

## Demo Example

### Adder Design Verification
  
Adder is used to add binary numbers. Adder circuit is basically a combinational logic circuit. It is a memory less circuit and performs an operation assigned to it 
logically by a Boolean expression. The output depends upon the present input at any given time.

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 

# Hackathon Challenges 

* Level1 Design1 - Multiplexer
* Level1 Design2 - Sequence Detector 1011
* Level2 Design  - Bit Manipulation Co-Processor 
* Level3 Design  - AXI Stream FIFO

## Level1 Design1 - Multiplexer

A multiplexer or mux is a combinational circuits that selects several analog or digital input signals and forwards the selected input into a single output line. 
A multiplexer of 2n inputs has n selected lines, are used to select which input line to send to the output.

![mux](https://user-images.githubusercontent.com/88897605/182018710-08601ec6-a5e3-4c1f-9189-d94139f15e61.png)

### Verification Environment

The values are assigned to the input port using:

```
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;
      and so on....
```

The error observed is:

```
assert dut.out.value == INP30, "Mux result is incorrect: {INP30} != {OUT}, expected value={EXP}".format(
                     AssertionError: Mux result is incorrect: 3 != 0, expected value=3
```

### Test Scenario:

* Test Inputs: Binary Numbers
* Expected Output: 3
* Observed Output in the DUT  dut.out.value == 0

### Design Bug

Based on the above test input and analysing the design, we see the following:

```
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;                                 ====> BUG
    endcase
  end

endmodule 
```

### Mux Bug 

![mux - test failed - inp30 bug exposed](https://user-images.githubusercontent.com/83152452/182036121-c6321665-1c1e-4836-85c6-0103436e7158.png)


### Design Fix

Based on the above Bug test input and analysing the design, we can Debug the following code by adding input values:

```
 5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;                                 ====> BUG RESOLVED 
      default: out = 0;
    endcase
  end

endmodule 
```

### Mux Bug Fix

Updating the design and re-running the test makes the test pass,

![mux_fix - test passed - inp30 bug corrected](https://user-images.githubusercontent.com/83152452/182036124-97f83516-a6f2-4b14-afba-b84b441a49a8.png)

The updated design is checked in as mux_fix.v

### Verification Strategy

A design verification strategy was developed to achieve the desired goal. The approach used has some basic concepts when rigorously applied, ensures a fully functional design.


# Level1 Design2 - Sequence Detector 1011

A sequence detector is a sequential state machine that takes an input string of bits and generates an output 1 whenever the target sequence has been detected

![seq_detect](https://user-images.githubusercontent.com/88897605/182020410-bbc07c8a-400a-4d49-893d-57797dcafc02.png)

### Verification Environment

The values are assigned to the input port using:

```
begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        next_state = IDLE;
      end
    endcase
  end
endmodule
```


The following error is seen:

```
 assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 01011. Model Output: {dut.seq_seen.value} Expected Ouput: 1'
```

### Test Scenario

```
* Test Inputs:  01011 
* Expected Output: 1
* Observed Output in the DUT  dut.out.value == 0
```

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code.

### Seq Dectect Bug

Based on the above test input and analysing the design, we see the following,

![seq_detect_1011_buggy-test failed](https://user-images.githubusercontent.com/83152452/182036327-72236a3d-258f-419b-a85d-7b2536084eae.png)


### Seq Dectect Bug Fix

Updating the design and re-running the test makes the test pass:

![seq_detect_1011-test passed](https://user-images.githubusercontent.com/83152452/182036332-2c2e63e7-8aa1-4b81-bdc6-6a4f299edad3.png)

The updated design is checked in as seq_detect_1011_fix.v


# Level2 Design - Bit Manipulation Co Processor 

Bit manipulation instructions sets (BMI sets) - The purpose of these instruction sets is to improve the speed of bit manipulation. All the instructions in these sets 
are non-SIMD and operate only on general-purpose registers.

![bit_manip](https://user-images.githubusercontent.com/88897605/182021873-17ac8bfe-6082-4a4a-b259-4cfba3ff7704.png)

### Verification Environment

The values are assigned to the input port,

The following error is seen:

```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x8 does not match MODEL = 0x0
```

### Test Scenario

```
* Test Inputs:  1ul
* Expected Output: 0x0
* Observed Output in the DUT  dut.out.value == 0x8
```

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code.

### Bit Manipulation Bug

![bitmanip_buggy-test fail](https://user-images.githubusercontent.com/83152452/182036445-9a0d2696-17f7-46c1-b0c9-c70502fa08ad.png)

### Bit Manipulation Bug Fix

Updating the design and re-running the test makes the test pass,

![bitmanu-test passed](https://user-images.githubusercontent.com/83152452/182036446-85f1577e-d057-4689-8fd6-fc9f8586b733.png)


The updated design is checked in as mkbitmanip_fix.v


# Level3 Design - AXI Stream FIFO

* The AXI Streaming FIFO allows memory mapped access to a AXI Streaming interface. The core can be used to interface to the AXI Ethernet without the need to use DMA. 
* The principal operation of this core allows the write or read of data packets to or from a device without any concern over the AXI Streaming interface. 
* The AXI Streaming interface is transparent to the user. The axis_fifo core is a simple FIFO (First Input First Output) with AXI streaming interfaces, supporting 
  synchronous and asynchronous operation modes. 
* Configurable word-based or frame-based synchronous FIFO with parametrizable data width, depth, type, and bad frame detection. 


### Introduction to AXI Stream FIFO

* AXI Stream FIFO allows developers to be able to access AXI streams from AXI memory mapped peripherals without the need to implement a full DMA solution. 
* To enable this, the AXI Stream FIFO provides the ability to read and write from AXI MM to AXI streams. 
* This can be used to interact with an AXI Virtual FIFO Controller or with IP like the Fast Fourier Transform which has configuration data over AXIS.
* The AXI Stream FIFO presents a simple register interface that enables the user to define the following:

- Transmission Length – The length of the data to be transmitted.
- Transmission Vacancy – The number of slots in the FIFO currently empty.
- Receive Length – The length of the data packet received.
- Receive Occupancy – The number of occupied slots in the FIFO.
- Receive / Transmission Destination – Side band AXIS Signal TIDest.
- System / Transmission and Receive Interrupts.
- Receive / Transmission ID – Side band AXIS Signal TId.
- Receive / Transmission User – Side band AXIS Signal TUser.
- System / Transmission and Receive Resets.

Data is written or read from the AXI Stream FIFO via a memory address which writes into or reads from the FIFO. 

### Verification Environment

The values are assigned to the input port,

### Test Scenario

```
* Test Inputs: AXI Stream Signals
* Expected Output: 124, 125, 126, 127, 128
* Observed Output in the DUT  dut.out.value == 0
```

### Design Bug

```
if (rst) begin
            out_fifo_wr_ptr_reg <= 1;                                             ====> BUG in the code
            out_fifo_rd_ptr_reg <= 1;                                             ====> BUG in the code
            m_axis_tvalid_reg <= 1'b0;
        end
    end
```

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code

![AXI stream FIFO - test fail](https://user-images.githubusercontent.com/83152452/182038115-ef824f13-afca-4a31-a8c7-962ccfd9d4d6.png)


### Design Fix

Based on the above Bug test input and analysing the design, we can Debug the following code by adding input values,

Updating the design and re-running the test makes the test pass:


```
if (rst) begin
            out_fifo_wr_ptr_reg <= 0;                                             ====> BUG resolved
            out_fifo_rd_ptr_reg <= 0;                                             ====> BUG resolved
            m_axis_tvalid_reg <= 1'b0;
        end
    end
```


### Design Bug Fix

![AXI stream FIFO - test pass](https://user-images.githubusercontent.com/83152452/182038116-a69653d3-4e76-4586-b4e8-fb8808980c64.png)


# Acknowledgements
- Lavanya J, CEO/Founder, Vyoma Systems
- Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd.
- TA's 


# Author
- [A Devipriya](https://github.com/Devipriya1921), B.E (Electronics and Communication Engineering), Bangalore - adevipriya1900@gmail.com




















