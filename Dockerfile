# This dockerfile creates a minimal pymmcore image for demonstration purposes
# (for example, DemoCamera should work).

FROM ubuntu:18.04

# System packages
RUN apt-get update && apt-get install -y \
        bzip2 \
        bc \
        build-essential \
        cmake \
        curl \
        g++ \
        gfortran \
        libboost-dev \
        libboost-thread-dev \
        libtool \
        autoconf \
        automake \
        git \
        pkg-config \
        software-properties-common \
        unzip \
        wget \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*
RUN addgroup --gid 1001 python && \
    useradd --uid 1001 --gid 1001 python

RUN git clone https://github.com/micro-manager/micro-manager.git
RUN cd micro-manager && \
    ./autogen.sh && \
    ./configure --without-java && \
    make && \
    # will be installed to /usr/local/lib/micro-manager/
    make install
ENV MMCORE_PATH=/usr/local/lib/micro-manager/
ENV MMCONFIG_DEMO_PATH=/micro-manager/bindist/any-platform/MMConfig_demo.cfg

# Install miniconda to /miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}

RUN conda update -y conda && \
    conda install -y python=3.7.6 numpy && \
    pip install --upgrade pip && \
    pip install pymmcore
