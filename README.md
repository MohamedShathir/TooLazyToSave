# TooLazyToSave
A zero-effort Python utility that watches your clipboard and auto-saves screenshots as sequentially numbered files. Because Ctrl+S is too much work.

# 😴 TooLazyToSave

**Because `Ctrl+V` → `Ctrl+S` → `Type Filename` → `Enter` is just too much work.**

TooLazyToSave is a Python script for developers and QAs who want to take screenshots without the hassle of saving them manually. It watches your clipboard in the background. When you take a screenshot (e.g., `Win+Shift+S`), it automatically grabs it, names it sequentially, and saves it to the folder.

## ✨ Why be lazy?

* **Zero-Click Saving:** Just take the screenshot. The script does the rest.
* **Smart Naming:** Automatically names files `TC_<VAR>_01.png`, `TC_<VAR>_02.png`.
* **Gap Filling:** If you delete `TC_02`, the next screenshot automatically fills that spot. No manual renaming required.
* **Windows Optimized:** Handles the weird "temp file" behavior of the Windows Snipping Tool.
* **Duplicate Protection:** Won't save the same image twice if you accidentally copy it again.

## 🛠️ Prerequisites

You just need Python and the **Pillow** library.

```bash
pip install Pillow
