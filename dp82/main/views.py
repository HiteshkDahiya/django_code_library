import razorpay
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from xhtml2pdf import pisa
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def payment_page(request):
    data = {
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1
    }
    payment = client.order.create(data=data)
    return render(request, 'main/payment.html', {
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    })

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        payment_id = data.get('razorpay_payment_id')
        order_id = data.get('razorpay_order_id')
        signature = data.get('razorpay_signature')

        try:
            # 🔐 Verify the payment signature
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            # 📦 Fetch payment details to get email
            payment_info = client.payment.fetch(payment_id)
            payer_email = payment_info.get('email')

            if not payer_email:
                return render(request, 'main/payment_failed.html', {"error": "Email not found in payment details."})

            # 🧾 Render invoice template to PDF
            html = render_to_string("main/invoice.html", {
                "payment_id": payment_id,
                "email": payer_email,
                "amount": 500.00,
                "date": datetime.now().strftime("%d %b %Y")
            })
            result = BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=result)

            if pisa_status.err:
                return render(request, "main/payment_failed.html", {"error": "PDF generation failed."})

            # 📧 Send invoice via email
            mail = EmailMessage(
                subject="Invoice for your Payment",
                body="Thank you for your purchase! Please find the invoice attached.",
                from_email=settings.EMAIL_HOST_USER,
                to=[payer_email],
            )
            mail.attach("invoice.pdf", result.getvalue(), "application/pdf")
            mail.send()

            return render(request, 'main/payment_success.html', {"email": payer_email})

        except razorpay.errors.SignatureVerificationError:
            return render(request, 'main/payment_failed.html', {"error": "Payment verification failed."})

    return render(request, 'main/payment_failed.html', {"error": "Invalid request method."})