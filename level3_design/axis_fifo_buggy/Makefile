# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/axis_fifo_buggy.v

TOPLEVEL :=  axis_fifo_buggy             # design
MODULE   :=  test_axis_fifo_buggy        # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
