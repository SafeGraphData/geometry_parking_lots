import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(
    page_title="Geometry Summary Statistics - Parking Lots",
    layout="wide"
)

####Parking coverage by region ####

state_df = read_from_gsheets("Parking - regions").assign(**{
        "total_parking_poi": lambda df: df["total_parking_poi"].astype(int),
        "%_poi_with_parking": lambda df: ((df["pct_poi_with_parking"].astype(float)) * 100).astype(float)
    }).rename(columns={"%_poi_with_parking": "% of POI with Parking Lot"})

state_df['% of POI with Parking Lot'] = [round(x,1) for x in state_df['% of POI with Parking Lot']]
state_df['total_parking_poi'] = state_df['total_parking_poi'].map('{:,.0f}'.format)

# Create the plot with USA scope, gray background, and tooltips
fig = px.choropleth(state_df,
                    locations='state',
                    color='% of POI with Parking Lot',
                    hover_name='state',
                    locationmode='USA-states',  # Use predefined US state boundaries
                    scope='usa',  # Set the scope to 'usa'
                    #title='Parking Coverage by Region',
                     color_continuous_scale=px.colors.diverging.RdYlGn,  # Reverse Reds color scale
                    range_color=[40, 80],  # Specify the range for the color scale
                    )

# Customize the background color
fig.update_layout(
    geo=dict(
        bgcolor='white',  # Set the background color
    )
)

# Add tooltips with state information
fig.update_traces(hovertemplate='State:  <b>%{hovertext}</b><br>% POI with Parking: %{z}%<br>Total Parking POI: %{text}<extra></extra>',
                  text=state_df['total_parking_poi'])

fig.update_layout(
    legend=dict(
        orientation='h',  # Set the orientation to horizontal
        x=0,  # Set the x position
        y=1.02,  # Set the y position
       # xanchor='left',  # Set the x anchor to left
        yanchor='bottom'  # Set the y anchor to bottom
    )
)
fig.update_layout(height=800, width=1400) 
#st.write('See the map below, where states are shaded based on the percentage of POI that have an associated parking lot POI')
st.plotly_chart(fig, use_container_width=True)


hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-03-29 14:27:03.075118
# Keep-alive comment: 2025-03-31 15:59:05.700606
# Keep-alive comment: 2025-03-31 19:24:44.192570
# Keep-alive comment: 2025-04-01 06:22:25.279304
# Keep-alive comment: 2025-04-01 17:23:18.960584
# Keep-alive comment: 2025-04-02 04:23:04.717420
# Keep-alive comment: 2025-04-02 15:23:03.900800
# Keep-alive comment: 2025-04-03 02:22:38.728781
# Keep-alive comment: 2025-04-03 13:23:44.161584
# Keep-alive comment: 2025-04-04 00:24:06.061790
# Keep-alive comment: 2025-04-04 11:23:36.940223
# Keep-alive comment: 2025-04-04 22:22:48.846087
# Keep-alive comment: 2025-04-05 09:22:39.041115
# Keep-alive comment: 2025-04-05 20:23:54.634797
# Keep-alive comment: 2025-04-06 07:23:24.194124
# Keep-alive comment: 2025-04-06 18:22:55.773570
# Keep-alive comment: 2025-04-07 05:23:19.391808
# Keep-alive comment: 2025-04-07 16:24:18.298814
# Keep-alive comment: 2025-04-08 03:23:34.714635
# Keep-alive comment: 2025-04-08 14:23:50.106606
# Keep-alive comment: 2025-04-09 01:23:18.485109
# Keep-alive comment: 2025-04-09 12:22:59.564689
# Keep-alive comment: 2025-04-09 23:23:19.126623
# Keep-alive comment: 2025-04-10 10:22:27.373189
# Keep-alive comment: 2025-04-10 21:22:52.480993
# Keep-alive comment: 2025-04-11 08:25:03.350262
# Keep-alive comment: 2025-04-11 19:25:23.994416
# Keep-alive comment: 2025-04-12 06:22:59.822240
# Keep-alive comment: 2025-04-12 17:23:13.107240
# Keep-alive comment: 2025-04-13 04:22:29.182289
# Keep-alive comment: 2025-04-13 15:23:27.603191
# Keep-alive comment: 2025-04-14 02:23:48.737562
# Keep-alive comment: 2025-04-14 13:23:12.042871
# Keep-alive comment: 2025-04-15 00:22:57.610201
# Keep-alive comment: 2025-04-15 11:23:19.264004
# Keep-alive comment: 2025-04-15 22:23:03.016309
# Keep-alive comment: 2025-04-16 09:23:42.409502
# Keep-alive comment: 2025-04-16 20:23:32.479495
# Keep-alive comment: 2025-04-17 07:23:03.740980
# Keep-alive comment: 2025-04-17 18:25:27.237779
# Keep-alive comment: 2025-04-18 05:22:48.000658
# Keep-alive comment: 2025-04-18 16:22:53.382079
# Keep-alive comment: 2025-04-19 03:23:18.668042
# Keep-alive comment: 2025-04-19 14:22:29.503368
# Keep-alive comment: 2025-04-20 01:22:27.862248
# Keep-alive comment: 2025-04-20 12:23:23.149086
# Keep-alive comment: 2025-04-20 23:22:57.932072
# Keep-alive comment: 2025-04-21 10:23:44.055384
# Keep-alive comment: 2025-04-21 21:23:07.376089
# Keep-alive comment: 2025-04-22 08:23:18.140171
# Keep-alive comment: 2025-04-22 19:23:18.130771
# Keep-alive comment: 2025-04-23 06:22:52.278103
# Keep-alive comment: 2025-04-23 17:22:53.605793
# Keep-alive comment: 2025-04-24 04:22:58.575719
# Keep-alive comment: 2025-04-24 15:23:53.970143
# Keep-alive comment: 2025-04-25 02:22:22.414131
# Keep-alive comment: 2025-04-25 13:23:53.131306
# Keep-alive comment: 2025-04-25 16:08:04.459986
# Keep-alive comment: 2025-04-25 16:17:59.539042
# Keep-alive comment: 2025-04-26 00:23:33.447665
# Keep-alive comment: 2025-04-26 11:23:29.210131
# Keep-alive comment: 2025-04-26 22:22:28.380288
# Keep-alive comment: 2025-04-27 09:22:58.990246
# Keep-alive comment: 2025-04-27 20:22:53.546805
# Keep-alive comment: 2025-04-28 07:23:04.708231
# Keep-alive comment: 2025-04-28 18:23:43.799082
# Keep-alive comment: 2025-04-29 05:23:13.743300
# Keep-alive comment: 2025-04-29 16:23:57.125121
# Keep-alive comment: 2025-04-30 03:22:48.588260
# Keep-alive comment: 2025-04-30 14:22:57.992627
# Keep-alive comment: 2025-05-01 01:23:27.836904
# Keep-alive comment: 2025-05-01 12:22:58.452126
# Keep-alive comment: 2025-05-01 23:22:31.905113
# Keep-alive comment: 2025-05-02 10:23:17.577095
# Keep-alive comment: 2025-05-02 21:22:27.717887
# Keep-alive comment: 2025-05-03 08:22:52.489567
# Keep-alive comment: 2025-05-03 19:23:12.482473
# Keep-alive comment: 2025-05-04 06:23:17.665886
# Keep-alive comment: 2025-05-04 17:22:27.072523
# Keep-alive comment: 2025-05-05 04:23:37.018443
# Keep-alive comment: 2025-05-05 15:22:52.598849
# Keep-alive comment: 2025-05-06 02:23:47.166282
# Keep-alive comment: 2025-05-06 13:22:47.858559
# Keep-alive comment: 2025-05-07 00:22:48.143985
# Keep-alive comment: 2025-05-07 11:22:47.787647
# Keep-alive comment: 2025-05-07 22:22:57.614568
# Keep-alive comment: 2025-05-08 09:22:47.672366
# Keep-alive comment: 2025-05-08 20:22:47.616915
# Keep-alive comment: 2025-05-09 07:22:58.072952
# Keep-alive comment: 2025-05-09 18:23:17.773766
# Keep-alive comment: 2025-05-10 05:22:57.757215
# Keep-alive comment: 2025-05-10 16:22:52.042094
# Keep-alive comment: 2025-05-11 03:22:52.224928
# Keep-alive comment: 2025-05-11 14:22:43.897685
# Keep-alive comment: 2025-05-12 01:22:49.217711
# Keep-alive comment: 2025-05-12 12:23:18.284001
# Keep-alive comment: 2025-05-12 23:22:52.498581
# Keep-alive comment: 2025-05-13 10:23:47.531203
# Keep-alive comment: 2025-05-13 21:22:52.597591
# Keep-alive comment: 2025-05-14 08:23:00.654700
# Keep-alive comment: 2025-05-14 19:23:17.995016
# Keep-alive comment: 2025-05-15 06:23:18.483624
# Keep-alive comment: 2025-05-15 17:23:42.678099
# Keep-alive comment: 2025-05-16 04:23:04.579481
# Keep-alive comment: 2025-05-16 15:22:03.480534
# Keep-alive comment: 2025-05-17 02:22:22.790501
# Keep-alive comment: 2025-05-17 13:22:59.550824
# Keep-alive comment: 2025-05-18 00:22:23.867933
# Keep-alive comment: 2025-05-18 11:22:52.815363
# Keep-alive comment: 2025-05-18 22:22:50.122870
# Keep-alive comment: 2025-05-19 09:23:20.793395
# Keep-alive comment: 2025-05-19 20:22:22.888516
# Keep-alive comment: 2025-05-20 07:22:40.044928
# Keep-alive comment: 2025-05-20 18:23:53.140962
# Keep-alive comment: 2025-05-21 05:22:25.208296
# Keep-alive comment: 2025-05-21 16:22:33.093034
# Keep-alive comment: 2025-05-22 03:22:27.561471
# Keep-alive comment: 2025-05-22 14:22:23.491101
# Keep-alive comment: 2025-05-23 01:22:29.990153
# Keep-alive comment: 2025-05-23 12:22:29.855749
# Keep-alive comment: 2025-05-23 23:22:34.883496
# Keep-alive comment: 2025-05-24 10:22:33.099084
# Keep-alive comment: 2025-05-24 21:22:29.487515
# Keep-alive comment: 2025-05-25 08:22:28.836386
# Keep-alive comment: 2025-05-25 19:22:34.667096
# Keep-alive comment: 2025-05-26 06:22:19.139317
# Keep-alive comment: 2025-05-26 17:22:24.186503
# Keep-alive comment: 2025-05-27 04:22:30.037079
# Keep-alive comment: 2025-05-27 15:22:33.382793
# Keep-alive comment: 2025-05-28 02:22:43.968663
# Keep-alive comment: 2025-05-28 13:22:31.151646
# Keep-alive comment: 2025-05-29 00:22:28.286094
# Keep-alive comment: 2025-05-29 11:22:22.778718
# Keep-alive comment: 2025-05-29 22:22:37.780049
# Keep-alive comment: 2025-05-30 09:22:22.343986
# Keep-alive comment: 2025-05-30 20:22:22.937381
# Keep-alive comment: 2025-05-31 07:22:35.058737
# Keep-alive comment: 2025-05-31 18:22:30.879937
# Keep-alive comment: 2025-06-01 05:22:29.417989
# Keep-alive comment: 2025-06-01 16:22:42.968337
# Keep-alive comment: 2025-06-02 03:22:44.187109
# Keep-alive comment: 2025-06-02 14:22:33.604994
# Keep-alive comment: 2025-06-03 01:22:25.002618
# Keep-alive comment: 2025-06-03 12:22:38.306327
# Keep-alive comment: 2025-06-03 23:22:32.682069
# Keep-alive comment: 2025-06-04 10:22:34.069740
# Keep-alive comment: 2025-06-04 21:22:12.815265
# Keep-alive comment: 2025-06-05 08:22:35.503856
# Keep-alive comment: 2025-06-05 19:22:24.344919
# Keep-alive comment: 2025-06-06 06:22:24.886756
# Keep-alive comment: 2025-06-06 17:22:07.668921
# Keep-alive comment: 2025-06-07 04:22:09.066947
# Keep-alive comment: 2025-06-07 15:22:19.148615
# Keep-alive comment: 2025-06-08 02:22:24.527637
# Keep-alive comment: 2025-06-08 13:22:26.099796
# Keep-alive comment: 2025-06-09 00:22:08.896077
# Keep-alive comment: 2025-06-09 11:22:22.958159
# Keep-alive comment: 2025-06-09 22:22:30.965285
# Keep-alive comment: 2025-06-10 09:22:33.037464
# Keep-alive comment: 2025-06-10 20:22:27.613857
# Keep-alive comment: 2025-06-11 07:22:28.552268
# Keep-alive comment: 2025-06-11 18:24:14.154078
# Keep-alive comment: 2025-06-12 05:22:25.681055
# Keep-alive comment: 2025-06-12 16:22:28.558857
# Keep-alive comment: 2025-06-13 03:22:30.076954
# Keep-alive comment: 2025-06-13 14:22:18.621601
# Keep-alive comment: 2025-06-14 01:22:39.025752
# Keep-alive comment: 2025-06-14 12:22:26.444064
# Keep-alive comment: 2025-06-14 23:22:17.585250
# Keep-alive comment: 2025-06-15 10:22:03.341100
# Keep-alive comment: 2025-06-15 21:22:38.764051
# Keep-alive comment: 2025-06-16 08:22:34.307667
# Keep-alive comment: 2025-06-16 19:22:18.620891
# Keep-alive comment: 2025-06-17 06:22:54.733596
# Keep-alive comment: 2025-06-17 17:22:23.147779
# Keep-alive comment: 2025-06-18 04:22:30.235248
# Keep-alive comment: 2025-06-18 15:22:25.396445
# Keep-alive comment: 2025-06-19 02:22:27.858894
# Keep-alive comment: 2025-06-19 13:22:26.175535
# Keep-alive comment: 2025-06-20 00:22:24.432164
# Keep-alive comment: 2025-06-20 11:23:13.200191
# Keep-alive comment: 2025-06-20 22:22:33.256211
# Keep-alive comment: 2025-06-21 09:22:19.153312
# Keep-alive comment: 2025-06-21 20:22:30.728988
# Keep-alive comment: 2025-06-22 07:22:23.942663
# Keep-alive comment: 2025-06-22 18:22:14.464035
# Keep-alive comment: 2025-06-23 05:22:31.297089
# Keep-alive comment: 2025-06-23 16:22:23.190222
# Keep-alive comment: 2025-06-24 03:22:29.854881
# Keep-alive comment: 2025-06-24 14:22:07.947208
# Keep-alive comment: 2025-06-25 01:22:02.883501