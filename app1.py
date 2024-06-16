from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Ammount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Ammount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={"backgroundColor": colors["background"]},
                      children=[
                          html.H1(style={"textAlign": "center",
                                         "color": colors["text"]},
                                  children="Hello Dash"),

                          html.Div(style={"textAlign": "center",
                                          "color": colors["text"]},
                                   children="""
    Dash: a web application framework for your data.
    """),

                          dcc.Graph(id="example-graph",
                                    figure=fig)
                      ])

if __name__ == "__main__":
    app.run(debug=True)
