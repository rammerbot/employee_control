from django.db import models


class EmployeeManager(models.Manager):

    # Buscador de empleado
    def employee_browser(self, card):
        try:
            employee = self.get(card = card)
            return employee
        except self.model.DoesNotExist:
            return "empty"