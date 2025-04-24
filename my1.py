import qrcode
from PIL import Image

# Посилання на ваш сайт
url = "https://vladisxs.github.io/cleaning/"

# Створення QR-коду
qr = qrcode.QRCode(
    version=1,  # Розмір QR-коду (1 - найменший)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Рівень корекції помилок
    box_size=10,  # Розмір кожного блоку QR-коду
    border=4,     # Розмір рамки навколо QR-коду
)

# Додавання даних до QR-коду
qr.add_data(url)
qr.make(fit=True)

# Створення зображення QR-коду
img = qr.make_image(fill_color="black", back_color="white")

# Збереження зображення
img.save("cleaning.png")

print("QR-код збережено як cleaning.png")