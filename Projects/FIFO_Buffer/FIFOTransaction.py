class FIFOTransaction:
    def __init__(self, data=None, read=False, write=False):
        self.read = read                  # Used to determine rd_en
        self.write = write                # Used to determine wr_en
        self.din = data                   # Data to be written (for write)
        self.dout = None                  # Will be set by monitor during read

    def __repr__(self):
        return f"FIFOTransaction(write={self.write}, read={self.read}, din={self.din}, dout={self.dout})"
