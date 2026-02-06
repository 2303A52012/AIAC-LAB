'''
1. generate a 5 simple and simple emails in categories:
• Billing
• Technical Support
• Feedback
• Others

'''

def generate_emails():
    """Generate simple emails in different categories."""
    emails = {
        "Billing": [
            "Subject: Invoice for Your Recent Purchase\n\nDear Customer,\n\nThank you for your recent purchase. Please find attached the invoice for your records.\n\nBest regards,\nBilling Team",
            "Subject: Payment Confirmation\n\nDear Customer,\n\nWe have received your payment successfully. Thank you for your promptness.\n\nBest regards,\nBilling Team",
            "Subject: Billing Inquiry\n\nDear Customer,\n\nIf you have any questions regarding your bill, please do not hesitate to contact us.\n\nBest regards,\nBilling Team",
            "Subject: Subscription Renewal Notice\n\nDear Customer,\n\nYour subscription is set to renew soon. Please ensure your payment information is up to date.\n\nBest regards,\nBilling Team",
            "Subject: Refund Processed\n\nDear Customer,\n\nWe have processed your refund. You should see the amount reflected in your account within 5-7 business days.\n\nBest regards,\nBilling Team"
        ],
        "Technical Support": [
            "Subject: Technical Support Request Received\n\nDear User,\n\nWe have received your technical support request and will get back to you shortly.\n\nBest regards,\nTech Support Team",
            "Subject: Issue Resolved\n\nDear User,\n\nWe are pleased to inform you that the issue you reported has been resolved. Please check and confirm.\n\nBest regards,\nTech Support Team",
            "Subject: Follow-up on Your Support Ticket\n\nDear User,\n\nWe wanted to follow up on your support ticket. Please let us know if you need further assistance.\n\nBest regards,\nTech Support Team",
            "Subject: Scheduled Maintenance Notification\n\nDear User,\n\nPlease be informed that we will be performing scheduled maintenance on our systems this weekend.\n\nBest regards,\nTech Support Team",
            "Subject: Software Update Available\n\nDear User,\n\nA new software update is available. Please update to the latest version for improved performance and security.\n\nBest regards,\nTech Support Team"
        ],
        "Feedback": [
            "Subject: We Value Your Feedback!\n\nDear Customer,\n\nWe would love to hear your thoughts on our services. Please take a moment to provide your feedback.\n\nBest regards,\nCustomer Service Team",
            "Subject: Thank You for Your Feedback\n\nDear Customer,\n\nThank you for taking the time to provide us with your feedback. We appreciate your input.\n\nBest regards,\nCustomer Service Team",
            "Subject: Feedback Request\n\nDear Customer,\n\nYour opinion matters to us. Please share your experience with our services.\n\nBest regards,\nCustomer Service Team",
            "Subject: Survey Invitation\n\nDear Customer,\n\nWe invite you to participate in our customer satisfaction survey. Your feedback helps us improve.\n\nBest regards,\nCustomer Service Team",
            "Subject: Improvements Based on Your Feedback\n\nDear Customer,\n\nWe have made several improvements based on your feedback. Thank you for helping us serve you better.\n\nBest regards,\nCustomer Service Team"
        ],
        "Others": [
            "Subject: Welcome to Our Service\n\nDear Customer,\n\nWe are excited to have you on board! Welcome to our service.\n\nBest regards,\nCustomer Service Team",
            "Subject: Important Update\n\nDear Customer,\n\nPlease be informed about an important update regarding our services.\n\nBest regards,\nCustomer Service Team",
            "Subject: Holiday Greetings\n\nDear Customer,\n\nWishing you a joyous holiday season and a prosperous New Year!\n\nBest regards,\nCustomer Service Team",
            "Subject: Event Invitation\n\nDear Customer,\n\nYou are cordially invited to our upcoming event. We hope to see you there!\n\nBest regards,\nCustomer Service Team",
            "Subject: Account Activation\n\nDear Customer,\n\nYour account has been successfully activated. You can now access all our services.\n\nBest regards,\nCustomer Service Team"
        ]
    }
    return emails
if __name__ == "__main__":
    email_dict = generate_emails()
    for category, email_list in email_dict.items():
        print(f"\nCategory: {category}\n")
        for email in email_list:
            print(email)
            print("-" * 50)
            
# make a list of all this emails in a single list in a random order
import random
def get_all_emails_randomized():
    """Get all emails in a single list in random order."""
    email_dict = generate_emails()
    all_emails = []
    for email_list in email_dict.values():
        all_emails.extend(email_list)
    random.shuffle(all_emails)
    return all_emails
if __name__ == "__main__":
    randomized_emails = get_all_emails_randomized()
    print("\nAll Emails in Random Order:\n")
    for email in randomized_emails:
        print(email)
        print("-" * 50)
    print(randomized_emails)
        
list=get_all_emails_randomized()
print(list)