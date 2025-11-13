**The description of current metasploit exploit**
This module can identify PostgreSQL 9.0, 9.1, and 9.2 servers that are          vulnerable to command-line flag injection through CVE-2013-1899. This          can lead to denial of service, privilege escalation, or even arbitrary          code execution.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/postgres/postgres_dbname_flag_injection
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 5432 - The target port (TCP)
* THREADS – default: 1 - The number of concurrent threads (max one per host)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```

---
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.