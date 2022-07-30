# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    # input driving
    dut.inp0 = 2;
    dut.inp1 = 2;
    dut.inp2 = 2;
    dut.inp3 = 2;
    dut.inp4 = 2;
    dut.inp5 = 2;
    dut.inp6 = 2;
    dut.inp7 = 2;
    dut.inp8 = 2;
    dut.inp9 = 2;
    dut.inp10 = 2;
    dut.inp11 = 2;
    dut.inp12 = 2;
    dut.inp13 = 2;
    dut.inp14 = 2;
    dut.inp15 = 2;
    dut.inp16 = 2;
    dut.inp17 = 2;
    dut.inp18 = 2;
    dut.inp19 = 2;
    dut.inp20 = 2;
    dut.inp21 = 2;
    dut.inp22 = 2;
    dut.inp23 = 2;
    dut.inp24 = 2;
    dut.inp25 = 2;
    dut.inp26 = 2;
    dut.inp27 = 2;
    dut.inp28 = 2;
    dut.inp29 = 2;
    dut.inp30 = 2;
    for i in range(35):

        dut.sel.value = random.randint(0, 31)
        await Timer(2, units='ns')
        assert dut.out.value == 2, "Randomised test failed with: {}  = {}".format(dut.sel.value, dut.out.value)
        cocotb.log.info('Running test')