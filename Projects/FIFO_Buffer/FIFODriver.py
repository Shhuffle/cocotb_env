from cocotb.triggers import RisingEdge
from FIFOTransaction import FIFOTransaction

class FIFODriver:
    def __init__(self, dut):
        self.dut = dut

    async def send(self, transaction: FIFOTransaction):
        if transaction.write:
           
            while self.dut.full.value:
                await RisingEdge(self.dut.clk)
            self.dut.din.value = transaction.din
            self.dut.wr_en.value = 1

        # Read logic
        if transaction.read:
            # Wait until FIFO is not empty
            while self.dut.empty.value:
                await RisingEdge(self.dut.clk)
            self.dut.rd_en.value = 1

        print(f"Sent transaction: {transaction}")

        # Apply for one clock cycle
        await RisingEdge(self.dut.clk)
        

        # Deassert controls
        self.dut.wr_en.value = 0
        self.dut.rd_en.value = 0
