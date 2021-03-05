import cv2
import pytesseract
import os
import re
import shutil

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def load_images_from_folder(folder):
  for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
      text = pytesseract.image_to_string(img)
      try:
        m = re.search('(19[0-9][0-9])', text)
        if m is None:
          # make the image in blue scale and repeat the process again
          img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          text = pytesseract.image_to_string(img)
          m = re.search('(19[0-9][0-9])', text)
        print(m.group(1))
        create_folder_if_not_present(os.getcwd() + '\\' + m.group(1))
        shutil.move(folder + '\\' + filename,
                    os.getcwd() + '\\' + m.group(1) + '\\' + filename)
      except:
        # extra unrecognized images
        create_folder_if_not_present(os.getcwd() + '\\' + "non-segregated")
        shutil.move(folder + '\\' + filename,
                    os.getcwd() + '\\' + "non-segregated" + '\\' + filename)


def create_folder_if_not_present(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)


load_images_from_folder(os.getcwd() + '\\test-data');
