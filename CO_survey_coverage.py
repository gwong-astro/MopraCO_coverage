####################################################################################
# Purpose: coverage of the CO survey compared to the dame et al survey
# Author: G. Wong
# Date: 1.7.16
# note: execfile('CO_survey_coverage.py')
####################################################################################

import matplotlib
matplotlib.use('PDF')

import astropy
import aplpy
import numpy as np
import matplotlib as mpl

def intended_coverage():
	glong = [10.5, 263.5, 263.5, 10.5, 10.5]
	glat = [1, 1, -1, -1, 1]
	boundry_array = np.array([glong, glat])
	return boundry_array

# def mgb_special():
# 	glong = [10.5, 263.5, 263.5, 10.5, 10.5]
# 	glat = [1, 1, -1, -1, 1]
# 	boundry_array = np.array([glong, glat])
# 	return boundry_array	

def carina_boundary():
	glong = [290, 289, 289, 285, 285, 286, 286, 287, 287, 288, 288, 289, 289, 290, 290]
	glat = [0, 0, 0.5, 0.5, -0.5, -0.5, -1.5, -1.5, -2, -2, -1.5, -1.5, -1, -1, 0]
	boundry_array = np.array([glong, glat])
	return boundry_array


def CMZ_boundary():
	# glong = [3.5, -2, -2, -0.5, -0.5, 3.5, 3.5]
	glong = [4, 358, 358, 355, 355, 358, 358, 4, 4]
	glat = [1, 1, 0.5, 0.5, -0.5, -0.5, -1, -1, 1]
	boundry_array = np.array([glong, glat])
	return boundry_array

def braiding_boundary():
	glong = [330, 327, 327, 320, 320, 330, 330]
	glat = [1, 1, 0.5, 0.5, -0.5, -0.5, 1]
	boundry_array = np.array([glong, glat])
	return boundry_array

fig = matplotlib.pyplot.figure(figsize=(40, 100))

img = aplpy.FITSFigure('Wco_DHT2001_-180_180.fits', figure=fig)
img.recenter(310, 0, width=120,height=5)      #pixel location you can find values by x_wld, y_wld = img.pixel2world(43, 24)img.set_frame_color('black')
img.set_tick_color('black')
img.ticks.set_length(15)
img.set_tick_labels_style('latex')
img.set_tick_labels_font(family='serif')
img.set_tick_labels_size(size='x-large')
# img.set_axis_labels(xlabel='Right Ascension (J2000)', ylabel='Declination (J2000)')
img.set_axis_labels_font(family='serif')
img.show_grayscale(vmin=0,vmax=20,invert=True,interpolation='nearest')#contrast
img.set_tick_labels_format(xformat='dd',yformat='dd')
#
# Start outlining the observation coverage
boungry_coverage = intended_coverage() # Full survey coverage
img.show_polygons([boungry_coverage],linewidth=2.5, edgecolor='orange', facecolor='none', linestyle='-', alpha=1) # obs area
#
img.show_rectangles(264,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(265,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(266,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(267,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(268,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(269,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(270,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(271,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(272,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(273,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(274,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(275,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(276,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(277,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(278,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(279,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(280,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(281,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(282,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)


img.show_rectangles(283,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(284,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(285,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(286,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(287,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(288,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(289,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(290,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)


img.show_rectangles(291,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(292,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(293,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(294,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)

img.show_rectangles(295,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)

img.show_rectangles(296,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(297,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(298,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(299,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)

img.show_rectangles(300,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(301,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(302,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(303,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(304,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(305,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(306,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(307,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(308,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(309,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(310,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(311,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(312,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(313,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(314,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(315,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(316,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(317,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(318,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(319,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(320,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)

img.show_rectangles(321,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(322,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
#img.show_rectangles(323,0,width=1,height=1, facecolor='blue', edgecolor='blue', linewidth=0.5) # the first obs by Burton et al 2013
img.show_rectangles(324,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(325,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(326,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(327,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(328,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(329,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(330,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(331,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(332,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(333,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(334,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(335,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(336,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(337,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(338,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(339,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(340,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(341,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(342,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(343,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(344,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(345,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(346,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(347,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(348,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(349,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(350,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(351,0,width=1,height=2, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(352,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(353,-0.25,width=1,height=1.5, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(354,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(355,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
#img.show_rectangles(356,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
#img.show_rectangles(357,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
#img.show_rectangles(358,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
#img.show_rectangles(360,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)


img.show_rectangles(4,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(5,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(6,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(7,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(8,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(9,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)
img.show_rectangles(10,0,width=1,height=1, facecolor='yellow', edgecolor='yellow', linewidth=0.5)


boundry_np = carina_boundary() # David's Obs towards Carina
img.show_polygons([boundry_np],linewidth=0.5, edgecolor='red', facecolor='red', linestyle='-', alpha=1) # obs area


boundry_np_CMZ = CMZ_boundary() # Rebecca's Obs towards the CMZ
img.show_polygons([boundry_np_CMZ],linewidth=0.5, edgecolor='green', facecolor='green', linestyle='-', alpha=1) # obs area

boundry_braiding = braiding_boundary() # Rebecca's Obs towards the CMZ
img.show_polygons([boundry_braiding],linewidth=0.5, edgecolor='purple', facecolor='purple', linestyle='-', alpha=1) # obs area

img.show_rectangles(323,0,width=1,height=1, facecolor='blue', edgecolor='blue', linewidth=0.5) # the first obs by Burton et al 2013






img.set_theme('publication')
# fo.close()
img.save('obs_overlay_projects_futureCoverage.pdf')
