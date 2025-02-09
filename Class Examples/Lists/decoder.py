encrypted_text = "·ËÌÖÌÖÄ×ÈÖ×¤¥¦ÄÅÆ"

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 99
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)
