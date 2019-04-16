import dwavebinarycsp
import matplotlib.pyplot as plt
import networkx as nx
from dwave.system.composites import EmbeddingComposite
from dwave.system.samplers import DWaveSampler

# SAPI configuration
config_sampler = DWaveSampler(
        endpoint='https://cloud.dwavesys.com/sapi',
        token='******',
        solver='DW_2000Q_2_1')

# Describe the map as a graph
areas = {'BM': ['CD', 'MW'],
         'CD': ['BM', 'EY', 'HF', 'MW', 'SR', 'VW'],
         'EY': ['CD', 'VW'],
         'HF': ['CD', 'HR', 'SR'],
         'HR': ['HF', 'SR'],
         'MW': ['BM', 'CD', 'SR'],
         'SR': ['CD', 'HF', 'HR', 'MW'],
         'SI': [],
         'VW': ['CD', 'EY']}
neighbours = [(i, j) for i in areas.keys() for j in areas[i]]

G = nx.Graph()
G.add_nodes_from(areas.keys())
G.add_edges_from(neighbours)

# Define unary colours
single_colours = {(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)}

# Create the problem
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)

# Apply constraints on nodes
for area in areas:
    x = [area + str(i) for i in range(len(single_colours))]
    csp.add_constraint(single_colours, x)

# Apply constraints on edges
for neighbour in neighbours:
    a, b = neighbour  # unpack tuple
    for i in range(len(single_colours)):
        x = [a + str(i), b + str(i)]
        csp.add_constraint((lambda a, b: not (a and b)), x)

# Convert to Machine Instruction
bqm = dwavebinarycsp.stitch(csp)

# Set up solver
sampler = EmbeddingComposite(config_sampler)
response = sampler.sample(bqm, num_reads=50)  # 50 times

# Extract the result from response
sample = next(response.samples())
if not csp.check(sample):
    print('An issue occurred.')
else:
    colour_map = {}  # dict with result colours
    for area in areas:
          for i in range(len(single_colours)):
            if sample[area + str(i)]:
                colour_map[area] = i
node_colours = [colour_map[node] for node in G.nodes()]

# Plot the graph
plt.figure(figsize=(10, 10))
plt.tight_layout()
nx.draw_circular(G, with_labels=1,
		 node_color=node_colors, node_size=3000,
		 cmap=plt.cm.rainbow, font_size=16)
plt.show()

