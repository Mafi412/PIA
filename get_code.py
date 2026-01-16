from nbformat import read, NO_CONVERT
from argparse import ArgumentParser


def read_python_code_from_notebook(notebook_file_path, output_python_file_path):
    notebook = read(notebook_file_path, NO_CONVERT)

    cells = notebook.cells
    code_cells = [c for c in cells if c.cell_type == "code"]

    with open(output_python_file_path, "w") as output_file:
        for cell in code_cells:
            # Output the cell content
            output_file.write(cell.source)
            
            # End the cell content by new-line (safeguard for when there is none present in the cell)
            output_file.write("\n")
            
            # Separate the cells by two empty lines
            output_file.write("\n\n")
            
            
def main(args):
    read_python_code_from_notebook(args.notebook_file_path, args.output_python_file_path)
            

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("notebook_file_path", type=str, help="Path to the Jupyter Notebook containing the desired Python code.")
    parser.add_argument("output_python_file_path", type=str, help="Path to the file the Python code will be written to.")
    
    main(parser.parse_args())
