Note: please use {...} to format the instruction for better readability and make it easier for me to review.

In this exercise, you will develop a new ROS service by applying the concepts that you have learned in this section.

The objective is to create a ROS service where a client sends two float numbers, width and height to the server, then the server will respond the area of the rectangle.

First, create a new ROS package, and call it ros_service_assignment.

You first need to define a service file called RectangleAeraService.srv.

The request part should contains two float values: the width and the height. Use float32 as a type. Refer to this ROS page for more information about available types in ROS. http://wiki.ros.org/msg

The response part should contain the area of the rectangle, which is width*height.

Write a Client and Server that implements this application using Python or C++.

Test your application and make sure that it works.

Questions for this assignment
Note: please use {...} to format the instruction for better readability and make it easier for me to review.

What is the command used to create a ROS package called ros_service_assignment?

Make sure to clarify the path where to create it.

What is the name of the folder when to create the service file?

Provide the absolute path to the file (from the root).

What is the content of the service file RectangleAreaService.srv?

What are the changes you need to do in the CMakeLists.txt. Copy/paste the whole CMakeLists.txt.

What are the changes you need to do the package.xml? Copy/paste the whole package.xml.

What is the command to build the new service and generate executable files?

How to make sure that service files are now created?

Note: please use {...} to format the instruction for better readability and make it easier for me to review.

Write the server application (C++ or Python)

Note: please use {...} to format the instruction for better readability and make it easier for me to review.

Write the client application (C++ or Python)

Note: please use {...} to format the instruction for better readability and make it easier for me to review.

What are the commands to test that the application works fine.


