from Table import Table
from Reader import Reader

t = Table()
r = Reader()

try:
    r.run(t.goto)
except KeyboardInterrupt:
    del t
    del r
    print("stopping gracefully")
