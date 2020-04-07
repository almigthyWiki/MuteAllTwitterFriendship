Script para silenciar cuentas que son seguidas en Twitter.

Requiere acceso API, puedes solicitarla en "https://developer.twitter.com/"

Ya con el acceso a la aplicación en modo desarrollador, reemplazar en el script
"mute_accounts.py" con las llaves correspondientes de la cuenta.

consumer_key = 'DnVDf530Dds534vfvWQDFsads564Ig'
consumer_secret = 'zktrgtaeferGweRHfWrgwergqaergWErqewerfErGt324Wz9RNpl'
access_token = '10626483dsafsdfas-283542hio8wedhlwfQk'
access_token_secret = 'sdfgaqksdfjhASLKEFGDQewrgweIH234gfsegradrfQOFwerJDQ932rg89wg2QFQjBM'
  
Utiliza "tweepy" para ejecutar el proceso y "time.sleep" en 6 segundos
para no incumplir con el "rate limit" que la API de Twitter permite.

Funcionamiento:

Si ya están registradas las llaves de acceso "python3 mute_accounts.py"
esperar hasta que termine el proceso.
