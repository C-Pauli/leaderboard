from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset (use the correct path to your CSV)
data_path = './data/dataset.csv'
df = pd.read_csv(data_path)

# Home route serving the HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to fetch data for the table
@app.route('/get_data', methods=['GET'])
def get_data():
    return df.to_json(orient='records')

# Chatbot endpoint to handle queries and generate graphs
@app.route('/chatbot', methods=['POST'])
def chatbot():
    query = request.json.get('query')
    response = handle_query(query)
    return jsonify(response)

def handle_query(query):
    # Suggested responses to guide users on the available features
    if query.lower() in ['help', 'what can you do', 'how do i use this']:
        return {"message": "You can ask me questions like:\n- Show samples that have 'yeti' in their name\n- Display a bar chart of Psilocin and Psilocybin\n- Show me a heatmap of the data\n- Generate a stacked bar chart\nFeel free to explore the data!"}
    
    # Generate charts based on user input
    if 'bar chart' in query.lower():
        return generate_chart_response(df, 'bar')
    elif 'heatmap' in query.lower():
        return generate_chart_response(df, 'heatmap')
    elif 'stacked bar chart' in query.lower():
        return generate_chart_response(df, 'stackedBar')
    
    # Filter samples based on user input
    elif 'show' in query.lower() and 'samples' in query.lower():
        return filter_samples_response(query)
    
    else:
        return {"message": "I can help you generate charts or filter samples! Try asking for a bar chart, heatmap, or stacked bar chart."}

# Function to generate charts
def generate_chart_response(df, chart_type):
    labels = df['Sample Name'].tolist()
    psilocin = df['Psilocin (mg/g)'].tolist()
    psilocybin = df['Psilocybin (mg/g)'].tolist()

    chart_data = {
        'type': chart_type,
        'labels': labels,
        'datasets': [
            {
                'label': 'Psilocin (mg/g)',
                'data': psilocin,
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Psilocybin (mg/g)',
                'data': psilocybin,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }
        ],
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
    }
    return {"message": "Here is your chart.", "chartData": chart_data}

# Function to filter samples based on keyword in the sample name
def filter_samples_response(query):
    keyword = query.split('show samples that have ')[1].strip().replace('"', '')
    matching_samples = df[df['Sample Name'].str.contains(keyword, case=False)]
    if matching_samples.empty:
        return {"message": f"No samples found for '{keyword}'."}
    else:
        return {"message": f"Showing samples with '{keyword}'", "filter": keyword}

if __name__ == '__main__':
    app.run(debug=True)

