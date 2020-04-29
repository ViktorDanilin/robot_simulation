import RPi.GPIO as GPIO
import MFRC522
import signal

import rospy
from std_msgs.msg import *
continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def main():
   pub=rospy.Publisher('/nfc',Int32MultiArray,queue_size = 16)
   rospy.init_node('ca_serial')
   r = rospy.Rate(0.2)
   signal.signal(signal.SIGINT, end_read)
   
   # Create an object of the class MFRC522
   MIFAREReader = MFRC522.MFRC522()
   
   # Welcome message
   print "Welcome to the MFRC522 data read example"
   print "Press Ctrl-C to stop."
   
   while not rospy.is_shutdown() and continue_reading:
      print "LOOP running"
      (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  
      # If a card is found
      if status == MIFAREReader.MI_OK:
          print "Card detected"
      
      # Get the UID of the card
      (status,uid) = MIFAREReader.MFRC522_Anticoll()
  
      # If we have the UID, continue
      if status == MIFAREReader.MI_OK:
  
          # Print UID
          print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
      
          # This is the default key for authentication
          key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
          
          # Select the scanned tag
          MIFAREReader.MFRC522_SelectTag(uid)
  
          # Authenticate
          status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 61, key, uid)
  
          # Check if authenticated
          if status == MIFAREReader.MI_OK:
              back_data = MIFAREReader.MFRC522_Read(61)
              if back_data != None:
                  fat = Int32MultiArray(data=back_data)
                  pub.publish(fat)
                  r.sleep();                      
              MIFAREReader.MFRC522_StopCrypto1()
          else:
              print "Authentication error"      

      
if __name__ == '__main__':
    main()      
