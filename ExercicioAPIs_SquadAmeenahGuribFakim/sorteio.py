import random

tarefas = [
    "1. Desenvolvedor de Rota para Listar Localizações",
    "2. Desenvolvedor de Rota para Listar Episódios",
    "3. Desenvolvedor de Rota para Exibir Perfil da Localização",
    "4. Desenvolvedor de Rota para Exibir Perfil do Episódio",
    "5. Desenvolvedor de Perfil do Personagem",
    "6. Desenvolvedor de Lógica de Integração para Localizações",
    "7. Desenvolvedor de Lógica de Integração para Episódios",
    "8. Testador de Integração e Qualidade",
]

squad = [
    "Ana Paula",
    "Aparecida",
    "Jessica",
    "Juliana",
    "Marcia",
    "Monique",
    "Núbia",
    "Rafaela",
]

random.shuffle(tarefas)

for tarefa, integrante in enumerate(squad):
    print(f"{integrante} -> Tarefa {tarefas[tarefa]}")
