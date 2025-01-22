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
