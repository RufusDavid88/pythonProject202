from django.db import models
from django.db.models import CharField
from django.utils import timezone


INW_CHOICES=[
    ('fabric', 'Fabric'),
    ('print work', 'Print work'),
    ('accessories', 'Accessories'),
    ('others', 'Others'),
]

DOC_TYPE=[
    ('challan', 'Challan'),
    ('invoice', 'Invoice'),
]

APPROV=[
    ('pending', 'Pending'),
    ('approved', 'Approved'),
]

REQT=[
    ('KG', 'kg'),
    ('PIECES', 'pieces'),
    ('BOX', 'box'),
    ('Palla', 'palla'),
    ('Roll', 'roll'),
]


VEND=[
    ('FRK Textile Screen Printing', 'FRK Textile Screen Printing'),
    ('Dhaga Ghar Threads Pvt Ltd', 'Dhaga Ghar Threads Pvt Ltd'),
    ('Om Embroidery', 'Om Embroidery'),
    ('Ocean International', 'Ocean International'),
    ('Sports Print', 'Sports Print'),
    ('Ritesh Knit Fab', 'Ritesh Knit Fab'),
    ('Hitesh Trading', 'Hitesh Trading'),
    ('Akash Enterprises', 'Akash Enterprises'),
    ('Gaurav Traders', 'Gaurav Traders'),
    ('Poonam Enterprises', 'Poonam Enterprises'),
    ('Maa Textiles', 'Maa Textiles'),
    ('Heena Arts', 'Heena Arts'),
    ('Tasa Graphic Prints LLP', 'Tasa Graphic Prints LLP'),
    ('Vastra Creations', 'Vastra Creations'),
    ('Global Touch', 'Global Touch'),
    ('R K Global', 'R K Global'),
    ('Poonam Enterprises', 'Poonam Enterprises'),
    ('RBS Creation', 'RBS Creation'),
    ('Knifaso Knits Fab', 'Knifaso Knits Fab'),
    ('ASHIRWAD CREATION', 'ASHIRWAD CREATION'),
    ('Patel Rib', 'Patel Rib'),
    ('Santosh Kumar Jaiswar', 'Santosh Kumar Jaiswar'),
    ('Netflex India Pvt Ltd', 'Netflex India Pvt Ltd'),
    ('High-Touch Services', 'High-Touch Services'),
    ('Santosh Kumar Thakur', 'Santosh Kumar Thakur'),
    ('JMS Group', 'JMS Group'),
    ('G. Vijay & Sons', 'G. Vijay & Sons'),
    ('Arkap Knits P.Ltd', 'Arkap Knits P.Ltd'),
    ('SUNART AGENCIES PVTLTD', 'SUNART AGENCIES PVTLTD'),
    ('INDU ENTERPRISES', 'INDU ENTERPRISES'),
    ('pramukh print', 'pramukh print'),
    ('TEJAS ENTERPRISE', 'TEJAS ENTERPRISE'),
    ('Nalanda Prints', 'Nalanda Prints'),
    ('Pappu Yadav','Pappu Yadav'),
    ('Ampersand', 'Ampersand'),
    ('R.R.Enterprises', 'R.R.Enterprises'),
    ('Shri Sai Knits', 'Shri Sai Knits'),
    ('Dilip Fabrics PVT LTD', 'Dilip Fabrics PVT LTD'),
    ('Rita sales agency', 'Rita sales agency'),
    ('SURAJ PAPER MART', 'SURAJ PAPER MART'),
    ('Alkemi Decor Designs Pvt Ltd', 'Alkemi Decor Designs Pvt Ltd'),
    ('Rampstar Clothing', 'Rampstar Clothing'),
    ('Alok Labels And Tags','Alok Labels And Tags'),
    ('Shivshakti Garments', 'Shivshakti Garments'),
    ('Gautam Fabrics', 'Gautam Fabrics'),
    ('S L Hosiery', 'S L Hosiery'),
    ('Dernier Overseas', 'Dernier Overseas'),
    ('Manki Art', 'Manki Art'),
    ('Royal Enterprises', 'Royal Enterprises'),
    ('Sahara Kaaj Buttons & Tailoring Material', 'Sahara Kaaj Buttons & Tailoring Material'),
    ('Trendy Incorp', 'Trendy Incorp'),
    ('Varun Overseas', 'Varun Overseas'),
    ('Sonal Enterprises', 'Sonal Enterprises'),
    ('Arihant Packaging', 'Arihant Packaging'),
    ('Y.S.Apparels', 'Y.S.Apparels'),
    ('Sahil Prints', 'Sahil Prints'),
    ('Naitik Trading Co.', 'Naitik Trading Co.'),
    ('Milan Packaging Solutions', 'Milan Packaging Solutions'),
    ('Rajshrey Text Pvt Ltd', 'Rajshrey Text Pvt Ltd'),
    ('Technocraft Industries Ltd', 'Technocraft Industries Ltd'),
    ('Hallmark Knit Fabrics P LTD', 'Hallmark Knit Fabrics P LTD'),
    ('J K Digital Prints', 'J K Digital Prints',),
    ('Others', 'others'),
]

def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
         return 'TSSPR00001'
    Gate_entry_no = last_invoice.Gate_entry_no
    invoice_int = int(Gate_entry_no.split('TSSPR')[-1])
    new_invoice_int = invoice_int + 1
    Gate_entry_no ='TSSPR0000' + str(new_invoice_int)
    return Gate_entry_no


class Invoice(models.Model):
    Gate_entry_no = models.CharField(max_length=500, default=increment_invoice_number, null=True, blank=True)
    Bill_no = models.CharField(max_length=20)
    Vendors: CharField = models.CharField(max_length=80, choices=VEND)
    Inventory_Date = models.DateField(max_length=20)
    Type_of_inward = models.CharField(max_length=20, choices=INW_CHOICES)
    Document_Type = models.CharField(max_length=20, choices=DOC_TYPE)
    Received_as_QTY = models.CharField(max_length=20, choices=REQT)
    Document_QTY = models.CharField(max_length=60)
    Doc_Value = models.CharField(max_length=30)
    Physical_QTY = models.CharField(max_length=60)
    Gate_Enty_Notes = models.CharField(max_length=260)
    Count_Uploades_by = models.CharField(max_length=60)
    Upload = models.ImageField(null=True, blank=True, upload_to="invoice_upload/")
    Approval_status = models.CharField(max_length=20, choices=APPROV)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Gate_entry_no


