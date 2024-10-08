# Image-Based Irrigation System

## Project Description

The Image-Based Irrigation System is a Python project that aims to design an irrigation path by analyzing an image of a field. The system utilizes various image processing techniques to avoid dark areas (ditches) and effectively plan irrigation paths. The system includes functionalities for:

- Loading and processing images.
- Generating nodes and edges based on image data.
- Using graph algorithms to determine the optimal irrigation path.
- Allowing user interaction for setting starting points and visualizing results.

## Features

- **Image Processing:** Convert images to grayscale and identify bright regions for placing irrigation nodes.
- **Node Generation:** Randomly generate nodes in bright regions of the image.
- **Interactive Plotting:** Allows users to select a starting point and visualize the irrigation path.
- **Graph Algorithms:** Utilize Delaunay triangulation and Minimum Spanning Tree (MST) to plan the irrigation path.
- **User Interaction:** Select starting points and visualize paths avoiding ditches and obstacles like trees and houses.

## Image Representation
<img src="https://github.com/user-attachments/assets/242f218d-e237-475a-a78e-15247699b974" alt="Irrigation graph" width="400"/>



## Contributing
  Contributions are welcome! Please fork the repository and submit a pull request with your changes.

