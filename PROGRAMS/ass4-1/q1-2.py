# classify an email as Billing, Technical Support, Feedback, or Others

def classify_email(email_text):
    billing_keywords = ["invoice", "payment", "billing", "charge", "due"]
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
    sample_emails = [
        "Dear Customer, your invoice for the recent purchase is attached.",
        "Hello, I am facing a technical issue with my account.",
        "I would like to provide some feedback on your service.",
        "Just wanted to say thank you for the great experience!",
        "Please confirm the payment has been received."
    ]

    for email in sample_emails:
        category = classify_email(email)
        print(f"Email: {email}\nClassified as: {category}\n")