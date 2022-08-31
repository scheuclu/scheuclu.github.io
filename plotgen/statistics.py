from dataclasses import dataclass
import plotly as py
import plotly.graph_objs as go
import pandas as pd

@dataclass
class AA:
    applicants: int
    addmitted: int

    def string(self):
        return f"applicants: {self.applicants},  addmitted: {self.addmitted},  percent: {round(self.addmitted/self.applicants*100,1)}"


@dataclass
class Dept:
    A: AA
    B: AA
    C: AA
    D: AA
    E: AA
    F: AA

    def string(self):
        return f"""  A: {self.A.string()}
  B: {self.B.string()}
  C: {self.C.string()}
  D: {self.D.string()}
  E: {self.E.string()}
  F: {self.F.string()}\n"""


@dataclass(repr=False)
class Uni:
    male: Dept
    female: Dept

    def string(self):
        return f"male:\n{self.male.string()}\n\nfemale:\n{self.female.string()}"

    def compute(self):
        self.maletotalapplicatns = sum([self.male.__getattribute__(dept).applicants for dept in ["A", "B", "C", "D", "E", "F"]])
        self.maletotaladdmitted  = sum([self.male.__getattribute__(dept).addmitted for dept in ["A", "B", "C", "D", "E", "F"]])
        self.femaletotalapplicatns = sum([self.female.__getattribute__(dept).applicants for dept in ["A", "B", "C", "D", "E", "F"]])
        self.femaletotaladdmitted  = sum([self.female.__getattribute__(dept).addmitted for dept in ["A", "B", "C", "D", "E", "F"]])

    def stat(self):
        self.compute()
        for dept in ["A", "B", "C", "D", "E", "F"]:
            print(dept)
            print("male:  ", self.male.__getattribute__(dept).string())
            print("female:", self.female.__getattribute__(dept).string())
            print("---")

        print("male-total")
        print(f"applicants:{self.maletotalapplicatns}, addmitted:{self.maletotaladdmitted},  percent:{round(100*self.maletotaladdmitted/self.maletotalapplicatns,1)}")
        print("female-total")
        print(f"applicants:{self.femaletotalapplicatns}, addmitted:{self.femaletotaladdmitted},  percent:{round(100*self.femaletotaladdmitted/self.femaletotalapplicatns,1)}")


realdata = Uni(
    male=Dept(
        AA(825, 528),
        AA(560, 353),
        AA(325, 120),
        AA(417, 138),
        AA(191, 53),
        AA(373, 22)),
    female=Dept(
        AA(108, 89),
        AA(25, 17),
        AA(593, 202),
        AA(375, 131),
        AA(393, 94),
        AA(341, 24))
)


f = Uni(
    male=Dept(
        AA(825, 528),
        AA(560, 353),
        AA(325, 110),
        AA(417, 138),
        AA(201, 53),
        AA(373, 22)),
    female=Dept(
        AA(108, 89),
        AA(25, 17),
        AA(593, 202),
        AA(375, 131),
        AA(393, 110),
        AA(341, 24))
)

print(f.stat())
f.compute()


parents=['',    'all',  'all',    'male',    'male',     'female',  'female']
labels= ['all', 'male', 'female', 'applied', 'accepted', 'applied', 'accepted']
values= [0,
         0,
         0,
         f.maletotalapplicatns,
         f.maletotaladdmitted,
         f.femaletotalapplicatns,
         f.femaletotaladdmitted]


dist_male=[f.male.__getattribute__(d).applicants for d in ["A", "B", "C", "D", "E", "F"] ]
dist_female=[f.female.__getattribute__(d).applicants for d in ["A", "B", "C", "D", "E", "F"] ]
all_applicant_depts = [f.male.__getattribute__(d).applicants+f.female.__getattribute__(d).applicants for d in ["A", "B", "C", "D", "E", "F"] ]
all_addmitted_depts = [f.male.__getattribute__(d).addmitted+f.female.__getattribute__(d).addmitted for d in ["A", "B", "C", "D", "E", "F"] ]
dept_ratio = [a/b for a,b in zip(all_addmitted_depts,all_applicant_depts)]

dept = ['A', 'B', 'C', 'D', 'E', 'F']
trace_male = go.Bar(x=dept, y=dist_male, name='male', marker_color='#54a8cc')
trace_female = go.Bar(x=dept, y=dist_female, name='female', marker_color='#E47B7B')
trace_ratio = go.Scatter(x=dept, y=dept_ratio, name='female', marker_color='#222222')

from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    trace_male,
    secondary_y=False,
)

fig.add_trace(
    trace_female,
    secondary_y=False,
)

fig.add_trace(
    trace_ratio,
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


# Set y-axes titles
fig.update_yaxes(title_text="male/female<br>acceptance ratio", secondary_y=False)
fig.update_yaxes(title_text="Overall department<br>acceptance ratio", secondary_y=True)
fig.update_xaxes(title_text="Department")



fig.write_json("../static/plots/simpsons.json")
#fig.show()


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')
#
# fig = go.Figure()
#
# fig.add_trace(go.Sunburst(
#     ids=df.ids,
#     labels=df.labels,
#     parents=df.parents,
#     domain=dict(column=1),
#     maxdepth=2,
#     insidetextorientation='radial'
# ))
#
# fig.update_layout(
#     margin = dict(t=10, l=10, r=10, b=10)
# )
#
# fig.show()

