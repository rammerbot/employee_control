from django.db import models


class EmployeeManager(models.Manager):

    # Buscador de empleado
    def employee_browser(self, card):
        employee = self.get(card = card)
        return employee
    