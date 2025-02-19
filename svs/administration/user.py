from administration.models import CustomUser

CustomUser.objects.create_superuser(
    username="pedro",
    email="pedro@pedro.com",
    cpf="024.682.832-36",
    password="123456"
)