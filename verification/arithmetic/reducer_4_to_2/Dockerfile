FROM debian:11

RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential \
    python3 \
    python3-pip \
    git \
    bison \
    flex \
    gperf \
    autoconf

RUN git clone https://github.com/steveicarus/iverilog.git && cd iverilog && git checkout v11_0 && \
    sh autoconf.sh && ./configure && make && make install

RUN pip3 install cocotb pytest

# Make sure to copy the files

RUN mkdir verify
COPY hdl verify/
COPY verification/arithmetic/reducer_4_to_2/Makefile verify/
COPY verification/arithmetic/reducer_4_to_2/reducer_4_to_2_tb.py verify/
WORKDIR verify
CMD ["make", "SIM=icarus"]






