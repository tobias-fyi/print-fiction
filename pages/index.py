import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

# ====== Data ====== #
from joblib import load
import pandas as pd

# Load in dataset
df = pd.read_csv("assets/must_read_books_009-03.csv")

# Load in scikit-learn RandomForest pipeline
pipeline = load("assets/rf_pipe.joblib")
print(f"Pipeline loaded successfuly.")


# ====== Header Components ====== #
main_header = html.Div(
    [
        html.Span(className="logo icon solid fa-book-open"),
        html.H1("Welcome to print(fiction)"),
        html.P("A predictive modeling project by Tobias Reaper"),
    ],
    id="header",
)

# ====== Introduction Components ====== #
intro_header = html.Div(
    html.A(html.H2("Introduction", id="introduction"), href="#introduction"),
    className="major container medium",
)

introduction = dbc.Container(
    dcc.Markdown(
        """
Selfies messenger bag scenester beard four loko.

Pinterest shabby chic pug, Truffaut seitan roof party. 
Tonx pop-up butcher hoodie, 3 wolf moon next level 
Intelligentsia—Echo Park—fashion axe asymmetrical chillwave. 
Narwhal iPhone semiotics Marfa Pitchfork paleo keffiyeh 
try-hard church-key master cleanse normcore banjo Etsy lo-fi.

Art party meggings tofu chambray vegan organic stumptown 
cornhole chia blog biodiesel distillery mlkshk Carles 
skateboard +1 tattooed selvage sustainable tote bag.
"""
    )
)

# ====== Predict Components ====== #
predict_header = html.Div(
    html.A(html.H2("Predict", id="predict"), href="#predict"), className="major container medium"
)

predict_left = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Tweak Book Features
            ---
            """
        ),
        dcc.Markdown("""##### **Avg Rating**"""),
        dcc.Slider(
            id="avg-rating",
            min=5,
            max=35,
            step=0.25,
            value=20,
            updatemode="drag",
            marks={n: str(n) for n in range(5, 36, 5)},
            className="mb-5",
        ),
        html.Div(id="avg-rating-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Number of Ratings**"""),
        dcc.Slider(
            id="num-ratings",
            min=500,
            max=40000,
            step=50,
            value=20000,
            updatemode="drag",
            marks={
                500: "$500",
                5000: "$5,000",
                10000: "$10,000",
                15000: "$15,000",
                20000: "$20,000",
                25000: "$25,000",
                30000: "$30,000",
                35000: "$35,000",
                40000: "$40,000",
            },
            className="mb-5",
        ),
        html.Div(id="num-ratings-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Number of Pages**"""),
        dcc.Slider(
            id="num-pages",
            min=5,
            max=1800,
            step=5,
            value=900,
            marks={5: "$5", 500: "$500", 1000: "$1,000", 1500: "$1,500", 1800: "$1,800"},
            className="mb-5",
        ),
        html.Div(id="num-pages-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Number of Characters in the Title**"""),
        dcc.Slider(
            id="title-char-count",
            min=10000,
            max=500000,
            step=500,
            value=250000,
            updatemode="drag",
            marks={10000: "$10,000", 50000: "$50,000"},
            className="mb-5",
        ),
        html.Div(id="title-char-count-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Publish Year**"""),
        dcc.Slider(
            id="publish-year",
            min=5,
            max=35,
            step=0.25,
            value=20,
            updatemode="drag",
            marks={n: str(n) for n in range(5, 36, 5)},
            className="mb-5",
        ),
        html.Div(id="publish-date-slider", style={"textAlign": "center"}),
        # dcc.Markdown("""##### **Boolean Features**"""),
        dcc.Checklist(
            options=[
                {"label": "Book has subtitle", "value": 1},
                {"label": "Book is part of series", "value": 1},
                {"label": "Title begins with 'The'", "value": 1},
            ]
        ),
        # # TODO: Take input of title and use that to get has_subtitle, title_char_length, the_title
    ],
    md=6,
)

