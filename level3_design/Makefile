# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/axis_fifo.v

TOPLEVEL :=  axis_fifo             # design
MODULE   :=  test_axis_fifo        # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build _pycache_