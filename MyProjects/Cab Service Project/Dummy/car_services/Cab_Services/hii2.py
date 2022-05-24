import time
import sys
def scroll_text(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

scroll_text("""     
                       _______
                      //  ||\ \\
                _____//___||_\ \___
                )  _ future Cab_   \\
                |_/ \________/ \___|
               ___\_/________\_/______
        """)
 
scroll_text("\n\t-------WELCOME TO FUTURE CAB SERVICE!-------\n")