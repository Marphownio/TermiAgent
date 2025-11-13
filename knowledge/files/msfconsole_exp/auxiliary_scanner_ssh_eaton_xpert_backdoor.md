**The description of current metasploit exploit**
Eaton Power Xpert Meters running firmware below version 12.x.x.x or          below version 13.3.x.x ship with a public/private key pair that          facilitate remote administrative access to the devices.          Tested on: Firmware 12.1.9.1 and 13.3.2.10.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ssh/eaton_xpert_backdoor
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 22 - The target port

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.