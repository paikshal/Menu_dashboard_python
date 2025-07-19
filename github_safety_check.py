#!/usr/bin/env python3
"""
GitHub Safety Check Script
This script checks for sensitive data before pushing to GitHub
"""

import os
import re
import sys

def check_for_sensitive_data():
    """Check for sensitive data in the codebase"""
    
    print("🔍 Checking for sensitive data before GitHub push...")
    print("=" * 60)
    
    sensitive_patterns = [
        # API Keys and Tokens
        r'[a-zA-Z0-9]{32,}',  # Long alphanumeric strings (potential API keys)
        r'sk_[a-zA-Z0-9]{24,}',  # Stripe secret keys
        r'pk_[a-zA-Z0-9]{24,}',  # Stripe public keys
        r'AIza[a-zA-Z0-9]{35}',  # Google API keys
        r'ya29\.[a-zA-Z0-9_-]+',  # Google OAuth tokens
        
        # Passwords and Secrets
        r'password\s*[:=]\s*["\'][^"\']+["\']',  # Hardcoded passwords
        r'secret\s*[:=]\s*["\'][^"\']+["\']',  # Hardcoded secrets
        r'token\s*[:=]\s*["\'][^"\']+["\']',  # Hardcoded tokens
        
        # Email addresses
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',  # Email addresses
        
        # Phone numbers
        r'\+?[1-9]\d{1,14}',  # International phone numbers
        
        # Credit card numbers (basic pattern)
        r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',  # Credit card numbers
        
        # Database connection strings
        r'mongodb://[^"\s]+',  # MongoDB connection strings
        r'postgresql://[^"\s]+',  # PostgreSQL connection strings
        r'mysql://[^"\s]+',  # MySQL connection strings
    ]
    
    # Files to check
    files_to_check = [
        '*.py',
        '*.js',
        '*.jsx',
        '*.ts',
        '*.tsx',
        '*.json',
        '*.txt',
        '*.md',
        '*.yml',
        '*.yaml',
        '*.env*',
        '*.config',
        '*.conf'
    ]
    
    # Files to ignore
    ignore_files = [
        '.git',
        'node_modules',
        '__pycache__',
        '.env',
        '.env.local',
        '.env.production',
        'passwords.txt',
        'creditina.json',
        'setup_env.py',
        'github_safety_check.py'
    ]
    
    issues_found = []
    
    def should_ignore_file(filepath):
        """Check if file should be ignored"""
        for ignore in ignore_files:
            if ignore in filepath:
                return True
        return False
    
    def scan_file(filepath):
        """Scan a single file for sensitive data"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    for pattern in sensitive_patterns:
                        matches = re.findall(pattern, line)
                        for match in matches:
                            # Skip if it's just a variable name or comment
                            if any(skip in line.lower() for skip in ['#', '//', '/*', '*/', 'variable', 'example', 'placeholder']):
                                continue
                            
                            # Skip if it's an environment variable reference
                            if 'os.getenv(' in line or 'process.env.' in line:
                                continue
                            
                            issues_found.append({
                                'file': filepath,
                                'line': line_num,
                                'content': line.strip(),
                                'match': match
                            })
        except Exception as e:
            print(f"⚠️  Could not read {filepath}: {e}")
    
    # Scan all files
    for root, dirs, files in os.walk('.'):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not should_ignore_file(os.path.join(root, d))]
        
        for file in files:
            filepath = os.path.join(root, file)
            if should_ignore_file(filepath):
                continue
            
            # Check file extensions
            if any(file.endswith(ext.replace('*', '')) for ext in files_to_check):
                scan_file(filepath)
    
    return issues_found

def check_git_status():
    """Check Git status for sensitive files"""
    print("\n🔍 Checking Git status...")
    
    # Check if .env is being tracked
    if os.path.exists('.env'):
        print("⚠️  .env file exists - make sure it's in .gitignore")
    
    # Check if passwords.txt is being tracked
    if os.path.exists('passwords.txt'):
        print("⚠️  passwords.txt exists - make sure it's in .gitignore")
    
    # Check .gitignore
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            gitignore_content = f.read()
            
        required_ignores = ['.env', 'passwords.txt', '*.key', '*.pem']
        missing_ignores = []
        
        for ignore in required_ignores:
            if ignore not in gitignore_content:
                missing_ignores.append(ignore)
        
        if missing_ignores:
            print(f"❌ Missing from .gitignore: {', '.join(missing_ignores)}")
        else:
            print("✅ .gitignore looks good")
    else:
        print("❌ No .gitignore file found")

def main():
    """Main function"""
    print("🛡️ GitHub Safety Check for Menu-Based Dashboard")
    print("=" * 60)
    
    # Check for sensitive data
    issues = check_for_sensitive_data()
    
    if issues:
        print(f"\n❌ Found {len(issues)} potential security issues:")
        print("-" * 60)
        
        for issue in issues[:10]:  # Show first 10 issues
            print(f"📁 {issue['file']}:{issue['line']}")
            print(f"   Content: {issue['content']}")
            print(f"   Match: {issue['match']}")
            print()
        
        if len(issues) > 10:
            print(f"... and {len(issues) - 10} more issues")
        
        print("🚨 RECOMMENDATION: Review these issues before pushing to GitHub!")
        print("   - Remove or replace hardcoded credentials")
        - Use environment variables instead
        - Add files to .gitignore if needed
        
        return False
    else:
        print("\n✅ No obvious sensitive data found!")
    
    # Check Git status
    check_git_status()
    
    print("\n✅ Safety check completed!")
    print("🚀 You can now safely push to GitHub")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 