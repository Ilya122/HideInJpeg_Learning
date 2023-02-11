from PIL import Image
import base64

class MessageHider:
    def __init__(self, fileName):
        self.__fileName = fileName + '.png'
        self.__hiddenFile = fileName + '_hidden.png'

    def Hide(self, message):
        msgLen = len(message)
        with Image.open(self.__fileName) as im:
            firstPixel = im.getpixel((0, 0))
            newPix = (firstPixel[0], firstPixel[1], msgLen)
            im.putpixel((0, 0), newPix)

            for i in range(msgLen):
                pixel = im.getpixel((0, i+1))
                newPix = (pixel[0], pixel[1], int(ord(message[i])))
                im.putpixel((0, i + 1), newPix)
            im.save(self.__hiddenFile)


    def HideBase64(self, message):
        msgLen = len(message)
        with Image.open(self.__fileName) as im:
            encoded = base64.b64encode(message.encode())
            msgLen = len(encoded)
            firstPixel = im.getpixel((0, 0))
            newPix = (firstPixel[0], firstPixel[1], msgLen)
            im.putpixel((0, 0), newPix)
            
            for i in range(msgLen):
                pixel = im.getpixel((0, i+1))
                newPix = (pixel[0], pixel[1], int(encoded[i]))
                im.putpixel((0, i + 1), newPix)
            im.save(self.__hiddenFile)
            
            
    def Show(self):
        message = ''

        with Image.open(self.__hiddenFile) as im:
            length = im.getpixel((0, 0))
            length = length[2]
            for i in range(length):
                message += chr(im.getpixel((0, (i+1)))[2])

        return message

    def ShowAscii(self):
        message = ''

        with Image.open(self.__hiddenFile) as im:
            width = im.size[0]
            height = im.size[1]
            for x in range(width):
                for y in range(height):
                    print(chr(im.getpixel((x, y))[2]), end=' ')
                break

        return message


hider = MessageHider(
    'C:\\Users\\ASUS\\AppData\\Local\\Temp\\PY\\HideInJpeg\\cat')

hider.HideBase64('eval(\'alert(\"hello world\")\')')
print(hider.Show())
hider.ShowAscii()
