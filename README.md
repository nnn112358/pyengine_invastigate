# pyengine_invastigate

This is a repository for reproducing this issue.
https://github.com/AXERA-TECH/pyaxengine/issues/22


```
root@m5stack-LLM:/opt/usr/# git clone https://github.com/nnn112358/pyengine_invastigate

root@m5stack-LLM:/opt/usr/pyengine_invastigate# python pyaxengine_test1.py
[INFO] Available providers:  ['AxEngineExecutionProvider']
[INFO] Using provider: AxEngineExecutionProvider
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680
Segmentation fault (core dumped)

`
root@m5stack-LLM:/opt/usr/pyengine_invastigate# python pyaxengine_test2.py
[INFO] Available providers:  ['AxEngineExecutionProvider']
[INFO] Using provider: AxEngineExecutionProvider
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680
Outputs saved to outputs.npy
```

```
root@m5stack-LLM:/opt/usr/pyengine_invastigate# gdb python
(gdb) run pyaxengine_test1.py
Starting program: /usr/bin/python pyaxengine_test1.py
[Detaching after vfork from child process 9032]
[Detaching after vfork from child process 9033]
[Detaching after vfork from child process 9036]
[Detaching after vfork from child process 9037]
[Detaching after vfork from child process 9038]
[Detaching after vfork from child process 9041]
[Detaching after vfork from child process 9042]
[INFO] Available providers:  ['AxEngineExecutionProvider']
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
warning: Cannot parse .gnu_debugdata section; LZMA support was disabled at compile time
[New Thread 0xfffff55cf120 (LWP 9043)]
[INFO] Using provider: AxEngineExecutionProvider
[Detaching after vfork from child process 9048]
[Detaching after vfork from child process 9049]
[Detaching after vfork from child process 9052]
[Detaching after vfork from child process 9053]
[Detaching after vfork from child process 9054]
[Detaching after vfork from child process 9055]
[Detaching after vfork from child process 9056]
[Detaching after vfork from child process 9059]
[Detaching after vfork from child process 9060]
[New Thread 0xfffff281f120 (LWP 9061)]
[New Thread 0xfffff260f120 (LWP 9064)]
[New Thread 0xfffff23ff120 (LWP 9065)]
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680

Thread 1 "python" received signal SIGSEGV, Segmentation fault.
0x0000fffff7d97c58 in ?? () from /lib/aarch64-linux-gnu/libc.so.6
```

