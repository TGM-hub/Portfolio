import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import mysql.connector
from config import create_connection
from dash.exceptions import PreventUpdate

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "Nutrition Tracker"

# Database connection function
def fetch_data(query, params=None):
    conn = create_connection()
    data = None
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
    return pd.DataFrame(data) if data else pd.DataFrame()

# Layout for authentication section
auth_section = dbc.Card([
    html.H4("User Login", className="card-title"),
    dbc.Input(id="username", placeholder="Enter username", type="text"),
    dbc.Input(id="password", placeholder="Enter password", type="password"),
    dbc.Button("Login", id="login-button", color="primary", className="mt-2"),
    html.Div(id="login-message", className="mt-2")
], body=True)

# Goal setting section layout
goal_section = dbc.Card([
    html.H4("Set Daily Goals", className="card-title"),
    dbc.InputGroup([
        dbc.Input(id="calories_goal", placeholder="Calories (kcal)", type="number"),
        dbc.Input(id="protein_goal", placeholder="Protéines (g)", type="number"),
        dbc.Input(id="fat_goal", placeholder="Lipides (g)", type="number"),
        dbc.Input(id="carbs_goal", placeholder="Glucides (g)", type="number")
    ], className="mb-3"),
    dbc.InputGroup([
        dbc.Input(id="vitamin_a_goal", placeholder="Vitamine A (%)", type="number"),
        dbc.Input(id="vitamin_b1_goal", placeholder="Vitamine B1 (%)", type="number"),
        dbc.Input(id="vitamin_b2_goal", placeholder="Vitamine B2 (%)", type="number"),
        dbc.Input(id="vitamin_b3_goal", placeholder="Vitamine B3 (%)", type="number"),
        dbc.Input(id="vitamin_b5_goal", placeholder="Vitamine B5 (%)", type="number"),
        dbc.Input(id="vitamin_b6_goal", placeholder="Vitamine B6 (%)", type="number"),
        dbc.Input(id="vitamin_b9_goal", placeholder="Vitamine B9 (%)", type="number"),
        dbc.Input(id="vitamin_b12_goal", placeholder="Vitamine B12 (%)", type="number"),
        dbc.Input(id="vitamin_c_goal", placeholder="Vitamine C (%)", type="number"),
        dbc.Input(id="vitamin_d_goal", placeholder="Vitamine D (%)", type="number"),
        dbc.Input(id="vitamin_e_goal", placeholder="Vitamine E (%)", type="number"),
        dbc.Input(id="vitamin_k_goal", placeholder="Vitamine K (%)", type="number"),
        dbc.Input(id="betaine_goal", placeholder="Betaine (%)", type="number"),
        dbc.Input(id="choline_goal", placeholder="Choline (%)", type="number"),
        dbc.Input(id="calcium_goal", placeholder="Calcium (%)", type="number"),
        dbc.Input(id="copper_goal", placeholder="Copper (%)", type="number"),
        dbc.Input(id="iron_goal", placeholder="Fer (mg)", type="number"),
        dbc.Input(id="magnesium_goal", placeholder="Magnésium (%)", type="number"),
        dbc.Input(id="manganese_goal", placeholder="Manganèse (%)", type="number"),
        dbc.Input(id="phosphorus_goal", placeholder="Phosphore (%)", type="number"),
        dbc.Input(id="potassium_goal", placeholder="Potassium (%)", type="number"),
        dbc.Input(id="selenium_goal", placeholder="Selenium (%)", type="number"),
        dbc.Input(id="sodium_goal", placeholder="Sodium (%)", type="number"),
        dbc.Input(id="zinc_goal", placeholder="Zinc (%)", type="number"),
    ], className="mb-3"),
    dbc.Button("Save Goals", id="save-goals-button", color="success"),
    html.Div(id="save-goals-message", className="mt-2")
], body=True)

# Food selection by category section layout
food_selection_section = dbc.Card([
    html.H4("Log Food Intake", className="card-title"),
    dcc.Dropdown(
        id="food-category-dropdown",
        options=[
            {'label': 'Protéine', 'value': 'protéine'},
            {'label': 'Glucide', 'value': 'glucide'},
            {'label': 'Lipide', 'value': 'lipide'},
            {'label': 'Légume', 'value': 'légume'},
        ],
        placeholder="Select Food Category"
    ),
    dcc.Dropdown(id="food-dropdown", placeholder="Select Food Item"),
    dbc.Input(id="food-quantity", placeholder="Quantity (g)", type="number"),
    dbc.Button("Add Food", id="add-food-button", color="info", className="mt-2"),
    html.Div(id="food-log-message", className="mt-2")
], body=True)

