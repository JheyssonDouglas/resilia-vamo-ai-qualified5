# Função
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    # Condição 1
    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada2 < tempo_chegada3):
        return(f"1 - {tempo_chegada1} minutos\n"
               f"2 - {tempo_chegada2} minutos\n"
               f"3 - {tempo_chegada3} minutos\n")
# Condição 2
    elif (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
        return(f"1 - {tempo_chegada1} minutos\n"
               f"2 - {tempo_chegada3} minutos\n"
               f"3 - {tempo_chegada2} minutos\n")
# Condição 3
    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada1 < tempo_chegada3:
        return(f"1 - {tempo_chegada2} minutos\n"
               f"2 - {tempo_chegada1} minutos\n"
               f"3 - {tempo_chegada3} minutos\n")
# Condição 4
    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada3 < tempo_chegada1:
        return(f"1 - {tempo_chegada2} minutos\n"
               f"2 - {tempo_chegada3} minutos\n"
               f"3 - {tempo_chegada1} minutos\n")
# Condição 5
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
        return(f"1 - {tempo_chegada3} minutos\n"
               f"2 - {tempo_chegada2} minutos\n"
               f"3 - {tempo_chegada1} minutos\n")
# Condição 6
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada2):
        return(f"1 - {tempo_chegada3} minutos\n"
               f"2 - {tempo_chegada1} minutos\n"
               f"3 - {tempo_chegada2} minutos\n")


# Print
print(podio_olimpico(20, 16, 12))
