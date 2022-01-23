#! /usr/bin/python3
import sys
import subprocess
import os

iota_counter = 0
def iota(reset=False):
  global iota_counter
  if reset:
    iota_counter = 0
  result = iota_counter 
  iota_counter += 1
  return result 

OP_PUSH = iota(True)
OP_PLUS = iota()
OP_MINUS = iota()
OP_EQUAL = iota()
OP_PRINT = iota()
OP_DUP = iota() 
OP_COUNT = iota()

def load_program_from_file(file_path):
  try:
    with open(file_path,"r") as f:
        program =  f.readlines()
        lexed_program = lex_file(program, file_path)
        return parse_as_op(lexed_program)
  except FileNotFoundError:
    print("[ERROR] File `%s` not found" % file_path)
    exit(1)

def find_col(line):
    return 0

def lex_line(line):
    tokens = line.split()
    for (idx, token) in enumerate(tokens):
        yield (find_col(line), token)

def lex_file(program, filepath):
    return [(filepath, row, col, token)
            for(row, line) in enumerate(program)
            for(col, token) in lex_line(line)]

def parse_token_as_op(token):
    (filepath, row, col, word) = token
    loc = (row, col)

    if word == "print":
        yield {'type': OP_PRINT, 'loc': loc}
    elif word == "+":
        yield {'type': OP_PLUS, 'loc': loc}
    elif word == "-":
        yield {'type': OP_MINUS, 'loc': loc}
    elif word == "=":
        yield {'type': OP_EQUAL, 'loc': loc}
    elif word == "dup":
        yield {'type': OP_DUP, 'loc': loc}
    else:
        try:
            yield {'type': OP_PUSH, 'value': int(word) ,'loc': loc}
        except ValueError:
            print("%s:%s:%s: `%s` does not exist" % (filepath, row, col, word))
            exit(1)

# A Word is a turple that the lexer generated
# It contains `filepath, location: (row, col), token`
def parse_as_op(program):
  return [op for Word in program 
          for op in parse_token_as_op(Word)]
    
def simulate_program(file_path):
    program = load_program_from_file(file_path)

    stack = []
    for Word in program:
      if Word['type'] == OP_PUSH:
        stack.append(Word['type'][1])
      elif Word['type'] == OP_PLUS:
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)
      elif Word['type'] == OP_MINUS:
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
      elif Word['type'] == OP_DUMP:
        if len(stack) == 0:
          print("Cannot `dump` from empty stack")
          exit(1)
        print(stack.pop())
      elif Word['type'] == OP_EQUAL:
        a = stack.pop()
        b = stack.pop()
        stack.append(int(a == b))
      elif Word['type'] == OP_DUP:
          a = stack.pop()
          b = a
          stack.append(a)
          stack.append(b)

