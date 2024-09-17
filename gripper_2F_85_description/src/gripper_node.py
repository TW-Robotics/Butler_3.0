#!/usr/bin/env python3
import serial
import time
import binascii
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Bool


class gripper:

    def __init__(self,port="/dev/ttyUSB0"):
        #Initialize connection
        self.ser = serial.Serial(port,baudrate=115200,timeout=0.2,parity="N",stopbits=1,bytesize=8)
        #Activate Gripper
        self.ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
        time.sleep(0.2)
        self.ser.write(b"\x09\x03\x07\xD0\x00\x01\x85\xCF")
        time.sleep(1)
        
        #Initialize ROS Publisher
        self.pub = rospy.Publisher('/joint_states', JointState, queue_size=100)
        rospy.init_node('gripper_commander', anonymous=False)
        self.rate = rospy.Rate(10)
        self.msg = JointState()
        self.openGripper()
        
        #Initialize ROS Subscriber
        rospy.Subscriber("/gripper_open", Bool, self.gripper_callback, queue_size=1)
        
    def gripper_callback(self,msg):
        if msg.data == True:
            self.openGripper()
        elif msg.data == False:
            self.closeGripper()
        else:
            print("Error: Wrong ROS Type")
            print(msg)
        
    def activate(self):
        while not rospy.is_shutdown():
            self.msg.header.stamp = rospy.Time.now()
            self.pub.publish(self.msg)
            #rospy.spin()
            self.rate.sleep()
    
        
    def closeGripper(self):
        self.ser.write(b"\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\xFF\xFF\xFF\x42\x29")
        time.sleep(1)
        self.msg.name = ['finger_joint']
        self.msg.position = [0.78539] #45 Grad
        
    def openGripper(self):
        self.ser.write(b"\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\x00\xFF\xFF\x72\x19")
        time.sleep(1)
        self.msg.name = ['finger_joint']
        self.msg.position = [0.0] #45 Grad
        


if __name__ == "__main__":
    g = gripper("/dev/ttyUSB0")
    g.activate()

