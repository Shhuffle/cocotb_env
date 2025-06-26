import cocotb
import cocotb.clock
from cocotb.triggers import RisingEdge, Timer 
from cocotb.clock import Clock
import random


@cocotb.test()
async def test_ALU(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rst.value = 0
    await Timer(20, units="ns")
    dut.rst.value = 1
    await RisingEdge(dut.clk)

    for i in range (10):
        sel = random.randint(0,3)
        a = random.randint(12,20)
        b = random.randint(0,12)

        dut.a.value = a
        dut.SEL.value = sel 
        dut.b.value = b 

        await RisingEdge(dut.clk)

        if sel == 0:
            expected = a * b
        elif sel == 1:
            expected = a // b
        elif sel == 2:
            expected = a + b
        elif sel == 3:
            expected = a - b
        else:
            expected = 0

        await RisingEdge(dut.clk)
        await RisingEdge(dut.clk)

        assert dut.y.value == expected, f"Test failed at i={i}: a={a}, b={b}, sel={sel}, got={dut.y.value}, expected={expected}"


        