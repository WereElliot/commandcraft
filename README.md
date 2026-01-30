# CommandCraft: Everyday Utility Hub Powered by Copilot CLI

## Problem Statement
In the fast-paced world of software development, efficiency is key. Developers often find themselves wrestling with complex shell commands, trying to remember the right syntax for tasks like file manipulation, system monitoring, or version control. This reliance on memory or constant searching for command-line snippets slows down workflows and introduces unnecessary friction into the development process.

## Solution Overview
CommandCraft is a terminal-based assistant that transforms natural language into working commands and scripts. Powered by the GitHub Copilot CLI, it acts as an intelligent layer between the user and their shell, allowing them to express their intent in plain English and receive the correct command instantly. This not only streamlines daily tasks but also serves as a learning tool for those less familiar with the command line.

## Feature List
- **Natural Language to Command:** Convert plain English into executable shell commands.
- **File Organization:** Automatically sort files in your `~/Downloads` folder by type (e.g., PDFs, images, archives).
- **System Insights:** Quickly display disk usage in a human-readable format.
- **Backup Utility:** Create compressed backups of project folders with a simple command.
- **Git Shortcuts:** Simplify common Git operations, such as undoing the last commit while keeping changes or viewing commit history.
- **Extensibility:** Easily add your own custom natural language shortcuts for personalized workflows.

## Demo Instructions
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/commandcraft.git
    cd commandcraft
    ```
2.  **Run the application:**
    ```bash
    python commandcraft.py
    ```
3.  **Try some of the following commands:**
    - "Organize my downloads by file type"
    - "Show me disk usage"
    - "Backup my project folder 'my-project' to 'backups'"
    - "Undo my last git commit"
    - "Show me my git history"

## Impact and Benefits
- **Accelerated Workflow:** Spend less time recalling command syntax and more time on what matters: building software.
- **Reduced Cognitive Load:** Offload the mental burden of remembering complex commands to an intelligent assistant.
- **Improved Accessibility:** Make the command line more approachable for beginners and non-experts.
- **Enhanced Productivity:** Automate repetitive tasks and streamline your development process.
- **Learn by Doing:** Discover new commands and shell features by seeing the output of your natural language queries.

## Screenshots/GIFs
  ██████╗ ██████╗ ███╗   ███╗███╗   ███╗ █████╗ ███╗   ██╗██████╗   ██████╗ ██████╗  █████╗ ███████╗████████╗
 ██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔══██╗████╗  ██║██╔══██╗ ██╔════╝ ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
 ██║     ██║   ██║██╔████╔██║██╔████╔██║███████║██╔██╗ ██║██   ██║ ██║      ██████╔╝███████║█████╗     ██║   
 ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║ ██║      ██╔══██╗██╔══██║██╔══╝     ██║   
 ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝ ╚██████╗ ██║  ██║██║  ██║██║        ██║   
  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
Welcome to CommandCraft: Your Everyday Utility Hub!   
Type your command in plain English, or 'exit' to quit.
> hello
Generating command with GitHub Copilot CLI...
Generated Command: echo hello
Execute this command? (y/n): y
hello
> list my files and folders in the downloads
Generating command with GitHub Copilot CLI...
Generated Command: dir %USERPROFILE%\Downloads
Execute this command? (y/n): y
 Volume in drive C has no label.
 Volume Serial Number is 28F0-21BA

 Directory of C:\Users\USER\Downloads

01/30/2026  11:45 AM    <DIR>          .
01/30/2026  11:45 AM    <DIR>          ..
01/26/2026  08:53 PM         6,732,741 05. SQL Injection Attacks and Defense.pdf
12/12/2025  10:22 AM    <DIR>          Compressed
12/19/2025  11:12 AM    <DIR>          Documents
01/29/2026  06:32 PM           514,699 image.jpg
11/23/2025  11:57 AM            20,267 IN130017523Outline.docx
01/14/2026  10:54 AM            10,904 Java Standard Zoom Recordings.xlsx
01/09/2026  04:54 PM            56,037 JOYCE INSURANCE LETTERS (1).xlsx  
01/09/2026  04:54 PM            56,037 JOYCE INSURANCE LETTERS.xlsx
01/30/2026  11:44 AM           652,495 Lab 1 (1).pdf
01/30/2026  11:44 AM           652,495 Lab 1.pdf
12/12/2025  10:22 AM    <DIR>          Music
01/26/2026  08:32 PM           826,590 steg.pdf
12/19/2025  01:20 PM    <DIR>          Video
01/30/2026  11:45 AM           135,160 Were ElliotCv.pdf
              10 File(s)      9,657,425 bytes
               6 Dir(s)  24,938,283,008 bytes free
> commit all the changes done to this project
Generating command with GitHub Copilot CLI...
Generated Command: git add . && git commit -m "Your commit message"
Execute this command? (y/n): y
warning: in the working copy of 'commandcraft.py', LF will be replaced by CRLF the next time Git touches it
[main ed22bd0] Your commit message
 6 files changed, 31 insertions(+), 148 deletions(-)
 create mode 100644 __pycache__/gen.cpython-314.pyc
 delete mode 100644 art.py
 delete mode 100644 generates_art.py
 delete mode 100644 temp_rose.jpg
> push to remote git
Generating command with GitHub Copilot CLI...
Generated Command: git push origin main
Execute this command? (y/n): y
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.46 KiB | 114.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/WereElliot/commandcraft.git
   9f41237..ed22bd0  main -> main
> exit
PS C:\Users\USER\Desktop\comandcraft>
