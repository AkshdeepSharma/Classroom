CIA_blimps = []
for i in range(1, 6):
    blimp = input()
    if "FBI" in blimp:
        CIA_blimps.append(str(i))
if len(CIA_blimps) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(CIA_blimps))
