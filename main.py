from utils.gui_utils import get_image_path, onclick
from utils.graph_utils import process_image, generate_graph
from utils.irrigation_utils import is_edge_valid, ensure_connected
from utils.plot_utils import plot_results
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

def main():
    # Get the image path
    image_path = get_image_path()
    if not image_path:
        raise ValueError("No image file selected!")

    # Load the image and convert to grayscale
    image = Image.open(image_path).convert("L")
    image_array = np.array(image)

    # Get image dimensions
    height, width = image_array.shape

    # Generate random points (nodes) avoiding dark areas
    num_points = 200  # Adjust as needed
    points = []

    while len(points) < num_points:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if 0 <= x < width and 0 <= y < height:
            if image_array[y, x] > 60:  # Only add points in bright regions
                points.append([x, y])

    points = np.array(points)

    # Interactive plot setup to allow user to select the starting point
    starting_point = [None, None]
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(image_array, cmap="gray", alpha=0.6)
    ax.set_title("Click to select the starting point")
    cid = fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, image_array, starting_point))
    plt.show()

    # Check if the user selected a valid point
    if None in starting_point:
        raise ValueError("No valid starting point was selected!")

    # Add the selected starting point to the points list
    points = np.vstack([starting_point, points])

    # Perform Delaunay triangulation and generate the graph
    tri, G = generate_graph(points, image_array, 60)

    # Compute the Minimum Spanning Tree and plot results
    mst = plot_results(tri, G, image_array, starting_point, points)

if __name__ == "__main__":
    main()
