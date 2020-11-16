# ns-newrelic-scrap

Script para identificar se o Produto New Relic possui alguma falha ou intermitência.

O scrapping é feito à partir da página https://status.newrelic.com/, mais especificamente na primeira tag <span> que fala sobre a integridade dos serviços.

Dependências:

 #### Requests:
 
 ```
 sudo pip install requets
 ```

#### Beautilfulsoup

```
sudo pip install beautifulsoup4
```