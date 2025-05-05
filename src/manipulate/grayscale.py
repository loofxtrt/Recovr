from PIL import Image

def grayscale(image):
    # converter pra escala de cinza e logo depois converter pra rgb de volta, agora dessaturada
    image = image.convert('L').convert('RGB')
    return image