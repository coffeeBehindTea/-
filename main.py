import re

def get_folder(file):
    a = file.split("\\")
    folder = ""
    for i in range(len(a) - 1):
        folder += a[i] + "\\"
    return folder



def remove_almost(file, filter, flash, hall, bloom):

    folder = get_folder(file)

    with open(file, 'r', encoding="UTF-8-sig") as f:
        with open(folder + "processed.adofai", 'w', encoding="UTF-8-sig") as out:
            lines = f.readlines()
            for s in lines:
                a = True if re.findall(r'SetFilter',s) != [] else False
                b = True if re.findall(r'Flash',s) != [] else False
                c = True if re.findall(r'HallOfMirrors',s) != [] else False
                d = True if re.findall(r'Bloom',s) != [] else False

                if not((a and filter) or (b and flash) or (c and hall) or (d and bloom)):
                # if re.findall(r'Flash',s) == []:
                    out.write(s)
