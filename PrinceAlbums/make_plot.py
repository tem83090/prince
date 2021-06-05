# This script was produced by glue and can be used to further customize a
# particular plot.

### Package imports

from glue.core.state import load
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')

### Set up data

data_collection = load('make_plot.py.data')

### Set up viewer

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='auto')

### Set up layers

## Layer 1: PrinceDataDeduped

layer_data = data_collection[0]

# Get main data values
x = layer_data['Delta']
y = layer_data['Rating']
keep = ~np.isnan(x) & ~np.isnan(y)

ax.plot(x[keep], y[keep], 'o', color='#595959', markersize=3, alpha=0.8, zorder=1, mec='none')

### Finalize viewer

# Set limits
ax.set_xlim(-28.0, 728.0)
ax.set_ylim(1.88, 5.12)

# Set scale (log or linear)
ax.set_xscale('linear')
ax.set_yscale('linear')

# Set axis label properties
ax.set_xlabel('Delta', weight='normal', size=10)
ax.set_ylabel('Rating', weight='normal', size=10)

# Set tick label properties
ax.tick_params('x', labelsize=8)
ax.tick_params('y', labelsize=8)

# Save figure
fig.savefig('glue_plot.png')
plt.close(fig)