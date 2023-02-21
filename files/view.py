import os
from controller import ControllerGeneral, ControllerCadastro, ControllerLogin

while True:
	print("=" * 15 + " MENU " + "=" * 15)
	print("Digite [1] para se cadastrar\n"
		  "Digite [2] para fazer login\n"
		  "Digite [3] para limpar a tela\n"
		  "Digite [0] para sair")
	escolha = int(input("> "))
	if escolha == 1:
		while True:
			print("=" * 15 + " CADASTRO " + "=" * 15)
			nome = input("Digite seu nome: ")
			email = input("Digite seu email: ")
			print("Sua senha deve conter:\n"
					"- Números\n"
					"- Letras\n"
					"- Caractes especiais\n"
					"- Um mínimo de 6 digitos")
			senha = input("Digite sua senha: ")
			cadastro = ControllerCadastro.register_user(nome,email,senha)
			if cadastro == 1:
				print("Cadastro realizado com sucesso!")
				break
			elif cadastro == 2:
				print("Seu nome deve conter menos que 50 caracteres!")
				break
			elif cadastro == 3:
				print("Cadastre um email válido!")
				break
			elif cadastro == 4:
				print("Sua senha não atende aos requisitos!")
				break
			else:
				print("Erro desconhecido!")
				break
	elif escolha == 2:
		while True:
			print("=" * 15 + " LOGIN " + "=" * 15)
			email = input("Digite seu email: ")
			print("Sua senha deve conter:\n"
					"- Números\n"
					"- Letras\n"
					"- Caractes especiais\n"
					"- Um mínimo de 6 digitos")
			senha = input("Digite sua senha: ")
			login = ControllerLogin.login(email, senha)
			if login:
				print(f"O usuário '{login}' está logado!")
				break
			else:
				print("Email ou senha incorretos!")
				break
	elif escolha == 3:
		os.system('cls' if os.name == 'nt' else 'clear')
	else:
		break

