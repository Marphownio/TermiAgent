**The description of current metasploit exploit**
Chargen is a debugging and measurement tool and a character        generator service. A character generator service simply sends        data without regard to the input.        Chargen is susceptible to spoofing the source of transmissions        as well as use in a reflection attack vector. The misuse of the        testing features of the Chargen service may allow attackers to        craft malicious network payloads and reflect them by spoofing        the transmission source to effectively direct it to a target.        This can result in traffic loops and service degradation with        large amounts of network traffic.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/chargen/chargen_probe
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 19 - The target port (UDP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.