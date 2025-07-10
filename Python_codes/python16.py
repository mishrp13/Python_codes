

# python code Extract error lines from a log file.

def extract_errors(log_file, output_file=None):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        # Filter lines that contain the word "error" (case-insensitive)
        error_lines = [line for line in lines if "error" in line.lower()]

        if output_file:
            with open(output_file, 'w') as out:
                out.writelines(error_lines)
            print(f"Found {len(error_lines)} error lines. Saved to '{output_file}'.")
        else:
            print("Error lines:")
            for line in error_lines:
                print(line, end='')

    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")

# Example usage
extract_errors('application.log', 'errors_only.log')
