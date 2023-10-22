
def hex_to_rgba(hex_color, alpha=1.0):
    # Remove the '#' character from the hex color if present
    hex_color = hex_color.lstrip('#')

    # Parse the hex color code into its RGB components
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    # Ensure the alpha value is within the range [0.0, 1.0]
    alpha = max(0.0, min(1.0, alpha))

    # Create the RGBA string
    rgba = f"rgba({red}, {green}, {blue}, {alpha})"

    return rgba


# Example usage
hex_color = "#007BFF"
alpha_value = 1
rgba_color = hex_to_rgba(hex_color, alpha_value)
print(f"Hex color: {hex_color}")
print(f"RGBA color: {rgba_color}")

