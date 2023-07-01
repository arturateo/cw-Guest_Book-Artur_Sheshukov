from django.db import models

status_field = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    guest_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя гостя')
    guest_email = models.EmailField(null=False, blank=False, verbose_name='Email гостя')
    text_records = models.TextField(max_length=300, null=True, blank=True, verbose_name='Доп. описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(null=False, blank=False, default='active',
                              verbose_name='Статус', choices=status_field)

    def __str__(self):
        return f'{self.guest_name} - {self.guest_email}'

    class Meta:
        db_table = 'guestbook'
        verbose_name = "гостевая книга"
        verbose_name_plural = "гостевая книга"