predict_right = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Prediction
            ---
            """
        ),
        daq.Gauge(
            id="ROI_Gauge",
            color={
                "gradient": True,
                "ranges": {
                    "red": [-100, 20],
                    "orange": [20, 40],
                    "yellow": [40, 60],
                    "green": [60, 100],
                },
            },
            showCurrentValue=True,
            units="Cents per Dollar Invested",
            value=0,
            min=-100,
            max=100,
            size=500,
        ),
    ]
)

# ====== Results Components ====== #
results_header = dbc.Container(
    html.Header(
        [
            html.Span(className="logo icon solid fa-poo-storm"),
            html.Div(html.A(html.H2("Results", id="results"), href="#results")),
            html.Br(),
        ],
        className="major container medium",
    )
)

results_block_1 = dbc.Container(
    dcc.Markdown(
        """
Selfies messenger bag scenester beard four loko.

Pinterest shabby chic pug, Truffaut seitan roof party. 
Tonx pop-up butcher hoodie, 3 wolf moon next level 
Intelligentsia—Echo Park—fashion axe asymmetrical chillwave. 
Narwhal iPhone semiotics Marfa Pitchfork paleo keffiyeh 
try-hard church-key master cleanse normcore banjo Etsy lo-fi.

Art party meggings tofu chambray vegan organic stumptown 
cornhole chia blog biodiesel distillery mlkshk Carles 
skateboard +1 tattooed selvage sustainable tote bag.
"""
    )
)

results_left = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src=app.get_asset_url("images/pic01.jpg")),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("The Left Thing"),
                    html.P(
                        "Vice XOXO banjo asymmetrical seitan (jean shorts) 3 wolf moon butcher bespoke literally readymade. Authentic VHS semiotics pork belly selvage sriracha salvia Neutra Tumblr."
                    ),
                ],
                className="content box",
            ),
        ],
        className="feature left",
    )
)

results_right = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src=app.get_asset_url("images/pic02.jpg")),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("The Right Thing"),
                    html.P(
                        "Heirloom farm-to-table XOXO tote bag Marfa deep v kale chips messenger bag distillery Thundercats whatever Neutra dreamcatcher crucifix actually Portland Odd Future ennui bespoke biodiesel."
                    ),
                ],
                className="content",
            ),
        ],
        className="feature right",
    )
)

results_block_2 = dbc.Container(
    dcc.Markdown(
        """
Selfies messenger bag scenester beard four loko.

Pinterest shabby chic pug, Truffaut seitan roof party. 
Tonx pop-up butcher hoodie, 3 wolf moon next level 
Intelligentsia—Echo Park—fashion axe asymmetrical chillwave. 
Narwhal iPhone semiotics Marfa Pitchfork paleo keffiyeh 
try-hard church-key master cleanse normcore banjo Etsy lo-fi.

Art party meggings tofu chambray vegan organic stumptown 
cornhole chia blog biodiesel distillery mlkshk Carles 
skateboard +1 tattooed selvage sustainable tote bag.
"""
    )
)

results_footer = (
    html.Footer(
        [
            html.H3("Get shady with data science!"),
            html.P("See how your prediction stacks up against a machine learning model!"),
            html.Ul(
                html.Li(
                    html.A("Read the machine like a book", href="/#predictions", className="button")
                ),
                className="actions special",
            ),
        ],
        className="major container medium",
    ),
)

# results = html.Div(
#     [
#         results_header,
#         html.Div(results_block_1, className="box alt container"),
#         html.Div([results_left, results_right], className="box alt container"),
#         html.Div(results_footer, className="box alt container"),
#     ],
#     className="main",
# )


# ====== Process Components ====== #
process_header = dbc.Container(
    html.Header(
        [
            html.Span(className="logo icon solid fa-poo-storm"),
            html.Div(html.A(html.H2("Process", id="process"), href="#process")),
            html.Br(),
        ],
        className="major container medium",
    )
)

process_block_1 = dbc.Container(
    dcc.Markdown(
        """
Selfies messenger bag scenester beard four loko.

