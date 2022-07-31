# Level1 Design1 - Multiplexer

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
