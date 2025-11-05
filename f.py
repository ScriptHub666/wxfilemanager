#!/usr/bin/env python3
import os
import sys
import re
import glob
import shutil
import signal
import webbrowser
from colorama import init, Fore, Style
init(autoreset=True)
EXTENSION_MAP = {
    'py': 'PY', 'txt': 'TXT', 'mp3': 'MP3', 'php': 'PHP', 'jpg': 'JPG', 'png': 'PNG',
    'pdf': 'PDF', 'doc': 'DOC', 'docx': 'DOCX', 'zip': 'ZIP', 'tar': 'TAR',
    'sh': 'SH', 'html': 'HTML', 'css': 'CSS', 'js': 'JS', 'json': 'JSON',
    'log': 'LOG', 'conf': 'CONF', 'yml': 'YAML', 'yaml': 'YAML',
}
DEFAULT_EXT = 'NOEXT'
def signal_handler(sig, frame):
    print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
def get_extension_display(item_name):
    if '.' not in item_name:
        return DEFAULT_EXT
    ext = item_name.split('.')[-1].lower()
    return EXTENSION_MAP.get(ext, DEFAULT_EXT)
def print_ascii_logo():
    logo = f"""{Fore.CYAN}{Style.BRIGHT}
   ███████╗ █████╗ ██████╗ ██╗    ██╗██╗  ██╗
   ██╔════╝██╔══██╗██╔══██╗██║    ██║╚██╗██╔╝
   ███████╗███████║██║  ██║██║ █╗ ██║ ╚███╔╝ 
   ╚════██║██╔══██║██║  ██║██║███╗██║ ██╔██╗ 
   ███████║██║  ██║██████╔╝╚███╔███╔╝██╔╝ ██╗
   ╚══════╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝
{Style.RESET_ALL}"""
    print(logo)
    print(f"{Fore.YELLOW}{Style.BRIGHT} File Manager{Style.RESET_ALL}\n")
def show_help():
    os.system('clear')
    print_ascii_logo()
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}COMMAND HELP:{Style.RESET_ALL}\n")
   
    commands = [
        ("[NUMBER]", "Open folder or edit file with nano"),
        ("[r N]", "Delete file/folder number N (with confirmation)"),
        ("[r N-M]", "Delete files/folders from N to M (with confirmation)"),
        ("[search <query>]", "Search for files/folders containing <query>"),
        ("[00]", "Go to previous page"),
        ("[0]", "Go to next page"),
        ("[b]", "Back to parent directory"),
        ("[home]", "Go to home directory"),
        ("[help]", "Show this help menu"),
        ("[t]", "Open Telegram channel"),
        ("[666/q/exit]", "Exit the program"),
    ]
   
    for cmd, desc in commands:
        print(f"{Fore.WHITE}{cmd:<20} {Fore.YELLOW}- {desc}{Style.RESET_ALL}")
   
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    input(f"\n{Fore.MAGENTA}Press Enter to continue...{Style.RESET_ALL}")
def open_telegram():
    os.system('clear')
    print_ascii_logo()
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"\n{Style.BRIGHT}{Fore.GREEN}Telegram Channel:{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}https://t.me/sadwxtm{Style.RESET_ALL}\n")
   
    telegram_url = "https://t.me/sadwxtm"
    try:
        os.system(f'termux-open-url {telegram_url} 2>/dev/null || xdg-open {telegram_url} 2>/dev/null || open {telegram_url} 2>/dev/null')
    except:
        pass
   
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    input(f"\n{Fore.MAGENTA}Press Enter to continue...{Style.RESET_ALL}")
def print_header(current_dir, page, total_pages):
    os.system('clear')
    print_ascii_logo()
    print(f"{Fore.YELLOW}Current Directory: {current_dir} (Page {page}/{total_pages}){Style.RESET_ALL}")
    print("-" * 70)
def list_items_vertical(items, page, total_pages):
    if not items:
        print(f"{Fore.YELLOW}No items.{Style.RESET_ALL}\n")
        return
   
    start_idx = (page - 1) * 20
    for i, (global_idx, item_name, is_dir) in enumerate(items):
        num = start_idx + i + 1
        ext = get_extension_display(item_name)
        prefix = "FOLDER" if is_dir else ext
        color = Fore.BLUE if is_dir else Fore.WHITE
        print(f"{Fore.WHITE}[{num}] - {color}[{prefix}]{Style.RESET_ALL} {item_name}")
    print()
    if page > 1:
        print(f"{Fore.WHITE}[00] - [BACK PAGE]{Style.RESET_ALL} back page")
    if len(items) == 20 and total_pages > page:
        print(f"{Fore.WHITE}[0] - [NEXT PAGE]{Style.RESET_ALL} NEXT PAGE")
    print(f"{Fore.WHITE}[b] - [BACK DIR]{Style.RESET_ALL} back to parent directory")
    print(f"{Fore.WHITE}[t] - [TELEGRAM]{Style.RESET_ALL} Open Telegram channel")
    print(f"{Fore.WHITE}[help] - [HELP]{Style.RESET_ALL} Show command help")
