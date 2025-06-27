import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def FIFO_test(dut):
    a = [1,0]
    b = [0,1]
    c = [0,12]

    dut.rst.value = 0
    await Timer(5, units = "ns")
    for i in range (5):
        dut.din.value = 12
        dut.rd_en.value = b[i]
        dut.wr_en.value = a[i]
        await Timer(5, units = "ns")
        out = dut.dout.value
        print(f"The value read from the dut {out}")
        assert c[i] == out, f"Out mismatach expected {c[i]} got {out}"
        


        






