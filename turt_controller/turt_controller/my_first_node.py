#!/usr/bin/env python3
import rclpy  # Python library for ROS2
from rclpy.node import Node

class MyNode(Node):  # Create node using OOP, inherits Node from rclpy
    def __init__(self):
        super().__init__("first_node")  # Constructor of Node class,setup the node
        self.create_timer(1.0,self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("Hello")
        

def main(args=None):  # Default arguments are None
    rclpy.init(args=args)  # Initialize ROS2 communication
    node = MyNode() # create a node
    rclpy.spin(node)  # Keeps the node running
    rclpy.shutdown()  # Ends the ROS2 communication

if __name__ == '__main__':  # Useful when directly running file in terminal
    main()
