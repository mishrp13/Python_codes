# Convert a text file to uppercase.

def convert_to_uppercase(input_file,output_file):

    try:

        with open (input_file,'r') as infile:
            content=infile.read()

        with open (output_file,'w') as oufile:
            oufile.write(content.upper())

        print(f"converted '{input_file}' to the '{oufile}")

    except FileNotFoundError:

        print(f"File, '{input_file}' not found")


convert_to_uppercase('prabal.txt','output.txt')

