from PIL import Image, ImageFont, ImageDraw

if __name__ == "__main__":
    print("Welcome to this application!")
    print("To begin, I need some information about the template and list of names to generate license")
    template_dir = input("Template image directory (any bitmap image): ")
    names_dir = input("Names file directory (.txt): ")
    font_dir = input("Font file directory (.ttf): ")
    font_size = int(input("Font size (in pixels): "))
    r_color, g_color, b_color = input("Text color in RGB format seperated by spaces: ").strip().split()
    r_color, g_color, b_color = int(r_color), int(g_color), int(b_color)
    x, y = input("Insert positions (x y): ").strip().split()
    x, y = int(x), int(y)

    template = Image.open(template_dir)

    with open(names_dir, 'r', encoding='utf8') as names_file:
        lines = names_file.readlines()

        for index, line in enumerate(lines):
            line = line.strip()
