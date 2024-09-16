import os

def handle_uploaded_file(f):
    # Define the base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the path where uploaded files will be stored
    files_path = os.path.join(base_dir, 'static', 'resume')

    # Ensure the directory exists, create it if it doesn't
    os.makedirs(files_path, exist_ok=True)

    # Define the file path
    file_path = os.path.join(files_path, f.name)

    # Open the file and write the uploaded content
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_path
