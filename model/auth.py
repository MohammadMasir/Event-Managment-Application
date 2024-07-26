# google_sign_in.py

import webbrowser
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import threading
import pymysql as pmql
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import secrets

# Define your OAuth 2.0 credentials
CLIENT_ID = '907112475964-hrf09450qh8p7bjh4j9ppfvd5th0e01q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8001/callback'
SCOPE = ['https://www.googleapis.com/auth/userinfo.email','https://www.googleapis.com/auth/userinfo.profile', 'openid']

# Set up the MySQL database connection
def get_db_connection():
    return pmql.connect(
        host="localhost",
        user="root",
        password="root",
        database="demo",
        port=3306,
        charset="utf8"
    )

u_id = None
def set_id(user):
    u_id = user
    return u_id

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
                    user_info = session.get('https://www.googleapis.com/oauth2/v2/userinfo').json()
                    email = user_info['email']
                    first_name = user_info.get('given_name', '')
                    last_name = user_info.get('family_name', '')
                    print(first_name, last_name)

                    # Generate a random password for the user
                    password = secrets.token_urlsafe(16)

                    # Store user info in the database
                    conn = get_db_connection()
                    try:
                        with conn.cursor() as c:
                            # Check if user already exists
                            # c.execute("SELECT * FROM user WHERE email = %s", (email,))
                            # existing_user = c.fetchone()
                            
                            # if existing_user:
                            #     # Update existing user
                            #     c.execute("UPDATE user SET first_name = %s, last_name = %s WHERE email = %s", 
                            #               (first_name, last_name, email))
                            # else:
                            #     # Insert new user
                            c.execute("INSERT INTO user (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)", 
                                          (email, password, first_name, last_name))
                            c.execute("SELECT user_id FROM user WHERE email = %s", (email,))
                            user_id = c.fetchone()
                            set_id(user_id)
                            conn.commit()
                    finally:
                        conn.close()

                    
                    # Store or use credentials as needed
                    print("Email:", email)
                    print("Access token:", credentials.token)
                    print("Refresh token:", credentials.refresh_token)
                    print("Expires at:", credentials.expiry)

                except Exception as e:
                    print(f"Error: {e}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>You can close this window now.</h1></body></html>")
            return 

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
        query = "SELECT user_id FROM user where email=%s and password=%s"
        self.cursor.execute(query, (email, password))
        user_id_value = self.cursor.fetchone()
        if user_id_value == None:
            return False
        else:
            self.user_id = user_id_value[0]
            if user_id_value:
                print("user_id in authenticate :", self.user_id)
                return self.user_id
            else:
                return False

# Usage
if __name__ == "__main__":
    app = GoogleSignInApp()
    app.handle_google_sign_in()