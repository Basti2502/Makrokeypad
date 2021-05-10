

# Makrokeypad with GUI Software | still in progress <h2> 
 
Version 1.0

### Preperation <h3>

1. Solder 9 Keyboard switches on GPIO 0 - 9 and 3.3V port 
 
2. Install CircuitPython on the Pi Pico 
   > (https://www.youtube.com/watch?v=1xctZfhZt_g)

3. Install the adafruit_hid libary's
   > (https://circuitpython.readthedocs.io/projects/hid/en/latest/)

4. Follow the software installation steps

5. Script will be generated for Pi Pico with Circuitpython

6. Use with 3d printed case and keycaps 
    > (https://www.thingiverse.com/thing:4816077)

### Software | How to? <h2>

1.  Please install python.exe on your PC
    > (https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe) 

2.  Make sure you have installed the requiered libarys (Adafruit_HID) on your cicutpy.

3.  Download the Folder `gen`, extract it and put it in the Download folder. 

4.  Run file `Step 1`

5.  Type in your Keycodes

    IMPORTANT: You have to fill ALL gaps!
    
    If you like to simulate more than one Key you must do this structure:
    
                Example1, Keycode.Example2, Keycode.Example3, ...

6.  Press save

7.  Close the Windows 

8.  Run file `Step 2`

9.  Congratulation!!! You have generated the final file "code.py"

10. Copy the file `code.py` to your circutpy

11. Plug your pi out and in 

12. Now it works!

### Updates? <h3>

I am developing an preset funktion to save 1 - 5 Presets

Comming soon!!!


### Galerie <h3>
    
![IMG_5689](https://user-images.githubusercontent.com/73909061/117584020-b9354f00-b10a-11eb-8d3a-ffbce342e9c3.jpg)
![IMG_5690](https://user-images.githubusercontent.com/73909061/117584014-b4709b00-b10a-11eb-8a34-c3ec8831a3a3.jpg)
![IMG_5715](https://user-images.githubusercontent.com/73909061/117584017-b76b8b80-b10a-11eb-9fbb-da153568554b.JPG)


