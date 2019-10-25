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
df = pd.read_csv("assets/must_read_books_subset.csv")

# Load in scikit-learn RandomForest pipeline
pipeline = load("assets/rf_pipe2.joblib")
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
> What separates fact from fiction?  

As is the case with many things nowadays, more data brings more answers to questions like this one. 
If not the actual answers, data can at least provide a lens through which these kinds of questions can be explored.

This project is dedicated to exploring that question as it relates to the printed page - how are our real 
stories different from our fictional ones?

I am an avid consumer of science-fiction, much of it in book form. Exploring fictional universes and 
following the storylines that wind through them play very significant roles in my 
daily inspiration and keep me full of wonder, even in the real world.

For this project, I was curious how much valuable insight I could gather from books from a quantitative perspective, 
as I am usually viewing them from the perspective of being sucked into and being fully immersed by the stories.

It is difficult to encapsulate and measure much the information that is found within the books by 
the simple means I had available to me while working on this project. However, there are still plenty of 
interesting avenues to peruse, and I hope you have fun doing so!

Go ahead and tweak the parameters a bit and watch the resulting predictions. 
See if you can notice any significant separating factors between nonfiction and fiction books; 
any patterns that the model may have picked up on.

I go into more detail about the model, the data, and the process later on. But to give a one-sentence overview, 
the model I trained for this project is a decision-tree-based machine learning model called a Random Forest Classifier.

Thanks to the wonders of the Cloud, this trained model evaluates the parameters in real time, 
providing its best guess at whether those parameters indicate "nonfiction" or "fiction".
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
            ## Tweak the Features
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
        html.Div(id="avg-rating-slider", style={"textAlign": "center"}, className="mb-5"),
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
        html.Div(id="num-ratings-slider", style={"textAlign": "center"}, className="mb-5"),
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
        html.Div(id="num-pages-slider", style={"textAlign": "center"}, className="mb-5"),
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
        html.Div(id="title-char-count-slider", style={"textAlign": "center"}, className="mb-5"),
        dcc.Markdown("""##### **Publish Year**"""),
        dcc.Slider(
            id="publish-year",
            min=1900,
            max=2020,
            step=20,
            value=20,
            updatemode="drag",
            marks={n: str(n) for n in range(1900, 2021, 20)},
            className="mb-5",
        ),
        html.Div(id="publish-year-slider", style={"textAlign": "center"}, className="mb-5"),
    ]
)

predict_middle = dbc.Col(
    [
        dcc.Markdown("""##### Title Begins with 'The'"""),
        daq.BooleanSwitch(id="the-title", on=False, className="mb-5"),
        dcc.Markdown("""##### Has Subtitle"""),
        daq.BooleanSwitch(id="has-subtitle", on=False, className="mb-5"),
        dcc.Markdown("""##### Part of Series"""),
        daq.BooleanSwitch(id="in-series", on=False, className="mb-5"),
        # # TODO: Take input of title and use that to get has_subtitle, title_char_length, the_title
    ]
)

predict_right = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Prediction
            ---
            """
        ),
        dbc.Container(html.Div(html.H3(["print(", html.Span(id="nonfiction-pred"), ")"]))),
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
## Data

Much of the up-front work on this project was spent on what I've been calling 
"target practice"—finding a target that is interesting to predict and is actually predictable. 
This is much more difficult than one would think, particularly with the range of data available 
nowadays, which vary wildly in quality and topic.
"""
    )
)

results_left = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src="num_ratings_outliers.png"), href="#", className="image"
            ),
            html.Div(
                [
                    html.H3("Outliers, Part 1"),
                    html.P(
                        "This data had some very significant outliers that made visualizing relatioships difficult."
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
                html.Img(src="num_reviews_outliers.png"), href="#", className="image"
            ),
            html.Div(
                [
                    html.H3("Outliers, Part 2"),
                    html.P(
                        "Filtering out the outliers reduced the size of the dataset by less than 1,000 rows—definitely worth it for the benefit."
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
Gathering and fully utilizing deep data on textual content such as books is difficult and 
requires either a lot of time or a lot of computing power. 
The scope of this project did not extend that far, so I had to get creative with what I had.

For some reason, predicting average ratings wasn't particularly interesting to me. 
After a few false starts I stumbled onto the idea of trying to predict whether a book is 
fictional or not, and things fell into place after that.

I engineered a bunch of features in quick succession, most of which I kept after analyzing 
their permutation importance. 
"""
    )
)

results_footer = (
    html.Footer(
        html.Img(src="scatterplot_matrix_no_outliers.png"),
        className="major container medium",
    ),
)


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
For some reason, predicting average ratings wasn't particularly interesting to me. 
After a few false starts I stumbled onto the idea of trying to predict whether a 
book is fictional or not, and things fell into place after that.
"""
    )
)

process_left = dbc.Container(
    html.Section(
        [
            html.A(
                html.Img(src="perm_import_light.png"),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("Permutation Importance"),
                    html.P(
                        "I engineered a bunch of features in quick succession, most of which I kept after analyzing their permutation importance."
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
                html.Img(src="num_pages_outliers.png"),
                href="#",
                className="image icon solid fa-signal",
            ),
            html.Div(
                [
                    html.H3("More Outliers"),
                    html.P(
                        "Some books had tens of thousands of pages, rendering most visualizations useless.."
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
### Choice of model and metrics

Predicting whether books are fiction or not is a binary classification problem. 
For classiciation, the actual value is either True or False, there is no in between. 
Therefore, optimizing predictive models is very different for classification as compared to 
linear regression which aim at a continuous target.

Logistic regression is not as complex as some of the other classification models, 
yet can usually provide a robust baseline on which to iterate. In my case, an accuracy score of ~65%.

To go beyond the baseline, I chose to use a gradient boosting classifier. 
Due to some dependency issues at the very end, I ended up having to go back 
and re-train a Random Forest Classifier.
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
predict_column_1 = dbc.Col(predict_left, width=5)
predict_column_2 = dbc.Col(predict_middle, width=4)
predict_column_3 = dbc.Col(predict_right, width=3)
predict_row = dbc.Row([predict_column_1, predict_column_2, predict_column_3])

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


@app.callback(Output("title-char-count-slider", "children"), [Input("title-char-count", "value")])
def title_char_count_output(x):
    return f"# Characters in Book Title: {x}"


@app.callback(Output("publish-year-slider", "children"), [Input("publish-year", "value")])
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

