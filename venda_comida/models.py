from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Endereco(models.Model):

	cep = models.CharField( max_length=50, blank=False, null=False )

	estado = models.CharField( max_length=50, blank=False, null=False )
	cidade = models.CharField( max_length=50, blank=False, null=False )

	bairro = models.CharField( max_length=50, blank=False, null=False )
	rua = models.CharField( max_length=50, blank=False, null=False )
	numero = models.CharField( max_length=50, blank=False, null=False )

	complemento = models.CharField( max_length=50, blank=True, null=True )

	ponto_referencia = models.CharField( max_length=50, blank=True, null=True )


class Horarios(models.Model):
	segunda = models.TimeField(default=timezone.now)
	segunda_fecha = models.TimeField(default=timezone.now)

	terca = models.TimeField(default=timezone.now)
	terca_fecha = models.TimeField(default=timezone.now)

class Restaurante(models.Model):
	user = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)

	nome = models.CharField( max_length=50, blank=False, null=False )

	endereco = models.ForeignKey(Endereco, null=True, blank=False, on_delete=models.SET_NULL)

	telefone = models.CharField( max_length=15, blank=True, null=True )
	horarios = models.OneToOneField(Horarios, related_name='horarios', null=True, on_delete=models.SET_NULL)

	avaliacao = models.IntegerField('avaliacao', null=True, blank=True, default=0)


class Promocao(models.Model):
	nome = models.CharField( max_length=50, blank=False, null=False )
	valor_percentual = models.FloatField(null=True, blank=True, default=None)


class Produto(models.Model):
	nome = models.CharField( max_length=50, blank=False, null=False )
	quantidade = models.IntegerField('quantidade', default=None)
	preco = models.FloatField(null=False, blank=False, default=None)
	promocao = models.ForeignKey(Promocao, null=True, blank=True, on_delete=models.SET_NULL)

	imagem = models.ImageField(upload_to = 'foto_produto/', null=True, blank=True)



class ClasseDeProdutos(models.Model):
	restaurante = models.ForeignKey(Restaurante, null=True, blank=False, on_delete=models.SET_NULL)
	nome = models.CharField( max_length=50, blank=False, null=False )
	produtos = models.ManyToManyField(Produto, related_name='produtos_da_classe')
	promocao = models.ForeignKey(Promocao, null=True, blank=True, on_delete=models.SET_NULL)



class Cliente(models.Model):
	# user = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)

	telefone = models.CharField(max_length=22, blank=False, null=False, unique=True)

	endereco = models.ForeignKey(Endereco, null=True, blank=False, on_delete=models.SET_NULL)



class HistoricoCarrinho(models.Model):

	cliente = models.ForeignKey(Cliente, null=True, blank=False, on_delete=models.SET_NULL)

	produtos = models.ManyToManyField(Produto, related_name='produtos_no_historico')

	avaliacao = models.IntegerField('numero_documentos_criar_mes_direito', default=0)




class Carrinho(models.Model):

	cliente = models.OneToOneField(Cliente, null=True, blank=False, on_delete=models.SET_NULL)

	produtos = models.ManyToManyField(Produto, related_name='produtos_no_carrinho')





# user = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)

# cpf = models.CharField(max_length=22, blank=True, null=True, unique=True)


# foto_usuario = models.ImageField(upload_to = 'foto_usuario/', default = settings.USER_FOTO_ROOT+'/None/no-img.jpg', null=True, blank=True)

# # Chave Privada, da qual consigo a Chave Publica
# # Nao mostrar ao usuario, informar somente no cadastro (por email) e quando solicitado.
# # Essa chave deve ser considerada a identidade digital do usuario
# chave_publica = models.TextField()

# # encryptad
# chave_privada = models.TextField()
# # salt usado para gerar a chave a partir da senha
# salt = models.TextField()
# # nonce para encryptar e descryptar a chave privada
# nonce = models.TextField()

# numero_documentos_criar_mes_direito = models.IntegerField('numero_documentos_criar_mes_direito', default=5)


# # fezcrop = models.BooleanField(default=False)

# # telefone = models.CharField(max_length=15, default="")

# # endereco = models.CharField(max_length=500, default="")

# # numero_downloads_direito = models.IntegerField('numero_downloads_direito', default=0)

# # plano = models.ForeignKey(Plano, null=True, blank=False, on_delete=models.SET_NULL)

# # inativo = models.BooleanField(default=False)

# data_plano = models.DateTimeField(default=timezone.now)



# def __str__(self):
#     return self.user.username + " " + str(self.cpf) + " " + str(self.numero_documentos_criar_mes_direito)
