# pyengine_invastigate

This is a repository for reproducing this issue.
https://github.com/AXERA-TECH/pyaxengine/issues/22
## Problem Description

## Environment 
Board name: m5stack-LLM
axengine:PyAXEngine 0.1.0 RC1
m5stack-LLM firmware:M5_LLM_ubuntu_v1.3_20241203-mini


```
root@m5stack-LLM: # pip list | grep axengine
axengine           0.1.0

root@m5stack-LLM: # uname -a
Linux m5stack-LLM 4.19.125 #1 SMP PREEMPT Wed Nov 20 14:43:36 CST 2024 aarch64 aarch64 aarch64 GNU/Linux
```

### Steps to reproduce

### bad case
 pyaxengine_test1.py is bad code. Segmentation fault in session.run.

```
root@m5stack-LLM:# python pyaxengine_test1.py
[INFO] Available providers:  ['AxEngineExecutionProvider']
[INFO] Using provider: AxEngineExecutionProvider
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680
Segmentation fault (core dumped)
```

```pyaxengine_test1.py
import axengine as axe
import numpy as np

def main():
    try:
        session = axe.InferenceSession('yolo11s.axmodel')
        input_data = np.random.randint(0, 255, (1, 640, 640, 3), dtype=np.uint8)
        outputs = session.run([o.name for o in session.get_outputs()], 
                           {session.get_inputs()[0].name: input_data})
        
        np.save('outputs.npy', outputs[0])
        print("Outputs saved to outputs.npy")
        
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
```

### good case

 pyaxengine_test2.py is good code.  Only the source code order is different.

```
root@m5stack-LLM: python pyaxengine_test2.py
[INFO] Available providers:  ['AxEngineExecutionProvider']
[INFO] Using provider: AxEngineExecutionProvider
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680
Outputs saved to outputs.npy
```


```pyaxengine_test2.py
import axengine as axe
import numpy as np

def main():
    try:
        input_data = np.random.randint(0, 255, (1, 640, 640, 3), dtype=np.uint8)
        session = axe.InferenceSession('yolo11s.axmodel')
        outputs = session.run([o.name for o in session.get_outputs()], 
                           {session.get_inputs()[0].name: input_data})
        
        np.save('outputs.npy', outputs[0])
        print("Outputs saved to outputs.npy")
        
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
```

Place the source code here.
https://github.com/nnn112358/pyengine_invastigate

### Detail GDB Log 

This is Detail GDB Log.
```
root@m5stack-LLM:/opt/usr/pyengine_invastigate# gdb python
(gdb) run pyaxengine_test1.py
Starting program: /usr/bin/python pyaxengine_test1.py
[Detaching after vfork from child process 9356]
[Detaching after vfork from child process 9357]
[Detaching after vfork from child process 9360]
[Detaching after vfork from child process 9361]
[Detaching after vfork from child process 9362]
[Detaching after vfork from child process 9365]
[Detaching after vfork from child process 9366]
[INFO] Available providers:  ['AxEngineExecutionProvider']
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
warning: Cannot parse .gnu_debugdata section; LZMA support was disabled at compile time
[New Thread 0xfffff55cf120 (LWP 9369)]
[INFO] Using provider: AxEngineExecutionProvider
[Detaching after vfork from child process 9372]
[Detaching after vfork from child process 9373]
[Detaching after vfork from child process 9376]
[Detaching after vfork from child process 9377]
[Detaching after vfork from child process 9378]
[Detaching after vfork from child process 9381]
[Detaching after vfork from child process 9382]
[Detaching after vfork from child process 9385]
[Detaching after vfork from child process 9386]
[New Thread 0xfffff281f120 (LWP 9387)]
[New Thread 0xfffff260f120 (LWP 9390)]
[New Thread 0xfffff23ff120 (LWP 9391)]
[INFO] Chip type: ChipType.MC20E
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Engine version: 2.6.3sp
[INFO] Model type: 1 (full core)
[INFO] Compiler version: 3.2-patch1 2b3a4680

Thread 1 "python" received signal SIGSEGV, Segmentation fault.
0x0000fffff7d97c58 in ?? () from /lib/aarch64-linux-gnu/libc.so.6

(gdb) bt
#0  0x0000fffff7d97c58 in ?? () from /lib/aarch64-linux-gnu/libc.so.6
#1  0x0000fffff2b34060 in b_memmove (self=<optimized out>,
    args=<optimized out>, kwds=<optimized out>) at src/c/_cffi_backend.c:7430
#2  0x0000aaaaaabadb94 in ?? ()
#3  0x0000aaaaaaba4180 in _PyObject_MakeTpCall ()
#4  0x0000aaaaaab9b440 in _PyEval_EvalFrameDefault ()
#5  0x0000aaaaaabae828 in _PyFunction_Vectorcall ()
#6  0x0000aaaaaab968ec in _PyEval_EvalFrameDefault ()
#7  0x0000aaaaaabae828 in _PyFunction_Vectorcall ()
#8  0x0000aaaaaab968ec in _PyEval_EvalFrameDefault ()
#9  0x0000aaaaaabae828 in _PyFunction_Vectorcall ()
#10 0x0000aaaaaab968ec in _PyEval_EvalFrameDefault ()
#11 0x0000aaaaaabae828 in _PyFunction_Vectorcall ()
#12 0x0000aaaaaab967b0 in _PyEval_EvalFrameDefault ()
#13 0x0000aaaaaac92d90 in ?? ()
#14 0x0000aaaaaac92c14 in PyEval_EvalCode ()
#15 0x0000aaaaaacc65cc in ?? ()
#16 0x0000aaaaaacbecd8 in ?? ()
#17 0x0000aaaaaacc627c in ?? ()
#18 0x0000aaaaaacc53e4 in _PyRun_SimpleFileObject ()
#19 0x0000aaaaaacc4fb0 in _PyRun_AnyFileObject ()
#20 0x0000aaaaaacb5870 in Py_RunMain ()
#21 0x0000aaaaaac83d08 in Py_BytesMain ()
```