def compile_program(source_path, output_path):
    with open(output_path, "w") as out:
        program = load_program_from_file(source_path)

        out.write("BITS 64\n") 
        out.write("global _start\n") 
        out.write("section .text\n\n")
        out.write("dump:\n")
        out.write("    push    rbp\n")
        out.write("    mov     rbp, rsp\n")
        out.write("    sub     rsp, 64\n")
        out.write("    mov     QWORD [rbp-56], rdi\n")
        out.write("    mov     QWORD [rbp-8], 1\n")
        out.write("    mov     eax, 32\n")
        out.write("    sub     rax, QWORD [rbp-8]\n")
        out.write("    mov     BYTE [rbp-48+rax], 10\n")
        out.write(".L2:\n")
        out.write("    mov     rcx, QWORD [rbp-56]\n")
        out.write("    mov     rdx, 7378697629483820647\n")
        out.write("    mov     rax, rcx\n")
        out.write("    imul    rdx\n")
        out.write("    mov     rax, rdx\n")
        out.write("    sar     rax, 2\n")
        out.write("    mov     rsi, rcx\n")
        out.write("    sar     rsi, 63\n")
        out.write("    sub     rax, rsi\n")
        out.write("    mov     rdx, rax\n")
        out.write("    mov     rax, rdx\n")
        out.write("    sal     rax, 2\n")
        out.write("    add     rax, rdx\n")
        out.write("    add     rax, rax\n")
        out.write("    sub     rcx, rax\n")
        out.write("    mov     rdx, rcx\n")
        out.write("    mov     eax, edx\n")
        out.write("    lea     edx, [rax+48]\n")
        out.write("    mov     eax, 31\n")
        out.write("    sub     rax, QWORD [rbp-8]\n")
        out.write("    mov     BYTE [rbp-48+rax], dl\n")
        out.write("    add     QWORD [rbp-8], 1\n")
        out.write("    mov     rcx, QWORD [rbp-56]\n")
        out.write("    mov     rdx, 7378697629483820647\n")
        out.write("    mov     rax, rcx\n")
        out.write("    imul    rdx\n")
        out.write("    mov     rax, rdx\n")
        out.write("    sar     rax, 2\n")
        out.write("    sar     rcx, 63\n")
        out.write("    mov     rdx, rcx\n")
        out.write("    sub     rax, rdx\n")
        out.write("    mov     QWORD [rbp-56], rax\n")
        out.write("    cmp     QWORD [rbp-56], 0\n")
        out.write("    jne     .L2\n")
        out.write("    mov     eax, 32\n")
        out.write("    sub     rax, QWORD [rbp-8]\n")
        out.write("    lea     rdx, [rbp-48]\n")
        out.write("    lea     rcx, [rdx+rax]\n")
        out.write("    mov     rax, QWORD [rbp-8]\n")
        out.write("    mov     rdx, rax\n")
        out.write("    mov     rsi, rcx\n")
        out.write("    mov     edi, 1\n")
        out.write("    mov     rax, 1\n")
        out.write("    syscall\n")
        out.write("    nop\n")
        out.write("    leave\n")
        out.write("    ret\n\n")
        out.write("_start:\n")
    
        for op in program:
            if op['type'] == OP_PUSH:
              out.write("    ;; -- push --\n")
              out.write("    push %s\n" % op['value'])
            elif op['type'] == OP_PRINT:
              out.write("    ;; -- dump --\n")
              out.write("    pop rdi\n")
              out.write("    call dump\n")
            elif op['type'] == OP_PLUS:
              out.write("    ;; -- plus --\n")
              out.write("    pop rax\n")
              out.write("    pop rdx\n")
              out.write("    add rax, rdx\n")
              out.write("    push rax\n")
            elif op['type'] == OP_MINUS:
              out.write("    pop rax\n")
              out.write("    pop rdx\n")
              out.write("    sub rdx, rax\n")
              out.write("    push rdx\n")
            elif op['type'] == OP_EQUAL:
              out.write("    ;; -- equal --\n")
              out.write("    mov rcx, 0\n")
              out.write("    mov rbx, 1\n")
              out.write("    pop rax\n")
              out.write("    pop rdx\n")
              out.write("    cmp rax, rdx\n")
              out.write("    cmove rcx, rbx\n")
              out.write("    push rcx\n")
            elif op['type'] == OP_DUP:
              out.write("    pop rax\n")
              out.write("    mov rbx, rax\n")
              out.write("    push rax\n")
              out.write("    push rbx\n")
        
        out.write("    mov rax, 60\n")
        out.write("    syscall\n")

def unconst(target):
  try:
    del target[0]
    return (target[0], target)
  except IndexError:
    return (None, None) 

def run_cmd(cmd):
    print("[CMD] %s" % ' '.join(cmd))
    subprocess.call(cmd)

def usage():
    print("Usage: <MODE> <ARGUMENTS> <FLAGS>")
    print(" * Compiling: com <filepath> <autorun>")
    print("    - Compiling into nativ machine code")
    print("    - autorun <flag for running program automaticly>")
    print(" * Simulating: sim <filepath>")
    print("    - Simulating program in python")
  
if __name__ == "__main__":
  (mode, argv)= unconst(sys.argv) 

  if mode == "sim":
    (target_file, argv)= unconst(argv) 
    print("[INFO] Simulating %s" % target_file)
    simulate_program(target_file)
  elif mode == "com":
    (source_path, argv) = unconst(argv) 
    output_name = os.path.basename(source_path).split(".")[0] 

    print("[INFO] Generating %s.asm" % output_name)
    compile_program(source_path, "%s.asm" % output_name)
    run_cmd(["nasm", "-f", "elf64", "%s.asm" % output_name, "-o", "%s.o" % output_name])
    run_cmd(["ld", "%s.o" % output_name, "-o", "%s" % output_name])
    
    (flag, argv) = unconst(argv) 
    if flag == "-r":
      run_cmd(["./%s" % output_name])
    else:
      print("[ERROR] Flag `%s` not found" % flag)
  elif mode == "help":
    usage()
  else:
    usage() 
