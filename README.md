# 🧠 Smart File Organizer

A lightweight file organizer that automatically sorts files from your Downloads folder into categorized folders on your Desktop.

> ⚠️ **Project Status: Under Development (Dev Stage)**
> This project is still being actively developed. Features may change and bugs may exist.

---

## 🚀 Features

* 📂 Automatically detects new files in Downloads
* 🧠 Uses AI (LLM via Ollama) to classify files
* 🗂️ Moves files into organized folders (Study, Bills, Images, etc.)
* 🔁 Handles duplicate filenames automatically
* ⚡ Runs in real-time using file system monitoring

---

## 🛠️ Tech Stack

* Python
* LangChain
* Ollama (Local LLM)
* Watchdog (file system monitoring)

---


## ⚙️ Setup

### 1. Install dependencies

```bash
pip install watchdog langchain langchain-community langchain-ollama
```

### 2. Install and run Ollama

```bash
ollama run gemma:4b
```

### 3. Run the program

```bash
python main.py
```

---

## 📌 How It Works

1. Watches the Downloads folder
2. Detects new files
3. Waits until file is fully downloaded
4. Classifies file using AI
5. Moves file to appropriate Desktop folder

---

## ⚠️ Known Limitations

* AI classification may not always be accurate
* Requires Ollama to be running
* Currently supports basic file types

---

## 🔮 Future Improvements

* Better classification accuracy
* GUI / desktop app
* User customization of categories
* File search functionality
* Background startup support

---

## 🤝 Contributing

This project is in early development. Suggestions and improvements are welcome.

---

## 📄 License

MIT License
