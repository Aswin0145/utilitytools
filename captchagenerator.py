from captcha.image import ImageCaptcha
from utilitymodule import generator

image = ImageCaptcha(width = 280, height = 90)
captcha = generator("captcha")
print(captcha)
data = image.generate(captcha)
image.write(captcha, 'CAPTCHA.png')