# Placeholder layout before login
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(auth_section, width=6, className="offset-3", id="auth-section"),
    ], className="mt-5"),
    html.Div(id="main-content", style={"display": "none"}),  # Main content hidden initially

    # Hidden placeholders to satisfy callback requirements
    dbc.Button(id="add-food-button", style={"display": "none"}),
    dcc.Dropdown(id="food-category-dropdown", style={"display": "none"}),
    dcc.Dropdown(id="food-dropdown", style={"display": "none"}),
    dbc.Button(id="save-goals-button", style={"display": "none"}),
    dbc.Input(id="food-quantity", style={"display": "none"}),  # Missing input for quantity in food logging
    dbc.Input(id="calories_goal", style={"display": "none"}),  # Additional goal inputs
    dbc.Input(id="protein_goal", style={"display": "none"}),
    dbc.Input(id="fat_goal", style={"display": "none"}),
    dbc.Input(id="carbs_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_a_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b1_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b2_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b3_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b5_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b6_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b7_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b9_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_b12_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_c_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_d_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_e_goal", style={"display": "none"}),
    dbc.Input(id="vitamin_k_goal", style={"display": "none"}),
    dbc.Input(id="betaine_goal", style={"display": "none"}),
    dbc.Input(id="choline_goal", style={"display": "none"}),
    dbc.Input(id="calcium_goal", style={"display": "none"}),
    dbc.Input(id="copper_goal", style={"display": "none"}),
    dbc.Input(id="iron_goal", style={"display": "none"}),
    dbc.Input(id="magnesium_goal", style={"display": "none"}),
    dbc.Input(id="manganese_goal", style={"display": "none"}),
    dbc.Input(id="phosphorus_goal", style={"display": "none"}),
    dbc.Input(id="potassium_goal", style={"display": "none"}),
    dbc.Input(id="selenium_goal", style={"display": "none"}),
    dbc.Input(id="sodium_goal", style={"display": "none"}),
    dbc.Input(id="zinc_goal", style={"display": "none"}),   
    html.Div(id="food-log-message", style={"display": "none"}),
    html.Div(id="save-goals-message", style={"display": "none"}),
])

# Callback to handle user login and dynamically load main content
@app.callback(
    [Output("login-message", "children"),
     Output("main-content", "children"),
     Output("main-content", "style"),
     Output("auth-section", "style")],
    [Input("login-button", "n_clicks")],
    [State("username", "value"), State("password", "value")]
)
def authenticate_user(n_clicks, username, password):
    if n_clicks:
        query = "SELECT * FROM user WHERE username = %s AND password_hash = %s"
        user = fetch_data(query, (username, password))
        if not user.empty:
            user_id = user.iloc[0]['user_id']  # Assuming 'user_id' is primary key for Users table
            main_content_layout = dbc.Row([
                dbc.Col(goal_section, width=6),
                dbc.Col(food_selection_section, width=6)
            ])
            return "Login successful!", main_content_layout, {"display": "block"}, {"display": "none"}
        return "Invalid username or password.", dash.no_update, {"display": "none"}, {"display": "block"}
    raise PreventUpdate

