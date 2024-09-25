def write_to_file(filename, content):
  """Writes the provided content to the specified file in write mode.

  Args:
      filename: The name of the file to write to.
      content: The content to be written to the file (list of strings).
  """
  try:
    with open(filename, 'w') as file:
      for line in content:
        file.write(line + "\n")
    print(f"Successfully wrote content to '{filename}'.")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to write to '{filename}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    if file:  # Check if the file object exists
      file.close()  # Close the file even if an exception occurred


def read_file(filename):
  """Reads the contents of the specified file and displays them on the console.

  Args:
      filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(f"Contents of '{filename}':\n{content}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to read from '{filename}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


def append_to_file(filename, content):
  """Appends the provided content to the specified file in append mode.

  Args:
      filename: The name of the file to append to.
      content: The content to be appended to the file (list of strings).
  """
  try:
    with open(filename, 'a') as file:
      for line in content:
        file.write(line + "\n")
    print(f"Successfully appended content to '{filename}'.")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to append to '{filename}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Write content to file
write_to_file("my_file.txt", ["Line 1: This is a test file.\n", "Line 2: You can write various content here.\n", "Line 3: Numbers like 42 are also possible.\n"])

# Read the file contents
read_file("my_file.txt")

# Append additional content
append_to_file("my_file.txt", ["Line 4: Appending some more lines.\n", "Line 5: The file is now richer in content.\n", "Line 6: Have fun with file handling!\n"])

# Read the appended content (optional)
read_file("my_file.txt")