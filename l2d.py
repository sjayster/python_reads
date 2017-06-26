l1 = ['_[1.2.3.4, 5.6.7.8]_', "port1: speed 100",
      "port2: vlan 10", "port3: trunk", '_3.3.3.3_', "port1: shut"]
l2 = ['_[1.2.3.4, 5.6.7.8]_', "port1: Eth1/1:FabricA", "port2: FC1/1",
      "port3: Eth2/2", "_3.3.3.3_", "port1: Eth15/16: access"]

d = {}

for items in l2:
    if "_" in items:
        d[items] = {}
        tmpk = items

    if ":" in items:
        word = items.split(":")
        d[tmpk][word[0]] = word[1:]

# print d

result = []
for items in l1:
    if "_" in items:
        tmpd = d[items]
        if items not in result:
            result.append(items)

    if ":" in items:
        t = items.split(":")
        if t[0] in tmpd:
            result.append(tmpd[t[0]])

# print result

for elt in result:
    print " ".join(elt)
