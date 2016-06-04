
import zlib

me = "LLFLFLFLFLFL"

comp = zlib.compress(me)
decomp = zlib.decompress(comp)

print "Originl",repr(me)
print "Comp",repr(comp)
print "decomp",repr(decomp)
