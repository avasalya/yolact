import numpy as np
import pyrealsense2 as rs


class RealsenseCapture:

    def __init__(self):
        """
        initialize realsense streaming parameters
        """

        self.width = 640
        self.height = 480
        self.fps = 30

        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, self.width, self.height, rs.format.bgr8, self.fps)
        self.config.enable_stream(rs.stream.depth, self.width, self.height, rs.format.z16, self.fps)

    def start(self):
        """
        start realsense camera
        """
        self.pipeline = rs.pipeline()
        self.pipeline.start(self.config)
        print('starting realsense pipeline')

    def read(self, img_array=True):
        """
        read each frame and convert it into numpy array
        """
        frames = self.pipeline.wait_for_frames()
        self.color_frame = frames.get_color_frame()
        self.depth_frame = frames.get_depth_frame()

        if not self.color_frame or not self.depth_frame:
            return (none, none)

        elif img_array:
            rgb = np.asanyarray(self.color_frame.get_data())
            depth = np.asanyarray(self.depth_frame.get_data())
            return (rgb, depth)

        else:
            return (self.color_frame, self.depth_frame)

    def stop(self):
        self.pipeline.stop()