from PIL import Image,ImageOps
import os

def invert_grayscale(filepath):
    image = Image.open(filepath)
    image = image.convert('L')
    image = ImageOps.invert(image)
    # processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + filename)
    # image.save(processed_filepath)
    return image

if __name__ == '__main__':
    invert_grayscale(os.path.join('static', 'uploads', 'euro.jpg'))

