Python 2.7.3 (default, Mar 14 2014, 11:57:14) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def num_primo(numero):

    # Para que un numero sea primodebe dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo

    for i in range(2,numero):

        if (numero%i)==0:

            # es divisible

            return False

    return True

 

while True:

    try:

        numero = int(raw_input("inserta un numero (0) salir >> "))

        if numero==0:

            break

        if es_primo(numero):

            print "\nEl numero %s es primo" % numero

        else:

            print "\nEl numero %s NO es primo" % numero
            
SyntaxError: invalid syntax
>>> def num_primo(numero):

    # Para que un numero sea primodebe dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo

    for i in range(2,numero):

        if (numero%i)==0:

            # es divisible

            return False

    return True



while True:

    try:

        numero = int(raw_input("inserta un numero (0) salir >> "))

        if numero==0:

            break

        if es_primo(numero):

            print "\nEl numero %s es primo" % numero

        else:

            print "\nEl numero %s NO es primo" % numero
            
SyntaxError: invalid syntax
>>> def es_primo(numero):

    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
   
    for i in range(2,numero):

        if (numero%i)==0:

            # es divisible

            return False

    return True

 

while True:

    try:

        numero = int(raw_input("inserta un numero (0) salir >> "))

        if numero==0:

            break

        if es_primo(numero):

            print "\nEl numero %s es primo" % numero

        else:

            print "\nEl numero %s NO es primo" % numero

    except:

        print "\nEl numero tiene que ser entero"
        
SyntaxError: invalid syntax
>>> def es_primo(numero):

    """

    Funcion que determina si un numero es primo

    Tiene que recibir el numero entero

    """

    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:

    #   1 - divisible entre 1

    #   2 - divisible entre el mismo

    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo

    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es

    # primo

    for i in range(2,numero):

        if (numero%i)==0:

            # es divisible

            return False

    return True

 

while True:

    try:

        numero = int(raw_input("inserta un numero (0) salir >> "))

        if numero==0:

            break

        if es_primo(numero):

            print "\nEl numero %s es primo" % numero

        else:

            print "\nEl numero %s NO es primo" % numero

    except:

        print "\nEl numero tiene que ser entero"
        
SyntaxError: invalid syntax
>>>  def es_primo(numero):

    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
   
    for i in range(2,numero):

        if (numero%i)==0:

            # es divisible

            return False

    return True

 

while True:

    try:

        numero = int(raw_input("inserta un numero (0) salir >> "))

        if numero==0:

            break

        if es_primo(numero):

            print "\nEl numero %s es primo" % numero

        else:

            print "\nEl numero %s NO es primo" % numero

    except:

        print "\nEl numero tiene que ser entero"
