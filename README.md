# Self-avoiding Random Walk

Inspired by Coding Challenge No. 162 from The Coding Train (https://www.youtube.com/watch?v=m6-cm6GZ1iw)

The scripts generates a 5 x 5 grid where each spot on the grid is an instance of the Spot class, containing whether the spot has already been visited in the current walk 
and which directions we are allowed to go towards. Starting from the upper left corner, we choose each time a direction at random from the available ones and we proceed 
until we get to the point where we have no direction to go towards. The only restriction to our movement is not to go over the grid and not visit a spot we have already 
visited before. The result is then plotted on a graph with coloured dot expressing the starting, intermediate and ending positions the current walk went through. 

I have used numpy arrays in order to more easily perform operations like vector addition and matrix splitting.
