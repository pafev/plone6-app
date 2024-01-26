# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="pafev <paulo.fernando@struct.unb.br>" \
      org.label-schema.name="plone-app-varnish" \
      org.label-schema.description="plone-app Varnish image." \
      org.label-schema.vendor="pafev"

COPY etc/varnish.vcl /etc/varnish/default.vcl
