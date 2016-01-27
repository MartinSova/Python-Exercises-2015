from exturtle import *
from math import pi, cos, sin

def star(turtle, x, y, points, R, r):
	
	"""This function uses turtle to draw a star center at (x, y). The points argument specifies the number
	of points that the star has. The R and r arguments specify the outer and inner radii respectively;
	the outer radius R is the distance from the center of the star to the points, and inner radius is
	the distance from the center of the star to the corners between the points."""
	
	penup(turtle)
	# pen is lifted so line not drawn from center of star to first corner
	
	theta = 2*pi/points
	# each point will be at an angle of theta from each other, forming a circular distribution of points (hence, why 2*pi radians is used)

	goto(turtle, x + r*sin((-0.5)*theta), y + r*cos((-0.5)*theta))
	# the turtle is moved to x and y coordinates of the first corner from which star will be drawn

	pendown(turtle) 
	turtle.begin_fill()
	for i in range(points):
	# 'for' loop repeats motion of turtle from corner to next point on star, to the following corner a number of times that there are points
		
		goto(turtle, x + R*sin(i*theta), y + R*cos(i*theta))
		goto(turtle, x + r*sin((i+0.5)*theta), y + r*cos((i+0.5)*theta))
		# the turtle begins drawing from the last corner again when the 'for' loop is repeated
	
	turtle.end_fill()

def ring(turtle, cx, cy, Nstars, radius, points, R, r):
	
	"""This function uses turtle to draw a ring of Nstar, where each star is the distance "radius" from the
	center of the ring (cx, cy). The points arguments specifies how many points each star has, and
	the R and r arguments specify the outer and inner radii from the center of the star to its points and corners,
	respectively. This ring function uses the star function to draw the individual stars."""

	angle = 2*pi/Nstars
	# 'angle' accounts for equally distribtued stars in a circular pattern (hence, why 2*pi radians is used)
	# the cneter of stars are at an angle 'angle' from each other  (hence, why divided by 'Nstars')
	
	for i in range(Nstars):
	# 'for' loop calls 'star' function for the number of star there are ('Nstars')
	# each star is centered at seperate coordinate (centerx, centery), forming a circular pattern around center of ring (cx, cy)
	
		penup(turtle) 
		centerx = cx + (-radius*sin(angle*(i)))
		centery = cy + (radius*cos(angle*(i)))
		star(turtle, centerx, centery, points, R, r)
		# coordinates for the center of each stars (centerx, centery) are calculated using radius and angle

fred = Turtle()

star(fred, -110, 0, 5, 35, 10)
star(fred, -30, 0, 6, 40, 15)
star(fred, 60, 0, 7, 45, 20)
star(fred, 160, 0, 8, 45, 22)
ring(fred, 30, 0, 12, 250, 5, 35, 15)
# the above five lines will print a ring of 12 5-pointed stars with a row of 5, 6, 7, and 8 pointed stars within the ring

mainloop()