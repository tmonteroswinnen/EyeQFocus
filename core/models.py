from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VisionTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.test_date}"


class MedicalReport(models.Model):
    test = models.ForeignKey(VisionTest, on_delete=models.CASCADE)
    result_text = models.TextField()

    def __str__(self):
        return f"{self.test} - {self.result_text}"
