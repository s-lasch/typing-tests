import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# use a global color palette
global color_discrete_sequence
color_discrete_sequence = px.colors.sequential.RdBu

# create a pie chart that shows the proportions of each mode of typing test
def pie(df, lang):
	df_pie = df[df["language"] == lang].groupby('mode')['mode'].count().to_frame().rename(columns={'mode':'count'}).reset_index()
	pie = px.pie(df_pie, 
		     title='<b>Most Common Modes</b>',
		     labels='mode',
		     values='count', 
		     custom_data=['mode'],
		     # height=500,
		     color_discrete_sequence=color_discrete_sequence)
	
	pie.update_traces(hovertemplate='<b>Mode:</b> %{customdata[0]}<br><b>Tests Taken:</b> %{value}</br>')
	pie.update_layout(title_x=0.5)
	return pie


# create a series of boxplots that shows descriptive stats about the data
def box(df, title, col):
	fig = px.box(df, 
		     title=f'<b>{title.upper()}</b>', 
		     y=col,
		     facet_col='mode',
		     color='mode',
		     color_discrete_map={'words': color_discrete_sequence[0], 'time': color_discrete_sequence[1],
					 'quote': color_discrete_sequence[2], 'custom': color_discrete_sequence[3], 
					 'zen': color_discrete_sequence[4]
					},
		     category_orders={'mode': df['mode'].value_counts().to_frame().reset_index().rename(columns={'index':'mode', 'mode':'count'}).sort_values('count', ascending=False)['mode']}
		    )
	
	fig.update_layout(title_x=0.5, showlegend=False)
	return fig


# creat a sunburst chart that shows the proportions of modes WITHIN each mode
def sun(df):
	fig = px.sunburst(df,
			  title='<b>Breakdown of Each Mode</b>',
			  path=['mode', 'mode2'], 
			  color_discrete_sequence=color_discrete_sequence
			 )
	
	fig.update_layout(title_x=0.5)
	return fig

