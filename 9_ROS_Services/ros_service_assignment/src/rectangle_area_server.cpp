#include "ros/ros.h"
#include "ros_service_assignment/RectangleAreaService.h"

bool areaRectangle(ros_service_assignment::RectangleAreaService::Request &req,
ros_service_assignment::RectangleAreaService::Response &res){
    
    res.area = req.height * req.width;
    ROS_INFO("request: height=%f, width=%f", (float)req.height, (float)req.width);
    ROS_INFO("sending back rectangle area: [%f]", (float)res.area);
    return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "rectangleArea_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("rectangleArea", areaRectangle);
  ROS_INFO("Ready to compute area of the rectangle.");
  ros::spin();

  return 0;
}