# robot_simulation and brover by @voltbro
robot simulation in ROS
## узнать ip:
* $ ipcongig
## подклчение к роверу по ssh:
* $ ssh pi@10.0.0.70 - turtlebot
* $ ssh pi@10.0.0.79- brover
* $ brobro
* $ export ROS_MASTER_URI='http://10.0.0.70:11311/' ip ровера
* $ export ROS_HOSTNAME=10.0.0.NN ip компа
* Если вы являетесь оператором ровера,то вышеуказанные команды нужно прописать в ~/.bashrc
* sudo nano ~/.bashrc 
## запуск камеры:
* roslaunch turtlebro uvc_camera.launch
* rostopic list
* данные с камеры публикуются в топик: front_camera/image_raw с типом данных sensor_msgs/Image
* включаем отображение в rviz командой $ rviz запускаем rviz и выбираем изображение с камеры
## запуск rplidar:
* rostopic list
* данные с rplidar лежат в топике /scan с типом данных sensor_msgs/LaserScan
* включаем отображение в rviz командой $ rviz запускаем rviz и выбираем отображение нашего топика
## запуск моторов:
* rostpic list
* данные в топике /cmd_vel, тип данных geometry_msgs/Twist
* для управления: $ rostopic pub /cmd_vel geometry_msgs/Twist -- '[0, 0, 0]' '[0, 0, 0]'
* '[10, 0, 0]' '[0, 0, 0]' - вперед 10 м/с
* '[0, 0, 0]' '[0, 0, 2]' - поворот 2 рад/с
