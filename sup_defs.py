import plotly.express as px
import plotly.graph_objects as go

def bar_plot(dataf, x, y, title, x_label='X', y_label='Y', height=500, width=700):
    fig = go.Figure(go.Bar(
        x=x,
        y=y,
        text=y,
        texttemplate='%{text:.3f}',
        marker_color=['#20bf6b', '#fa8231'])
    )
    fig.update_layout(height = height, 
                      width = width,
                      title_text=title,
                      xaxis_title=x_label,
                      yaxis_title=y_label,
                      font_color='#484848',
                      template='plotly_white',
                     )
    return fig