from django.db import models
from num2words import num2words

# Create your models here.
class StaffDetails(models.Model):
    billid = models.CharField(max_length=10)
    Name_Of_Exam = models.CharField(max_length=100)
    Name_Of_Sub = models.CharField(max_length=100)
    branch_choices = [
        ('CIV', 'CIV'),
        ('MECH', 'MECH'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('AI&ML', 'AI&ML'),
        ('CAD', 'CAD')
    ]

    branch = models.CharField(max_length=10, choices=branch_choices)
    Name_Of_Staff = models.CharField(max_length=200)
    MobileNum = models.CharField(max_length=15)
    des_choices = [
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Sr. Assistant Professor', 'Sr. Assistant Professor'),
        ('Professor', 'Professor'),
        ('Others', 'Others')
    ]
    designation = models.CharField(max_length=40, choices=des_choices)
    Name_of_College = models.CharField(max_length=50)
    Name_of_Bank = models.CharField(max_length=100)

    Bank_Location = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=20)
    acc_num = models.CharField(max_length=50)

class RemunerationDetails(models.Model):

    staff = models.OneToOneField(StaffDetails, on_delete=models.CASCADE, primary_key = True)    
    work_choices = [
        ('Question Paper Setting', 'Question Paper Setting'),
        ('Paper Valuation', 'Paper Valuation'),
        ('Chief Examiner', 'Chief Examiner'),
        ('Lab Examiner', 'Lab Examiner'),
        ('Thesis Viva Voce', 'Thesis Viva Voce')
    ]  
    nature_of_work = models.CharField(max_length=30, choices=work_choices)

    number_of_papers = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    da_days = models.IntegerField(blank=True, default=0)
    da_rate = models.IntegerField(blank=True, default=0)
    ta_days = models.IntegerField(blank=True, default=0)
    ta_rate = models.IntegerField(blank=True, default=0)

    def getId(self):
        return self.billid
    def getFacultyName(self):
        return self.Name_Of_Staff
    def getRemuneration(self):
        return self.number_of_papers * self.rate
    def getTAAmount(self):
        return self.ta_days * self.ta_rate
    def getDAAmount(self):
        return self.da_days * self.da_rate
    def remTotal(self):
        return self.getRemuneration() + self.getDAAmount() + self.getTAAmount()
    def get_total_words(self):
        return num2words(self.remTotal())

