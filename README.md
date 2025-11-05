# 📁 SADWX File Manager

```
   ███████╗ █████╗ ██████╗ ██╗    ██╗██╗  ██╗
   ██╔════╝██╔══██╗██╔══██╗██║    ██║╚██╗██╔╝
   ███████╗███████║██║  ██║██║ █╗ ██║ ╚███╔╝ 
   ╚════██║██╔══██║██║  ██║██║███╗██║ ██╔██╗ 
   ███████║██║  ██║██████╔╝╚███╔███╔╝██╔╝ ██╗
   ╚══════╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝
```

**A powerful, user-friendly terminal file manager with emoji support and Termux compatibility!** 🚀

## ✨ Features

- 🎨 **Beautiful ASCII Logo** - Eye-catching 3D logo design
- 📱 **Termux Compatible** - Works perfectly on Android with Termux
- 🔍 **Recursive Search** - Search files and folders recursively
- 🗑️ **Safe Deletion** - Delete files/folders with confirmation prompts
- 📄 **File Editing** - Edit files directly with nano
- 📂 **Folder Navigation** - Easy navigation with pagination
- 💬 **Telegram Integration** - Quick access to Telegram channel
- 🎯 **Emoji Support** - Colorful and intuitive emoji indicators
- ⌨️ **Simple Commands** - Easy-to-remember command system

## 📦 Installation

### Requirements
- Python 3.6+
- pip (Python package manager)

### Install Dependencies

```bash
pip install colorama
```

For Termux users:
```bash
pkg install python
pip install colorama
```

### Download

```bash
git clone https://github.com/ScriptHub666/wxfilemanager.git
cd wxfilemanager
chmod +x f.py
```

## 🚀 Usage

Run the file manager:
```bash
python3 f.py
```

Or make it executable:
```bash
chmod +x f.py
./f.py
```

## 📖 Commands

| Command | Description |
|---------|-------------|
| 🔢 `[NUMBER]` | Open folder or edit file with nano |
| 🗑️ `r N` | Delete file/folder number N (with confirmation) |
| 🗑️ `r N-M` | Delete files/folders from N to M (with confirmation) |
| 🔍 `search <query>` | Search for files/folders containing query |
| ⬅️ `00` | Go to previous page |
| ➡️ `0` | Go to next page |
| 🔙 `b` | Back to parent directory |
| 🏠 `home` | Go to home directory |
| ❓ `help` | Show command help menu |
| 💬 `t` | Open Telegram channel |
| 🚪 `666/q/exit` | Exit the program |

## 💡 Examples

### Navigate to a folder
```
[❯] : 3
```

### Search for files
```
[❯] : search myfile
```

### Delete a file
```
[❯] : r 5
```

### Delete multiple files
```
[❯] : r 3-7
```

### Go to home directory
```
[❯] : home
```

## 🎯 Features in Detail

### 📁 Smart File Display
- Files show their extensions (PY, TXT, MP3, etc.)
- Folders are clearly marked with 📁 icon
- Color-coded for easy identification

### 🔍 Recursive Search
Search through all subdirectories to find your files quickly:
```
[❯] : search document
```

### 🗑️ Safe Deletion
Every deletion requires confirmation to prevent accidents:
- Single file/folder deletion: `r 5`
- Range deletion: `r 3-8`
- Folders are deleted recursively (all contents removed)

### 📄 Pagination
Browse through large directories with automatic pagination (20 items per page)

## 🔗 Links

- 💬 **Telegram Channel**: [https://t.me/sadwxtm](https://t.me/sadwxtm)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/ScriptHub666/wxfilemanager/issues)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**SADWX**
- 💬 Telegram: [@sadwxtm](https://t.me/sadwxtm)

## ⭐ Support

If you find this project helpful, please give it a star! ⭐

---

Made with ❤️ by SADWX
