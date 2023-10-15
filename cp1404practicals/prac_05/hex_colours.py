# Define a dictionary with color names and their corresponding hexadecimal codes
COLORS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


# Function to look up and display the hexadecimal color code

def lookup_color(color_name):
    try:
        color_code = COLORS[color_name]
        print(f"The hexadecimal code for {color_name} is {color_code}")
    except KeyError:
        print("Invalid color name. Please try again.")


# Main function to run the program


def main():
    while True:
        color_name = input("Enter a color name (or blank to exit): ").lower()
        if color_name == "":
            break
        lookup_color(color_name)


main()