Pinterest shabby chic pug, Truffaut seitan roof party. 
Tonx pop-up butcher hoodie, 3 wolf moon next level 
Intelligentsia—Echo Park—fashion axe asymmetrical chillwave. 
Narwhal iPhone semiotics Marfa Pitchfork paleo keffiyeh 
try-hard church-key master cleanse normcore banjo Etsy lo-fi.

Art party meggings tofu chambray vegan organic stumptown 
cornhole chia blog biodiesel distillery mlkshk Carles 
skateboard +1 tattooed selvage sustainable tote bag.
"""
    )
)

process_left = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src=app.get_asset_url("images/pic01.jpg")),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("The Left Thing"),
                    html.P(
                        "Vice XOXO banjo asymmetrical seitan (jean shorts) 3 wolf moon butcher bespoke literally readymade. Authentic VHS semiotics pork belly selvage sriracha salvia Neutra Tumblr."
                    ),
                ],
                className="content box",
            ),
        ],
        className="feature left",
    )
)

process_right = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src=app.get_asset_url("images/pic02.jpg")),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("The Right Thing"),
                    html.P(
                        "Heirloom farm-to-table XOXO tote bag Marfa deep v kale chips messenger bag distillery Thundercats whatever Neutra dreamcatcher crucifix actually Portland Odd Future ennui bespoke biodiesel."
                    ),
                ],
                className="content",
            ),
        ],
        className="feature right",
    )
)

process_block_2 = dbc.Container(
    dcc.Markdown(
        """
Selfies messenger bag scenester beard four loko.

Pinterest shabby chic pug, Truffaut seitan roof party. 
Tonx pop-up butcher hoodie, 3 wolf moon next level 
Intelligentsia—Echo Park—fashion axe asymmetrical chillwave. 
Narwhal iPhone semiotics Marfa Pitchfork paleo keffiyeh 
try-hard church-key master cleanse normcore banjo Etsy lo-fi.

Art party meggings tofu chambray vegan organic stumptown 
cornhole chia blog biodiesel distillery mlkshk Carles 
skateboard +1 tattooed selvage sustainable tote bag.
"""
    )
)


# ============================================= #
# ===============  Page Layout  =============== #
# ============================================= #

# ======  Layout Utils ====== #
line_style = {"borderWidth": "2px"}
line_column = dbc.Col(html.Div(html.Hr(style=line_style)))
line_row = dbc.Row(line_column)
# =========================== #

header_column = dbc.Col(main_header, width=True)

intro_column = dbc.Col(introduction, width=True)
intro_row = dbc.Row([intro_header, intro_column])

predict_header_row = dbc.Container(dbc.Row(dbc.Col(predict_header)))
predict_column_1 = dbc.Col(predict_left, width=True)
predict_column_2 = dbc.Col(predict_right, width=True)
predict_row = dbc.Row([predict_column_1, predict_column_2])

results_header_row = dbc.Container(dbc.Row(dbc.Col(results_header, width=True)))
results_column_1 = dbc.Col(results_left, width=True)
results_column_2 = dbc.Col(results_right, width=True)
results_block_1_row = dbc.Row(dbc.Col(results_block_1))
results_block_2_row = dbc.Row(dbc.Col(results_block_2))
results_row = dbc.Row([results_column_1, results_column_2])

process_header_row = dbc.Container(dbc.Row(dbc.Col(process_header, width=True)))
process_column_1 = dbc.Col(process_left, width=True)
process_column_2 = dbc.Col(process_right, width=True)
process_block_1_row = dbc.Row(dbc.Col(process_block_1))
process_block_2_row = dbc.Row(dbc.Col(process_block_2))
process_row = dbc.Row([process_column_1, process_column_2])

layout = dbc.Container(
    [
        main_header,
        intro_row,
        line_row,
        predict_header_row,
        predict_row,
        results_header_row,
        results_block_1_row,
        results_row,
        results_block_2_row,
        process_header_row,
        process_block_1_row,
        process_row,
        process_block_2_row,
    ],
    fluid=True,
)