# Callback to save user goals
@app.callback(
    Output("save-goals-message", "children"),
    [Input("save-goals-button", "n_clicks")],
    [State("calories_goal", "value"), State("protein_goal", "value"), State("fat_goal", "value"),
     State("carbs_goal", "value"), State("vitamin_a_goal", "value"), State("vitamin_b1_goal", "value"),
     State("vitamin_b2_goal", "value"), State("vitamin_b3_goal", "value"), State("vitamin_b5_goal", "value"),
     State("vitamin_b6_goal", "value"), State("vitamin_b9_goal", "value"), State("vitamin_b12_goal", "value"),
     State("vitamin_c_goal", "value"), State("vitamin_d_goal", "value"), State("vitamin_e_goal", "value"),
     State("vitamin_k_goal", "value"), State("betaine_goal", "value"), State("choline_goal", "value"),
     State("calcium_goal", "value"), State("copper_goal", "value"), State("iron_goal", "value"),
     State("magnesium_goal", "value"), State("manganese_goal", "value"), State("phosphorus_goal", "value"),
     State("potassium_goal", "value"), State("selenium_goal", "value"), State("sodium_goal", "value"), State("zinc_goal", "value"),
     State("username", "value")]  # Retrieve username to identify user
)
def save_user_goals(n_clicks, calories, protein, fat, carbs, vitamin_a, vitamin_b1, vitamin_b2, vitamin_b3,
                    vitamin_b5, vitamin_b6, vitamin_b9, vitamin_b12, vitamin_c, vitamin_d, vitamin_e,
                    vitamin_k, betaine, choline, calcium, copper, iron, magnesium, manganese, phosphorus,
                    potassium, selenium, sodium, zinc, username):
    if n_clicks:
        # Fetch user ID based on the username
        query = "SELECT id FROM user WHERE username = %s"
        user_id = fetch_data(query, (username,)).iloc[0]['id']
        
        # Insert or update user goals in the database
        query = """
        INSERT INTO Goals (user_id, calories, protein, fat, carbs, vitamin_a, vitamin_b1, vitamin_b2, vitamin_b3,
                           vitamin_b5, vitamin_b6, vitamin_b9, vitamin_b12, vitamin_c, vitamin_d, vitamin_e,
                           vitamin_k, betaine, choline, calcium, copper, iron, magnesium, manganese, phosphorus,
                           potassium, selenium, sodium, zinc)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            calories=%s, protein=%s, fat=%s, carbs=%s, vitamin_a=%s, vitamin_b1=%s, vitamin_b2=%s, vitamin_b3=%s,
            vitamin_b5=%s, vitamin_b6=%s, vitamin_b9=%s, vitamin_b12=%s, vitamin_c=%s, vitamin_d=%s, vitamin_e=%s,
            vitamin_k=%s, betaine=%s, choline=%s, calcium=%s, copper=%s, iron=%s, magnesium=%s, manganese=%s,
            phosphorus=%s, potassium=%s, selenium=%s, sodium=%s, zinc=%s
        """
        
        # Prepare parameters for the query
        params = (user_id, calories, protein, fat, carbs, vitamin_a, vitamin_b1, vitamin_b2, vitamin_b3,
                  vitamin_b5, vitamin_b6, vitamin_b9, vitamin_b12, vitamin_c, vitamin_d, vitamin_e,
                  vitamin_k, betaine, choline, calcium, copper, iron, magnesium, manganese, phosphorus,
                  potassium, selenium, sodium, zinc,
                  calories, protein, fat, carbs, vitamin_a, vitamin_b1, vitamin_b2, vitamin_b3,
                  vitamin_b5, vitamin_b6, vitamin_b9, vitamin_b12, vitamin_c, vitamin_d, vitamin_e,
                  vitamin_k, betaine, choline, calcium, copper, iron, magnesium, manganese, phosphorus,
                  potassium, selenium, sodium, zinc)
        
        # Execute the query to save data
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
        
        return "Goals saved successfully!"
    raise PreventUpdate

# Callback for food category selection
@app.callback(
    Output("food-dropdown", "options"),
    [Input("food-category-dropdown", "value")]
)
def update_food_dropdown(selected_category):
    if selected_category:
        query = "SELECT id, name FROM Food_Items WHERE category = %s"
        food_items = fetch_data(query, (selected_category,))
        return [{'label': item['name'], 'value': item['id']} for index, item in food_items.iterrows()]
    return []

# Callback to log food intake
@app.callback(
    Output("food-log-message", "children"),
    [Input("add-food-button", "n_clicks")],
    [State("food-dropdown", "value"), State("food-quantity", "value"),
     State("username", "value")]  # Retrieve username to identify user
)
def log_food_intake(n_clicks, food_item_id, quantity, username):
    if n_clicks and food_item_id and quantity:
        query = "SELECT id FROM user WHERE username = %s"
        user_id = fetch_data(query, (username,)).iloc[0]['id']
        
        # Add food log to the database
        query = "INSERT INTO Daily_Entries (user_id, food_item_id, date, quantity) VALUES (%s, %s, CURDATE(), %s)"
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (user_id, food_item_id, quantity))
        conn.commit()
        cursor.close()
        conn.close()
        return "Food item logged successfully!"
    raise PreventUpdate

if __name__ == "__main__":
    app.run_server(debug=True)