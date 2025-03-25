from core.database import DatabaseManager
from datetime import datetime, timedelta

def test_database():
    # Initialize database
    db = DatabaseManager()
    
    # Create a new session
    session_id = db.create_session(notes="Behavioral biometrics test session")
    print(f"Created session with ID: {session_id}")
    
    # Test keystroke dynamics
    db.add_keystroke_data(
        session_id=session_id,
        key_pressed="a",
        key_released="a",
        press_duration=0.15,
        inter_key_interval=0.2
    )
    print("Added keystroke data")
    
    # Test mouse movements
    db.add_mouse_movement(
        session_id=session_id,
        x_position=100,
        y_position=200,
        movement_speed=150.5,
        acceleration=2.3,
        click_type="left"
    )
    print("Added mouse movement data")
    
    # Test behavioral pattern
    db.add_behavioral_pattern(
        session_id=session_id,
        pattern_type="typing_rhythm",
        confidence_score=0.95,
        pattern_data="{'avg_press_duration': 0.15, 'avg_interval': 0.2}"
    )
    print("Added behavioral pattern")
    
    # Test login patterns
    user_id = "test_user"
    db.add_login_pattern(
        user_id=user_id,
        start_hour=8,
        end_hour=18,
        login_days="0,1,2,3,4",  # Monday to Friday
        max_duration=30  # 30 seconds max login time
    )
    print("Added login pattern")
    
    # Test login attempt
    db.add_login_attempt(
        user_id=user_id,
        success=True,
        duration=2.5,
        ip_address="192.168.1.1",
        device_info="Windows 10",
        is_suspicious=False
    )
    print("Added login attempt")
    
    # Test suspicious login detection
    suspicious_time = datetime.now().replace(hour=3)  # 3 AM
    is_suspicious, reason = db.check_login_suspicious(user_id, suspicious_time, 2.5)
    print(f"\nSuspicious login check:")
    print(f"Is suspicious: {is_suspicious}")
    print(f"Reason: {reason}")
    
    # Get session summary
    summary = db.get_session_summary(session_id)
    print("\nSession Summary:")
    print(f"Session Info: {summary['session_info']}")
    print(f"Keystroke Count: {summary['keystroke_count']}")
    print(f"Mouse Movement Count: {summary['mouse_count']}")
    
    # Get full session data
    session_data = db.get_session_data(session_id)
    print("\nFull Session Data:")
    print(f"Session: {session_data['session']}")
    print(f"Keystroke Data: {session_data['keystroke_data']}")
    print(f"Mouse Data: {session_data['mouse_data']}")
    print(f"Behavioral Patterns: {session_data['behavioral_patterns']}")
    
    # Get login history
    login_attempts = db.get_recent_login_attempts(user_id)
    print("\nRecent Login Attempts:")
    for attempt in login_attempts:
        print(f"Attempt: {attempt}")
    
    # End session
    db.end_session(session_id)
    print("\nEnded session")

if __name__ == "__main__":
    test_database() 