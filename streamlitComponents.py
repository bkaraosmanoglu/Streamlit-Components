import streamlit as st 
import pandas as pd
import altair as alt
import numpy as np

#Title
st.title('Components')

#Header
st.header('This is a header')

#SubHeader
st.subheader('This is a subheader')

#Text
st.text('This is some text.')

#Markdown
st.markdown('Streamlit is **_really_ cool**.')

#Formulation
st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

#Write
st.write(1234)
st.write(pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40],
}))

st.write('1 + 1 = ', 2)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

#Chart Write
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

#Streaming code with syntax
code = '''def hello():
        print("Hello, Streamlit!")'''
st.code(code, language='python')

#Displaying data
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

#Pandas Styler :)
df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

#Display a Static Table
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

#Json Body
st.json({
         'foo': 'bar',
    'baz': 'boz',
     'stuff': [
         'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

#Display Chart
#streamlit.line_chart(data=None, width=0, height=0, use_container_width=True)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Display Chart
#streamlit.area_chart(data=None, width=0, height=0, use_container_width=True)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

#Display Chart
#streamlit.bar_chart(data=None, width=0, height=0, use_container_width=True)
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

#Display Chart
#streamlit.pyplot(fig=None, clear_figure=None, **kwargs)
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#Dislay Chart
#streamlit.vega_lite_chart(data=None, spec=None, use_container_width=False, **kwargs)
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

#Display Chart
#streamlit.bokeh_chart(figure, use_container_width=False)
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

#Display Chart
#streamlit.pydeck_chart(pydeck_obj=None, use_container_width=False)
import pydeck as pdk
df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

#Display Chart
#streamlit.graphviz_chart(figure_or_dot, use_container_width=False)
import graphviz as graphviz
# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

#Display Chart
#streamlit.map(data=None, zoom=None, use_container_width=True)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


#Display Media
#Image
#streamlit.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
from PIL import Image
#image = Image.open('D:/Python/Streamlit/kusadasi.jpg')

#st.image(image, caption='Kusadasi')

#Display Media
#Audio
#streamlit.audio(data, format='audio/wav', start_time=0)
#audio_file = open('myaudio.ogg', 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/ogg')

#Display Media
#Video
#streamlit.video(data, format='video/mp4', start_time=0)
#video_file = open('myvideo.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

#Interactive Widgets
#Button
#streamlit.button(label, key=None, help=None)
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#Check Box
#streamlit.checkbox(label, value=False, key=None, help=None)
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

#Radio
#streamlit.radio(label, options, index=0, format_func=<class 'str'>, key=None, help=None)
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

#Display a select widget
#streamlit.selectbox(label, options, index=0, format_func=<class 'str'>, key=None, help=None)
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#Multi Select
#streamlit.multiselect(label, options, default=None, format_func=<class 'str'>, key=None, help=None)
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

#Slider
#streamlit.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None)
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

#Select Slider
#streamlit.select_slider(label, options=[], value=None, format_func=<class 'str'>, key=None, help=None)
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

#Text Input
#streamlit.text_input(label, value='', max_chars=None, key=None, type='default', help=None)
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#Number Input
#streamlit.number_input(label, min_value=None, max_value=None, value=<streamlit.elements.utils.NoValue object>, step=None, format=None, key=None, help=None)
number = st.number_input('Insert a number')
st.write('The current number is ', number)

#Text Area
#streamlit.text_area(label, value='', height=None, max_chars=None, key=None, help=None)
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
#st.write('Sentiment:', run_sentiment_analysis(txt))

#Date Input
#streamlit.date_input(label, value=None, min_value=None, max_value=None, key=None, help=None)
#d = st.date_input(
#    "When's your birthday",
#    datetime.date(2019, 7, 6))
#st.write('Your birthday is:', d)

#Time Input
#streamlit.time_input(label, value=None, key=None, help=None)
#t = st.time_input('Set an alarm for', datetime.time(8, 45))
#st.write('Alarm is set for', t)

#File Uploader
#streamlit.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
#Insert a file uploader that accepts multiple files at a time:
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

#Color Picker
#streamlit.color_picker(label, value=None, key=None, help=None)
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

#Add Widgets to Sidebar
add_write = st.sidebar.write("Sidebar")

#Lay out your app
#streamlit.beta_container()
with st.beta_container():
   st.write("This is inside the container")
   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")

#Beta Columns
#streamlit.beta_columns(spec)
col1, col2, col3 = st.beta_columns(3)
with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

#Beta Expander
#streamlit.beta_expander(label=None, expanded=False)
st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
with st.beta_expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

#Display Code
#streamlit.echo(code_location='above')
with st.echo():
    st.write('This code will be printed')

#Display Progress and status
#streamlit.progress(value)
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

#Display Progress and status
#streamlit.spinner(text='In progress...')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

#Balloons
#streamlit.balloons()

#Errors
#streamlit.error(body)
st.error('This is an error')

#Warning
#streamlit.warning(body)
st.warning('This is a warning')

#Info
#streamlit.info(body)
st.info('This is a purely informational message')

#Success
#streamlit.success(body)
st.success('This is a success message!')

#Exception
#streamlit.exception(exception)
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)


