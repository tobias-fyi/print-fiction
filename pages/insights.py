import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

results = html.Div(
    [
        html.Header(
            [
                html.H2("Turn the knobs."),
                html.H3("Try the dials."),
                html.H4("Slide the sliders."),
                html.Span(className="logo icon solid fa-cog"),
                html.Br(),
                html.P("I dare you..."),
            ],
            className="major container medium",
        ),
        html.Div(
            [
                html.Section(
                    [
                        html.A(
                            [html.Img(src="assets/images/pic01.jpg")],
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
                            [html.Img(src="assets/images/pic02.jpg")],
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
                            [html.Img(src="assets/images/pic03.jpg")],
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
                    [
                        html.Li(
                            html.A(
                                "Read the machine like a book",
                                href="/predictions",
                                className="button",
                            )
                        )
                    ],
                    className="actions special",
                ),
            ],
            className="major container medium",
        ),
    ],
    className="main",
)


column2 = dbc.Col([])

layout = dbc.Row([results, column2])
