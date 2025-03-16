#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class DummyPublisher(Node):
    def __init__(self):
        super().__init__('ros2_dummy')
        self.publisher_ = self.create_publisher(Int32, 'image_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_value)  # Publish every 1 second

    def publish_value(self):
        msg = Int32()
        msg.data = 5
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing 5 to image_topic from ros2')

def main(args=None):
    rclpy.init(args=args)
    node = DummyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
