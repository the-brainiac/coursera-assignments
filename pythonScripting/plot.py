import pygal
import random

def draw_line(title, xvals, yvals):
	lineplot = pygal.Line(heihgt=400)
	lineplot.title = title
	lineplot.x_labels = xvals
	lineplot.add('Data', yvals)
	lineplot.render_in_browser()

def draw_xy(title, xvals, yvals):
	coord = [(xval, yval) for xval, yval in zip(xvals, yvals)]
	xyplot = pygal.XY(heihgt=400)
	xyplot.title = title
	xyplot.add('Data', coord)
	xyplot.add('Student', coord)
	xyplot.render_in_browser()

xvals = [1, 3, 5, 7, 2, 8, 9, 4]
yvals = [1, 2, 4, 6, 2, 8, 9, 4, 6, 8, 9]

draw_line("My Line Plot", xvals, yvals)
draw_xy("My Line Plot", xvals, yvals)