FROM mongo

COPY init.json /init.json

CMD mongoimport -h mongo -u fruitfacts -p fruitfacts --db fruitfacts --authenticationDatabase admin -c fruits --type json --file /init.json --jsonArray --mode=upsert --upsertFields=name