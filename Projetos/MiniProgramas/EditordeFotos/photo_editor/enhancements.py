from PIL import Image, ImageEnhance, ImageFilter

def aumentar_contraste(img, factor=1.5):
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

def aumentar_nitidez(img):
    return img.filter(ImageFilter.SHARPEN)

def ajustar_brilho(img, factor=1.5):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def converter_cinza(img):
    return img.convert('L')

def rotacionar_imagem(img, angulo):
    return img.rotate(angulo)
