import base64
import random
import sys
a=random.sample(range(1, 100), 20)
for i in a:
    num='{0:03}'.format(i)
    image = open('pictures/'+num+'.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    print image_64_encode
    k=input()
    if i<=50:
        my=1
    else:
        my=0
    if k!=my:
        print 'No flag for you!'
        exit(0)
print 'Congrats flag is: xiomara{you_just_processed_an_image}'
