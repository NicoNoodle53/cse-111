import math

#find the volume with given radius and height
def get_volume(radius, height):
    volume = math.pi * (radius * radius) * height
    return volume

#find the surface with a given radius and height
def get_surface_area(radius,height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def main():
    #set up the information in lists
    radius = [6.83 , 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    #print the storage efficiency of each can
    for i in range(12) :
        print(f"{name[i]} {get_volume(radius[i], height[i]) / get_surface_area(radius[i], height[i]):.2f}")

main() 