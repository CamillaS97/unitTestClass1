from src.service.service_user import ServiceUser

service = ServiceUser()
resultado = service.add_user("Camilla", "Teste")
print(resultado)

print(service.store.bd[0].name)

outro_result = service.remove_user("Camilla", "Teste")
print(outro_result)