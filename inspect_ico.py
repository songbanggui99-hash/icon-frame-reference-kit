import sys, struct, hashlib, json
from pathlib import Path
b=Path(sys.argv[1]).read_bytes()
if len(b)<6 or b[:4]!=b"\x00\x00\x01\x00": raise ValueError("Not an ICO")
n=struct.unpack_from("<H",b,4)[0]; end=6+16*n
if not n or end>len(b): raise ValueError("Invalid directory")
rows=[]
for i in range(n):
 p=6+16*i; length,offset=struct.unpack_from("<II",b,p+8)
 if not length or offset<end or offset+length>len(b): raise ValueError("Invalid frame byte range")
 payload=b[offset:offset+length]
 rows.append(dict(entry=i+1,width=b[p] or 256,height=b[p+1] or 256,bytes=length,encoding="PNG" if payload.startswith(b"\x89PNG\r\n\x1a\n") else "DIB or other",sha256=hashlib.sha256(payload).hexdigest()))
print(json.dumps(rows,indent=2))
