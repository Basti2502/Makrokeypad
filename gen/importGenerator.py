datei = open('key1.txt','r')
x1 = (datei.readline())

datei = open('key2.txt','r')
x2 = (datei.readline())

datei = open('key3.txt','r')
x3 = (datei.readline())

datei = open('key4.txt','r')
x4 = (datei.readline())

datei = open('key5.txt','r')
x5 = (datei.readline())

datei = open('key6.txt','r')
x6 = (datei.readline())

datei = open('key7.txt','r')
x7 = (datei.readline())

datei = open('key8.txt','r')
x8 = (datei.readline())

datei = open('key9.txt','r')
x9 = (datei.readline())




with open("gen.txt", "w") as txt:
    #imports
    txt.write("import board") 
    txt.write("\n") 
    txt.write("import digitalio")
    txt.write("\n") 
    txt.write("import time") 
    txt.write("\n") 
    txt.write("import usb_hid") 
    txt.write("\n")
    txt.write("from adafruit_hid.keyboard import Keyboard")
    txt.write("\n")
    txt.write("from adafruit_hid.keycode import Keycode") 
    txt.write("\n")
    txt.write("from adafruit_hid.consumer_control_code import ConsumerControlCode")
    txt.write("\n")
    
    #deklars
    txt.write("keyboard = Keyboard(usb_hid.devices)")
    txt.write("\n")
    txt.write("B1 = board.GP0")
    txt.write("\n")
    txt.write("B2 = board.GP2")
    txt.write("\n")
    txt.write("B3 = board.GP3")
    txt.write("\n")
    txt.write("B4 = board.GP4")
    txt.write("\n")
    txt.write("B5 = board.GP5")
    txt.write("\n")
    txt.write("B6 = board.GP6")
    txt.write("\n")
    txt.write("B7 = board.GP7")
    txt.write("\n")
    txt.write("B8 = board.GP8")
    txt.write("\n")
    txt.write("B9 = board.GP9")
    txt.write("\n")
    txt.write("B1 = digitalio.DigitalInOut(B1)")
    txt.write("\n")
    txt.write("B1.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B1.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B2 = digitalio.DigitalInOut(B2)")
    txt.write("\n")
    txt.write("B2.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B2.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B3 = digitalio.DigitalInOut(B3)")
    txt.write("\n")
    txt.write("B3.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B3.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B4 = digitalio.DigitalInOut(B4)")
    txt.write("\n")
    txt.write("B4.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B4.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B5 = digitalio.DigitalInOut(B5)")
    txt.write("\n")
    txt.write("B5.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B5.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B6 = digitalio.DigitalInOut(B6)")
    txt.write("\n")
    txt.write("B6.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B6.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B7 = digitalio.DigitalInOut(B7)")
    txt.write("\n")
    txt.write("B7.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B7.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B8 = digitalio.DigitalInOut(B8)")
    txt.write("\n")
    txt.write("B8.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B8.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("B9 = digitalio.DigitalInOut(B9)")
    txt.write("\n")
    txt.write("B9.direction = digitalio.Direction.INPUT")
    txt.write("\n")
    txt.write("B9.pull = digitalio.Pull.DOWN")
    txt.write("\n")
    txt.write("\n")
    txt.write("\n")
    txt.write("\n")
    txt.write("B1_bool= False")
    txt.write("\n")
    txt.write("B2_bool= False")
    txt.write("\n")
    txt.write("B3_bool= False")
    txt.write("\n")
    txt.write("B4_bool= False")
    txt.write("\n")
    txt.write("B5_bool= False")
    txt.write("\n")
    txt.write("B6_bool= False")
    txt.write("\n")
    txt.write("B7_bool= False")
    txt.write("\n")
    txt.write("B8_bool= False")
    txt.write("\n")
    txt.write("B9_bool= False")
    txt.write("\n")
    txt.write("\n")
    txt.write("\n")
    txt.write("while True:")
    txt.write("\n")
    
    txt.write("    if B1.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x1) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x1) +")")
    txt.write("\n")
    txt.write("        B1_bool = not B1_bool")
    txt.write("\n")
    txt.write("\n")
    
    txt.write("    if B2.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x2) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x2) +")")
    txt.write("\n")
    txt.write("        B2_bool = not B2_bool")
    txt.write("\n")
    txt.write("\n")
    
    txt.write("    if B3.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x3) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x3) +")")
    txt.write("\n")
    txt.write("        B3_bool = not B3_bool")
    txt.write("\n")
    txt.write("\n")
    
    txt.write("    if B4.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x4) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x4) +")")
    txt.write("\n")
    txt.write("        B4_bool = not B4_bool")
    txt.write("\n")
    
    txt.write("\n")
    txt.write("    if B5.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x5) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x5) +")")
    txt.write("\n")
    txt.write("        B5_bool = not B5_bool")
    txt.write("\n")
    
    txt.write("\n")
    txt.write("    if B6.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x6) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x6) +")")
    txt.write("\n")
    txt.write("        B6_bool = not B6_bool")
    txt.write("\n")
    
    txt.write("\n")
    txt.write("    if B7.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x7) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x7) +")")
    txt.write("\n")
    txt.write("        B7_bool = not B7_bool")
    txt.write("\n")
    
    txt.write("\n")
    txt.write("    if B8.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x8) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x8) +")")
    txt.write("\n")
    txt.write("        B8_bool = not B8_bool")
    txt.write("\n")
    
    txt.write("\n")
    txt.write("    if B9.value:")
    txt.write("\n")
    txt.write("        keyboard.press(Keycode." + str(x9) +")")
    txt.write("\n")
    txt.write("        time.sleep(0.15)")
    txt.write("\n")
    txt.write("        keyboard.release(Keycode." + str(x9) +")")
    txt.write("\n")
    txt.write("        B9_bool = not B9_bool")
    txt.write("\n")
    txt.write("\n")
    txt.write("\n")
    txt.write("    time.sleep(0.1)")

    
    
    
    
