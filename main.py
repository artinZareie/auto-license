from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


def generate_images():
    print("To begin, I need some information about the template and list of names to generate license")
    template_dir = input("Template image directory (any bitmap image): ")
    names_dir = input("Names file directory (.txt): ")
    font_dir = input("Font file directory (.ttf): ")
    font_size = int(input("Font size (in pixels): "))
    r_color, g_color, b_color = input("Text color in RGB format seperated by spaces: ").strip().split()
    r_color, g_color, b_color = int(r_color), int(g_color), int(b_color)
    x, y = input("Insert positions (x y): ").strip().split()
    x, y = int(x), int(y)

    font = ImageFont.truetype(font_dir, font_size)

    with open(names_dir, 'r', encoding='utf8') as names_file:
        lines = names_file.readlines()

        for index, line in enumerate(lines):
            print(f"Processing image {index + 1} out of {len(lines)} images.")
            template = Image.open(template_dir)  # We need to load image for new person each time.
            line = line.strip()
            drawer = ImageDraw.Draw(template)
            drawer.text((x, y), line, (r_color, g_color, b_color), font = font)
            template.save(f"outputs/License {index + 1} - {line}.png")


def show_temp():
    template_dir = input("Please enter path of the template you'd like to try: ")
    sample_text = input("Plese give me a sample text: ")
    font_path = input("Please give me a ttf font: ")
    font_size = int(input("Please give me an initial font size: "))
    font = ImageFont.truetype(font_path, font_size)
    r, g, b = input("Please give me an initial color formatted in <r g b>: ").strip().split()
    r, g, b = int(r), int(g), int(b)
    while True:
        if input("Do you want to continue (y/n)? ") == 'n':
            break
        x, y = input("Please give me the new (x y): ").strip().split()
        x, y = int(x), int(y)
        image = Image.open(template_dir)
        drawer = ImageDraw.Draw(image)
        drawer.text((x, y), sample_text, (r, g, b), font = font)
        plt.imshow(image)
        plt.show()


if __name__ == "__main__":
    print("Welcome to this application!")
    options_desc = """
Please select one of options below:
1) generate licenses.
2) investigate a template using matplotlib.
    """
    print(options_desc)


    option = int(input())

    if option == 1:
        generate_images()
    else:
        show_temp()
