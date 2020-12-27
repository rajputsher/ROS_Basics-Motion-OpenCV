#include "ros/ros.h"
#include "ros_service_assignment/RectangleAreaService.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "rectangleArea_client");
  if (argc != 3)
  {
    ROS_INFO("usage: rectangleArea_client height width");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<ros_service_assignment::RectangleAreaService>("rectangleArea");
  ros_service_assignment::RectangleAreaService srv;
  srv.request.height = atoll(argv[1]);
  srv.request.width = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Rectangle Area: %f", (float)srv.response.area);
  }
  else
  {
    ROS_ERROR("Failed to call service rectangleArea");
    return 1;
  }

  return 0;
}