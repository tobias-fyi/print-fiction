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

# # Load in dataset
# df = pd.read_csv("assets/must_read_books_subset.csv")

# Load in scikit-learn RandomForest pipeline
pipeline = load("assets/rf_pipe2.joblib")
print(f"Pipeline loaded successfuly.")


img_style = {
    # "height": "80%",
    # "align": "center",
    "width": "80%"
}


# ====== Header Components ====== #
main_header = html.Div(
    [
        html.Span(className="logo icon solid fa-book-open"),
        html.H1(
            [
                "Welcome to print(",
                html.Span("fiction", style={"color": "#4eb980"}, id="nonfiction-pred"),
                ")",
            ]
        ),
        html.P("A predictive modeling project by Tobias Reaper"),
    ],
    id="header",
)

# ====== Introduction Components ====== #
intro_header = html.Div(
    html.A(html.H2("Introduction", id="introduction"), href="#introduction"),
    className="major container medium",
)

introduction1 = dbc.Container(
    dcc.Markdown(
        """
> What separates fact from fiction?  

As is the case with many things nowadays, more data brings more answers to questions like this one. 
If not the actual answers, data can at least provide a lens through which these kinds of 
questions can be explored in novel ways.

This project, print(fiction) is dedicated to exploring that question as it relates to the printed page - how are our real 
stories different from our fictional ones?

I am an avid consumer of science-fiction, much of it in book form. Exploring fictional universes and 
following the storylines that wind through them play very significant roles in my 
daily inspiration and keep me full of wonder, even in the real world.

For this project, I was curious how much valuable insight I could gather from books using a quantitative perspective, 
as I am usually viewing them from the perspective of being sucked into and being fully immersed by the stories.
"""
    )
)

intro_photo = dbc.Container(
    html.Div(
        html.Img(src="/assets/images/booklineshelf.jpg", style=img_style),
        className="image feature2",
    )
)

introduction2 = dbc.Container(
    dcc.Markdown(
        """
> Is there a line separating fact from fiction?

Well...that depends what kind of model you use.

It could be a gradient; the stories we tell or hear others tell are never 100%
nonfiction.
We all like to boost our own narratives just a little bit every now and again.

But in the case of my project, what separates fiction from nonfiction is...

> ...several sliders and a few boolean switches.

I go into more detail about the data, the model, and the process in my portfolio:

> [tobias.fyi - print(fiction)](https://tobias.fyi/workshop/printfiction/)

To give a brief overview, I built a pipeline that scraped and wrangled book metadata
from GoodReads, which I used to train and validate a series of machine learning models.
My baseline was a simple logistic regression model that achieved an F1 score of .65.
I iterated on the models, engineered some new features and tuned some hyperparameters,
ultimately getting the best performance/complexity ratio with a random forest, which
achieved an F1 of about .80.

Thanks to the wonders of the Cloud, this model was trained on my laptop, and now lives
on one or more servers somewhere, happily evaluating the tweaking of its parameters in
real time. 

The entire point of its existence?

To provide its best guess at whether those parameters indicate a nonfiction or fiction
book.

Go ahead and tweak the input a bit and watch the results. The green text represents the
model's prediction based on the parameters given to it via the sliders and switches.

Be on the lookout for any significant separating factors between nonfiction and fiction books; 
any patterns that the model may have picked up on. They're in there somewhere...
"""
    )
)

# ====== Predict Components ====== #
predict_header = dbc.Container(
    html.Header(
        [
            html.Span(className="logo icon solid fa-poo-storm"),
            html.Div(html.A(html.H2("Predict", id="predict"), href="#predict")),
            dbc.Container(
                html.Div(
                    html.H3(
                        [
                            "print(",
                            html.Span(id="nonfiction-pred", style={"color": "#4eb980"}),
                            ")",
                        ]
                    )
                )
            ),
            html.Br(),
        ],
        className="container medium",
    )
)

predict_left = dbc.Col(
    [
        dcc.Markdown(
            """
            ### Tweak the Features
            ---
            """
        ),
        dcc.Markdown("""##### **Avg Rating**"""),
        dcc.Slider(
            id="avg-rating",
            min=1,
            max=5,
            step=1,
            value=4,
            updatemode="drag",
            marks={n: str(n) for n in range(1, 6)},
            className="mb-5",
        ),
        html.Div(
            id="avg-rating-slider", style={"textAlign": "center"}, className="mb-5"
        ),
        dcc.Markdown("""##### **Number of Ratings**"""),
        dcc.Slider(
            id="num-ratings",
            min=1,
            max=1000000,
            step=200000,
            value=20000,
            updatemode="drag",
            marks={n: str(n) for n in range(0, 1000001, 200000)},
            className="mb-5",
        ),
        html.Div(
            id="num-ratings-slider", style={"textAlign": "center"}, className="mb-5"
        ),
        dcc.Markdown("""##### **Number of Pages**"""),
        dcc.Slider(
            id="num-pages",
            min=5,
            max=1006,
            step=100,
            value=200,
            marks={n: str(n) for n in range(5, 1006, 100)},
            className="mb-5",
        ),
        html.Div(
            id="num-pages-slider", style={"textAlign": "center"}, className="mb-5"
        ),
    ]
)

