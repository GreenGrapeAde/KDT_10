	.file	"main.c"
	.text
	.section .rdata,"dr"
.LC0:
	.ascii "\354\240\225\354\210\230\353\245\274 \354\236\205\353\240\245\355\225\230\354\204\270\354\232\224: \0"
.LC1:
	.ascii "%d\0"
	.align 8
.LC2:
	.ascii "\354\236\205\353\240\245\355\225\230\354\213\240 \354\240\225\354\210\230\353\212\224 %d\354\236\205\353\213\210\353\213\244!\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	leaq	.LC0(%rip), %rax
	movq	%rax, %rcx
	call	printf
	leaq	-4(%rbp), %rax
	leaq	.LC1(%rip), %rcx
	movq	%rax, %rdx
	call	scanf
	movl	-4(%rbp), %eax
	leaq	.LC2(%rip), %rcx
	movl	%eax, %edx
	call	printf
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev8, Built by MSYS2 project) 15.2.0"
	.def	printf;	.scl	2;	.type	32;	.endef
	.def	scanf;	.scl	2;	.type	32;	.endef
