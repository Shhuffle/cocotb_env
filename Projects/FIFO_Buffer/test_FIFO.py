import cocotb
import cocotb.clock
from cocotb.triggers import RisingEdge, Timer 
from cocotb.clock import Clock
import random


@cocotb.test()
async def FIFO_test(dut):
    a = [1,0]
    b = [0,1]
    c = [0,12]

    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rst.value = 0
    await Timer(20, units="ns")
    dut.rst.value = 1
    await RisingEdge(dut.clk)

    for i in range (2):
        dut.din.value = 12
        dut.rd_en.value = b[i]
        dut.wr_en.value = a[i]
        await Timer(5, units = "ns")
        out = dut.dout.value
        print(f"{i} Wd en {dut.wr_en.value} | Rd en {dut.rd_en.value}|Count {dut.count.value}|Val {out} | Full {dut.full.value} | Empty {dut.empty.value} | wr_ptr {dut.wr_ptr.value} | rd_ptr {dut.rd_ptr.value} | rst {dut.rst.value} | clk {dut.clk.value}")
        assert c[i] == out, f"Out mismatach expected {c[i]} got {out}"

        



        






