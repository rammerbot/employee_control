from datetime import datetime, timedelta

from django.db import models

# Manager de sucursales
class BranchManager(models.Manager):

# obtener sucursal
    def branch_browser(self, branch):
        result = self.get(branch__icontains = branch)
        return result

# Manager de enntradas
class EntryHoursManager(models.Manager):

    # verificar o crear entrada 
    def verify_or_create_entry(self, employee, branch):
        date = datetime.now().date()
        register = self.filter(created__icontains =  date, employee = employee.id)
        if register:
            return "created"
        else:
            self.create(
                employee = employee,
                branch = branch
            )
            return "success"
    
# Manager inicio de almuerzo    
class LunchEstartManager(models.Manager):

    # Crea o verifica el inicio del almuerzo
    def verify_or_create_start_lunch(self, employee, branch):

        date = datetime.now().date()
        ten_minutes_ago = timedelta(minutes=10)
        register = self.filter(created__icontains =  date, employee = employee.id)
        if register:
            if datetime.now() >= register[0].created + ten_minutes_ago:
                return "created"
            else:
                return "too_soon"  
        else:
            self.create(
                employee = employee,
                branch = branch
            )
            return "success"
# Manager de Termino de almuerzo        
class LunchEndManager(models.Manager):

    # Crea o verifica el termino del almuerzo
    def verify_or_create_end_lunch(self, employee, branch):

        date = datetime.now().date()
        register = self.filter(created__icontains =  date, employee = employee.id)
        if register:
            return "created"
        else:
            self.create(
                employee = employee,
                branch = branch
            )
            return "success"
        
# Manager de registro de salida        
class ExitHoursManager(models.Manager):

    # Crea o verifica las salidas
    def verify_or_create_exit(self, employee, branch):
        date = datetime.now().date()
        register = self.filter(created__icontains =  date, employee = employee.id)
        if register:
            return "created"
        else:
            self.create(
                employee = employee,
                branch = branch
            )
            return "success"