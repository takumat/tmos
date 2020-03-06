
参考文献
	30日でできる！OS自作入門
	Raspberry Pi で学ぶコンピュータアーキテクチャ
	BareMetal で遊ぶ Raspberry Pi https://tatsu-zine.com/books/raspi-bm


Windows10 にクロスコンパイル環境を用意する

ubuntu on windows を使用
こちらのページを参考にした
1. https://qiita.com/iwatake2222/items/5b20558f8ab3f27ca4a4
2. https://blog.ikeryo1182.com/cross-compile/
3. https://github.com/bztsrc/raspi3-tutorial/tree/master/00_crosscompiler


 *ubuntu on windows のシェルでコピペを有効にするにはこちらのページをみた
    https://ex1.m-yabe.com/archives/3388


とりあえず，1. のブログに書いてあった，ラズパイのgithubからクローンした
git clone https://github.com/raspberrypi/tools

このツールを展開して，このコマンドで sample.c をコンパイルし，出力された a.out を
ラズパイに転送，実行権を付けて実行したらとりあえず動いた。
Makefile つくらないと辛そう。
ARCH=arm ~/raspberry/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-gcc sample.c

3. の00_crosscompiler/README.md によると，以下のようだ

The executables we are interested in:

・aarch64-elf-as - the assembler
・aarch64-elf-gcc - the C compiler
・aarch64-elf-ld - the linker
・aarch64-elf-objcopy - to convert ELF executable into IMG format
・aarch64-elf-objdump - utility to disassemble executables (for debugging)
・aarch64-elf-readelf - an useful utility to dump sections and segments in executables (for debugging)

If you have all of the above six executables and you can also run them without error messages, congrats! You have all the tools needed, you can start to work with my tutorials! 

