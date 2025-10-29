class Smartphone:
    def __init__(self, marka_phone, model_phone, number):
        self.marka_phone = marka_phone
        self.model_phone = model_phone
        self.number = number

    def __str__(self):
        return f"{self.marka_phone} - {self.model_phone}. {self.number}"