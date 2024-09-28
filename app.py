from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset
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
#@app.route('/chatbot', methods=['POST'])
#def chatbot():
 #   query = request.json.get('query')
  #  response = handle_query(query)
   # return jsonify(response)

def handle_query(query):
    # Suggested responses to guide users on available features
    if query.lower() in ['help', 'what can you do', 'how do i use this']:
        return {"message": "You can ask me questions like:\n- Show samples that have 'yeti' in their name\n- Display a bar chart of specific analytes like Psilocin and Psilocybin\n- Show me a heatmap or stacked bar chart\n- Compare multiple samples.\nFeel free to explore the data!"}
    
    # Generate charts based on user input
    if 'chart' in query.lower():
        return generate_chart_response(df, query)
    
    # Filter samples based on user input
    elif 'show' in query.lower() and 'samples' in query.lower():
        return filter_samples_response(query)
    
    else:
        return {"message": "I can help you generate charts or filter samples! Try asking for a bar chart, heatmap, or stacked bar chart."}

# Function to generate charts dynamically
def generate_chart_response(df, query):
    # Extract the type of chart and the analytes
    if 'bar' in query.lower():
        chart_type = 'bar'
    elif 'heatmap' in query.lower():
        chart_type = 'heatmap'
    elif 'line' in query.lower():
        chart_type = 'line'
    else:
        chart_type = 'bar'  # Default to bar chart
    
    analytes = []
    if 'psilocin' in query.lower():
        analytes.append('Psilocin (mg/g)')
    if 'psilocybin' in query.lower():
        analytes.append('Psilocybin (mg/g)')
    
    # Default analytes if none specified
    if not analytes:
        analytes = ['Psilocin (mg/g)', 'Psilocybin (mg/g)']
    
    labels = df['Sample Name'].tolist()
    datasets = []
    
    for analyte in analytes:
        datasets.append({
            'label': analyte,
            'data': df[analyte].tolist(),
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 1
        })
    
    chart_data = {
        'type': chart_type,
        'labels': labels,
        'datasets': datasets,
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

