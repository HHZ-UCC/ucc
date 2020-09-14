

# Implementierung Service

# Bot
- Aufruf der Card URLs mit Payload und User Context - Erledigt

## Base
- Anlage des Users wenn nicht vorhanden in der Datenbank
- Zur Verfügungstellung einer Middleware damit services das benutzen können

## Maintenance Service:
- Skeleton für maintenance service               - Erledigt
- Integration mit Datenbank                      - Erledigt
- Integarton der Mainteannce Service Cards       - Erledigt
    1. Zeigen aller offenen Tickets Card         - Offen
    2. Ticket Assignment Card                    - Erledigt
    3. Bestätigungs Card                         - Erledigt
- Integration an Kafka als Consumer              - Erledigt
- Regelwerk für Thingsboard erstellen            - Erledigt
- Regelwerk von Thingsboard an Kafka anbinden    - Erledigt
- Anbinden Device (Postman an ThingsBoard)       - Erledigt

## Kassenalert Service:
- Skeleton für kassenalert service                    - Erledigt
- Integration mit Datenbank                           - Erledigt
- Integarton der Service Cards                        - Offen
    1. Zeigen aller Kassen Alerts                     - Offen
    1. Assignment Card                                - Offen
    2. Bestätigungs Card                              - Offen
- Regelwerk für Thingsboard erstellen                 - Erledigt
- Regelwerk von Thingsboard an Kafka anbinden         - Erledigt
- Anbinden Dasbutton (Postman oder physikalisch       - Erledigt 
an ThingsBoard)

## Registry Service:
- Skeleton für registry service                       - Erledigt
- Integration mit Datenbank                           - Keine Datenbank erforderlich
- Integartion der Service Cards                       - Erledigt
     1. Optionen der Services mit der Card            - Erledigt
- Registrierungs API                                  - Erledigt

## Deployment
- Django docker image                                 - Erledigt
- Bot docker image                                    - Erledigt
- Kafka                                               - Erledigt
- Thingsboard                                         - Erledigt


## Dokumentation                                      - Offen

## Testing                                            - Offen
- Integration
- Deployment