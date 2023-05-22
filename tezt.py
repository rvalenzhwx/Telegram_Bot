#!/usr/bin/env python3

import keyring
import keyring.util.platform_ as keyring_platform

print(keyring_platform.config_root())
print(keyring.get_keyring())

SERV="dedfded"
TOK="efdefefefe"

keyring.set_password(SERV, TOK, "3-python3-jeepney_0.8.0-3_all.deb")
cred=keyring.get_credential(SERV, TOK)
print(cred.username)
print(cred.password)

