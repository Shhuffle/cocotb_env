from cocotb.triggers import RisingEdge
from FIFOTransaction import FIFOTransaction

class FIFOMonitor:
    def __init__(self, dut):
        self.dut = dut
        self.observed = []

    async def observe(self):
        while True:
            await RisingEdge(self.dut.clk)
            if self.dut.rd_en.value == 1 and self.dut.empty.value == 0:
                val = int(self.dut.dout.value)
                txn = FIFOTransaction(read=True)
                txn.dout = val
                self.observed.append(txn)
                print(f"[Monitor] Read observed: {val}")
