# Searching LDAP in interesting ways

## All active users

## NIS Netgroup Triple

(&(objectClass=nisNetgroup)(nisNetgroupTriple=\(deathstar,,\)))

```bash
ldapsearch -ZxLL '(&(objectClass=nisNetgroup)(nisNetgroupTriple=\(deathstar-01,,\)))' dn
version: 1

dn: cn=static_mounts,cn=miscellaneous,ou=Netgroups,dc=example,dc=com
```