def get_items_paginated(current_dir, page=1):
    try:
        all_items = os.listdir(current_dir)
       
        if not all_items:
            return [], 1, page
        sorted_items = sorted(all_items)
        combined = [(item, os.path.isdir(os.path.join(current_dir, item))) for item in sorted_items]
       
        items_per_page = 20
        total_pages = (len(combined) + items_per_page - 1) // items_per_page
        start = (page - 1) * items_per_page
        end = start + items_per_page
        paginated = combined[start:end]
       
        items_with_idx = [(start + i + 1, name, is_dir) for i, (name, is_dir) in enumerate(paginated)]
       
        return items_with_idx, total_pages, page
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return [], 1, page
def search_files(current_dir, query):
    print(f"{Fore.YELLOW}Searching '{query}'...{Style.RESET_ALL}")
    pattern = f"**/*{query}*"
    results = glob.glob(os.path.join(current_dir, pattern), recursive=True)
    if not results:
        print(f"{Fore.RED}No results.{Style.RESET_ALL}")
        return
   
    for result in results:
        rel_path = os.path.relpath(result, current_dir)
        is_dir = os.path.isdir(result)
        ext = get_extension_display(os.path.basename(result))
        prefix = "FOLDER" if is_dir else ext
        color = Fore.BLUE if is_dir else Fore.WHITE
        print(f"{color}[{prefix}]{Style.RESET_ALL} {rel_path}")
def delete_item(path, is_dir):
    try:
        if is_dir:
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"{Fore.GREEN}Deleted successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error deleting: {e}{Style.RESET_ALL}")
def handle_input_command(current_dir, items, page, total_pages):
    try:
        command = input(f"\n{Fore.MAGENTA}[?] : {Style.RESET_ALL}").strip()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
        sys.exit(0)
   
    command_lower = command.lower()
   
    if command_lower in ['666', 'q', 'exit']:
        print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
        sys.exit(0)
   
    if command_lower == 'help':
        show_help()
        return current_dir, page
   
    if command_lower == 't':
        open_telegram()
        return current_dir, page
   
    if command_lower == 'home':
        return os.path.expanduser("~"), 1
   
    if command == '00':
        if page > 1:
            return current_dir, page - 1
        else:
            print(f"{Fore.RED}First page.{Style.RESET_ALL}")
            return current_dir, page
   
    if command == '0':
        if len(items) == 20 and total_pages > page:
            return current_dir, page + 1
        else:
            print(f"{Fore.RED}Last page.{Style.RESET_ALL}")
            return current_dir, page
   
    if command_lower == 'b':
        parent_dir = os.path.dirname(current_dir)
        if parent_dir != current_dir:
            print(f"{Fore.GREEN}Back to {parent_dir}{Style.RESET_ALL}")
            return parent_dir, 1
        else:
            print(f"{Fore.RED}At root.{Style.RESET_ALL}")
            return current_dir, page
   
    if command_lower.startswith('search '):
        query = command[7:].strip()
        if query:
            search_files(current_dir, query)
        else:
            print(f"{Fore.RED}Usage: search <query>{Style.RESET_ALL}")
        return current_dir, page
   
    if re.match(r'^r\s+(\d+)$', command_lower):
        match = re.match(r'^r\s+(\d+)$', command_lower)
        num = int(match.group(1))
        if 1 <= num <= len(items):
            _, item_name, is_dir = items[num-1]
            path = os.path.join(current_dir, item_name)
            msg = f"Delete folder '{item_name}' and all contents?" if is_dir else f"Delete file '{item_name}'?"
            confirm = input(f"{Fore.YELLOW}{msg} (y/n): {Style.RESET_ALL}").lower()
            if confirm == 'y':
                delete_item(path, is_dir)
            else:
                print(f"{Fore.YELLOW}Cancelled.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid.{Style.RESET_ALL}")
        return current_dir, page
   
    if re.match(r'^r\s+(\d+)-(\d+)$', command_lower):
        match = re.match(r'^r\s+(\d+)-(\d+)$', command_lower)
        start, end = int(match.group(1)), int(match.group(2))
        if start > end or end > len(items):
            print(f"{Fore.RED}Invalid range.{Style.RESET_ALL}")
            return current_dir, page
       
        to_delete = [items[i-1][1] for i in range(start, end + 1)]
        to_delete_dirs = [items[i-1][2] for i in range(start, end + 1)]
       
        if not to_delete:
            print(f"{Fore.RED}No items.{Style.RESET_ALL}")
            return current_dir, page
       
        print(f"Items to delete: {', '.join(to_delete)}")
        confirm = input(f"{Fore.YELLOW}Delete all (including folders recursively)? (y/n): {Style.RESET_ALL}").lower()
        if confirm == 'y':
            for name, is_dir in zip(to_delete, to_delete_dirs):
                path = os.path.join(current_dir, name)
                delete_item(path, is_dir)
        else:
            print(f"{Fore.YELLOW}Cancelled.{Style.RESET_ALL}")
        return current_dir, page
   
    if command.isdigit():
        num = int(command)
        if 1 <= num <= len(items):
            _, item_name, is_dir = items[num-1]
            path = os.path.join(current_dir, item_name)
            if os.path.exists(path):
                if is_dir:
                    print(f"{Fore.GREEN}Entering {item_name}{Style.RESET_ALL}")
                    return os.path.abspath(path), 1
                else:
                    print(f"{Fore.GREEN}Opening {item_name} with nano{Style.RESET_ALL}")
                    os.system('clear')
                    os.system(f'nano "{path}"')
                    input(f"{Fore.YELLOW}Press Enter...{Style.RESET_ALL}")
                    return current_dir, page
            else:
                print(f"{Fore.RED}Not found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid number.{Style.RESET_ALL}")
        return current_dir, page
   
    print(f"{Fore.RED}Unknown command. Type 'help' for commands list.{Style.RESET_ALL}")
    return current_dir, page
def main():
    current_dir = os.getcwd()
    page = 1
   
    while True:
        items, total_pages, _ = get_items_paginated(current_dir, page)
        print_header(current_dir, page, total_pages)
        list_items_vertical(items, page, total_pages)
        current_dir, page = handle_input_command(current_dir, items, page, total_pages)
if __name__ == "__main__":
    main()
