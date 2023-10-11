import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def display_annotated_image(img_path, annotations):
    """Display image with annotated bounding boxes and text."""
    # Load the image
    img = Image.open(img_path)
    fig, ax = plt.subplots(1)
    ax.imshow(img)
    
    # Draw the bounding boxes and text
    for ann in annotations:
        transcription = ann["transcription"]
        points = ann["points"]
        
        # Extract starting point for the text and bounding box
        start_point = points[0]
        
        # Convert points for polygon drawing
        polygon_points = [(point[0], point[1]) for point in points]
        poly = patches.Polygon(polygon_points, closed=True, edgecolor='r', fill=False)
        
        ax.add_patch(poly)
        
        # Annotate with transcription text
        plt.text(start_point[0], start_point[1], transcription, fontsize=10, color='red')

    # Display the image
    plt.axis('off')
    save_path = img_path.rsplit('.', 1)[0] + '_annotated.png'
    plt.savefig(save_path)
    #plt.show()

# Open the file and process each line
with open('train_data/total_text/test/test.txt', 'r') as f:
    for line in f:
        line = line.strip()
        
        # Split the line into image path and annotations
        img_path, annotation_str = line.split('\t')
        
        # Parse the annotations
        annotations = json.loads(annotation_str)
        
        img_path = "train_data/total_text/test/" + img_path
        
        # Display annotated image
        display_annotated_image(img_path, annotations)

