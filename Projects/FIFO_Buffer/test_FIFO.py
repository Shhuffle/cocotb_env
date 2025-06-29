import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

from cocotb.triggers import Timer
from FIFOTransaction import FIFOTransaction
from FIFODriver import FIFODriver
from FIFOMonitor import FIFOMonitor
from FIFOScoreboard import FIFOScoreboard



@cocotb.test()
async def run_fifo_test(dut):
    driver = FIFODriver(dut)
    monitor = FIFOMonitor(dut)
    scoreboard = FIFOScoreboard()

    cocotb.start_soon(monitor.observe())
    cocotb.start_soon(Clock(dut.clk, 5, units="ns").start())

    # Reset
    dut.rst.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 0
    await Timer(10, units="ns")
    dut.rst.value = 1
    await RisingEdge(dut.clk)

    reference_fifo = [0] #During the first cycle the dout is reset to 0 so our first output from the dut is expected to be 0

    # Write phase
    for _ in range(10):
        val = random.randint(0, 255)
        txn = FIFOTransaction(data=val, write=True)
        await driver.send(txn)
        reference_fifo.append(val)
        await Timer(10, units="ns")

    # Read phase
    for _ in range(10):
        txn = FIFOTransaction(read=True)
        await driver.send(txn)
        expected_val = reference_fifo.pop(0)
        scoreboard.add_expected(expected_val)

    await Timer(50, units="ns")

    for txn in monitor.observed:
        scoreboard.add_actual(txn.dout)

    scoreboard.check()
