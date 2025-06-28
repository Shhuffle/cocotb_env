import cocotb
import random
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

    # Reset DUT
    dut.rst.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 0
    await Timer(10, units="ns")
    dut.rst.value = 1
    await Timer(10, units="ns")

    # Write 10 values
    for _ in range(10):
        val = random.randint(0, 255)
        txn = FIFOTransaction(data=val, write=True)
        await driver.send(txn)
        scoreboard.add_expected(val)

    # Read 10 values
    for _ in range(10):
        txn = FIFOTransaction(read=True)
        await driver.send(txn)

    # Give monitor time to capture
    await Timer(50, units="ns")
    for txn in monitor.observed:
        scoreboard.add_actual(txn.dout)

    scoreboard.check()
