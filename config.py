import os

BASE_DIR = os.path.expanduser("~/Downloads")
DESKTOP_DIR = os.path.expanduser("~/Desktop/AI_Organizer")

DESTINATIONS = {
    "Study": os.path.join(DESKTOP_DIR, "Study"),
    "Bills": os.path.join(DESKTOP_DIR, "Bills"),
    "Code": os.path.join(DESKTOP_DIR, "Code"),
    "Images": os.path.join(DESKTOP_DIR, "Images"),
    "Docs": os.path.join(DESKTOP_DIR, "Documents"),
    "Others": os.path.join(DESKTOP_DIR, "Others"),
}