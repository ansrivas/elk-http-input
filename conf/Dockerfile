FROM sebp/elk

WORKDIR ${LOGSTASH_HOME}

RUN gosu logstash bin/logstash-plugin install logstash-input-http

RUN cd /etc/logstash/conf.d/ \
 && rm -f 01-lumberjack-input.conf 02-beats-input.conf 10-syslog.conf 11-nginx.conf \
        30-output.conf

ADD http-input.conf /etc/logstash/conf.d/http-input.conf
