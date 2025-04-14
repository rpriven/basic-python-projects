import re
from collections import Counter

def analyze_log_file(log_file):
    """Analyze a simple log file for patterns."""
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    try:
        with open(log_file, 'r') as file:
            # Read all lines
            log_lines = file.readlines()
            
            # Extract IP addresses
            ip_addresses = []
            for line in log_lines:
                found_ips = re.findall(ip_pattern, line)
                ip_addresses.extend(found_ips)
            
            # Count occurrences
            ip_counts = Counter(ip_addresses)
            
            # Prepare results
            results = {
                'total_lines': len(log_lines),
                'unique_ips': len(ip_counts),
                'most_common': ip_counts.most_common(5),
                'ip_counts': dict(ip_counts)
            }
            
            return results
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Demo usage
if __name__ == "__main__":
    log_file = input("Enter the path to a log file: ")
    results = analyze_log_file(log_file)
    
    if results:
        print(f"\nLog Analysis Results:")
        print(f"Total log entries: {results['total_lines']}")
        print(f"Unique IP addresses: {results['unique_ips']}")
        
        print("\nTop 5 most frequent IP addresses:")
        for ip, count in results['most_common']:
            print(f"  {ip}: {count} occurrences")
