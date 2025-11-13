**The description of current metasploit exploit**
A vulnerability in Internet Key Exchange version 1 (IKEv1) packet          processing code in Cisco IOS, Cisco IOS XE, and Cisco IOS XR Software          could allow an unauthenticated, remote attacker to retrieve memory          contents, which could lead to the disclosure of confidential information.          The vulnerability is due to insufficient condition checks in the part          of the code that handles IKEv1 security negotiation requests.          An attacker could exploit this vulnerability by sending a crafted IKEv1          packet to an affected device configured to accept IKEv1 security          negotiation requests. A successful exploit could allow the attacker          to retrieve memory contents, which could lead to the disclosure of          confidential information.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ike/cisco_ike_benigncertain
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 500 - The target port

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.