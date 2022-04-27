import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_zeros(dut):

    x = 0
    y = 0
    cin = 0

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 0, f"sum {dut.sum.value} is not 0!"
    assert dut.cout.value == 0, f"cout {dut.cout.value} is not 0!"


@cocotb.test()
async def test_add(dut):

    x = 5
    y = 6
    cin = 1

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 12, f"sum {dut.sum.value} is not 12!"
    assert dut.cout.value == 0, f"cout {dut.cout.value} is not 0!"


@cocotb.test()
async def test_overflow(dut):

    x = 255
    y = 1
    cin = 1

    dut.x.value = x
    dut.y.value = y
    dut.cin.value = cin

    await Timer(10, units="us")

    assert dut.sum.value == 1, f"sum {dut.sum.value} is not 1!"
    assert dut.cout.value == 1, f"cout {dut.cout.value} is not 1!"
