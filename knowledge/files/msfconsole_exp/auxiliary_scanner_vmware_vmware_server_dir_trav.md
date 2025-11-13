**The description of current metasploit exploit**
This modules exploits the VMware Server Directory Traversal        vulnerability in VMware Server 1.x before 1.0.10 build 203137 and 2.x before        2.0.2 build 203138 on Linux, VMware ESXi 3.5, and VMware ESX 3.0.3 and 3.5        allows remote attackers to read arbitrary files. Common VMware server ports        80/8222 and 443/8333 SSL.  If you want to download the entire VM, check out        the gueststealer tool.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/vmware/vmware_server_dir_trav
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8222 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.