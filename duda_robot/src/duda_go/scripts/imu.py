#!/usr/bin/env python

import ahrs
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from math import radians

def fetchData():

    x = [ahrs.roll(),ahrs.pitch(),ahrs.yaw(),ahrs.accelerometer()[0],ahrs.accelerometer()[1],ahrs.accelerometer()[2]]


def imuPublisher():
    pub = rospy.Publisher('imu_data', Imu, queue_size=1)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(100) # 100hz
    seq = 0
    while not rospy.is_shutdown():
        imu_msg = Imu()
        # Orientation
        imu_msg.orientation.x = (ahrs.roll())
        imu_msg.orientation.y = (ahrs.pitch())
        imu_msg.orientation.z = (ahrs.yaw())
        # Angular Velocity
        imu_msg.angular_velocity.x = 0
        imu_msg.angular_velocity.x = 0
        imu_msg.angular_velocity.x = 0
        # Linear Velocity
        imu_msg.linear_acceleration.x = 0
        imu_msg.linear_acceleration.y = 0
        imu_msg.linear_acceleration.z = 0
        # Header
        imu_msg.header.stamp = rospy.Time.now()
        imu_msg.header.frame_id = "/odom"
        imu_msg.header.seq = seq

        pub.publish(imu_msg)
        seq = seq + 1
        rate.sleep()

if __name__ == '__main__':
    try:
        imuPublisher()
    except rospy.ROSInterruptException:
        pass
