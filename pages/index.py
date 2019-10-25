import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

header1 = html.Div(
    [html.H1("Welcome to print(fiction)"), html.P("A predictive modeling project by Tobias Reaper")], id="header"
)

mainDiv = html.Div(
    [
        html.Header(
            [
                html.H2("Turn the knobs."),
                html.H2("Try the dials."),
                html.H2("Slide the sliders."),
                html.P("I dare you..."),
            ],
            className="major container medium",
        ),
        html.Div(
            [
                html.Section(
                    [
                        html.A(
                            [html.Img(src=app.get_asset_url("images/pic01.jpg"))],
                            href="#",
                            className="image icon solid fa-signal",
                        ),
                        html.Div(
                            [
                                html.H3("The First Thing"),
                                html.P(
                                    "Vitae natoque dictum etiam semper magnis enim feugiat amet curabitur tempor orci penatibus. Tellus erat mauris ipsum fermentum etiam vivamus eget. Nunc nibh morbi quis fusce lacus."
                                ),
                            ],
                            className="content",
                        ),
                    ],
                    className="feature left",
                ),
                html.Section(
                    [
                        html.A(
                            [html.Img(src=app.get_asset_url("images/pic02.jpg"))],
                            href="#",
                            className="image icon solid fa-signal",
                        ),
                        html.Div(
                            [
                                html.H3("The Second Thing"),
                                html.P(
                                    "Heirloom farm-to-table XOXO tote bag Marfa deep v kale chips messenger bag distillery Thundercats whatever Neutra dreamcatcher crucifix actually Portland Odd Future ennui bespoke biodiesel."
                                ),
                            ],
                            className="content",
                        ),
                    ],
                    className="feature right",
                ),
                html.Section(
                    [
                        html.A(
                            [html.Img(src=app.get_asset_url("images/pic03.jpg"))],
                            href="#",
                            className="image icon solid fa-signal",
                        ),
                        html.Div(
                            [
                                html.H3("The Third Thing"),
                                html.P(
                                    "McSweeney's PBR Intelligentsia readymade organic pickled hashtag fanny pack Carles typewriter gastropub cray meh cred post-ironic brunch."
                                ),
                            ],
                            className="content",
                        ),
                    ],
                    className="feature left",
                ),
            ],
            className="box alt container",
        ),
        html.Footer(
            [
                html.H3("Get shady with data science!"),
                html.P("See how your prediction stacks up against a machine learning model!"),
                html.Ul(
                    [html.Li(html.A("Read like a book", href="#", className="button"))], className="actions special"
                ),
            ],
            className="major container medium",
        ),
    ],
    className="main",
)

intro = """
        ## Is It Fiction?

        🤔 Make a prediction if the book title belongs a fiction or nonfiction book.

        🎯 See how your prediction stacks up against the model!
        """


column1 = dbc.Col(header1, width=12)

column2 = dbc.Col(mainDiv, width=12)

# gapminder = px.data.gapminder()
# fig = px.scatter(
#     gapminder.query("year==2007"),
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=True,
#     size_max=60,
# )

# column2 = dbc.Col([dcc.Graph(figure=fig)])

layout = dbc.Container([dbc.Row(column1), dbc.Row(column2)], fluid=True)
