FROM traefik:v2.0
RUN mkdir -p /etc/traefik/acme
RUN touch /etc/traefik/acme/acme.json
RUN chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/production/traefik/traefik.yml /etc/traefik
ENV DO_AUTH_TOKEN=953d6ed6d444f173f3be833cf69403003a1ca41f0e2cdc8deff8dd4021c4294e
