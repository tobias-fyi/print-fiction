import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app, server
from pages import index


# ====== Navigation ====== #
nav = html.Ul(
    [
        html.Li(html.A("print(fiction)", href="/", className="nav-link")),
        html.Li(html.A("Introduction", href="/#introduction", className="nav-link")),
        html.Li(html.A("Predict", href="/#predict", className="nav-link")),
        html.Li(html.A("Results", href="/#results", className="nav-link")),
        html.Li(html.A("Process", href="/#process", className="nav-link")),
    ],
    className="nav",
)

# ====== Footer ====== #
customFooter = dbc.Container(
    html.Div(
        html.Div(
            [
                html.H2("Tobias Reaper"),
                html.Ul(
                    [
                        html.Li(
                            html.A(
                                html.I(className="fas fa-envelope-square mr-1"),
                                href="mailto:tobyreaper@gmail.com",
                            )
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
                                html.I(className="fab fa-twitter-square mr-1"),
                                href="https://twitter.com/tobiasfyi/",
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
    [
        dcc.Location(id="url", refresh=False),
        nav,
        dbc.Container(id="page-content", fluid=True),
        html.Hr(),
        customFooter,
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return index.layout
    else:
        return dcc.Markdown("## Page not found")


if __name__ == "__main__":
    app.run_server(debug=True)
