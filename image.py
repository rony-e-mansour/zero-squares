from PIL import Image
import os

def resize_images(folder_path, output_folder="resized_images"):
    """
    Resize all images in a folder to a square shape while preserving content.
    
    :param folder_path: Path to the folder containing images
    :param output_folder: Optional output folder path
    """
    # Set desired dimensions for the resized images
    target_width = 500
    target_height = 500
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image file
            filepath = os.path.join(folder_path, filename)
            img = Image.open(filepath)
            
            # Get image dimensions
            width, height = img.size
            
            # Calculate aspect ratio
            aspect_ratio = width / height
            
            # Determine whether to use landscape or portrait orientation
            if aspect_ratio > 1:
                new_size = (target_width, int(target_width * height / width))
            else:
                new_size = (int(target_height * width / height), target_height)
            
            # Resize the image
            img.thumbnail(new_size)
            
            # Create a new square image with white background
            new_img = Image.new('RGB', (target_width, target_height), color='white')
            
            # Paste the original image onto the new square image
            if aspect_ratio > 1:
                new_img.paste(img, (0, (target_height - new_size[1]) // 2))
            else:
                new_img.paste(img, ((target_width - new_size[0]) // 2, 0))
            
            # Save the resized image
            output_filepath = os.path.join(output_folder, filename)
            new_img.save(output_filepath)
            
            print(f"Resized {filename} to {target_width}x{target_height}")

# Call the function
resize_images("images")