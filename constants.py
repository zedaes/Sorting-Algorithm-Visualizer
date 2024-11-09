window_width = 1366
window_height = 768
square_size = 1  
num_bars = 1366

white = (255, 255, 255)

def rainbow_color(index, total):
    red = (index % (total // 3)) * 255 // (total // 3)
    green = ((index + total // 3) % (total // 3)) * 255 // (total // 3)
    blue = ((index + 2 * total // 3) % (total // 3)) * 255 // (total // 3)
    return (red, green, blue)
