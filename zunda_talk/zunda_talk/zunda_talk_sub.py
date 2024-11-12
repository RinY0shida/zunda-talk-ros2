import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from zunda_talk.voice_vox_synthesizer import VoiceVoxSynthesizer


class ZundaTalkSub(Node):

    def __init__(self):
        super().__init__('zunda_talk_sub')
        self.subscription = self.create_subscription(
            String,
            'zunda_talk',
            self.__zunda_callback,
            50)
        self.synthesizer = VoiceVoxSynthesizer()


    def __zunda_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.synthesizer.synthesize_and_play(msg.data)


def main(args=None):
    rclpy.init(args=args)
    zunda_talk_sub = ZundaTalkSub()
    rclpy.spin(zunda_talk_sub)
    zunda_talk_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
