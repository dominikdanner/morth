# Morth

**WARNING! THIS LANGUAGE IS A WORKING PROGRESS. THIS IS JUST A HOBBY PROJECT**

Inspired by [Tsoding](https://www.youtube.com/c/TsodingDaily)

Roudmap for Morth (Milestones)
- [x] Compiled
- [x] Interpreted (Simulated) 
- [x] Stack based 
- [ ] Easy to use (for a stack based language)
- [ ] Turing-complete 
- [ ] Dynamically typed
- [ ] Optimized 

#### Syntax Example

```python
30 30 + 60 = if
    100 print
end

// Output: 100

```

## Workflow of the compiler
- Analysing Source File
- -> Converting Words in Operation Codes
- -> Generating Assembly Code
- -> Compiling Assembly with NASM
- -> Linking Objectfile with the GNU Linker
- -> Selfcontaining Executable
