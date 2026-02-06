'''
observe the following example
Email: Dear Customer, your invoice for the recent purchase is attached.
Classified as: Billing

Email: Hello, I am facing a technical issue with my account.
Classified as: Technical Support

Email: I would like to provide some feedback on your service.
Classified as: Feedback

Email: Just wanted to say thank you for the great experience!
Classified as: Others

Email: Please confirm the payment has been received.
Classified as: Billing

now catorrise the followinf email 
Email: Subject: Invoice for Your Recent Purchase
using python code
'''
# classify an email as Billing, Technical Support, Feedback, or Others
def classify_email(email_text):
    billing_keywords = ["invoice", "payment", "billing", "charge", "due","refund"]
    technical_keywords = ["error", "bug", "issue", "problem", "technical"]
    feedback_keywords = ["suggestion", "feedback", "comment", "review"]

    email_text_lower = email_text.lower()

    billing_count = sum(1 for keyword in billing_keywords if keyword in email_text_lower)
    technical_count = sum(1 for keyword in technical_keywords if keyword in email_text_lower)
    feedback_count = sum(1 for keyword in feedback_keywords if keyword in email_text_lower)

    if billing_count > 0:
        return "Billing"
    elif technical_count > 0:
        return "Technical Support"
    elif feedback_count > 0:
        return "Feedback"
    else:
        return "Others"
# Example usage
if __name__ == "__main__":
    email = input("Enter the email content: ")
    category = classify_email(email)
    print(f"Email: {email}\nClassified as: {category}\n")
    
