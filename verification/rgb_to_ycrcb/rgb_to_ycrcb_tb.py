import cocotb
import random
import cv2 as cv
import numpy as np
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


class RGB_to_YCbCr:
    def __init__(self, r, g, b):
        self.y = 0.296875 * r + 0.5859375 * g + 0.140625 * b
        self.cr = (r - self.y) * 0.7109375 + 128
        self.cb = (b - self.y) * 0.5625 + 128

    def get_y(self):
        return int(self.y) if self.y < 255 else 255

    def get_cr(self):
        return int(self.cr)

    def get_cb(self):
        return int(self.cb)


@cocotb.test()
async def test_zeros(dut):

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.r.value = 57
    dut.g.value = 142
    dut.b.value = 116

    ycbcr = RGB_to_YCbCr(57, 142, 116)

    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)

    assert dut.y.value == ycbcr.get_y(), f'{dut.y.value} does not equal {ycbcr.get_y()}'
    assert dut.cb.value == ycbcr.get_cb(), f'{dut.cb.value} does not equal {ycbcr.get_cb()}'
    assert dut.cr.value == ycbcr.get_cr(), f'{dut.cr.value} does not equal {ycbcr.get_cr()}'


@cocotb.test()
async def test_random_rgb(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    dut.r.value = r
    dut.g.value = g
    dut.b.value = b

    ycbcr = RGB_to_YCbCr(r, g, b)

    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)

    assert dut.y.value == ycbcr.get_y(), f'{dut.y.value} does not equal {ycbcr.get_y()}'
    assert dut.cb.value == ycbcr.get_cb(), f'{dut.cb.value} does not equal {ycbcr.get_cb()}'
    assert dut.cr.value == ycbcr.get_cr(), f'{dut.cr.value} does not equal {ycbcr.get_cr()}'


@cocotb.test()
async def validate_against_opencv(dut):

    errors_y = []
    errors_cr = []
    errors_cb = []

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    for i in range(0, 256):
        for j in range(0, 256):
            for k in range(0, 256):
                r = i
                g = j
                b = k

                rgb = np.uint8([[[r, g, b]]])
                ycrcb = cv.cvtColor(rgb, cv.COLOR_RGB2YCrCb)

                dut.r.value = r
                dut.g.value = g
                dut.b.value = b

                await FallingEdge(dut.clk)
                await FallingEdge(dut.clk)
                await FallingEdge(dut.clk)

                error_y = abs(dut.y.value - ycrcb[0][0][0])
                error_cr = abs(dut.cr.value - ycrcb[0][0][1])
                error_cb = abs(dut.cb.value - ycrcb[0][0][2])

                errors_y.append(error_y)
                errors_cr.append(error_cr)
                errors_cb.append(error_cb)

    sum_y = 0
    sum_cr = 0
    sum_cb = 0
    for i in range(0, len(errors_y)):
        sum_y += errors_y[i]
        sum_cr += errors_cr[i]
        sum_cb += errors_cb[i]

    print(f'Mean absolute error for y is {sum_y / len(errors_y)} units')
    print(f'Mean absolute error error for cr is {sum_cr / len(errors_cr)} units')
    print(f'Mean absolute error error for cb is {sum_cb / len(errors_cb)} units')
