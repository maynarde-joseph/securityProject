import os

file_path = "./decrypted.txt"
text = ""
with open(file_path, "r") as f:
  for l in f:
    #split each line
    parts = l.strip().split(" - ")
    if len(parts) == 2:
      key_press = parts[1]

      if key_press.startswith("'") and key_press.endswith("'"):
          text += key_press.strip("'")
      elif key_press == "Key.space":
          text += " "
      elif key_press == "Key.backspace":
          text = text[:-1]

words = text.split()
print(' '.join(words))
