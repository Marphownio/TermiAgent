**The description of current metasploit exploit**
The SMTP service has two internal commands that allow the enumeration        of users: VRFY (confirming the names of valid users) and EXPN (which        reveals the actual address of users aliases and lists of e-mail        (mailing lists)). Through the implementation of these SMTP commands can        reveal a list of valid users.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/smtp/smtp_enum
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 25 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.