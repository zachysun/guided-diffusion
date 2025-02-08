import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Plot images from npz file')
parser.add_argument('--data_dir', type=str, required=True, help='Path to npz file')
args = parser.parse_args()

# Load the npz file
data = np.load(args.data_dir)

# Get the array from the npz file and process it
images = data.f.arr_0

rows = 2
cols = 2

fig, axes = plt.subplots(rows, cols, figsize=(10, 10))

# Plot each image
for i in range(4):
    row = i // cols
    col = i % cols
    
    img = images[i].squeeze()
    
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f'Sampled Image {i+1}')

plt.tight_layout()
plt.show()

# Optionally save the plot
# plt.savefig('samples_visualization.png', dpi=300, bbox_inches='tight')
