from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.CharField("이메일", max_length=128)
    name = models.CharField("이름", max_length=32)

    is_active = models.BooleanField("활성화 여부", default=False)
    is_staff = models.BooleanField("직원 여부", default=False)
    is_admin = models.BooleanField("어드민 계정 여부", default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email", "password", "name"]

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    domain_allowlist = [
        "apple.com",
        "facebook.com",
        "gmail.com",
        "kakao.com",
        "naver.com",
    ]

    class Meta:
        db_table = "users"
        verbose_name = "유저"
        verbose_name_plural = "유저 목록"

    def __str__(self) -> str:
        return self.nickname

    @property
    def has_staff_perm(self) -> bool:
        return self.is_staff

    @property
    def has_admin_perm(self) -> bool:
        return self.is_admin

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_active

    def has_perms(self, perm_list, obj=None) -> bool:
        return self.is_active

    def has_module_perms(self, app_label) -> bool:
        return self.is_active
