# Level3 Design - AXI Stream FIFO

* The AXI Streaming FIFO allows memory mapped access to a AXI Streaming interface. The core can be used to interface to the AXI Ethernet without the need to use DMA. 
* The principal operation of this core allows the write or read of data packets to or from a device without any concern over the AXI Streaming interface. 
* The AXI Streaming interface is transparent to the user. The axis_fifo core is a simple FIFO (First Input First Output) with AXI streaming interfaces, supporting 
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
