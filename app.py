from flask import Flask, render_template, request
from msal import ConfidentialClientApplication

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-token', methods=['POST'])
def api():
    # Get the token for provided backend
    if request.method == 'POST':
        client_id = request.form['client_id']
        tenant_id = request.form['tenant_id']
        backend_guid = request.form['backend_guid']

        application = ConfidentialClientApplication( 
            client_id = client_id,
            authority = "https://login.microsoftonline.com/" + tenant_id
            )
        
        # Get the token for the backend
        result = application.acquire_token_for_client(scopes=[backend_guid + "/.default"])

        return render_template('result.html', token=result)