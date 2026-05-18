from firebase_config import db

Courses = {
    'Monday': [
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'ENT 211',
            'location': 'LH',
            'program': {'Software Engineering', 'Computer Science', 'Microbiology', 'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'MCB 201',
            'location': 'LH',
            'program': {'Microbiology', 'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'ASE-CSC 203',
            'location': 'LH',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'ASE-PED 221',
            'location': 'LR 4',
            'program': {'Public Health'}
        }
    ],

    'Tuesday': [
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'ASE-GST 213',
            'location': 'LH',
            'program': {'Software Engineering', 'Computer Science', 'Microbiology', 'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'ASE-SEN 203',
            'location': 'LR 3',
            'program': {'Software Engineering'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'CHM 207',
            'location': 'LAB 1',
            'program': {'Microbiology'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'ANA 203',
            'location': 'LR 5',
            'program': {'Medical Laboratory Science'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'PHS 203',
            'location': 'LR 6',
            'program': {'Public Health'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'ASE-CSC 201',
            'location': 'LR 3',
            'program': {'Computer Science'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'MCB 231',
            'location': 'LAB 2',
            'program': {'Microbiology'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'MLS 201',
            'location': 'LAB 3',
            'program': {'Medical Laboratory Science'}
        }
    ],

    'Wednesday': [
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'CSC 203',
            'location': 'LR 5',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'BCH 201',
            'location': 'LAB 2',
            'program': {'Microbiology', 'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'COS 201',
            'location': 'LR 3',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'BCH 203',
            'location': 'LAB 2',
            'program': {'Microbiology', 'Medical Laboratory Science'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'STA 201',
            'location': 'LH',
            'program': {'Microbiology', 'Medical Laboratory Science'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'ASE-NCS 207',
            'location': 'LR 4',
            'program': {'Public Health'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'MTH 201',
            'location': 'LR 2',
            'program': {'Software Engineering', 'Computer Science'}
        }
    ],

    'Thursday': [
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'IFT 211',
            'location': 'LR 3',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'CHM 211',
            'location': 'LAB 2',
            'program': {'Microbiology'}
        },
        {
            'time': '9:00 AM - 11:00 AM',
            'course': 'PIO 201',
            'location': 'LR 5',
            'program': {'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'MTH 205',
            'location': 'LR 1',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'ASE-MCB 203',
            'location': 'LAB 1',
            'program': {'Microbiology'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'PIO 203',
            'location': 'LR 4',
            'program': {'Medical Laboratory Science'}
        },
        {
            'time': '11:00 AM - 1:00 PM',
            'course': 'PHS 201',
            'location': 'LR 5',
            'program': {'Public Health'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'SEN 201',
            'location': 'LR 3',
            'program': {'Software Engineering', 'Computer Science'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'ANA 201',
            'location': 'LR 5',
            'program': {'Medical Laboratory Science', 'Public Health'}
        },
        {
            'time': '2:00 PM - 4:00 PM',
            'course': 'CHM 213',
            'location': 'LAB 2',
            'program': {'Microbiology'}
        }
    ],
    'Friday': [],
    'Saturday': [],
    'Sunday': []
}

# Store as STRING (important)
db.child("Courses").set(str(Courses))

print("✔ Courses successfully added to database")
