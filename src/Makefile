#
# Copyright (C) 2020 takumat (takumat@github)
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
#

#CROSS= arm-linux-gnueabihf-
CROSS=aarch64-elf-

SRCS= $(wildcard ./*/*.c)
CC= $(CROSS)gcc
LD= $(CROSS)ld
OBJCOPY= $(CROSS)objcopy


STARTUP= ./boot/startup.o
OBJS= $(SRCS:.c=.o)

# add library objs
OBJS+= 

CFLAGS= -mlittle-endian
CFLAGS+= -nostdinc -fno-builtin -ffreestanding -fno-stack-protector
CFLAGS+= -O2

#################
all:		kernel8.img

kernel8.elf: $(STARTUP) $(OBJS)
		$(LD) -static -nostdlib -T ./boot/tmos.lds $^  -o $@ 

 .SUFFIXES: .elf .img
 
 .elf.img:
		$(OBJCOPY) -O binary $< $@ 
 
 .c.o:
		$(CC) $(CFLAGS) -c $< -o $@ 

 .S.o:
		$(CC) $(CFLAGS) -c $< -o $@ 

clean::
		$(RM) -f *.o *.img */*.elf */*.o */*/*.o
		$(RM) -f tags *~

tags::
		ctags *.[chS]


