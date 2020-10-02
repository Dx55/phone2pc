
import os, time
path_to_watch = "/storage/emulated/0/Pictures/Screenshots"  #itoddler btfo
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
#print(before)
while 1:
  time.sleep(2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  #removed = [f for f in before if not f in after]
  if added:
    with open('filename', 'w') as f:
      print('durgasoft') #durgasoft doesn't code for tim coock
      f.writelines(added)
    exit(0)
  #if removed: print ("Removed: ", ", ".join (removed))
  before = after
