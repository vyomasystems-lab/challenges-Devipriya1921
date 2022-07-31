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
