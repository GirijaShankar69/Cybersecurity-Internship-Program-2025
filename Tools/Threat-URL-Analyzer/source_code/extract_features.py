import re
from urllib.parse import urlparse, parse_qs

def extract_url_features(url):
    parsed = urlparse(url)
    features = {}

    features['url_length'] = len(url)
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['has_at'] = 1 if '@' in url else 0
    features['has_hyphen'] = 1 if '-' in parsed.netloc else 0
    features['num_subdomains'] = parsed.netloc.count('.') - 1
    features['uses_https'] = 1 if parsed.scheme == 'https' else 0
    features['num_query_params'] = len(parse_qs(parsed.query))
    features['path_length'] = len(parsed.path)
    features['domain_length'] = len(parsed.netloc)
    features['num_digits'] = len(re.findall(r'\d', url))
    features['has_encoded_chars'] = 1 if '%' in url else 0
    features['count_dots'] = url.count('.')
    features['count_slashes'] = url.count('/')
    features['count_equals'] = url.count('=')
    features['count_question'] = url.count('?')
    suspicious_keywords = ['login', 'verify', 'secure', 'account', 'update', 'bank', 'free', 'password']
    features['has_suspicious_keywords'] = 1 if any(word in url.lower() for word in suspicious_keywords) else 0

    return features
