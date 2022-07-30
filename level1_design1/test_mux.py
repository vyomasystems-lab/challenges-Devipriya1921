# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    dut.inp0.value = 1
    dut.sel.value = 0
    await Timer(2,units="ns")
    assert dut.out.value ==1