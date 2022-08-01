import plotly
import numpy as np
import plotly.graph_objects as go

SIZE_INPUT_SPACE=256
SIZE_OUTPUT_SPACE=256


def dummy_hash(n):
  b=bin(n)
  b=b[2:].rjust(8, '0')
  h=int(b[-1::-1],2)
  return h


def dummy_hash_string(s):
    return sum([dummy_hash(ord(i)) for i in s]) % 2**8

x=np.array(list(range(0,2**8)))
y=np.array([dummy_hash(n) for n in x])
assert(y.max()<SIZE_OUTPUT_SPACE)
z=0+y[1:]-y[:-1]
z=np.append(z,0)

# Plot output over input
layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(title="Input"),
    yaxis=dict(title="Output")
)
fig = go.Figure(data=go.Scatter(
        x=x,
        y=y,
        marker=dict(color=x),
        mode='markers'),
        layout=layout)
fig.write_json("../static/plots/input_to_output.json")


# Plot outout patterns
layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(title="Ouput(n)"),
    yaxis=dict(title="Ouput(n)-Ouput(n+1)")
)
fig = go.Figure(data=go.Scatter(
        x=y,
        y=z,
        marker=dict(color=x),
        mode='markers'),
        layout=layout)
fig.write_json("../static/plots/pattern.json")

