from django.contrib.auth.mixins import UserPassesTestMixin


class AdminRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.is_superuser


class HeadOfficeRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.department.type == 'HEAD'


class SatelliteOfficeRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.department.type == 'SATELLITE'
