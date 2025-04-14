import os

def count_files_by_type(directory="."):
    """Count files by their extension in the given directory."""
    # Dictionary to store counts
    file_counts = {}
    
    # Walk through the directory
    for filename in os.listdir(directory):
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            extension = os.path.splitext(filename)[1].lower()
            
            # If empty extension, count as "no extension"
            if extension == "":
                extension = "no extension"
                
            # Increment the count
            if extension in file_counts:
                file_counts[extension] += 1
            else:
                file_counts[extension] = 1
    
    return file_counts

# Run the function
if __name__ == "__main__":
    directory = input("Enter directory path (press Enter for current directory): ") or "."
    
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
    else:
        # Count files
        file_counts = count_files_by_type(directory)
        
        # Print results
        print(f"\nFile types in {directory}:")
        print("-" * 30)
        
        # Sort by extension
        for extension, count in sorted(file_counts.items()):
            print(f"{extension}: {count} files")
        
        # Print total
        total = sum(file_counts.values())
        print("-" * 30)
        print(f"Total: {total} files")
