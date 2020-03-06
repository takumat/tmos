

#define GPFSEL1 0x20200004
#define GPSET0 0x2020001C
#define GPCLR0 0x20200028

extern void init_screen();
extern int print_str(const char* str);

int main(void)
{
	extern void* __bss_start;
	extern void* __bss_end;
	
	unsigned int* p;
	unsigned int* start = (unsigned int*)&__bss_start;
	unsigned int* end = (unsigned int*)&__bss_end;
	
	for(p = start; p < end; p++) {
		*p = 0;
	}
	
	init_screen();
	
	print_str("Hello, World!");
	
	while(1);
	
	return 0;
}

