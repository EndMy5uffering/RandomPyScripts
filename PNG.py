import struct
import zlib
import math

# code from https://developer.blender.org/diffusion/B/browse/master/release/bin/blender-thumbnailer.py$155
# and https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
class PNG:

    def __init__(self, buffer=None, width = 1, height = 1, bcolor=0xff000000):
        if buffer:
            self.__b = buffer
            self.__w = len(buffer[0])
            self.__h = len(buffer)
        else :
            self.__b = [[bcolor for _ in range(width)] for _ in range(height)]
            self.__w = width
            self.__h = height
        

    def setPixel(self, x, y, color):
        x = self.__rest(x, 0, self.__w-1)
        y = self.__rest(y, 0, self.__h-1)
        self.__b[y][x] = color

    def getPixel(self, x, y):
        x = self.__rest(x, 0, self.width-1)
        y = self.__rest(y, 0, self.height-1)
        return self.__b[y][x]
    
    def __setitem__(self, key, value):
        self.__b[key] = value
    
    def __getitem__(self, index):
        return self.__b[index]

    def __rest(self, n, a, b):
        if n < a:
            n = a
        elif n > b:
            n = b
        return n

    def __write_png(self, buf, width, height):
        # reverse the vertical line order and add null bytes at the start
        width_byte_4 = width * 4
        raw_data = b"".join(b'\x00' + buf[span:span + width_byte_4] for span in range((height - 1) * width * 4, -1, - width_byte_4))

        def png_pack(png_tag, data):
            chunk_head = png_tag + data
            return struct.pack("!I", len(data)) + chunk_head + struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head))

        return b"".join([
            b'\x89PNG\r\n\x1a\n',
            png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
            png_pack(b'IDAT', zlib.compress(raw_data, 9)),
            png_pack(b'IEND', b'')])

    def saveAsPNG(self, filename="temp.png"):
        if any([len(row) != len(self.__b[0]) for row in self.__b]):
            raise ValueError("Array should have elements of equal size") 

        flat = []; list(map(flat.extend, reversed(self.__b)))
        buf = b''.join([struct.pack('>I', ((0xffFFff & i32)<<8)|(i32>>24)) for i32 in flat])
        
        data = self.__write_png(buf, len(self.__b[0]), len(self.__b))
        f = open(filename, 'wb')
        f.write(data)
        f.close()

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def getARGB(color):
    return (color >> 24) & 0xff, (color >> 16) & 0xff, (color >> 8) & 0xff, color & 0xff

def ARGBToHex(a, r, g, b):
    a = clamp(a, 0, 255)
    r = clamp(r, 0, 255)
    g = clamp(g, 0, 255)
    b = clamp(b, 0, 255)
    c = 0
    return ((((((c | a) << 8) | r) << 8) | g) << 8) | b