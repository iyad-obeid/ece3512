from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider, Label
from bokeh.plotting import figure, output_file, show
from math import cos, sin, radians, pi

output_file("..\docs\cos_equiv.html")

# define the unit circle
xx = [cos(radians(xx)) for xx in range(-1,360)]
yy = [sin(radians(yy)) for yy in range(-1,360)]

# init the degree indicator circles
a = 15*pi/180 #degrees
x = [cos(a), cos(a)]
y = [sin(a), -sin(a)]
myString = ['\u03A9 = 123']

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_width=400, plot_height=400, match_aspect=True, tools='save')
plot.line(xx,yy,color="forestgreen",line_width=2)
plot.circle('x', 'y', source=source, size=20, line_alpha=0.6,color='tomato')
plot.rect(0,0,3,3,fill_alpha=0,line_alpha=0)

citation = Label(x=0, y=0, x_units='data', y_units='data',
                 text=myString[0])

plot.add_layout(citation)

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var a = Math.PI * cb_obj.value / 180
        x = data['x']
        y = data['y']
        x[0] = Math.cos(a)
        y[0] = Math.sin(a)
        x[1] = Math.cos(a)
        y[1] = -Math.sin(a)
        source.change.emit();
    """)

slider = Slider(width=350,start=0, end=360, value=15, step=15, title="\u03A9", callback=callback)
layout = column(slider, plot)

show(layout)

