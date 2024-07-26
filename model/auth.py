# google_sign_in.py

import webbrowser
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import threading
import pymysql as pmql
from google_auth_oauthlib.flow import InstalledAppFlow
import requests

# Define your OAuth 2.0 credentials
CLIENT_ID = '907112475964-hrf09450qh8p7bjh4j9ppfvd5th0e01q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8001/callback'
SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'openid']

# Set up the MySQL database connection
def get_db_connection():
    return pmql.connect(
        host="localhost",
        user="root",
        password="root",
        database="event_manager",
        port=3306,
        charset="utf8"
    )

class GoogleSignInApp:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()
        self.start_server()

    def handle_google_sign_in(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            "model\client_secret.json", scopes=SCOPE, redirect_uri=REDIRECT_URI
        )
        authorization_url, state = flow.authorization_url(
            access_type="offline", prompt="consent"
        )
        return webbrowser.open(authorization_url)
        
    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        parent_app = None

        def do_GET(self):
            query = urlparse(self.path).query
            query_components = parse_qs(query)
            if "code" in query_components:
                code = query_components["code"][0]
                flow = InstalledAppFlow.from_client_secrets_file(
                    "model\client_secret.json", scopes=SCOPE, redirect_uri=REDIRECT_URI
                )
                try:
                    flow.fetch_token(code=code)
                    credentials = flow.credentials
                    # Get user info
                    session = requests.Session()
                    session.headers.update({'Authorization': f'Bearer {credentials.token}'})
                    
                    # First, try to get email from userinfo endpoint
                    userinfo_response = session.get('https://www.googleapis.com/oauth2/v2/userinfo').json()
                    print("Userinfo response:", userinfo_response)  # Debug print
                    
                    email = userinfo_response.get('email', 'No email found')
                    
                    # Then, try to get name from People API
                    people_response = session.get('https://people.googleapis.com/v1/people/me?personFields=names').json()
                    print("People API response:", people_response)  # Debug print
                    
                    if 'names' in people_response and people_response['names']:
                        first_name = people_response['names'][0].get('givenName', 'No first name found')
                        last_name = people_response['names'][0].get('familyName', 'No last name found')
                    else:
                        first_name = last_name = 'Name not available'

                    # Store user info in the database
                    with self.parent_app.conn.cursor() as c:
                        c.execute("INSERT INTO user (email, first_name, last_name) VALUES (%s, %s, %s)", 
                                (email, first_name, last_name))
                        self.parent_app.conn.commit()

                    # Store or use credentials as needed
                    print("Email:", email)
                    print("First Name:", first_name)
                    print("Last Name:", last_name)
                    print("Access token:", credentials.token)
                    print("Refresh token:", credentials.refresh_token)
                    print("Expires at:", credentials.expiry)
                except Exception as e:
                    print(f"Error: {e}")
                    print(f"Error details: {str(e)}")
                    import traceback
                    traceback.print_exc()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>You can close this window now.</h1></body></html>")

    def start_server(self):
        GoogleSignInApp.CallbackHandler.parent_app = self
        server_address = ("", 8001)
        httpd = socketserver.TCPServer(server_address, GoogleSignInApp.CallbackHandler)
        httpd.allow_reuse_address = True  # Allow reuse of the address
        print("Starting local web server on port 8001...")
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()


class Auth():
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()
        
    def authenticate(self, email, password):
        query = "SELECT user_id FROM admin where username=%s and password=%s"
        self.cursor.execute(query, (email, password))
        user_id_value = self.cursor.fetchone()
        try:
            self.user_id = user_id_value[0]
        except:
            print("Exception is raised")
            return False
        if user_id_value:
            print("user_id in authenticate :", self.user_id)
            return self.user_id
        else:
            return False
        
        