# Python script to Replace a string in file


file_path=r"C:\python_automation_scripts\python_codes\prabal.txt"
old_text="Raj"
new_text="Yahoo"


with open (file_path,'r') as file:
    content=file.read()


content=content.replace(old_text,new_text)


with open(file_path,'w') as file:
    file.write(content)


print(f"The file that contained '{old_text}' is changed with '{new_text}'")