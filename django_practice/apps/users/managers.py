from typing import Dict
from typing_extensions import Self

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _type_check_values(self, **kwargs: Dict[str, str]) -> None:
        email = kwargs["email"]
        name = kwargs["name"]
        password = kwargs["password"]

        if not isinstance(email, str):
            raise TypeError(f"email is expected str but {type(email)} is given")
        if not isinstance(name, str):
            raise TypeError(f"name is expected str but {type(name)} is given")
        if not isinstance(password, str):
            raise TypeError(f"password is expected str but {type(password)} is given")

        return None

    def create_user(self, **kwargs: Dict[str, str]) -> Self:
        try:
            self._type_check_values(**kwargs)
            password = kwargs.pop("password")
            user = self.model(**kwargs)

            user.set_password(password)
            user.save(using=self._db)
            return user

        except KeyError as exc:
            raise KeyError("") from exc

    def create_admin(self, **kwargs):
        admin = self.create_user(**kwargs)
        admin.is_staff = True
        admin.is_active = True
        admin.save(using=self._db)
        return admin

    def create_superuser(self, **kwargs):
        superuser = self.create_admin(**kwargs)
        superuser.is_admin = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser
