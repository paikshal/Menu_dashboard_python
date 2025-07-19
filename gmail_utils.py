import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path=os.path.join('config', '.env'))

def send_gmail(sender_email, sender_password, to_email, subject, message, is_html=False, attachments=None):
    """
    Send email using Gmail SMTP.
    Args:
        sender_email (str): Gmail address
        sender_password (str): Gmail app password
        to_email (str or list): Recipient email(s)
        subject (str): Email subject
        message (str): Email body
        is_html (bool): Whether message is HTML format
        attachments (list): List of file paths to attach
    Returns:
        str: Success or error message
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject
        
        # Handle multiple recipients
        if isinstance(to_email, list):
            msg['To'] = ', '.join(to_email)
        else:
            msg['To'] = to_email
        
        # Add body
        if is_html:
            msg.attach(MIMEText(message, 'html'))
        else:
            msg.attach(MIMEText(message, 'plain'))
        
        # Add attachments
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(file_path)}'
                    )
                    msg.attach(part)
                else:
                    logging.warning(f"Attachment not found: {file_path}")
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Convert to_email to list for sending
        recipients = to_email if isinstance(to_email, list) else [to_email]
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        
        return f"✅ Email sent successfully to {', '.join(recipients)}"
        
    except Exception as e:
        logging.error(f"Gmail error: {e}")
        return f"Error sending email: {e}"

def send_gmail_html(sender_email, sender_password, to_email, subject, html_content, attachments=None):
    """
    Send HTML email using Gmail SMTP.
    """
    return send_gmail(sender_email, sender_password, to_email, subject, html_content, is_html=True, attachments=attachments)

def send_gmail_bulk(sender_email, sender_password, recipients_list, subject, message, is_html=False):
    """
    Send bulk emails to multiple recipients.
    Args:
        recipients_list (list): List of email addresses
        subject (str): Email subject
        message (str): Email body
        is_html (bool): Whether message is HTML format
    Returns:
        str: Success or error message
    """
    try:
        success_count = 0
        failed_count = 0
        
        for recipient in recipients_list:
            result = send_gmail(sender_email, sender_password, recipient, subject, message, is_html)
            if "successfully" in result:
                success_count += 1
            else:
                failed_count += 1
                logging.error(f"Failed to send to {recipient}: {result}")
        
        return f"✅ Bulk email completed: {success_count} sent, {failed_count} failed"
        
    except Exception as e:
        logging.error(f"Bulk email error: {e}")
        return f"Error in bulk email: {e}" 

def send_gmail_template(sender_email, sender_password, to_email, template_name, template_data, attachments=None):
    """
    Send email using predefined templates.
    Args:
        sender_email (str): Gmail address
        sender_password (str): Gmail app password
        to_email (str or list): Recipient email(s)
        template_name (str): Name of the template to use
        template_data (dict): Data to fill in the template
        attachments (list): List of file paths to attach
    Returns:
        str: Success or error message
    """
    # Email templates
    templates = {
        'welcome': {
            'subject': 'Welcome to Our Service!',
            'html': '''
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
                    <h2 style="color: #007bff;">Welcome, {name}!</h2>
                    <p>Thank you for joining our service. We're excited to have you on board!</p>
                    <p>Your account details:</p>
                    <ul>
                        <li><strong>Email:</strong> {email}</li>
                        <li><strong>Account ID:</strong> {account_id}</li>
                        <li><strong>Join Date:</strong> {join_date}</li>
                    </ul>
                    <p>If you have any questions, feel free to contact us.</p>
                    <p>Best regards,<br>The Team</p>
                </div>
            </body>
            </html>
            '''
        },
        'notification': {
            'subject': 'Important Notification',
            'html': '''
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background-color: #fff3cd; padding: 20px; border-radius: 10px; border-left: 5px solid #ffc107;">
                    <h3 style="color: #856404;">{title}</h3>
                    <p>{message}</p>
                    <p><strong>Date:</strong> {date}</p>
                    <p><strong>Priority:</strong> {priority}</p>
                    <p>Please take necessary action if required.</p>
                </div>
            </body>
            </html>
            '''
        },
        'report': {
            'subject': 'Monthly Report - {month}',
            'html': '''
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background-color: #d1ecf1; padding: 20px; border-radius: 10px;">
                    <h2 style="color: #0c5460;">Monthly Report</h2>
                    <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                        <tr style="background-color: #e2e3e5;">
                            <th style="padding: 10px; border: 1px solid #dee2e6; text-align: left;">Metric</th>
                            <th style="padding: 10px; border: 1px solid #dee2e6; text-align: left;">Value</th>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">Total Users</td>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">{total_users}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">Revenue</td>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">${revenue}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">Growth Rate</td>
                            <td style="padding: 10px; border: 1px solid #dee2e6;">{growth_rate}%</td>
                        </tr>
                    </table>
                    <p><strong>Summary:</strong> {summary}</p>
                </div>
            </body>
            </html>
            '''
        },
        'custom': {
            'subject': '{subject}',
            'html': '{html_content}'
        }
    }
    
    try:
        if template_name not in templates:
            return f"Error: Template '{template_name}' not found. Available templates: {', '.join(templates.keys())}"
        
        template = templates[template_name]
        
        # Fill template with data
        subject = template['subject'].format(**template_data)
        html_content = template['html'].format(**template_data)
        
        # Send email using existing function
        return send_gmail(sender_email, sender_password, to_email, subject, html_content, is_html=True, attachments=attachments)
        
    except KeyError as e:
        return f"Error: Missing required template data: {e}"
    except Exception as e:
        logging.error(f"Template email error: {e}")
        return f"Error sending template email: {e}"

def send_gmail_newsletter(sender_email, sender_password, subscribers_list, newsletter_title, newsletter_content, attachments=None):
    """
    Send newsletter to subscribers with professional formatting.
    Args:
        sender_email (str): Gmail address
        sender_password (str): Gmail app password
        subscribers_list (list): List of subscriber email addresses
        newsletter_title (str): Newsletter title
        newsletter_content (str): Newsletter content (can be HTML)
        attachments (list): List of file paths to attach
    Returns:
        str: Success or error message
    """
    try:
        # Newsletter template
        newsletter_html = f'''
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 700px; margin: 0 auto; background-color: #f4f4f4;">
            <div style="background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="color: #333; margin-bottom: 10px;">{newsletter_title}</h1>
                    <p style="color: #666; font-size: 14px;">{datetime.now().strftime('%B %d, %Y')}</p>
                </div>
                
                <div style="line-height: 1.6; color: #333;">
                    {newsletter_content}
                </div>
                
                <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                
                <div style="text-align: center; color: #666; font-size: 12px;">
                    <p>This newsletter was sent to you because you're subscribed to our updates.</p>
                    <p>To unsubscribe, click <a href="#" style="color: #007bff;">here</a></p>
                </div>
            </div>
        </body>
        </html>
        '''
        
        success_count = 0
        failed_count = 0
        
        for subscriber in subscribers_list:
            result = send_gmail(sender_email, sender_password, subscriber, newsletter_title, newsletter_html, is_html=True, attachments=attachments)
            if "successfully" in result:
                success_count += 1
            else:
                failed_count += 1
                logging.error(f"Failed to send newsletter to {subscriber}: {result}")
        
        return f"✅ Newsletter sent: {success_count} delivered, {failed_count} failed"
        
    except Exception as e:
        logging.error(f"Newsletter error: {e}")
        return f"Error sending newsletter: {e}" 