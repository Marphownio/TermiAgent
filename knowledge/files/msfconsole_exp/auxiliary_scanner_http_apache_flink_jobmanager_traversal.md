**The description of current metasploit exploit**
This module exploits an unauthenticated directory traversal vulnerability          in Apache Flink versions 1.11.0 <= 1.11.2. The JobManager REST API fails          to validate user-supplied log file paths, allowing retrieval of arbitrary          files with the privileges of the web server user.          This module has been tested successfully on Apache Flink version 1.11.2          on Ubuntu 18.04.4.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/apache_flink_jobmanager_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8081 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.