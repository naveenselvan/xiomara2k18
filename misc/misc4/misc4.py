import base64
import random
import sys
print """  Human or Not??
We are giving you 20 base64 encodings of jpg images.
You just need to tell me if it is a human or not.
print 1 if there is a human and 0 if there is no human!
"""
a=random.sample(range(1, 100), 20)
for i in a:
    num='{0:03}'.format(i)
    image = open('pictures/'+num+'.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    print image_64_encode
    sys.stdout.flush()
    k=raw_input()
    k=int(k)
    if i<=50:
        my=1
    else:
        my=0
    if k!=my:
        print 'No flag for you!'
        exit(0)
print 'Congrats flag is: xiomara{you_just_processed_an_image}'
