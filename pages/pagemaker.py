import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


headerPred = html.Div(
    [
        html.Span(className="logo icon solid fa-poo-storm"),
        html.H1("Predictions"),
        html.P("print(fiction)"),
    ],
    id="header",
)

feature = dbc.Container(
    html.Header(
        [html.H2("Predictions"), html.Span(className="logo icon solid fa-cog"), html.Br()],
        className="major container medium",
    )
)


def feature_flux(headline="Flux", icon="cog"):
    """
    Returns a feature container rendered with 'headline' text
    and specified fontawesome icon name. 
    https://fontawesome.com/icons?d=gallery&m=free
    """
    return dbc.Container(
        html.Header(
            [html.H2(headline), html.Span(className=f"logo icon solid fa-{icon}"), html.Br()],
            className="major container medium",
        )
    )


featureTop = dbc.Container(
    html.Header(
        [html.H2("Fiction"), html.Span(className="logo icon solid fa-bolt"), html.Br()],
        className="major container medium",
    )
)

featureLeft = dbc.Container(
    html.Section(
        [
            html.A(
                [html.Img(src=app.get_asset_url("images/pic01.jpg"))],
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

featureRight = dbc.Container(
    html.Section(
        [
            html.A(
                [html.Img(src=app.get_asset_url("images/pic02.jpg"))],
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

results = html.Div(
    [featureTop, html.Div([featureLeft, featureRight], className="box alt container")],
    className="main",
)

# ====== Simple Centered ====== #
featureCenter = dbc.Container(
    html.Section(
        [
            html.A(
                [html.Img(src=app.get_asset_url("images/pic01.jpg"))],
                href="#",
                className="image icon solid fa-cog",
            ),
            html.Div(
                [
                    html.H3("Insightations"),
                    html.P(
                        "Tousled shabby chic scenester Odd Future Carles paleo Pinterest pug vegan Portland ugh cliche wayfarers four loko wolf tofu locavore."
                    ),
                ],
                className="content",
            ),
        ],
        className="feature",
    )
)

# ====== Header Components ====== #
description = dbc.Container(
    html.Div(
        dcc.Markdown(
            """
### Quinoa Letterpress

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
)

description = dbc.Container(
    html.Div(
        dcc.Markdown(
            """
### Quinoa Letterpress

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
)

description = dbc.Container(
    html.Div(
        dcc.Markdown(
            """
### Quinoa Letterpress

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

# ====== DAQ Components ====== #

predict_left = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Tweak Book Features
            ---
            """
        ),
        dcc.Markdown("""##### **Interest Rate**"""),
        dcc.Slider(
            id="interest",
            min=5,
            max=35,
            step=0.25,
            value=20,
            updatemode="drag",
            marks={n: str(n) for n in range(5, 36, 5)},
            className="mb-5",
        ),
        html.Div(id="interest-rate-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Loan Amount**"""),
        dcc.Slider(
            id="loan",
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
        html.Div(id="loan-amount-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Sub Grade**"""),
        dcc.Slider(
            id="subgrade",
            min=1,
            max=35,
            step=1,
            value=35,
            updatemode="drag",
            marks={
                1: "A1",
                2: "A2",
                3: "A3",
                4: "A4",
                5: "A5",
                6: "B1",
                7: "B2",
                8: "B3",
                9: "B4",
                10: "B5",
                11: "C1",
                12: "C2",
                13: "C3",
                14: "C4",
                15: "C5",
                16: "D1",
                17: "D2",
                18: "D3",
                19: "D4",
                20: "D5",
                21: "E1",
                22: "E2",
                23: "E3",
                24: "E4",
                25: "E5",
                26: "F1",
                27: "F2",
                28: "F3",
                29: "F4",
                30: "F5",
                31: "G1",
                32: "G2",
                33: "G3",
                34: "G4",
                35: "G5",
            },
            className="mb-5",
        ),
        dcc.Markdown("""##### **Monthly Installment Payment**"""),
        dcc.Slider(
            id="installment",
            min=5,
            max=1800,
            step=5,
            value=900,
            marks={5: "$5", 500: "$500", 1000: "$1,000", 1500: "$1,500", 1800: "$1,800"},
            className="mb-5",
        ),
        html.Div(id="installment-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Annual Income of Loan Applicant**"""),
        dcc.Slider(
            id="income",
            min=10000,
            max=500000,
            step=500,
            value=250000,
            updatemode="drag",
            marks={
                10000: "$10,000",
                50000: "$50,000",
                100000: "$100,000",
                150000: "$150,000",
                200000: "$200,000",
                250000: "$250,000",
                300000: "$300,000",
                350000: "$350,000",
                400000: "$400,000",
                450000: "$450,000",
                500000: "$500,000",
            },
            # tooltip={'always_visible':True, 'placement':'bottomLeft'}, THIS LOOKS BAD!
            className="mb-5",
        ),
        html.Div(id="annual-income-slider", style={"textAlign": "center"}),
        dcc.Markdown("""##### **Term of Loan**"""),
        dcc.RadioItems(
            id="term",
            options=[{"label": "36 Months", "value": 1}, {"label": "60 Months", "value": 2}],
            value=2,
            labelStyle={"margin-right": "20px"},
            className="mb-5",
        ),
    ],
    md=6,
)


# ============================================= #
# ================== Lay Out ================== #
# ============================================= #

# ====== DAQ Section ====== #
columnSlider = dbc.Col(labelSlider, width=6)
columnDisplay = dbc.Col(ledDisplay, width=6)
rowSingleDaq = dbc.Row(columnSlider)

rowSplitDaq = dbc.Container(dbc.Row([columnSlider, columnDisplay]))

# ====== Header Section ====== #
columnHeader = dbc.Col(headerPred, width=True)
rowHeader = dbc.Row(columnHeader)

# ====== Simple Central ====== #
columnCenter = dbc.Col(featureCenter)
rowCenter = dbc.Row(columnHeader)

# ====== Split Section ====== #
columnLeft = dbc.Col(plainParagraph1, md=6)
columnRight = dbc.Col(plainParagraph2, md=6)
rowSplit = dbc.Row([columnLeft, columnRight])
rowSingle = dbc.Row(plainParagraph2)

# twoOneRow = dbc.Row()

# ====== Feature Section ====== #
columnFeature = dbc.Col([mainDiv])
rowFeature = dbc.Row([columnFeature])

# ====== Layout Utils ====== #
# TODO: utils section for layout functions and snippets
line_style = {"borderWidth": "2px"}
line_column = dbc.Col(html.Div(html.Hr(style=horizStyle)))

# ====== Define Layout ====== #
# Define rows before inserting into layout container list
layout = dbc.Container([feature, rowSplitDaq, horizCol, rowSplit, rowFeature], fluid=True)

# layout = dbc.Row([column1, column2])

