**The description of current metasploit exploit**
This module check and exploits a directory traversal vulnerability in Total.js prior to 3.2.4.          Here is a list of accepted extensions: flac, jpg, jpeg, png, gif, ico, js, css, txt, xml,          woff, woff2, otf, ttf, eot, svg, zip, rar, pdf, docx, xlsx, doc, xls, html, htm, appcache,          manifest, map, ogv, ogg, mp4, mp3, webp, webm, swf, package, json, md, m4v, jsx, heif, heic

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/totaljs_traversal
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