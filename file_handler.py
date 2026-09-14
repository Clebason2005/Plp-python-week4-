# File handling challenge
try:
    with open("input.txt", "w") as f:
        f.write("Hello Python\nLearning file handling\nWeek 4 assignment")

    with open("input.txt", "r") as f:
        content = f.read()
    
    words = len(content.split())
    lines = len(content.splitlines())
    modified = content.upper()

    with open("output.txt", "w") as f:
        f.write(modified)
    
    print(f"Words: {words}")
    print(f"Lines: {lines}")
    print("File processed successfully!")

except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"An error occurred: {e}")
