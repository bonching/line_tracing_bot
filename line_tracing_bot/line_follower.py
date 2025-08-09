#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# from sensor_msgs.msg import Image
# from geometry_msgs.msg import Twist
# import cv2
# import numpy as np
# from cv_bridge import CvBridge


class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')
        # self.subscription = self.create_subscription(
        #     Image, '/camera/image_raw', self.image_callback, 10)
        # self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        # self.bridge = CvBridge()
        self.get_logger().info('Line Follower Node Started')

    # def image_callback(self, msg):
    #     # Convert ROS Image to OpenCV image
    #     cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
    #
    #     # Convert to HSV for better color detection
    #     hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    #
    #     # Define red color range
    #     lower_red = np.array([0, 120, 70])
    #     upper_red = np.array([10, 255, 255])
    #     mask1 = cv2.inRange(hsv, lower_red, upper_red)
    #     lower_red = np.array([170, 120, 70])
    #     upper_red = np.array([180, 255, 255])
    #     mask2 = cv2.inRange(hsv, lower_red, upper_red)
    #     mask = mask1 + mask2
    #
    #     # Crop bottom part of image to focus on line
    #     h, w = mask.shape
    #     crop = mask[int(h * 0.7):h, :]
    #
    #     # Find contours
    #     contours, _ = cv2.findContours(crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     twist = Twist()
    #     if contours:
    #         # Get largest contour
    #         largest_contour = max(contours, key=cv2.contourArea)
    #         M = cv2.moments(largest_contour)
    #         if M['m00'] != 0:
    #             cx = int(M['m10'] / M['m00'])
    #             # Calculate error from center
    #             error = cx - w // 2
    #             # Simple proportional control
    #             twist.linear.x = 0.2  # Constant forward speed
    #             twist.angular.z = -float(error) / 100  # Adjust angular velocity
    #     else:
    #         # No line detected, stop
    #         twist.linear.x = 0.0
    #         twist.angular.z = 0.0
    #
    #     self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = LineFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()