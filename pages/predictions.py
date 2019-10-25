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

# spacer = dbc.Container(html.Div([html.Div(html.Br(), html.Br())], className="header"))

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

mainDiv = html.Div(
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

plainParagraph1 = dbc.Container(
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

plainParagraph2 = dbc.Container(
    html.Div(
        dcc.Markdown(
            """
### Biodiesel Beard

_Flannel Blue Bottle sustainable whatever..._

Pinterest ethical photo booth *raw denim blog* gluten-free 
readymade chambray. Sartorial banh mi disrupt PBR plaid 
American Apparel trust fund.

> You probably haven't heard of them.

DIY Etsy cray squid direct trade. Neutra next level skateboard 
hashtag actually deep v keytar ugh mixtape Kickstarter normcore 
pork belly. Chillwave viral Pitchfork drinking vinegar banjo 
8-bit High Life cardigan aesthetic literally chia polaroid 
try-hard Bushwick pug.

Artisan flexitarian fanny pack +1!
"""
        )
    )
)

# ====== DAQ ====== #
ledDisplay = dbc.Container(daq.LEDDisplay(id="LED-display", label="Higher!", value=6))

labelSlider = dbc.Container(
    daq.Slider(
        id="vertical-slider",
        min=0,
        max=100,
        value=50,
        handleLabel={"showCurrentValue": True, "label": "VALUE"},
        step=10,
        size=500,
        vertical=True,
    )
)

knob = dbc.Container(daq.Knob(id="daq-knob-doe", min=0, value=8, max=10))

indicator = dbc.Container(daq.Indicator(id="my-daq-indicator", value=True, color="#00cc96"))
numberInput = dbc.Container(daq.NumericInput(id="my-daq-numericinput", min=0, value=5, max=10))


@app.callback(
    dash.dependencies.Output("LED-display", "value"),
    [dash.dependencies.Input("vertical-slider", "value")],
)
def update_output(value):
    return str(value)


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


# ====== Define Layout ====== #
# Define rows before inserting into layout container list
layout = dbc.Container([feature, rowSplitDaq, rowSplit, rowFeature], fluid=True)

# layout = dbc.Row([column1, column2])
