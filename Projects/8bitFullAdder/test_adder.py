import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    a_vals = [0, 6, 4, 3, 1]
    b_vals = [0, 1, 2, 5, 8]

    for i in range(5):
        a = a_vals[i]
        b = b_vals[i]
        c = random.randint(0, 1)

        dut.a.value = a
        dut.b.value = b
        dut.cin.value = c

        await Timer(2, units='ns')

        expected_sum = (a + b + c) & 0xFF
        expected_carry = (a + b + c) >> 8

        dut_sum = int(dut.sum.value)
        dut_carry = int(dut.carry.value)

        print(f"Test {i}: a={a}, b={b}, cin={c} => sum={dut_sum}, carry={dut_carry}")
        
        assert dut_sum == expected_sum, f"SUM mismatch: {a}+{b}+{c} = {expected_sum}, got {dut_sum}"
        assert dut_carry == expected_carry, f"CARRY mismatch: {a}+{b}+{c} = carry {expected_carry}, got {dut_carry}"
