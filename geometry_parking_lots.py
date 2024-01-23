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
                    title='Parking Coverage by Region',
                     color_continuous_scale=px.colors.diverging.RdYlGn,  # Reverse Reds color scale
                    range_color=[40, 80],  # Specify the range for the color scale
                    )

# Customize the background color
fig.update_layout(
    geo=dict(
        bgcolor='lightgray',  # Set the background color
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
st.write('See the map below, where states are shaded based on the percentage of POI that have an associated parking lot POI')
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
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)
