import segno

# Configuration
url = "https://dulce-experience.netlify.app/"
fg_color = "#c4a484"
bg_color = "#0f1113"
output_path = "assets/qr-code.png"

# Generate QR Code
# micro=False ensures it's a standard QR code
# scale=10 makes it high resolution
qr = segno.make(url, error='H') # High error correction for robustness
qr.save(
    output_path,
    scale=20,
    dark=fg_color,
    light=bg_color,
    border=4,
)

print(f"QR Code generated at {output_path}")
