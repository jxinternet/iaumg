# Import necessary libraries
import qrcode
import time
from machine import I2C, Pin
import ssd1306

# Define constants
WIDTH = 128
HEIGHT = 64
SCL_PIN = 22
SDA_PIN = 23
BUTTON_PIN = 2

# Initialize I2C communication
i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Define function to generate QR code
def generate_qr():
    # Clear display
    oled.fill(0)
    oled.show()

    # Get input text from user
    text = input("Enter text: ")

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    # Display QR code on OLED screen
    oled_qr = qrcode.image.pil.PilImage(qr.make_image(fill_color="black", back_color="white"))
    oled.image(oled_qr)
    oled.show()

# Define function to handle button press
def button_handler(pin):
    generate_qr()

# Set up button interrupt
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Main loop
while True:
    time.sleep(1)
