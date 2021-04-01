from pyzbar import pyzbar
import cv2
import argparse
import json

class DecodeResult:
    def __init__(self, barcode):
        self.barcode = barcode.decode("utf-8")


def decode(image):
    decoded_objects = pyzbar.decode(image)
    
    barcodes = []
    for obj in decoded_objects:
        barcodes.append(DecodeResult(obj.data))

    return barcodes

def obj_dict(obj):
    return obj.__dict__

if __name__ == "__main__":
    from glob import glob

    parser = argparse.ArgumentParser()
    parser.add_argument("--f", help="path to image with isbn barcode")
    args = parser.parse_args()
    
    decoded = []
    try:
        img = cv2.imread(args.f)
        decoded = decode(img)
    except:
        None

    jsonStr = json.dumps(decoded, default = lambda x: x.__dict__)
    print(jsonStr)
