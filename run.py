#!/usr/bin/env python
from base64 import b64decode
import sys
import time
import random
def typeprint(string):
	x=""
	for i in string:
		x+=i
		print(x,end="\r")
		z=random.randint(50,100)
		time.sleep(z/1000)
	time.sleep(2)
	x=""
	for i in string:
		x+=" "
	print(x,end="\r")
def getstring(code):
	out=b64decode(code).decode("utf-8")
	out=out.strip()
	return out
typeprint(getstring("R2l0SHViIHdhcyBhIHdvbmRlcmZ1bCBwbGF0Zm9ybS4uLgo="))
typeprint(getstring("SXQgc3RhcnRlZCBmYWxsaW5nIGFwYXJ0IHdpdGggZm91bmRlciByZXNpZ25pbmcuLi4K"))
typeprint(getstring("Tm93IG1pY3Jvc29mdCBib3VnaHQgaXQhIAo="))
typeprint(getstring("TWljcm9zb2Z0IGlzIGEgY29tcGFueSB0aGF0IGhhcyBubyByZWFzb24gdG8gZXhpc3QuLi4gCg=="))
typeprint(getstring("Tm93IHRoZXkgYXJlIGdvaW5nIGtpbGwgdGhpcyB3b25kZXJmdWwgcGxhdGZvcm0sIAo="))
typeprint(getstring("V2hpY2ggZXZlcnlvbmUgbG92ZXMhIAo="))
typeprint(getstring("SSBkb250IGtub3cgd2hhdCBpcyBnb2luZyB0byBoYXBwZW4sIAo="))
typeprint(getstring("QnV0IG15IG1pbmQgc2F5cyBpdHMgZ29pbmcgdG8gYmUgYmFkISAK"))
typeprint(getstring("QW5kIG5vdyBJIGFtIG1vdmluZyB0byBnaXRsYWIsIGZyb20gdGhlIHBsYXRmb3JtIAo="))
typeprint(getstring("SSBsb3ZlZCB0aGUgbW9zdCEgCg=="))
typeprint(getstring("QW0gSSBzYWQsIHllcyB3aHkgbm90Li4gQnV0IHRoZSBzaGlwIGlzIGFscmVhZHkgc2lua2luZyAK"))
typeprint(getstring("VGhlcmUgaXMgbm8gcmVhc29uIHRvIGRpZSB3aXRoIGl0Cg=="))
typeprint(getstring("U28gZmFyZVdlbGwgZ2l0aHViLCB5b3UgbWFkZSBpdCBhbGwgaGFwcGVuLCBUaGFuayB5b3UhIAo="))
i=getstring('''X19fX19fICAgICAgICAgICAgICBfICAgIF8gICAgICBfIF8gICBfX19fXyBfIF8gICBfICAgICAg
ICAgICBfICAgICAKfCAgX19ffCAgICAgICAgICAgIHwgfCAgfCB8ICAgIHwgfCB8IHwgIF9fIChf
KSB8IHwgfCAgICAgICAgIHwgfCAgICAKfCB8XyBfXyBfIF8gX18gX19fIHwgfCAgfCB8IF9fX3wg
fCB8IHwgfCAgXC9ffCB8X3wgfF9fICBfICAgX3wgfF9fICAKfCAgXy8gX2AgfCAnX18vIF8gXHwg
fC9cfCB8LyBfIFwgfCB8IHwgfCBfX3wgfCBfX3wgJ18gXHwgfCB8IHwgJ18gXCAKfCB8fCAoX3wg
fCB8IHwgIF9fL1wgIC9cICAvICBfXy8gfCB8IHwgfF9cIFwgfCB8X3wgfCB8IHwgfF98IHwgfF8p
IHwKXF98IFxfXyxffF98ICBcX19ffCBcLyAgXC8gXF9fX3xffF98ICBcX19fXy9ffFxfX3xffCB8
X3xcX18sX3xfLl9fLyAK''')
print(i)
