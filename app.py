import dash
import dash_bootstrap_components as dbc


external_stylesheets = [
    "/assets/css/main.css",
    "https://use.fontawesome.com/releases/v5.9.0/css/all.css",  # for social media icons
    # "/assets/css/bootstrap.css",
    # dbc.themes.SANDSTONE,  # Bootswatch theme
]

meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = "print(fiction)"  # appears in browser title bar
server = app.server

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body class="is-preload">
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            <script src="assets/js/jquery.min.js"></script>
            <script src="assets/js/browser.min.js"></script>
            <script src="assets/js/breakpoints.min.js"></script>
            <script src="assets/js/util.js"></script>
            <script src="assets/js/main.js"></script>
            {%renderer%}
        </footer>
    </body>
</html>
"""

