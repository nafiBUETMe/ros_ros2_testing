#!/usr/bin/env python3

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Changed to Float32 to support decimal values

class UserInputPublisher(Node):
    def __init__(self):
        super().__init__('ros2_user_input_publisher')
        self.publisher_ = self.create_publisher(Float32, 'image_topic', 10)
        self.get_logger().info("Enter a number to publish. Type 'exit' to stop.")
        
    def publish_value(self, value):
        msg = Float32()
        msg.data = value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {value} was typed from ros2')

def main(args=None):
    rclpy.init(args=args)
    node = UserInputPublisher()
    
    try:
        while rclpy.ok():
            user_input = input("Type a number: ")
            if user_input.lower() == "exit":
                break
            try:
                value = float(user_input)  # Convert input to float
                node.publish_value(value)
            except ValueError:
                node.get_logger().error("Invalid input. Please enter a valid number.")
                
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Int32

# class DummyPublisher(Node):
#     def __init__(self):
#         super().__init__('ros2_dummy')
#         self.publisher_ = self.create_publisher(Int32, 'image_topic', 10)
#         self.timer = self.create_timer(1.0, self.publish_value)  # Publish every 1 second

#     def publish_value(self):
#         msg = Int32()
#         msg.data = 5
#         self.publisher_.publish(msg)
#         self.get_logger().info('Publishing 5 to image_topic from ros2')

# def main(args=None):
#     rclpy.init(args=args)
#     node = DummyPublisher()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
