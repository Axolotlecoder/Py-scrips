import pyautogui
import time

nachricht = "Moin"
anzahl = 100

print("Du hast 5 Sekunden Zeit, um zum WhatsApp-Web-Chat zu wechseln...")
time.sleep(5)  # Zeit zum Wechseln ins WhatsApp-Chatfenster

for i in range(anzahl):
	pyautogui.typewrite(nachricht)
	pyautogui.press("enter")
	time.sleep(0)  # kurze Pause, damit es stabil läuft (ändere die warte zeit :))



