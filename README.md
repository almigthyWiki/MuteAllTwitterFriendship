Script para silenciar cuentas que son seguidas en Twitter.

Requiere acceso API, puedes solicitarla en "https://developer.twitter.com/"

Ya con el acceso a la aplicación en modo desarrollador, reemplazar en el script
"mute_accounts.py" con las llaves correspondientes de la cuenta.

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
  
Utiliza "tweepy" para ejecutar el proceso y "time.sleep" en 6 segundos
para no incumplir con el "rate limit" que la API de Twitter permite.

Funcionamiento:

Si ya están registradas las llaves de acceso "python3 mute_accounts.py"
esperar hasta que termine el proceso.
