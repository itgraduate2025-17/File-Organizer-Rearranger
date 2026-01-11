import os
import shutil
import gradio as gr

# dictionary to map file extensions to folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        return "Folder does not exist."

    moved_files = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(folder_path, folder)
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                    shutil.move(file_path, os.path.join(dest_folder, file_name))
                    moved_files.append(f"{file_name} → {folder}")
                    moved = True
                    break
            if not moved:
                # move to Others folder
                dest_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                moved_files.append(f"{file_name} → Others")

    if moved_files:
        return "Files rearranged:\n" + "\n".join(moved_files)
    else:
        return "No files found to organize."

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## File Organizer / Rearranger")
    gr.Markdown("Enter the folder path, and files will be moved into subfolders by type.")

    folder_input = gr.Textbox(label="Folder Path")
    output_text = gr.Textbox(label="Result", lines=10)

    organize_btn = gr.Button("Organize Files")
    organize_btn.click(
        organize_files,
        inputs=folder_input,
        outputs=output_text
    )

demo.launch()
