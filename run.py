import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app, server
from pages import index, predictions, insights, process


nav = html.Ul(
    [
        html.Li(html.A("print(fiction)", href="/", className="nav-link")),
        html.Li(html.A("Predictions", href="/predictions", className="nav-link")),
        html.Li(html.A("Insights", href="/insights", className="nav-link")),
        html.Li(html.A("Process", href="/process", className="nav-link")),
    ],
    className="nav",
)

# nav = dbc.Nav(
#     [
#         dbc.NavItem(dbc.NavLink("print(fiction)", href="/", className="nav-link")),
#         dbc.NavItem(dbc.NavLink("Predictions", href="/predictions", className="nav-link")),
#         dbc.NavItem(dbc.NavLink("Insights", href="/insights", className="nav-link")),
#         dbc.NavItem(dbc.NavLink("Process", href="/process", className="nav-link")),
#     ]
# )

# navbar = dbc.NavbarSimple(
#     brand="print(fiction)",
#     brand_href="/",
#     children=[
#         dbc.NavItem(dcc.Link("Predictions", href="/predictions", className="nav-link")),
#         dbc.NavItem(dcc.Link("Insights", href="/insights", className="nav-link")),
#         dbc.NavItem(dcc.Link("Process", href="/process", className="nav-link")),
#     ],
#     sticky="top",
#     color="dark",
#     light=False,
#     dark=True,
# )

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span("Tobias Reaper", className="mr-2"),
                    html.A(html.I(className="fas fa-envelope-square mr-1"), href="mailto:tobyreaper@gmail.com"),
                    html.A(
                        html.I(className="fab fa-github-square mr-1"),
                        href="https://github.com/tobias-fyi/print-fiction/",
                    ),
                    html.A(
                        html.I(className="fab fa-linkedin mr-1"), href="https://www.linkedin.com/in/tobias-ea-reaper/"
                    ),
                    html.A(html.I(className="fab fa-twitter-square mr-1"), href="https://twitter.com/tobiasfyi/"),
                ],
                className="lead",
            )
        )
    )
)

customFooter = dbc.Container(
    html.Div(
        html.Div(
            [
                html.H2("Tobias Reaper"),
                html.Ul(
                    [
                        html.Li(
                            html.A(html.I(className="fas fa-envelope-square mr-1"), href="mailto:tobyreaper@gmail.com")
                        ),
                        html.Li(
                            html.A(
                                html.I(className="fab fa-github-square mr-1"),
                                href="https://github.com/tobias-fyi/print-fiction/",
                            )
                        ),
                        html.Li(
                            html.A(
                                html.I(className="fab fa-linkedin mr-1"),
                                href="https://www.linkedin.com/in/tobias-ea-reaper/",
                            )
                        ),
                        html.Li(
                            html.A(
                                html.I(className="fab fa-twitter-square mr-1"), href="https://twitter.com/tobiasfyi/"
                            )
                        ),
                    ],
                    className="icons",
                ),
            ],
            className="container medium",
        ),
        id="footer",
    ),
    fluid=True,
)

# ====== URL Routing ====== #
# https://dash.plot.ly/urls #

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), nav, dbc.Container(id="page-content", fluid=True), html.Hr(), customFooter]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return index.layout
    elif pathname == "/predictions":
        return predictions.layout
    elif pathname == "/insights":
        return insights.layout
    elif pathname == "/process":
        return process.layout
    else:
        return dcc.Markdown("## Page not found")


if __name__ == "__main__":
    app.run_server(debug=True)
