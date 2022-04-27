import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_diff_simple(dut):

    x = 0
    y = 0
    cin = 0

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 0, "Adder result is incorrect"

@cocotb.test()
async def test_2(dut):

    x = 5
    y = 6
    cin = 0

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 11, "Adder result is incorrect"

@cocotb.test()
async def test_3(dut):

    x = 255
    y = 0
    cin = 1

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 0, "Adder result is incorrect"
    assert dut.cout.value == 1, "Adder result is incorrect"
