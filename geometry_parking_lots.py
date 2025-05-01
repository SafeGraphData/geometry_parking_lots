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