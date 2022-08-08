#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
class NumberCounterNode(Node):
    
    def __init__(self):
        super().__init__("number_counter")    
        self.counter_= 5
        self.subscriber = self.create_subscription(Int64, "number", self.callback_number, 10)    
        self.publisher = self.create_publisher(Int64, "number_count", 10)
        self.get_logger().info("Number Publisher Node has been started")
        
        self.server_ = self.create_service(
            SetBool, "reset_counter", self.callback_reset_counter)

    def callback_number(self, msg):
#        self.get_logger().info(str(msg.data))
        self.counter_+=msg.data
        msg = Int64()
        msg.data = self.counter_
        self.publisher.publish(msg)

    def callback_reset_counter(self, request, response):
        if (request.data):
            self.counter_= 0
            response.success = True
            response.message = "Successful!"  
        else:
            response.success = False
            response.message = "Nothing to do."
        return response
            
def main(args=None):
    rclpy.init(args=args)
    
    node = NumberCounterNode() #Node("py_test")
    
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ =="__main__":
    main()