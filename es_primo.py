Python 2.7.3 (default, Mar 14 2014, 11:57:14) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.

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
