import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_zeros(dut):

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.r.value = 57
    dut.g.value = 142
    dut.b.value = 116

    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)

    print(f'y value is {dut.y.value}')
    print(f'cr value is {dut.cr.value}')
    print(f'cb value is {dut.cb.value}')