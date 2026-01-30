import subprocess
import json
import re
from gen import mini_commandcraft_intro
from colorama import Fore, Style, init

init() # Initialize Colorama for cross-platform ANSI escape code interpretation

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
    print(f"{Fore.WHITE}Organizing downloads...{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Generating script with GitHub Copilot CLI...{Style.RESET_ALL}")
    # This prompt can be refined to be more specific or dynamic
    prompt = "move all pdf files from downloads to a new folder called PDFs in downloads, move all image files (jpg, png, gif) to a new folder called Images in downloads, and move all zip files to a new folder called Zips in downloads."
    
    generated_script = get_command_from_copilot(prompt)

    if generated_script and not generated_script.startswith("Error"):
        print(f"{Fore.WHITE}Generated Script:\n{generated_script}{Style.RESET_ALL}")
        confirm = input(f"{Fore.WHITE}Execute this command? (y/n): {Style.RESET_ALL}")
        if confirm.lower() == 'y':
            try:
                # Save the script to a temporary file and execute it
                script_path = "scripts\\organize_downloads.bat" # For Windows batch script
                with open(script_path, "w") as f:
                    f.write(generated_script)
                subprocess.run(script_path, shell=True, check=True)
                print(f"{Fore.WHITE}Downloads organized successfully!{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.WHITE}Error executing script: {e}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.WHITE}An error occurred: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.WHITE}Could not generate script: {generated_script}{Style.RESET_ALL}")

def main():
    """
    Main function for the CommandCraft CLI.
    """
    mini_commandcraft_intro()
    print(f"{Fore.BLUE}Welcome to CommandCraft: Your Everyday Utility Hub!")
    print(f"{Fore.BLUE}Type your command in plain English, or 'exit' to quit.{Style.RESET_ALL}")

    while True:
        try:
            user_input = input(f"{Fore.MAGENTA}> {Style.RESET_ALL}")
            if user_input.lower() == 'exit':
                break

            if user_input.lower() == "organize my downloads by file type":
                organize_downloads()
            elif user_input:
                print(f"{Fore.BLUE}Generating command with GitHub Copilot CLI...{Style.RESET_ALL}")
                generated_command = get_command_from_copilot(user_input)
                print(f"{Fore.WHITE}Generated Command: {generated_command}{Style.RESET_ALL}")

                if generated_command and not generated_command.startswith("Error"):
                    confirm = input(f"{Fore.WHITE}Execute this command? (y/n): {Style.RESET_ALL}")
                    if confirm.lower() == 'y':
                        try:
                            subprocess.run(generated_command, shell=True, check=True)
                        except subprocess.CalledProcessError as e:
                            print(f"{Fore.WHITE}Error executing command: {e}{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"{Fore.WHITE}\nExiting CommandCraft.{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()

