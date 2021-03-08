def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada2 < tempo_chegada3):
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")

    elif (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")

    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada1 < tempo_chegada3:
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")

    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada3 < tempo_chegada1:
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")
                
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")
      
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada2):
        return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
                f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
                f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")
      
tempo_chegada1 = 38
tempo_chegada2 = 49
tempo_chegada3 = 54
nome_corredor1 = "Jheysson"
nome_corredor2 = "Raquel"
nome_corredor3 = "Maria Fernanda"

print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3))


def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
  if(tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada2 < tempo_chegada3):
    return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
            f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
            f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")

  elif(tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
    return( f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n"
            f"2 - {nome_corredor3} - {tempo_chegada3} minutos\n"
            f"3 - {nome_corredor2} - {tempo_chegada2} minutos\n")

  elif(tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and (tempo_chegada1 < tempo_chegada3):
    return( f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n"
            f"2 - {nome_corredor1} - {tempo_chegada1} minutos\n"
            f"3 - {nome_corredor3} - {tempo_chegada3} minutos\n")

  elif(tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada1):
    return( f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n"
            f"2 - {nome_corredor3} - {tempo_chegada3} minutos\n"
            f"3 - {nome_corredor1} - {tempo_chegada1} minutos\n")
  
  elif(tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada2):
      return( f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n"
              f"2 - {nome_corredor1} - {tempo_chegada1} minutos\n"
              f"3 - {nome_corredor2} - {tempo_chegada2} minutos\n")
    
  elif(tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
      return( f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n"
              f"2 - {nome_corredor2} - {tempo_chegada2} minutos\n"
              f"3 - {nome_corredor1} - {tempo_chegada1} minutos\n")

tempo_chegada1 = 54
tempo_chegada2 = 87
tempo_chegada3 = 56
nome_corredor1 = "Jheysson"
nome_corredor2 = "Raquel"
nome_corredor3 = "Maria Fernanda"

print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3))