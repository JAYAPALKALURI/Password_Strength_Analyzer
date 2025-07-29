
from zxcvbn import zxcvbn


def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']
    suggestions = result['feedback']['suggestions']
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    return {
        'password': password,
        'score': score,
        'suggestions': suggestions,
        'crack_time': crack_time
    }
