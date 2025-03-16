FROM osrf/ros:humble-desktop-full

RUN apt-get update
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    python3-colcon-common-extensions
WORKDIR /root/ros2_in_jetson_ws/src

RUN git clone https://......
RUN . /opt/ros/humble/setup.sh && colcon build

RUN echo "ALL DONE !"