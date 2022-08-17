import itertools

for i in itertools.chain(range(1, 399), range(501, 523)):
    istr = str(i)
    while (len(istr) < 3):
        istr = "0" + istr
    print(f"import image{istr} from 'assets/images/monsters/{istr}.png'")

print("const MONSTER_IMAGES = {")
for i in itertools.chain(range(1, 399), range(501, 523)):
    istr = str(i)
    while (len(istr) < 3):
        istr = "0" + istr
    print(f"  [`image{istr}`]: image{istr},")
print("}")
