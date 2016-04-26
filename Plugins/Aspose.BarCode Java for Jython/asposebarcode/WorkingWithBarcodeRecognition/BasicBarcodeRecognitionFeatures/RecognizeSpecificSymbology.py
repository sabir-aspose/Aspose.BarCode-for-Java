from asposebarcode import Settings
from com.aspose.barcoderecognition import BarCodeReadType
from com.aspose.barcoderecognition import BarCodeReader

class RecognizeSpecificSymbology:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithBarcodeRecognition/AdvancedBarcodeRecognitionFeatures/RecognizeSpecificSymbology/'
        
        # initialize barcode reader
        img = dataDir + "barcode.jpg"
        barcode_reader_type = BarCodeReadType
        rd = BarCodeReader(img, barcode_reader_type.Code39Standard)

        # read barcode
        while (rd.read()):
            # print the code text, if barcode found
            print "CodeText: "
            print rd.getCodeText()

            # print the symbology type
            print "Type: "
            print rd.getReadType()

if __name__ == '__main__':        
    RecognizeSpecificSymbology()