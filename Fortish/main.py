#### Importation des librairies :
import hashlib
import os



#### Création d'un compte utilisateur :
def account_creation() :   
    print('\n----------- ACCOUNT CREATION -----------')
    
    # On demande à l'utilisateur ses credentials, le mot de passe doit comporter plus de 8 caractères.
    print('\nPlease enter an username')
    print('username : ', end=' ')
    username = input()
    
    print('Please enter a password twice, password must be more than 8 characters')
    print('password : ', end=' ')
    password1 = input()
    print('password : ', end=' ')
    password2 = input()
    
    if password1 == password2 and len(password1) >= 8:
    
        # Concaténation du couple id/mdp.
        idpassword = username + password1
        
        
        # Création et sauvegarde du salt rattaché au compte que l'utilisateur créé.
        salt = str(os.urandom(10).hex())
        fichier = open("salts.txt", "w")
        fichier.write(salt)
        fichier.close()
        
        # Création et sauvegarde du hash rattaché au compte que l'utilisateur créé.
        fichier = open("hashs.txt", "w")
        fichier.write(str(hashlib.pbkdf2_hmac('sha256', str.encode(idpassword), str.encode(salt), 100000).hex()))
        fichier.close()
        
        print('\nAccount creation successful')
        success = 1 # Le compte a été créé avec succès.
        
    else :
        print('\nDifferent passwords or password too short, please try again')
        success = 0 # Le compte n'a pas été créé avec succès.
    
    return success



#### Autentification de l'utilisateur :
def authentication():
    print('\n-----------  AUTHENTICATION  -----------')
    
    # On demande à l'utilisateur ses credentials.
    print('\nPlease enter your username and your pasword')
    print('username : ', end=' ')
    username = input()
    print('password : ', end=' ')
    password = input()
    
    #Concaténation du couple id/mdp
    idpassword = username + password
    
    #Ouverture du fichier comportant le salt relié au compte de l'utilisateur.
    with open("salts.txt", "r") as saltsfile:
        salt = saltsfile.read()
    
    #Calcul du hash du couple id/mdp que l'utilisateur a donné.
    hash = str(hashlib.pbkdf2_hmac('sha256', str.encode(idpassword), str.encode(salt), 100000).hex())
    
    
    #Ouverture du fichier comportant le hash du couple id/mdp du compte créé.
    with open("hashs.txt", "r") as hashsfile:
        goodhash = hashsfile.read()
    
    #Comparaison des hashs des credentials du compte créé et des credentials donnés par l'utilisateur.
    if goodhash == hash:
        print('\nHello again ' + username)
        credentials = 1    #Les credentials donnés par l'utilisateur sont bons.
    else:
        print('\nYour username or password is wrong')
        print('ACCESS DENIED')
        credentials = 0    #Les credentials donnés par l'utilisateur ne sont pas bons.
    return credentials




#### Fonction main : 
print('\nDo you have an account? (Yes/No)')
print('         - ', end=' ')
answer1 = input()

# Vérification de la possession d'un compte.
if answer1 == 'Yes' or answer1 == 'yes' or answer1 == 'Y' or answer1 == 'y' or answer1 == 'Ye' or answer1 == 'ye':
    authentication()

elif answer1 == 'No' or answer1 == 'no' or answer1 == 'N' or answer1 == 'n' :
    success = account_creation()
    if success == 1 :
        authentication()
    else :
        print('\nEnd')