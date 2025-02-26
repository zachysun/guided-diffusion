import numpy as np
import matplotlib.pyplot as plt
import argparse
import random

parser = argparse.ArgumentParser(description='Plot images from npz file')
parser.add_argument('--data_dir', type=str, required=True, help='Path to npz file')
parser.add_argument('--k', type=int, default=4, help='Number of random images to display')
args = parser.parse_args()

# Load the npz file
data = np.load(args.data_dir)

images = data.f.arr_0

# number of images to display (k)
k = min(args.k, len(images))

# Randomly select k indices
random_indices = random.sample(range(len(images)), k)

# Calculate rows and columns for the subplot grid
cols = 2
rows = (k + 1) // cols  # Ceiling division to ensure enough rows

fig, axes = plt.subplots(rows, cols, figsize=(10, 10))

if rows == 1:
    axes = np.array([axes])

# Plot each randomly selected image
for i, idx in enumerate(random_indices):
    row = i // cols
    col = i % cols
    
    img = images[idx].squeeze()
    
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f'Sampled Image {idx}')


plt.tight_layout()
plt.show()

# save the plot
# plt.savefig('samples_visualization.png', dpi=300, bbox_inches='tight')
