from datetime import datetime
import qrcode

domain = 'https://smvistesen.github.io/digital-business-card/'

def create_qr_code(output_path: str):
    """Create QR code image from content to output path."""
    qr_object = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr_object.add_data(domain)
    qr_object.make(fit=True)

    img = qr_object.make_image(fill_color="black", back_color="white").convert("RGBA")
    img.save(output_path)


if __name__ == "__main__":
    create_qr_code("BusinessCard.png")
