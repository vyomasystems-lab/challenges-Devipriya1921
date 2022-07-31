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
