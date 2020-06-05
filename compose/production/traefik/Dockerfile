FROM traefik:v2.0
RUN mkdir -p /etc/traefik/acme
RUN touch /etc/traefik/acme/acme.json
RUN chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/production/traefik/traefik.yml /etc/traefik
ENV DO_AUTH_TOKEN=ed0f97ea6e9dbcbf273720912b420640ce22d8fd2ac41299746dd127a5438b63
