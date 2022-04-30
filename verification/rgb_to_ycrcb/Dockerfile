FROM debian:11

RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential \
    python3 \
    python3-pip \
    git \
    bison \
    flex \
    gperf \
    autoconf \
    python3-opencv

RUN git clone https://github.com/steveicarus/iverilog.git && cd iverilog && git checkout v11_0 && \
    sh autoconf.sh && ./configure && make && make install

RUN pip3 install cocotb pytest

# Make sure to copy the files

RUN mkdir verify
COPY hdl verify/
COPY verification/rgb_to_ycrcb/Makefile verify/
COPY verification/rgb_to_ycrcb/rgb_to_ycrcb_tb.py verify/
WORKDIR verify
CMD ["make", "SIM=icarus"]






