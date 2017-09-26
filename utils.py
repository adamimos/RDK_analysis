def simpleaxis(ax, bottom = False):
	'''
	remove the top and right spines and ticks from the axis. 
	'''
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	if bottom:
		ax.spines['bottom'].set_visible(False)
		ax.get_xaxis().set_ticks([])
	else:
		ax.get_xaxis().tick_bottom()
	

	ax.get_yaxis().tick_left()