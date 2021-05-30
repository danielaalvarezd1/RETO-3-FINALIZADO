import  min_salud_ancon  as  asc

def leer_cdia_humasciiano():
  print("==========REGISTRO DE HUMASCIIANO PARA VACUNACIÓN========")
  print("INFORMACION DEL SOLICITANTE HUMASCIIANO: ")
  asc.lista_profesion()
  print("----------------------------------------------------------")
  cod_cdia_humasciiano =str(input("DIGITAR No. DE CDIA DEL HUMASCIIANO: "))
  print("")
  print("***************************************************")
  codigo_cdia_hu = cod_cdia_humasciiano.upper()
  print("EL CDIA SE HA ACTUALIZADO AL NUEVO FORMATO")
  print(f"EL NUEVO FORMATO DEL CDIA DEL HUMASCIIANO ES: {codigo_cdia_hu}")
  print("***************************************************")
  validar=asc.proc_control(codigo_cdia_hu)

  if validar==True:
    print("--------------------BIENVENIDO CIUDADANO HUMASCIIANO-----------------")
    print("")
    print("Como ciudadano registrado debes constestar las siguientes preguntas:\n")
    asc.formulario()
  else:
    print("USTED NO CUMPLE LOS REQUISITOS DE REGISTRO")




leer_cdia_humasciiano()
