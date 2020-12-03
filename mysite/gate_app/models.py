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
    ('G. VIJAY & SONS.', 'G. VIJAY & SONS.'),
    ('ARKAP KNITS P.LTD.', 'ARKAP KNITS P.LTD.'),
    ('R.R.ENTERPRISES', 'R.R.ENTERPRISES'),
    ('Akash Enterprise', 'Akash Enterprise'),
    ('Naitik Trading Company', 'Naitik Trading Company'),
    ('Ritesh Knit Fab', 'Ritesh Knit Fab'),
    ("Knifaso Knit's Fab" ,"Knifaso Knit's Fab"),
    ('Netflex (India) Pvt Ltd', 'Netflex (India) Pvt Ltd'),
    ('Gautam Fabrics', 'Gautam Fabrics'),
    ('Technocraft Industries India Ltd', 'Technocraft Industries India Ltd'),
    ('Dilip Fabrics Pvt.Ltd.', 'Dilip Fabrics Pvt.Ltd.'),
    ('Vastra Creations', 'Vastra Creations'),
    ('Ampersand', 'Ampersand'),
    ('Global Touch', 'Global Touch'),
    ('FRK Textile Screen Printing', 'FRK Textile Screen Printing'),
    ('RBS Creation', 'RBS Creation'),
    ('Nalanda Prints', 'Nalanda Prints'),
    ('JMS Group', 'JMS Group'),
    ('Om Embroidery', 'Om Embroidery'),
    ('Dhaga Ghar Threads Pvt Ltd', 'Dhaga Ghar Threads Pvt Ltd'),
    ('Gaurav Traders', 'Gaurav Traders'),
    ('R K Global', 'R K Global'),
    ('Hitesh Treding', 'Hitesh Treding'),
    ("Shri Sai Knit's", "Shri Sai Knit's"),
    ('S L Hosiery', 'S L Hosiery'),
    ('Others', 'others')
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
    upload = models.FileField(null=True)
    Approval_status = models.CharField(max_length=20, choices=APPROV)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Gate_entry_no


