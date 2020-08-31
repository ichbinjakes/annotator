from xml_util import read_annotation_file, render_annotation_page, check_annotations
import os

# Path to .annot files
annotation_path = 'annotations'

# Path to write the html files to
output_dir = 'html'
                
### Main
def main():
    for i in os.listdir(annotation_path):
        if '.epub' in i:
            if check_annotations(f"{annotation_path}\\{i}"):
                data = read_annotation_file(f"{annotation_path}\\{i}")
                render_annotation_page(data, output_dir)
                
if __name__ == '__main__':
    main()