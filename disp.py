import i2c_lcd_driver #imports functions from i2c_lcd_driver.py file

mylcd = i2c_lcd_driver.lcd() 

mylcd.lcd_clear() #clear the LCD screen
mylcd.lcd_display_string("This is a test", 1) #Display text on Line 1 of the LCD screen
mylcd.lcd_display_string("It works", 2) #Display text on Line 2 of the LCD screen