predict_right = dbc.Col(
    [
        dcc.Markdown(
            """
            ### Tweak More Features
            ---
            """
        ),
        dcc.Markdown("""##### Title Begins with 'The'"""),
        daq.BooleanSwitch(id="the-title", on=False, className="mb-5"),
        dcc.Markdown("""##### Has Subtitle"""),
        daq.BooleanSwitch(id="has-subtitle", on=False, className="mb-5"),
        dcc.Markdown("""##### Part of Series"""),
        daq.BooleanSwitch(id="in-series", on=False, className="mb-5"),
        # # TODO: Take input of title and use that to get has_subtitle, title_char_length, the_title
        dcc.Markdown("""##### **Number of Characters in the Title**"""),
        dcc.Slider(
            id="title-char-count",
            min=2,
            max=252,
            step=25,
            value=50,
            updatemode="drag",
            marks={n: str(n) for n in range(2, 253, 25)},
            className="mb-5",
        ),
        html.Div(
            id="title-char-count-slider",
            style={"textAlign": "center"},
            className="mb-5",
        ),
        dcc.Markdown("""##### **Publish Year**"""),
        dcc.Slider(
            id="publish-year",
            min=1900,
            max=2020,
            step=20,
            value=2000,
            updatemode="drag",
            marks={n: str(n) for n in range(1900, 2021, 20)},
            className="mb-5",
        ),
        html.Div(
            id="publish-year-slider", style={"textAlign": "center"}, className="mb-5"
        ),
    ]
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

intro_column_1 = dbc.Col(introduction1, width=True)
intro_col_photo = dbc.Col(intro_photo, width=True)
intro_column_2 = dbc.Col(introduction2, width=True)
intro_row = dbc.Row([intro_header, intro_column_1, intro_col_photo, intro_column_2])

predict_header_row = dbc.Container(dbc.Row(dbc.Col(predict_header)))
predict_column_1 = dbc.Col(predict_left, width=6)
# predict_column_2 = dbc.Col(predict_middle, width=4)
predict_column_3 = dbc.Col(predict_right, width=6)
predict_row = dbc.Row([predict_column_1, predict_column_3])

# results_header_row = dbc.Container(dbc.Row(dbc.Col(results_header, width=True)))
# results_column_1 = dbc.Col(results_left, width=True)
# results_column_2 = dbc.Col(results_right, width=True)
# results_block_1_row = dbc.Row(dbc.Col(results_block_1))
# results_block_2_row = dbc.Row(dbc.Col(results_block_2))
# results_row = dbc.Row([results_column_1, results_column_2])

# process_header_row = dbc.Container(dbc.Row(dbc.Col(process_header, width=True)))
# process_column_1 = dbc.Col(process_left, width=True)
# process_column_2 = dbc.Col(process_right, width=True)
# process_block_1_row = dbc.Row(dbc.Col(process_block_1))
# # process_shap_row = dbc.Row(process_shap)
# process_block_2_row = dbc.Row(dbc.Col(process_block_2))
# process_row = dbc.Row([process_column_1, process_column_2])

layout = dbc.Container(
    [
        main_header,
        intro_row,
        line_row,
        predict_header_row,
        predict_row,
        # results_header_row,
        # results_block_1_row,
        # results_row,
        # results_block_2_row,
        # process_header_row,
        # process_block_1_row,
        # process_row,
        # process_shap_row,
        # process_block_2_row,
    ],
    fluid=True,
)

# ====== Callbacks ====== #


@app.callback(Output("avg-rating-slider", "children"), [Input("avg-rating", "value")])
def avg_rating_output(x):
    return f"Average Rating: {x}"


@app.callback(Output("num-ratings-slider", "children"), [Input("num-ratings", "value")])
def num_ratings_output(x):
    return f"# Ratings: {x}"


@app.callback(Output("num-pages-slider", "children"), [Input("num-pages", "value")])
def num_pages_output(x):
    return f"# Pages: {x}"


@app.callback(
    Output("title-char-count-slider", "children"), [Input("title-char-count", "value")]
)
def title_char_count_output(x):
    return f"# Characters in Book Title: {x}"


@app.callback(
    Output("publish-year-slider", "children"), [Input("publish-year", "value")]
)
def publish_year_output(x):
    return f"Year Published: {x}"


@app.callback(
    Output("nonfiction-pred", "children"),
    [
        Input("avg-rating", "value"),
        Input("num-ratings", "value"),
        Input("num-pages", "value"),
        Input("title-char-count", "value"),
        Input("publish-year", "value"),
        Input("the-title", "value"),
        Input("has-subtitle", "value"),
        Input("in-series", "value"),
    ],
)
def predict(
    avg_rating,
    num_ratings,
    num_pages,
    title_char_count,
    publish_year,
    the_title,
    has_subtitle,
    in_series,
):
    df = pd.DataFrame(
        columns=[
            "avg_rating",
            "num_ratings",
            "num_pages",
            "title_char_count",
            "publish_year",
            "the_title",
            "has_subtitle",
            "in_series",
        ],
        data=[
            [
                avg_rating,
                num_ratings,
                num_pages,
                title_char_count,
                publish_year,
                the_title,
                has_subtitle,
                in_series,
            ]
        ],
    )
    y_pred = pipeline.predict(df)[0]
    return "Nonfiction" if y_pred == 0 else "Fiction"

