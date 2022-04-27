import random
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_zeros(dut):
    dut.w.value = 0
    dut.x.value = 0
    dut.y.value = 0
    dut.z.value = 0
    dut.cin.value = 0

    await Timer(10, units="us")

    assert dut.sum.value == 0, f"sum {dut.sum.value} is not 0!"
    assert dut.cout.value == 0, f"cout {dut.cout.value} is not 0!"
    assert dut.carry.value == 0, f"carry {dut.carry.value} is not 0!"

@cocotb.test()
async def test_add(dut):

    for i in range(10):
        w = random.randint(0, 255)
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        cin = random.randint(0, 1)

        dut.w.value = w
        dut.x.value = x
        dut.y.value = y
        dut.z.value = z
        dut.cin.value = cin

        await Timer(10, units="us")

        expected_sum = w + x + y + z + cin
        expected_cout = 1 if expected_sum >
