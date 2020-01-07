FROM jekyll/jekyll:pages
ARG with
ARG without

COPY Gemfile* /srv/jekyll/

WORKDIR /srv/jekyll

RUN apk update && \
	apk add ruby-dev gcc make curl build-base libc-dev libffi-dev zlib-dev libxml2-dev libgcrypt-dev libxslt-dev python

RUN bundle config build.nokogiri --use-system-libraries && \
	bundle install --with=${with} --without=${without}

EXPOSE 4000