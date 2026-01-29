import subprocess
import json
import re
import art

def extract_command(text):
    """
    Extracts the command from the markdown code block.
    """
    match = re.search(r"```(?:\w+)?\n(.*?)\n```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_command_from_copilot(prompt, shell_type="windows command prompt"):
    """
    Uses GitHub Copilot CLI to generate a command from a natural language prompt.
    """
    try:
        copilot_command = f"copilot -p \"suggest a shell command for {shell_type} for {prompt}\""
        result = subprocess.run(copilot_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return extract_command(result.stdout.strip())
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"An error occurred: {e}"

def organize_downloads():
    """
    Organizes files in the downloads folder by type.
    """
    print("Organizing downloads...")
    # This prompt can be refined to be more specific or dynamic
    prompt = "move all pdf files from downloads to a new folder called PDFs in downloads, move all image files (jpg, png, gif) to a new folder called Images in downloads, and move all zip files to a new folder called Zips in downloads."
    
    generated_script = get_command_from_copilot(prompt)

    if generated_script and not generated_script.startswith("Error"):
        print(f"Generated Script:\n{generated_script}")
        confirm = input("Execute this script? (y/n): ")
        if confirm.lower() == 'y':
            try:
                # Save the script to a temporary file and execute it
                script_path = "scripts\\organize_downloads.bat" # For Windows batch script
                with open(script_path, "w") as f:
                    f.write(generated_script)
                subprocess.run(script_path, shell=True, check=True)
                print("Downloads organized successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error executing script: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print(f"Could not generate script: {generated_script}")

def main():
    """
    Main function for the CommandCraft CLI.
    """
    print(art.ANSI_ART)
    print(art.ART_NAME)
    print("Welcome to CommandCraft: Your Everyday Utility Hub!")
    print("Type your command in plain English, or 'exit' to quit.")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break

            if user_input.lower() == "organize my downloads by file type":
                organize_downloads()
            elif user_input:
                generated_command = get_command_from_copilot(user_input)
                print(f"Generated Command: {generated_command}")

                if generated_command and not generated_command.startswith("Error"):
                    confirm = input("Execute this command? (y/n): ")
                    if confirm.lower() == 'y':
                        try:
                            subprocess.run(generated_command, shell=True, check=True)
                        except subprocess.CalledProcessError as e:
                            print(f"Error executing command: {e}")
        except KeyboardInterrupt:
            print("\nExiting CommandCraft.")
            break

if __name__ == "__main__":
    main()
