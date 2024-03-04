from PIL import Image, ImageDraw, ImageFont

# Text settings
watermark_text = "  AdeolaCodes  "
font_size = 80  # Increase the font size for a larger watermark
font = ImageFont.truetype("arial.ttf", font_size)

# Source image
source_image = "demo.png"

# Load the image
original_image = Image.open(source_image)

# Calculate the diagonal length of the image
diagonal_len = int((original_image.width ** 2 + original_image.height ** 2) ** 0.5)

# Calculate the watermark size based on the diagonal length
text_width, text_height = font.getmask(watermark_text).size
num_repetitions = int(diagonal_len / text_width) + 1
long_text = watermark_text * num_repetitions

# Calculate the position for the watermark text
start_position = (0, original_image.height)
end_position = (original_image.width, 0)
position = (
    (start_position[0] + end_position[0] - text_width) // 2,
    (start_position[1] + end_position[1] - text_height) // 2
)

# Create a transparent watermark image
watermark = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(watermark)

## Draw the diagonal watermark
for i in range(num_repetitions):
    draw.text((i * text_width, -i * text_width), long_text, font=font, fill=(255, 0, 0, 128))  # Red color


# Rotate the watermark by 45 degrees
rotated_watermark = watermark.rotate(45, expand=1)

# Overlay the rotated watermark on the original image
original_image.paste(rotated_watermark, (0, 0), rotated_watermark)

# Save the watermarked image
output_path = "watermarked_demoA.png"
original_image.save(output_path, format="png", quality=70)

# Show the watermarked image
original_image.show()
