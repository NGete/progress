def modify_content(content):
   
    return content.upper()

def read_and_write_files():
    try:
        filename = input("Enter the filename to read: ")
        
       
        with open(filename, "r") as file:
            content = file.read()
        
       
        modified_content = modify_content(content)
        
      
        output_filename = "modified_" + filename
        with open(output_filename, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content has been saved to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please provide a valid filename.")
    except IOError:
        print("Error: Unable to read the file. Check permissions or try another file.")

# Run the function
read_and_write_files()