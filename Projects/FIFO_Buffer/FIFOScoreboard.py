class FIFOScoreboard:
    def __init__(self):
        self.expected = []
        self.actual = []
        self.errors = 0

    def add_expected(self, val):
        self.expected.append(val)

    def add_actual(self, val):
        self.actual.append(val)

    def check(self):
        for i in range(len(self.actual)):
            exp = self.expected[i] if i < len(self.expected) else None
            act = self.actual[i]
            if exp != act:
                print(f"[Scoreboard]  Mismatch at {i}: expected={exp}, actual={act}")
                self.errors += 1
            else:
                print(f"[Scoreboard]  Match at {i}: {act}")

        if self.errors == 0:
            print("[Scoreboard]  All matched")
        else:
            print(f"[Scoreboard]  Total mismatches: {self.errors}")
