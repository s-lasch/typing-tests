import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# use a global color palette
global color_discrete_sequence
color_discrete_sequence = px.colors.sequential.RdBu


def filter_language(df, lang):
    '''
    Filters an input dataset by the desired language. If there is no language specified, just
    return the whole dataset.

    Parameters:
        DataFrame df: DataFrame to filter.
        str lang: Desired language to filter for. If None, then return data for all langauges
                  available.
    Returns:
        A pandas DataFrame.
    '''

    if lang is not None:
        return df[df["language"] == lang]

    return df

# create a pie chart that shows the proportions of each mode of typing test
def pie(df, lang=None):
    '''
    Creates a pie chart showing proportions of each typing test mode.

    Parameters:
        DataFrame df: Input data.
        str lang:     Desired language. If None, will use all languages available.
    Returns:
        Pie chart depicting proportions of each typing test mode.
    '''

    df_pie = filter_language(df, lang)

    df_pie = df_pie.groupby('mode')['mode'].count().to_frame().rename(columns={'mode':'count'}).reset_index()
    
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
    
# create a pie chart that shows the proportions of each language
def lang_pie(df):
    '''
    Creates a pie chart showing proportions of each typing test language used.

    Parameters:
        DataFrame df: Input data.
    Returns:
        Pie chart depicting proportions of each typing test language.
    '''

    df_pie = df.groupby('language')['language'].count().to_frame().rename(columns={'language':'count'}).reset_index()
    
    pie = px.pie(df_pie, 
		     title='<b>Languages</b>',
		     labels='language',
		     values='count', 
		     custom_data=['language'],
		     # height=500,
		     color_discrete_sequence=color_discrete_sequence)
	
    pie.update_traces(hovertemplate='<b>Language:</b> %{customdata[0]}<br><b>Tests Taken:</b> %{value}</br>')
    pie.update_layout(title_x=0.5)
    return pie


# create a series of boxplots that shows descriptive stats about the data
def box(df, title, col, lang=None):
    '''
    Create a series of box-and-whisker plots that shows stats. There is an option to filter by 
    language for this plot.

    Parameters:
        DataFrame df: Input data.
        str title:    Title of the plot.
        str col:      Column to show. One of 'wpm', 'acc', 'rawWpm', or 'consistency'.
        str lang:     Desired language. If None, will use all languages available.
    '''

    df_box = filter_language(df, lang)

    fig = px.box(df_box, 
		     title=f'<b>{title.upper()}</b>', 
		     y=col,
		     facet_col='mode',
		     color='mode',
		     color_discrete_map={'words': color_discrete_sequence[0], 'time': color_discrete_sequence[1],
					 'quote': color_discrete_sequence[2], 'custom': color_discrete_sequence[3], 
					 'zen': color_discrete_sequence[4]
					},
		     category_orders={'mode': df_box['mode'].value_counts().to_frame().reset_index().rename(columns={'index':'mode', 'mode':'count'}).sort_values('count', ascending=False)['mode']}
		    )
	
    fig.update_layout(title_x=0.5, showlegend=False)
    return fig


# create a sunburst chart that shows the proportions of modes WITHIN each mode
def sun(df, lang=None):
    '''
    Create a sunburst chart showing nested proportions.

    Parameters:
        DataFrame df: Input data.
        str lang:     Desired language. If None, will use all languages available.
    '''

    df_sun = filter_language(df, lang)

    fig = px.sunburst(df,
			  title='<b>Breakdown of Each Mode</b>',
			  path=['mode', 'mode2'], 
			  color_discrete_sequence=color_discrete_sequence
			 )
	
    fig.update_layout(title_x=0.5)
    return fig

