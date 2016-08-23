import time
import os

study=0;
breaktime=0
while 1:
    now = time.time()
    future = now + 30000
    saved=0;
    while time.time() < future:
        if(int(time.time()-now)-saved>0.5):
            os.system('clear')
            saved=int(time.time()-now)
            print("===============================STUDY TIME===============================")
            print("Time Remaining:",3000-int(time.time()-now))  
            print("Time Spent Studying:",study+int(time.time()-now))
            print("Time On Break", breaktime)
        pass
    print("Done")
    study=study+3000;
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 200))
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 150))
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 200))
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 150))
    now = time.time()
    future = now + 600
    saved=0;
    while time.time() < future:
        if(int(time.time()-now)-saved>0.5):
            os.system('clear')
            saved=int(time.time()-now)
            print("===============================BREAK TIME===============================")
            print("Time Remaining:",600-int(time.time()-now))
            print("Time Spent Studying:",study)
            print("Time On Break", breaktime+int(time.time()-now))  
        pass
    print("Done")
    breaktime=breaktime+600