import base64
from io import BytesIO
from PIL import Image

# Coloque sua imagem em base64 aqui 
base64_image = "iVBORw0KGgoAAAANSUhEUgAAAA8AAABaCAMAAABQS/w8AAAAA3NCSVQICAjb4U/gAAAAwFBMVEX///8IGyMjqwDBCgDWLQAQrwAIEiPhQADFIABDpQD/dwA1pQD/hwAAACmjOAAUECOsmQCIUgZxDwb/ZgDmVgCLOwZaqQCAKQeOFgB2pAD2WgDbkACRlgDvVgC2WQA8YgUAACkzMzPPkgDshAC+jQD///9qnQBtagAcdgBVXAYAATuSngBVbwCDBQAAAADv9PKhoaGJZQBCAGAzMzP26ugysQCpXwASVAP///8XGRQIGyNycnIiIiJmZmYAAAAnJycGvpX/AAAAQHRSTlMAd/////93////////M/93/////////////////////yKI//////////8i////Iv///xFE/////xEzM2aZ3Xe7lQEPkwAAAAlwSFlzAAALEgAACxIB0t1+/AAAABZ0RVh0Q3JlYXRpb24gVGltZQAwNC8wNC8xN+KP8MYAAAAcdEVYdFNvZnR3YXJlAEFkb2JlIEZpcmV3b3JrcyBDUzbovLKMAAABqklEQVQ4jY3U6XaCMBAFYLUWV4yI1CJSRVERW1RcqArm/d+qEwLJuJ7efx+ZTGIIFgosAaXHgswlWa9pIBgkq+l0TeXwerraTZMAe/XSO0hyOUKYiz9vkE7Cgnz+hSCf8vn/9PbK1Q6lTubPKqRzCoJri/pHLmOXHzl2nCsXt1thSG+E6plPz10plys9/8YKyfu1UseONATVc6svbaP9tLrMJ7Hflt3t2j15XqkN1B/cN9Tn7t9bN9B6um3rBmXJ3O/rhnOGMCvc4r4oX6lV6bqu1+/sI0MMcV6PraH6Zr3e1NQXhmijG5P8vJRDczJpanFMriz7HybMKrJlTbAtCPLGGo8tNJ9bvA9lM3bdsaaK9bnl/jYueI76ue22izxvQxaiP+EW9wk8GLQX4rwyo/rlYLBcqE/9nXokbZrmcgHnxXec2hzC98K/GPBsZg59VM+M5s8g2B8Q5OFD5/18WmMZxpxhVONp8AdxI3PNO6bD+0YedjuJJ7z3Qij39qUse89nLomwcRJJR6w/fRdJFyRRzijkG8geRPlfLqGR50U0zH9PISRxnL2LPwkkT5HCkC/iAAAAAElFTkSuQmCC"

# Decodificar a imagem em base64
image_data = base64.b64decode(base64_image)

# Carregar a imagem usando o módulo PIL (Pillow)
image = Image.open(BytesIO(image_data))

# Salvar a imagem em PNG Modique o nome da imagem se preferir
image.save("imagem_convertida.png", "PNG")
