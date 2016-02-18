import os, shutil
cd = "~/Desktop"
ss_folder = "Screenshots/"
cd = os.path.expanduser(cd)+"/"
moved = 0

for f in os.listdir(cd):
    if f.startswith("Screen Shot "):
        shutil.move(cd+f, cd+ss_folder+f)
        moved+=1

print("Moved {} files".format(moved))
