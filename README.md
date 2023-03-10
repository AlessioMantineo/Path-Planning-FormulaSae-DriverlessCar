# Turtlesim-Middle-Point-Avoidance
The algorithm that has been developed is designed exclusively for route research during the first lap of the "Formula Sae", in which the vehicle will move in a totally unknown environment at a low speed.

<img align="right" alt="Coding" width="400" src="https://i.ytimg.com/vi/vkVBi9LWJo0/maxresdefault.jpg">

The development environment used is 
ROS, which is nothing more than a process communication system, capable for example in our case of sending messages from the vision module to the planning module to communicate the position of the cones. 


#
During the development of the work, a particular method was chosen to find the ideal path, which is basically based on the midpoints between two cones.
And it was called the Middle Points Algorithm.
 
The algorithm does not aim to be anything too complex, but simply aims to move the vehicle to the centre of the track during the first lap of the competition.

# How the algorithm works :</h3>
From the vision module will come the co-ordinates of the cones, divided by colour, which will be the input to our algorithm.
Once the midpoint between two cones facing each other is found, this is communicated to the control block, which sets that point as the goal-point. 

<img align="right" alt="Coding" width="400" src="https://automaticaddison.com/wp-content/uploads/2021/05/13-goal-has-been-reached.jpg">

With this method we are faced with a major problem.
The vehicle, when facing a curve or in the event that the camera makes some measurement error and does not detect the position of a cone along the track, will find itself with a trajectory that is no longer one that allows it to remain in the centre of the track, but could actually lead to a collision.

# Solution : </h3>
A solution developed for this problem is to consider the midpoint between the first left cone and the first right cone (with respect to the vehicle) and then, instead of taking the midpoint between the second right cone and the second left cone as we saw earlier, consider the midpoint of the segment joining the first left cone with the second right cone.

With this method of goal-point detection we obtain a 'safer' path for our vehicle, which allows us to limit the damage of any errors in detecting the position he obstacles.

# A simulation was developed using turtlesim that follows the midpoints coming from the planning block </h3>
<img align="right" alt="Coding" width="400" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ros_logo.svg/1280px-Ros_logo.svg.png">
# STEPS TO FOLLOW : </h3> 


(1) make a catkin_ws folder

(2) Once you have the 3 folders devel buin and src take what you find in this src folder in the git and copy it into your

(3) In a terminal you launch roscore

(4) Then you launch the turtle sim with the command: rosrun turtlesim turtlesim_node

(5) Then you rosrun turtlesim turtlesim_teleop_key

(6) And keyboard commands and put the turtle in the centre left to avoid it going off the screen

(7) rosrun vision vision_new.py is not needed in the simulation but is present if you want to run it

(8) then run rosrun control go_to_goal.py. Launch the control first so it waits for the path and as soon as it arrives it starts.

(9) Finally, you can launch the planning with the command  rosrun planning triangolazione.py


