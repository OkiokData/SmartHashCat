#!/bin/bash

echo '[*] Installing required packages'
apt install hashcat python3

echo '[*] Downloading HashCat rule OneRuleToRuleThemAll'
wget https://raw.githubusercontent.com/NotSoSecure/password_cracking_rules/master/OneRuleToRuleThemAll.rule
mv -v OneRuleToRuleThemAll.rule /usr/share/hashcat/rules/

echo '[*] Deploying SmartHashCat files'
cp -rv usr/ /
cp -rv SmartHashCat /opt/
chmod +x /opt/SmartHashCat/SmartHashCat.py

if [ -f /usr/share/SmartHashCat/lists/rockyou.txt ]; then
    echo '[*] Skipping Rockyou database download'
else
    echo '[*] Downloading Rockyou database'
    wget https://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
    bunzip2 rockyou.txt.bz2
    mv rockyou.txt /usr/share/SmartHashCat/lists/
fi
