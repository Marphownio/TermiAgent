**The description of current metasploit exploit**
The Moxa protocol listens on 4800/UDP and will respond to broadcast          or direct traffic.  The service is known to be used on Moxa devices          in the NPort, OnCell, and MGate product lines.          A discovery packet compels a Moxa device to respond to the sender          with some basic device information that is needed for more advanced          functions.  The discovery data is 8 bytes in length and is the most          basic example of the Moxa protocol.  It may be sent out as a          broadcast (destination 255.255.255.255) or to an individual device.          Devices that respond to this query may be vulnerable to serious          information disclosure vulnerabilities, such as CVE-2016-9361.          The module is the work of Patrick DeSantis of Cisco Talos and is          derived from original work by K. Reid Wightman. Tested and validated          on a Moxa NPort 6250 with firmware versions 1.13 and 1.15.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/scada/moxa_discover
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 4800 - The target port (UDP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.