import sqlite3
from datetime import datetime
import os
from pathlib import Path

class DatabaseManager:
    def __init__(self):
        # Create data directory if it doesn't exist
        self.data_dir = Path(__file__).parent.parent.parent / 'data'
        self.data_dir.mkdir(exist_ok=True)
        
        # Database file path
        self.db_path = self.data_dir / 'bbiometrics.db'
        
        # Initialize database
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create sessions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_time TIMESTAMP NOT NULL,
                    end_time TIMESTAMP,
                    status TEXT NOT NULL,
                    notes TEXT
                )
            ''')
            
            # Create keystroke_dynamics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS keystroke_dynamics (
                    keystroke_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    key_pressed TEXT NOT NULL,
                    key_released TEXT NOT NULL,
                    press_duration REAL NOT NULL,
                    inter_key_interval REAL,
                    FOREIGN KEY (session_id) REFERENCES sessions (session_id)
                )
            ''')
            
            # Create mouse_movements table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mouse_movements (
                    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    x_position INTEGER NOT NULL,
                    y_position INTEGER NOT NULL,
                    movement_speed REAL,
                    acceleration REAL,
                    click_type TEXT,
                    FOREIGN KEY (session_id) REFERENCES sessions (session_id)
                )
            ''')
            
            # Create behavioral_patterns table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS behavioral_patterns (
                    pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    pattern_type TEXT NOT NULL,
                    confidence_score REAL NOT NULL,
                    pattern_data TEXT NOT NULL,
                    FOREIGN KEY (session_id) REFERENCES sessions (session_id)
                )
            ''')
            
            # Create login_patterns table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS login_patterns (
                    pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    normal_login_start_hour INTEGER NOT NULL,
                    normal_login_end_hour INTEGER NOT NULL,
                    normal_login_days TEXT NOT NULL,  -- Comma-separated days (0-6)
                    max_login_duration INTEGER NOT NULL,  -- in seconds
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            ''')
            
            # Create login_attempts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS login_attempts (
                    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    attempt_time TIMESTAMP NOT NULL,
                    success BOOLEAN NOT NULL,
                    duration REAL NOT NULL,  -- in seconds
                    ip_address TEXT,
                    device_info TEXT,
                    is_suspicious BOOLEAN NOT NULL,
                    reason TEXT
                )
            ''')
            
            conn.commit()
    
    def create_session(self, notes=None):
        """Create a new session and return its ID"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sessions (start_time, status, notes)
                VALUES (?, ?, ?)
            ''', (datetime.now(), 'active', notes))
            conn.commit()
            return cursor.lastrowid
    
    def end_session(self, session_id):
        """End an existing session"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE sessions 
                SET end_time = ?, status = 'completed'
                WHERE session_id = ?
            ''', (datetime.now(), session_id))
            conn.commit()
    
    def add_keystroke_data(self, session_id, key_pressed, key_released, 
                          press_duration, inter_key_interval=None):
        """Add keystroke dynamics data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO keystroke_dynamics (
                    session_id, timestamp, key_pressed, key_released,
                    press_duration, inter_key_interval
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (session_id, datetime.now(), key_pressed, key_released,
                 press_duration, inter_key_interval))
            conn.commit()
    
    def add_mouse_movement(self, session_id, x_position, y_position,
                          movement_speed=None, acceleration=None, click_type=None):
        """Add mouse movement data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO mouse_movements (
                    session_id, timestamp, x_position, y_position,
                    movement_speed, acceleration, click_type
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (session_id, datetime.now(), x_position, y_position,
                 movement_speed, acceleration, click_type))
            conn.commit()
    
    def add_behavioral_pattern(self, session_id, pattern_type, confidence_score, pattern_data):
        """Add analyzed behavioral pattern data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO behavioral_patterns (
                    session_id, timestamp, pattern_type,
                    confidence_score, pattern_data
                ) VALUES (?, ?, ?, ?, ?)
            ''', (session_id, datetime.now(), pattern_type,
                 confidence_score, pattern_data))
            conn.commit()
    
    def add_login_pattern(self, user_id, start_hour, end_hour, login_days, max_duration):
        """Add or update login pattern for a user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            now = datetime.now()
            
            # Check if pattern exists
            cursor.execute('''
                SELECT pattern_id FROM login_patterns 
                WHERE user_id = ?
            ''', (user_id,))
            
            existing = cursor.fetchone()
            
            if existing:
                # Update existing pattern
                cursor.execute('''
                    UPDATE login_patterns 
                    SET normal_login_start_hour = ?,
                        normal_login_end_hour = ?,
                        normal_login_days = ?,
                        max_login_duration = ?,
                        updated_at = ?
                    WHERE user_id = ?
                ''', (start_hour, end_hour, login_days, max_duration, now, user_id))
            else:
                # Create new pattern
                cursor.execute('''
                    INSERT INTO login_patterns (
                        user_id, normal_login_start_hour, normal_login_end_hour,
                        normal_login_days, max_login_duration, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (user_id, start_hour, end_hour, login_days, max_duration, now, now))
            
            conn.commit()
    
    def add_login_attempt(self, user_id, success, duration, ip_address=None, 
                         device_info=None, is_suspicious=False, reason=None):
        """Record a login attempt"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO login_attempts (
                    user_id, attempt_time, success, duration,
                    ip_address, device_info, is_suspicious, reason
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, datetime.now(), success, duration,
                 ip_address, device_info, is_suspicious, reason))
            conn.commit()
    
    def get_session_data(self, session_id):
        """Retrieve all data for a specific session"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get session info
            cursor.execute('SELECT * FROM sessions WHERE session_id = ?', (session_id,))
            session = cursor.fetchone()
            
            # Get keystroke data
            cursor.execute('SELECT * FROM keystroke_dynamics WHERE session_id = ?', (session_id,))
            keystroke_data = cursor.fetchall()
            
            # Get mouse movements
            cursor.execute('SELECT * FROM mouse_movements WHERE session_id = ?', (session_id,))
            mouse_data = cursor.fetchall()
            
            # Get behavioral patterns
            cursor.execute('SELECT * FROM behavioral_patterns WHERE session_id = ?', (session_id,))
            patterns = cursor.fetchall()
            
            return {
                'session': session,
                'keystroke_data': keystroke_data,
                'mouse_data': mouse_data,
                'behavioral_patterns': patterns
            }
    
    def get_active_sessions(self):
        """Get all active sessions"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sessions WHERE status = "active"')
            return cursor.fetchall()
    
    def get_session_summary(self, session_id):
        """Get a summary of the session data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get basic session info
            cursor.execute('''
                SELECT start_time, end_time, status, notes 
                FROM sessions 
                WHERE session_id = ?
            ''', (session_id,))
            session_info = cursor.fetchone()
            
            # Get keystroke count
            cursor.execute('''
                SELECT COUNT(*) 
                FROM keystroke_dynamics 
                WHERE session_id = ?
            ''', (session_id,))
            keystroke_count = cursor.fetchone()[0]
            
            # Get mouse movement count
            cursor.execute('''
                SELECT COUNT(*) 
                FROM mouse_movements 
                WHERE session_id = ?
            ''', (session_id,))
            mouse_count = cursor.fetchone()[0]
            
            return {
                'session_info': session_info,
                'keystroke_count': keystroke_count,
                'mouse_count': mouse_count
            }
    
    def get_keystroke_data(self, session_id):
        """Retrieve keystroke dynamics data for a session"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM keystroke_dynamics 
                WHERE session_id = ?
                ORDER BY timestamp
            ''', (session_id,))
            return cursor.fetchall()
    
    def get_mouse_movements(self, session_id):
        """Retrieve mouse movement data for a session"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM mouse_movements 
                WHERE session_id = ?
                ORDER BY timestamp
            ''', (session_id,))
            return cursor.fetchall()
    
    def get_behavioral_patterns(self, session_id):
        """Retrieve behavioral patterns for a session"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM behavioral_patterns 
                WHERE session_id = ?
                ORDER BY timestamp
            ''', (session_id,))
            return cursor.fetchall()
    
    def get_login_pattern(self, user_id):
        """Get login pattern for a user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM login_patterns 
                WHERE user_id = ?
            ''', (user_id,))
            return cursor.fetchone()
    
    def get_recent_login_attempts(self, user_id, limit=10):
        """Get recent login attempts for a user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM login_attempts 
                WHERE user_id = ?
                ORDER BY attempt_time DESC
                LIMIT ?
            ''', (user_id, limit))
            return cursor.fetchall()
    
    def check_login_suspicious(self, user_id, login_time, duration):
        """Check if a login attempt is suspicious based on patterns"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get user's login pattern
            cursor.execute('''
                SELECT * FROM login_patterns 
                WHERE user_id = ?
            ''', (user_id,))
            pattern = cursor.fetchone()
            
            if not pattern:
                return True, "No login pattern established"
            
            # Check if login time is within normal hours
            login_hour = login_time.hour
            if not (pattern[2] <= login_hour <= pattern[3]):
                return True, "Login outside normal hours"
            
            # Check if login day is allowed
            login_day = str(login_time.weekday())
            if login_day not in pattern[4].split(','):
                return True, "Login on non-allowed day"
            
            # Check if duration exceeds maximum
            if duration > pattern[5]:
                return True, "Login duration exceeds maximum"
            
            return False, None 