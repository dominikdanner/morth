BITS 64
global _start
dump:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 64
    mov     QWORD [rbp-56], rdi
    mov     QWORD [rbp-8], 1
    mov     eax, 32
    sub     rax, QWORD [rbp-8]
    mov     BYTE [rbp-48+rax], 10
.L2:
    mov     rcx, QWORD [rbp-56]
    mov     rdx, 7378697629483820647
    mov     rax, rcx
    imul    rdx
    mov     rax, rdx
    sar     rax, 2
    mov     rsi, rcx
    sar     rsi, 63
    sub     rax, rsi
    mov     rdx, rax
    mov     rax, rdx
    sal     rax, 2
    add     rax, rdx
    add     rax, rax
    sub     rcx, rax
    mov     rdx, rcx
    mov     eax, edx
    lea     edx, [rax+48]
    mov     eax, 31
    sub     rax, QWORD [rbp-8]
    mov     BYTE [rbp-48+rax], dl
    add     QWORD [rbp-8], 1
    mov     rcx, QWORD [rbp-56]
    mov     rdx, 7378697629483820647
    mov     rax, rcx
    imul    rdx
    mov     rax, rdx
    sar     rax, 2
    sar     rcx, 63
    mov     rdx, rcx
    sub     rax, rdx
    mov     QWORD [rbp-56], rax
    cmp     QWORD [rbp-56], 0
    jne     .L2
    mov     eax, 32
    sub     rax, QWORD [rbp-8]
    lea     rdx, [rbp-48]
    lea     rcx, [rdx+rax]
    mov     rax, QWORD [rbp-8]
    mov     rdx, rax
    mov     rsi, rcx
    mov     edi, 1
    mov     rax, 1
    syscall
    nop
    leave
    ret

_start:
    ;; -- push --
    push 30
    ;; -- duplicate --
    pop rax
    push rax
    push rax
    ;; -- plus --
    pop rax
    pop rdx
    add rax, rdx
    push rax
    ;; -- push --
    push 50
    ;; -- equal --
    mov rcx, 0
    mov rbx, 1
    pop rax
    pop rdx
    cmp rax, rdx
    cmove rcx, rbx
    push rcx
    ;; -- if --
    pop rax
    test rax, rax
    jz addr_8
    ;; -- push --
    push 1
    ;; -- dump --
    pop rdi
    call dump
    ;; -- end --
addr_8:
    ;; -- push --
    push 30
    ;; -- duplicate --
    pop rax
    push rax
    push rax
    ;; -- plus --
    pop rax
    pop rdx
    add rax, rdx
    push rax
    ;; -- push --
    push 60
    ;; -- equal --
    mov rcx, 0
    mov rbx, 1
    pop rax
    pop rdx
    cmp rax, rdx
    cmove rcx, rbx
    push rcx
    ;; -- if --
    pop rax
    test rax, rax
    jz addr_17
    ;; -- push --
    push 2
    ;; -- dump --
    pop rdi
    call dump
    ;; -- end --
addr_17:
    ;; -- push --
    push 30
    ;; -- duplicate --
    pop rax
    push rax
    push rax
    ;; -- plus --
    pop rax
    pop rdx
    add rax, rdx
    push rax
    ;; -- push --
    push 50
    ;; -- equal --
    mov rcx, 0
    mov rbx, 1
    pop rax
    pop rdx
    cmp rax, rdx
    cmove rcx, rbx
    push rcx
    ;; -- if --
    pop rax
    test rax, rax
    jz addr_26
    ;; -- push --
    push 3
    ;; -- dump --
    pop rdi
    call dump
    ;; -- end --
addr_26:
    ;; -- push --
    push 30
    ;; -- duplicate --
    pop rax
    push rax
    push rax
    ;; -- plus --
    pop rax
    pop rdx
    add rax, rdx
    push rax
    ;; -- push --
    push 50
    ;; -- equal --
    mov rcx, 0
    mov rbx, 1
    pop rax
    pop rdx
    cmp rax, rdx
    cmove rcx, rbx
    push rcx
    ;; -- if --
    pop rax
    test rax, rax
    jz addr_35
    ;; -- push --
    push 4
    ;; -- dump --
    pop rdi
    call dump
    ;; -- end --
addr_35:
    mov rax, 60
    mov rdi, 0
    syscall
