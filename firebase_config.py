import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyDe7GodG9CY9DGNhbep7c2stRBe7dxwoFE",
    "authDomain": "student-portal-1-5d411.firebaseapp.com",
    "projectId": "student-portal-1-5d411",
    "storageBucket": "student-portal-1-5d411.firebasestorage.app",
    "messagingSenderId": "144766130008",
    "appId": "1:144766130008:web:dbe3d649ad4ef23b0d772d",
    "databaseURL": "https://student-portal-1-5d411-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
